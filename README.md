\# Phishing Analysis \& Threat Intelligence Lab



A hands-on SOC analyst project focused on phishing email triage, email authentication analysis, Indicator of Compromise (IoC) extraction, threat intelligence, incident scoping, response and Python-based security automation.



> \*\*Lab Notice:\*\* This project uses fictional and documentation-safe indicators for training. No real malicious infrastructure is intentionally accessed or presented as confirmed malicious.



\---



\## Project Objectives



The objective of this lab is to simulate the workflow of a Junior / L1 SOC Analyst investigating a reported phishing email.



The investigation covers:



\- Manual phishing email triage

\- Email header analysis

\- SPF, DKIM and DMARC interpretation

\- IoC extraction

\- Domain and URL investigation

\- Threat intelligence methodology

\- Campaign scoping

\- User exposure assessment

\- Incident containment and escalation

\- SOC incident reporting

\- Python-based IoC extraction automation



\---



\## Investigation Workflow



```text

Suspicious Email Report

&#x20;       |

&#x20;       v

Manual Email Triage

&#x20;       |

&#x20;       v

Header \& Authentication Analysis

&#x20;       |

&#x20;       v

IoC Extraction

&#x20;       |

&#x20;       v

Threat Intelligence

&#x20;       |

&#x20;       +---- VirusTotal

&#x20;       +---- urlscan

&#x20;       +---- WHOIS / DNS

&#x20;       +---- AbuseIPDB

&#x20;       |

&#x20;       v

Evidence Correlation

&#x20;       |

&#x20;       v

Analyst Classification

&#x20;       |

&#x20;       v

Scope \& User Exposure

&#x20;       |

&#x20;       v

Containment / Escalation

&#x20;       |

&#x20;       v

Final SOC Report

```



\---



\## Case Scenario — PHISH-001



A user reported an email claiming to originate from Microsoft Security.



The email warned that the user's Microsoft 365 password would expire and that the account would be suspended unless immediate verification was completed.



\### Key Observations



The investigation identified several suspicious characteristics:



\- Microsoft brand impersonation

\- Non-official Microsoft-themed sender domain

\- Sender and Reply-To domain inconsistency

\- Urgency-based social engineering

\- Threat of account suspension

\- Suspicious account-verification URL

\- Request for immediate user action



The training sample displayed:



\- \*\*SPF:\*\* PASS

\- \*\*DKIM:\*\* PASS

\- \*\*DMARC:\*\* PASS



This demonstrates an important security concept:



> Passing SPF, DKIM and DMARC authenticates aspects of the sending domain/message but does not by itself prove that the sender is the organization being impersonated or that the email is benign.



\---



\## Indicators of Compromise



The following fictional indicators were extracted from the training sample:



```text

Sender:

security@microsoft-support-verification\[.]com



Reply-To:

accountverify@outlook-security-help\[.]com



Sender Domain:

microsoft-support-verification\[.]com



Reply-To Domain:

outlook-security-help\[.]com



URL Domain:

microsoft-login-verification\[.]com



URL:

hxxps://microsoft-login-verification\[.]com/verify



Training IP:

192.0.2.25

```



Indicators are defanged for safe documentation.



`192.0.2.25` is used as a documentation/training address and is not presented as real malicious infrastructure.



\---



\## Threat Intelligence Methodology



The project demonstrates how multiple intelligence sources can support an investigation.



\### VirusTotal



Used to understand:



\- Vendor detection results

\- Domain reputation context

\- Domain information

\- Relationships between indicators

\- Registration and infrastructure information



A key lesson from the investigation:



```text

0 detections != guaranteed safe

```



Threat intelligence is supporting evidence and should not be treated as an absolute verdict.



\### urlscan



Used to understand:



\- Submitted and effective URLs

\- HTTP redirects

\- Page behavior

\- Domains contacted

\- IP infrastructure

\- ASN information

\- Historical scans

\- Related page information



\### WHOIS / DNS



Used to understand:



\- Domain registration history

\- Domain age

\- DNS records

\- Infrastructure relationships



A newly registered domain may increase suspicion when combined with other phishing indicators, but domain age alone does not determine whether a domain is malicious.



\### AbuseIPDB



Used to understand IP reputation concepts including:



\- Abuse reports

\- Reporting history

\- ISP / network information

\- ASN context

\- Abuse categories



Community reports are treated as intelligence evidence rather than proof that a particular incident is malicious.



\---



\## Python IoC Extractor



A Python utility was developed to automate indicator extraction from phishing email samples.



\### Current Capabilities



The script can:



\- Read a text-based email sample

\- Extract email addresses

\- Extract URLs

\- Normalize defanged URLs for parsing

\- Re-defang URLs for safer output

\- Extract domains from email addresses

\- Extract domains from URLs

\- Remove duplicate domains

\- Extract IPv4 candidates

\- Validate IPv4 addresses

\- Reject invalid IPv4 values

\- Export extracted indicators to a text file

\- Handle missing input files cleanly



\### Usage



From the repository root:



```powershell

python .\\scripts\\ioc\_extractor.py .\\samples\\phishing-email-01.txt

```



Example output:



```text

Email Addresses:

&#x20; - security@microsoft-support-verification.com

&#x20; - accountverify@outlook-security-help.com

&#x20; - bounce@microsoft-support-verification.com



URLs:

&#x20; - hxxps://microsoft-login-verification\[.]com/verify



Domains:

&#x20; - microsoft-login-verification.com

&#x20; - microsoft-support-verification.com

&#x20; - outlook-security-help.com



IPv4 Addresses:

&#x20; - 192.0.2.25

```



