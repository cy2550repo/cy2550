# Case Brief: macOS Insider Data Exfiltration

---
## Background
Applied Logic Platforms (ALP) is a SaaS company that develops internal developer tooling and customer workflow automation software. 

Engineers have access to internal documentation, API credentials, and limited customer data for testing purposes.

ALP maintains centralized monitoring and alerting capabilities, but developer systems—particularly travel laptops—are not fully locked down. These systems allow flexibility for development workflows, including browser access and cloud services, even if not all services are strictly restricted.

---
## Situation
An employee, Jason Wang, recently submitted his two-week resignation notice.

Shortly after, the security team observed unusual activity associated with his account over the weekend.

This activity included:
* Activity involving internal files occurring outside normal working hours
* Interaction with external, cloud-based services
* A login to a Google account from an unfamiliar IP address shortly after the observed activity

Due to the timing and context, this activity has been flagged for review.

---
## System Information
* **Hostname:** alp-macbook-jwang
* **Operating System:** macOS Sonoma
* **Timezone:** America/New_York
* **User:** jwang

This system is Jason’s company-issued travel laptop. It contains a mix of work-related and personal activities and is not configured as a tightly restricted enterprise device.

### Account Context
Jason uses multiple Google accounts on this system:
* A work-related account used for development activity  
* A personal account accessible within the same browser  

This configuration allows multiple accounts to be active within a single browser session.

---
## Investigation Scope
You have been provided with forensic artifacts extracted from Jason’s system.

Your task is to determine:
* What activity occurred on the system
* Whether any internal data was accessed, copied, or transferred
* Whether the observed behavior is consistent with normal usage or something more concerning

Some activity may need to be inferred through correlation of multiple artifacts rather than directly observed.

---
## Important Notes
* The user has legitimate access to the files on this system
* No assumptions should be made about intent
* All conclusions must be based on observable evidence

This investigation focuses on what happened, not why.

---
## Objective
Analyze the provided artifacts and reconstruct a clear, evidence-supported sequence of events.

No conclusions have been made. The purpose of the investigation is to determine what occurred and whether any sensitive data may have been mishandled. 
