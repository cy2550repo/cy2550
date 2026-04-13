# Workspace Guide
This directory contains the files you will use to organize your investigation and submit your answers.

---
## Overview
Your goal is to analyze the provided artifacts, reconstruct what happened, and answer the investigation questions using evidence.

A typical workflow is:
1. Analyze the evidence
2. Build a timeline (recommended)
3. Record your answers
4. Run validation

---
### Step 1 — Analyze the Evidence
Examine the artifacts in the `evidence/` directory.

Focus on:
* Filesystem structure
* Browser activity
* Relationships between artifacts

Not all artifacts are relevant. Your goal is to identify meaningful patterns and connections.

---
### Step 2 — Build a Timeline (Recommended)
Use `timeline_template.csv` to organize events into a sequence.

The timeline is not graded, but it is the most effective way to:
* Understand what happened
* Correlate multiple artifacts
* Answer the investigation questions

#### How to Use the Timeline
Each row should represent a meaningful event and include:
* What happened
* Which artifact supports it
* Why the artifact supports your conclusion

The timeline template includes more rows than you will likely need.

* You are not expected to use every row
* Only include meaningful events supported by evidence
* Focus on quality of events, not quantity  

#### Important Context for This Case
* Filesystem artifacts do not include full timestamp metadata
* Most timestamps come from browser artifacts
* Some steps must be inferred through correlation

You are expected to combine multiple artifacts and use logical reasoning to build a sequence of events.

---
### Step 3 — Record Your Answers
Use `answers_template.json` to record your answers.

#### Creating Your Working File
1. From the case root directory, run: `cp workspace/answers_template.json workspace/answers.json`.
2. Open `workspace/answers.json` and fill in your answers. You can edit this file using any text editor.

#### Example Format
Use exact values from the artifacts.

Example of a string field: `"q0_example": "/Users/jwang/full_directory_path_here"`

Example of an array field: `"q0_example": ["example1", "example2", "example3"]`

Some questions require a short, structured sequence rather than a single value. For example: `"q0_example_sequence_of_actions": ["First step in the sequence", "Second step in the sequence", "Third step in the sequence"]`

---
### Step 4 — Run Validation
From the case root directory, run: `python validation/check_answers.py`.

The validation script checks whether your answers are correct, but it only reports correct or incorrect. It does not provide the correct answers, partial credit, or step-by-step hints. This is intentional.

The goal of this case is not just to get the right answers, but to develop the ability to:
* Interpret artifacts
* Correlate evidence
* Reach defensible conclusions independently

---
## Final Goal
By the end of this process, you should be able to:
* Reconstruct a clear sequence of events
* Explain how artifacts relate to each other
* Support your conclusions with evidence
* Answer all investigation questions confidently

---
A strong investigation is not about finding a single clue—it is about connecting multiple pieces of evidence into a coherent explanation.
