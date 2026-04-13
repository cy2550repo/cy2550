# DFIR Simulation Platform
**Developers:** Emma Trowbridge and Cam Zabroski

## macOS Insider Data Exfiltration

---
## Overview
This case simulates a digital forensics and incident response (DFIR) investigation involving potential **insider data exfiltration on a macOS system.**

You are provided with a curated set of forensic artifacts extracted from a company-issued device. Your objective is to analyze the evidence, reconstruct what occurred, and produce evidence-based conclusions.

This is an **introductory-level (easy)** case. The scenario is intentionally structured to be clear and focused, allowing you to develop core DFIR skills such as artifact analysis, identifying relevant activity, timeline reconstruction, correlating evidence across sources, and reconstructing a sequence of events.

---
## Getting Started
Begin by cloning the repository and navigating into it:
```
git clone https://github.com/emmatrowbridge/DFIR-Simulation-Platform.git
cd DFIR-Simulation-platform/macOS_insider_data_exfiltration
```
Start by reading:
* `case_brief.md` for background and context
* `investigation_questions.md` for what you need to answer

---
## Investigation Approach
All evidence is located in the `evidence/` directory. You should download and analyze these files locally on your machine, not directly in GitHub.

A typical workflow looks like this:
* explore the directory structure in your terminal
* open files using appropriate tools (text editor, spreadsheet viewer, PDF viewer)
* identify which artifacts are relevant
* begin connecting activity across files

You are not expected to use specialized forensic tools for this case. Basic file inspection and careful reasoning are sufficient.

Focus on identifying patterns such as:
* where sensitive files are located
* whether files appear in multiple directories
* whether any directory appears to be used for staging
* browser activity that connects to external services

Most importantly, do not treat artifacts in isolation. This case requires correlating multiple sources of evidence to understand what happened.

---
## Recording Your Answers
All answers should be completed in the `workspace/` directory.

Create your working file by copying the template: `cp workspace/answers_template.json workspace/answers.json`.

Open `answers.json` in a text editor and fill in your answers.

Make sure:
* you use exact file names and paths where applicable
* your answers are directly supported by evidence
* the file remains valid JSON (do not remove quotes, commas, or brackets)

You may also use `timeline_template.csv` to organize events as you investigate. This is not required, but it can make it much easier to track relationships between artifacts.

---
## Checking Your Work
Once you have completed your answers, run: `python validation/check_answers.py`.

The script will evaluate each answer and report whether it is correct or incorrect, along with a final summary.

### About the Validation System
The validation system is included to support self-guided learning and immediate feedback.

The file `validation/answer_key.json` contains the expected answers used by the script. While it is included in the repository, you should not rely on it during the investigation. The goal of this case is to develop your ability to interpret artifacts and reach conclusions independently.

---
## Final Notes
A strong investigation is not about finding a single clue—it is about connecting multiple pieces of evidence into a coherent explanation.

Individual actions may appear normal on their own. Your task is to determine whether they form a meaningful pattern when viewed together.

---
**Good luck!**
