#!/usr/bin/env python3
"""
DFIR Simulation Platform - Answer Validation Script

Supported validation rule types
-------------------------------
- exact_string : exact text match, case-insensitive
- exact_path   : exact path match, tolerant of slash formatting
- exact_set    : exact list match, order-insensitive
- keyword_text : flexible short-answer validation using required keyword groups in text
- keyword_list : flexible validation using one or more acceptable keywords
- sequence     : flexible sequence validation requiring multiple keyword groups and a sequence structure
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

ANSWERS_PATH = Path("workspace/answers.json")
ANSWER_KEY_PATH = Path("validation/answer_key.json")

def load_json_file(path: Path, description: str) -> dict[str, Any]:
    """Load a JSON file and ensure it is a dictionary."""
    if not path.exists():
        print(f"[ERROR] Could not find {description}: {path}")
        sys.exit(1)

    try:
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {path}: {e}")
        sys.exit(1)

    if not isinstance(data, dict):
        print(f"[ERROR] {description} must contain a top-level JSON object.")
        sys.exit(1)

    return data

def normalize_string(value: Any) -> str:
    """Normalize string for case-insensitive comparison."""
    if value is None:
        return ""
    return " ".join(str(value).strip().split()).lower()

def normalize_path(value: Any) -> str:
    """Normalize path (slashes, duplicates, trailing slash)."""
    if value is None:
        return ""
    text = str(value).strip().replace("\\", "/")
    while "//" in text:
        text = text.replace("//", "/")
    return text.rstrip("/") if text != "/" else text

def normalize_list_of_strings(value: Any) -> list[str]:
    """Convert input to cleaned list of non-empty strings."""
    if not isinstance(value, list):
        return []
    result: list[str] = []
    for item in value:
        if isinstance(item, str):
            cleaned = item.strip()
            if cleaned:
                result.append(cleaned)
    return result

def normalize_string_set(value: Any) -> set[str]:
    """Convert list to set for order-insensitive comparison."""
    return {item.strip() for item in normalize_list_of_strings(value)}

def contains_any(text: str, keywords: list[str]) -> bool:
    """Check if any keyword appears in text."""
    return any(keyword in text for keyword in keywords)

def validate_exact_string(student_value: Any, expected_value: str) -> bool:
    """Validate exact string match (case-insensitive)."""
    return normalize_string(student_value) == normalize_string(expected_value)

def validate_exact_path(student_value: Any, expected_value: str) -> bool:
    """Validate exact path match (normalized)."""
    return normalize_path(student_value) == normalize_path(expected_value)

def validate_exact_set(student_value: Any, expected_values: list[str]) -> bool:
    """Validate exact set of values (order does not matter)."""
    return normalize_string_set(student_value) == {v.strip() for v in expected_values}

def validate_keyword_text(student_value: Any, required_groups: dict[str, list[str]]) -> bool:
    """Validate text contains at least one keyword from each required group."""
    if isinstance(student_value, list):
        combined = " ".join(str(v) for v in student_value)
    else:
        combined = str(student_value)

    norm = normalize_string(combined)

    for keywords in required_groups.values():
        normalized_keywords = [normalize_string(k) for k in keywords]
        if not contains_any(norm, normalized_keywords):
            return False
    return True

def validate_keyword_list(student_value: Any, allowed_keywords: list[str]) -> bool:
    """Validate text contains at least one allowed keyword."""
    if isinstance(student_value, list):
        combined = " ".join(str(v) for v in student_value)
    else:
        combined = str(student_value)

    norm = normalize_string(combined)
    normalized_keywords = [normalize_string(k) for k in allowed_keywords]

    return contains_any(norm, normalized_keywords)

def validate_sequence(student_value: Any, required_groups: dict[str, list[str]]) -> bool:
    """Validate sequence includes all required concept groups and multiple steps."""
    if isinstance(student_value, list):
        items = [str(v).strip() for v in student_value if str(v).strip()]
        combined = " ".join(items)
        has_multiple_steps = len(items) >= 2
    else:
        combined = str(student_value)
        has_multiple_steps = False

    norm = normalize_string(combined)

    for keywords in required_groups.values():
        normalized_keywords = [normalize_string(k) for k in keywords]
        if not contains_any(norm, normalized_keywords):
            return False

    sequence_markers = ["first", "then", "next", "after", "before", "finally", "and then", "followed by", "which led to", "subsequently"]
    has_sequence_language = contains_any(norm, sequence_markers) or has_multiple_steps

    return has_sequence_language

def validate_field(student_value: Any, rule: dict[str, Any]) -> bool:
    """Dispatch validation based on rule type."""
    rule_type = rule.get("type")

    if rule_type == "exact_string":
        return validate_exact_string(student_value, rule["expected"])

    if rule_type == "exact_path":
        return validate_exact_path(student_value, rule["expected"])

    if rule_type == "exact_set":
        return validate_exact_set(student_value, rule["expected"])

    if rule_type == "keyword_text":
        return validate_keyword_text(student_value, rule["required_groups"])

    if rule_type == "keyword_list":
        return validate_keyword_list(student_value, rule["keywords"])

    if rule_type == "sequence":
        return validate_sequence(student_value, rule["required_groups"])

    raise ValueError(f"Unknown validation type: {rule_type}")

def main() -> None:
    """
    Main program flow.

    Steps:
    1. Load student answers
    2. Load case answer key
    3. Check that all required fields are present
    4. Validate each required field
    5. Print per-question CORRECT/INCORRECT
    6. Print final summary line
    7. Exit 0 only if everything is correct
    """
    answers = load_json_file(ANSWERS_PATH, "answers file")
    answer_key = load_json_file(ANSWER_KEY_PATH, "answer key")

    case_name = answer_key.get("case_name", "Unnamed Case")
    required_fields = answer_key.get("required_fields", [])
    validators = answer_key.get("validators", {})

    if not isinstance(required_fields, list) or not required_fields:
        print("[ERROR] Invalid answer key configuration.")
        sys.exit(1)

    missing_fields = [field for field in required_fields if field not in answers]
    if missing_fields:
        print("[ERROR] Missing required fields:")
        for field in missing_fields:
            print(f"- {field}")
        sys.exit(1)

    total_questions = len(required_fields)
    correct_count = 0

    print("DFIR Simulation Platform - Validation Results")
    print(f"Case: {case_name}")
    print()

    for field in required_fields:
        rule = validators.get(field)

        if not rule:
            print(f"{field}: INCORRECT")
            continue

        try:
            is_correct = validate_field(answers.get(field), rule)
        except Exception:
            is_correct = False

        if is_correct:
            print(f"{field}: CORRECT")
            correct_count += 1
        else:
            print(f"{field}: INCORRECT")

    print()
    print(f"{correct_count}/{total_questions} questions correct")

    sys.exit(0 if correct_count == total_questions else 1)

if __name__ == "__main__":
    main()
