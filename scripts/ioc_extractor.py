import re
import sys
import ipaddress
from urllib.parse import urlparse

print("SOC Phishing IoC Extractor")
print("--------------------------")


if len(sys.argv) < 2:
	print("Usage: python ioc_ extractor.py <email_file>")
	sys.exit()


file_path = sys.argv[1]


try:
    with open(file_path, "r", encoding="utf-8") as file:
        email_content = file.read()

except FileNotFoundError:
    print(f"\nError: File not found: {file_path}")
    sys.exit(1)

except PermissionError:
    print(f"\nError: Permission denied: {file_path}")
    sys.exit(1)

except UnicodeDecodeError:
    print(f"\nError: Unable to decode file as UTF-8: {file_path}")
    sys.exit(1)

print("\nEmail file loaded successfully.")
print(f"Characters analyzed: {len(email_content)}")

# Extract email addresses
email_pattern = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

email_addresses = re.findall(email_pattern, email_content)


print("\nEmail Addresses:")
for address in email_addresses:
	print(f"  - {address}")

# Extract domains from email addresses
domains = set()

for address in email_addresses:
    domain = address.split("@")[1]
    domains.add(domain)


# Normalize defanged indicators for analysis

normalized_content = email_content.replace("[.]", ".")
normalized_content = normalized_content.replace("hxxps://", "https://")
normalized_content = normalized_content.replace("hxxp://", "http://")

# Extract URLs
url_pattern = r'https?://[^\s<>"]+'
urls = re.findall(url_pattern, normalized_content)

# Extract domains from URLs
for url in urls:
    parsed_url = urlparse(url)

    if parsed_url.hostname:
        domains.add(parsed_url.hostname)

print("\nURLs:")
for url in urls:
    safe_url = url.replace("https://", "hxxps://")
    safe_url = safe_url.replace("http://", "hxxp://")
    safe_url = safe_url.replace(".", "[.]")
    print(f"  - {safe_url}")

print("\nDomains:")
for domain in sorted(domains):
    print(f"  - {domain}")

# Extract and validate IPv4 addresses
ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ip_candidates = re.findall(ip_pattern, normalized_content)

valid_ips = set()

for ip in ip_candidates:
    try:
        address = ipaddress.ip_address(ip)

        if address.version == 4:
            valid_ips.add(ip)

    except ValueError:
        pass

print("\nIPv4 Addresses:")
for ip in sorted(valid_ips):
    print(f"  - {ip}")

# Export extracted IoCs to a text file
output_file = r".\iocs\extracted-iocs.txt"

with open(output_file, "w", encoding="utf-8") as file:
    file.write("SOC Phishing IoC Extraction Results\n")
    file.write("===================================\n")

    file.write("\nEMAIL ADDRESSES\n")
    for address in sorted(set(email_addresses)):
        file.write(f"{address}\n")

    file.write("\nURLS\n")
    for url in urls:
        safe_url = url.replace("https://", "hxxps://")
        safe_url = safe_url.replace("http://", "hxxp://")
        safe_url = safe_url.replace(".", "[.]")
        file.write(f"{safe_url}\n")

    file.write("\nDOMAINS\n")
    for domain in sorted(domains):
        safe_domain = domain.replace(".", "[.]")
        file.write(f"{safe_domain}\n")

    file.write("\nIPv4 ADDRESSES\n")
    for ip in sorted(valid_ips):
        file.write(f"{ip}\n")

print(f"\nResults exported to: {output_file}")