The script also exports the extracted indicators to:



```text

iocs/extracted-iocs.txt

```



\---



\## Campaign Scoping



The training scenario was expanded to simulate an organization-wide phishing investigation.



```text

Matching emails:      12

Delivered:             9

Quarantined:           3

Known link clicks:     0

```



This demonstrates the distinction between:



```text

Delivered

&#x20;  |

&#x20;  v

Opened

&#x20;  |

&#x20;  v

Clicked

&#x20;  |

&#x20;  v

Credentials Submitted

&#x20;  |

&#x20;  v

Potential Account Compromise

```



Delivery alone does not mean that a user opened or interacted with the message.



\---



\## Response \& Containment



Recommended actions in the training scenario include:



1\. Remove or quarantine matching delivered emails where supported.

2\. Notify affected users not to interact with the suspicious message.

3\. Search the environment for matching sender addresses, domains, URLs and subjects.

4\. Block confirmed malicious or suspicious indicators according to organizational procedures.

5\. Continue monitoring for related campaign activity.



If credential submission is identified, the case should be escalated according to organizational procedures.



Potential response actions may include:



\- Password reset

\- Active session/token revocation

\- MFA review

\- Sign-in history investigation

\- Source IP investigation

\- Device/location review

\- Mailbox-rule investigation

\- Additional account activity analysis



Actions depend on analyst authorization and organizational incident-response procedures.



\---



\## Analyst Classification



\*\*Classification: Suspicious\*\*



The training email contains multiple characteristics consistent with credential phishing.



However, PHISH-001 uses fictional training infrastructure and does not contain independent threat-intelligence confirmation of malicious infrastructure.



For this reason, the case is documented as \*\*Suspicious rather than conclusively Malicious\*\*.



\---



\## Repository Structure



```text

phishing-analysis-lab/

|

|-- evidence/

|   `-- PHISH-001-analysis.txt

|

|-- iocs/

|   |-- PHISH-001-iocs.txt

|   `-- extracted-iocs.txt

|

|-- reports/

|   `-- PHISH-001-incident-report.md

|

|-- samples/

|   `-- phishing-email-01.txt

|

|-- scripts/

|   `-- ioc\_extractor.py

|

|-- .gitignore

`-- README.md

```



\---



\## Skills Demonstrated

## Investigation Evidence

The following screenshots document key stages of the lab workflow.

### Python IoC Extraction

The custom Python utility automatically extracts email addresses, URLs, domains and validated IPv4 addresses from the phishing training sample.

![Python IoC Extractor](screenshots/01-ioc-extractor-output.png)

### Automated IoC Report

Extracted indicators are automatically exported into a structured text artifact for further investigation and documentation.

![Extracted IoCs](screenshots/02-extracted-iocs.png)

### VirusTotal Analysis

VirusTotal was used as a safe baseline example to study domain reputation, vendor detections, passive DNS relationships and infrastructure context.

The screenshot below analyzes the legitimate `microsoft.com` domain and is included to demonstrate threat-intelligence methodology. It is not presented as evidence that the fictional PHISH-001 infrastructure is malicious.

![VirusTotal Analysis](screenshots/03-virustotal-analysis.png)

### urlscan Analysis

urlscan was used to study URL behavior, redirects, HTTP activity, contacted infrastructure, IP/ASN information and page behavior.

The screenshot below uses the legitimate Microsoft website as a safe baseline example and demonstrates the investigation methodology rather than evidence against PHISH-001.

![urlscan Analysis](screenshots/04-urlscan-analysis.png)

---

\### SOC Analysis



\- Phishing email triage

\- Email header analysis

\- IoC extraction

\- Evidence correlation

\- Campaign scoping

\- User exposure assessment

\- Incident escalation

\- Containment recommendations

\- SOC case documentation



\### Email Security



\- SPF

\- DKIM

\- DMARC

\- Sender analysis

\- Reply-To analysis

\- Brand impersonation identification

\- Social-engineering analysis



\### Threat Intelligence



\- VirusTotal

\- urlscan

\- WHOIS

\- DNS

\- AbuseIPDB

\- IP reputation

\- ASN / ISP context

\- Domain and URL analysis



\### Automation



\- Python

\- Regular expressions

\- URL parsing

\- IoC normalization

\- IPv4 validation

\- Duplicate removal

\- File input/output

\- Exception handling



\---



\## Key Lessons



This lab demonstrates several principles relevant to SOC investigations:



\- A passed SPF/DKIM/DMARC result does not automatically make an email trustworthy.

\- A zero-detection threat-intelligence result does not guarantee an indicator is benign.

\- Threat-intelligence reports should be correlated with incident evidence.

\- Delivery of an email does not prove user interaction.

\- Suspicious activity does not automatically mean confirmed compromise.

\- Analyst conclusions should match the available evidence.

\- Escalation and containment actions should follow organizational authorization and procedures.



\---



\## Disclaimer



This repository is intended for cybersecurity education, defensive security training and portfolio demonstration.



All suspicious domains and URLs used in PHISH-001 are fictional training indicators and are defanged in documentation. Documentation/test IP space is used where an IP example is required.



The project does not intentionally provide or interact with live malicious infrastructure.

