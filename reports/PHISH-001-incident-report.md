\# Phishing Investigation Report — PHISH-001



\## 1. Case Information



\*\*Case ID:\*\* PHISH-001  

\*\*Case Type:\*\* Suspected Phishing Email  

\*\*Analyst Classification:\*\* Suspicious  

\*\*Environment:\*\* Controlled Training Lab  



\---



\## 2. Executive Summary



A suspicious email claiming to originate from Microsoft Security was analyzed after being reported by a user.



The email attempted to create urgency by stating that the recipient's Microsoft 365 password would expire and that the account would be suspended unless immediate verification was completed.



Analysis identified multiple phishing indicators, including a non-official Microsoft-themed sender domain, a mismatched Reply-To domain, urgency-based social engineering, and a suspicious account-verification URL.



The email was classified as \*\*Suspicious\*\*.



\---



\## 3. Key Indicators



\### Sender



security@microsoft-support-verification\[.]com



\### Reply-To



accountverify@outlook-security-help\[.]com



\### Sender Domain



microsoft-support-verification\[.]com



\### Reply-To Domain



outlook-security-help\[.]com



\### URL Domain



microsoft-login-verification\[.]com



\### URL



hxxps://microsoft-login-verification\[.]com/verify



Indicators are defanged for safe documentation.



\---



\## 4. Email Authentication



\*\*SPF:\*\* PASS  

\*\*DKIM:\*\* PASS  

\*\*DMARC:\*\* PASS



The authentication results indicate that the message was authenticated for the sending domain.



However, successful SPF, DKIM, and DMARC results do not establish that the sending domain belongs to Microsoft or that the message itself is trustworthy.



\---



\## 5. Investigation Findings



\### Brand Impersonation



The email claims to originate from Microsoft Security, but the sender uses a Microsoft-themed domain rather than the expected official Microsoft domain.



\### Reply-To Mismatch



The Reply-To domain differs from the sender domain, introducing an additional inconsistency in the sender identity.



\### Social Engineering



The subject and message use urgency and fear of account suspension to pressure the recipient into taking immediate action.



\### Suspicious Verification URL



The embedded verification URL uses Microsoft-related terminology but does not use the expected official Microsoft domain.



The combination of these characteristics is consistent with a credential-phishing scenario.



\---



\## 6. Threat Intelligence Methodology



VirusTotal, urlscan, WHOIS/DNS information, and AbuseIPDB were studied as part of the threat-intelligence workflow.



The investigation demonstrated how an analyst can use multiple intelligence sources to evaluate:



\- Domain and URL reputation

\- Security-vendor detections

\- Domain registration history

\- DNS and IP infrastructure

\- ASN and network ownership

\- Website behavior and redirects

\- IP abuse-reporting history

\- Relationships between indicators



PHISH-001 uses fictional training indicators. Therefore, external threat-intelligence results from unrelated test or baseline indicators were not presented as evidence against the PHISH-001 domains.



\---



\## 7. Campaign Scope



Training scenario scope:



\*\*Matching messages identified:\*\* 12  

\*\*Successfully delivered:\*\* 9  

\*\*Quarantined:\*\* 3  

\*\*Known link clicks:\*\* 0



The scenario demonstrates how an analyst can determine whether a reported phishing email represents an isolated message or a broader campaign.



\---



\## 8. User Exposure



The reporting user opened the email but did not:



\- Click the verification URL

\- Download an attachment

\- Reply to the sender

\- Submit credentials



Based on the available scenario evidence, no credential exposure or account compromise was identified for the reporting user.



\---



\## 9. Recommended Response



Recommended actions include:



1\. Remove or quarantine matching delivered messages where supported.

2\. Notify affected users not to interact with the suspicious email.

3\. Search the email environment for additional matching indicators.

4\. Block confirmed malicious or suspicious indicators according to organizational procedures.

5\. Continue monitoring for additional campaign activity.



\---



\## 10. Escalation Criteria



Escalation to L2 / Incident Response should be considered if evidence identifies:



\- Phishing-link interaction

\- Credential submission

\- Suspicious attachment execution

\- Suspicious authentication activity

\- Unauthorized account changes

\- Other evidence indicating potential compromise



If credential exposure is confirmed, authorized responders should consider actions such as password reset, active-session/token revocation, MFA review, sign-in investigation, and account-activity analysis according to organizational procedures.



\---



\## 11. Analyst Verdict



\*\*Verdict: SUSPICIOUS\*\*



The email contains multiple characteristics consistent with credential phishing, including brand impersonation, sender/Reply-To inconsistency, urgency-based social engineering, and a suspicious verification URL.



SPF, DKIM, and DMARC passing does not establish that Microsoft sent the message.



Because PHISH-001 uses fictional training infrastructure and does not contain independent threat-intelligence confirmation of malicious infrastructure, the case is classified as \*\*Suspicious rather than conclusively Malicious\*\*.



\---



\## 12. Skills Demonstrated



\- Phishing email triage

\- Email header analysis

\- SPF, DKIM, and DMARC interpretation

\- Indicator of Compromise (IoC) extraction

\- URL and domain analysis

\- Threat-intelligence methodology

\- VirusTotal analysis

\- urlscan analysis

\- WHOIS/DNS investigation

\- IP reputation analysis

\- AbuseIPDB analysis

\- Evidence correlation

\- Campaign scoping

\- User-exposure assessment

\- Incident escalation

\- Containment recommendations

\- SOC incident documentation



\---



\## 13. Safety and Limitations



This investigation was performed as a controlled cybersecurity training exercise.



The PHISH-001 domains and URLs are fictional training indicators and were documented in defanged form. No real malicious infrastructure was intentionally accessed during the exercise.

