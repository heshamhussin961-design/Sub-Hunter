# 🏹 Sub-Hunter

**Sub-Hunter** is a fast, multi-threaded subdomain enumeration tool written in Python. It is designed for Penetration Testers and Bug Bounty Hunters to quickly identify valid subdomains and resolve their IP addresses.

## ⚡ Features
- **Multi-threaded:** Scans thousands of domains in seconds.
- **Stealth Mode:** Uses random User-Agents to bypass basic firewalls.
- **IP Resolution:** Resolves IP addresses for valid subdomains.
- **Live Check:** Filters out dead domains automatically.
- **Output Saving:** Saves results to a text file for reporting.

## 🚀 Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/Sub-Hunter.git](https://github.com/YOUR_USERNAME/Sub-Hunter.git)

  Install requirements:

```Bash

pip install requests colorama fake_useragent



```Bash

python sub_hunter.py <target_domain> <wordlist_file>
Example:

Bash

python sub_hunter.py tesla.com subdomains_5000.txt
