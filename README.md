# 🛡️ Threat Aggregator – Real-Time IOC Intelligence Dashboard

A lightweight and efficient threat intelligence aggregator that collects and displays real-time Indicators of Compromise (IOCs) from public feeds, helping cybersecurity professionals access structured and searchable threat data in one place.



## 🚀 Hackathon Challenge Summary: Threat Intelligence Feed Aggregator

**Challenge Statement:**  
Develop a tool to **aggregate**, **store**, and **present** real-time threat intelligence from multiple sources — especially IOCs like malicious IPs, domains, and hashes — in a **filterable and readable** format.



## ✅ Our Solution

We built a **modular, fast, and intuitive threat feed aggregator** with the following key functionalities:

### 🔍 Core Features
- **Live Feed Aggregation** from top open-source intelligence platforms:
  - [ThreatFox](https://threatfox.abuse.ch)
  - [AlienVault OTX](https://otx.alienvault.com)
- **IOC Parsing** with proper identification and categorization (IPs, Domains, URLs, Hashes).
- **Auto-Folder Creation & Storage:**  
  All fetched feed data is organized under a common directory (`feeds/`) with filenames reflecting the date of fetch.
- **User-Friendly Web Dashboard (Django-based):**
  - IOC viewing and searching
  - Filtering by threat type (IP, Domain, Hash)
  - Filtering by source



## ✨ What Makes This Project Unique and Innovative?

✅ **Unified Aggregation System**  
Feeds are fetched via a simple, clean, and portable Bash script — no external dependencies beyond `curl` and Python. Easily extendable to more sources.

✅ **Consistent Folder Structure**  
Automatically creates a `feeds/` directory regardless of where the script is run. This ensures consistent organization and removes manual overhead for users — perfect for deployment on cloud or isolated VMs.

✅ **Source-Specific Normalization**  
Feed data is normalized into a common format regardless of its original structure, enabling seamless integration into the dashboard.

✅ **Ethical, Non-Invasive Design**  
Unlike auto-blocking or intervention-based systems, this tool is focused on **intelligence and awareness** — ensuring it's non-destructive, safe for researchers, and usable in controlled or audit environments.

✅ **Minimal & Effective Stack**  
Built with **Bash + Django**, this system avoids complex ML, heavy DBs, or cloud dependencies — perfect for quick deployment, testing, or demos in hackathon settings.



## 📁 Project Structure

```bash
threat-aggregator/
├── feeds/                         # Feed data (auto-created)
├── fetch_feeds.sh                # Bash script to collect IOCs
├── threat_dashboard/             # Django project
│   ├── dashboard/                # Django app for views/templates
│   └── ...
├── requirements.txt              # Python dependencies
└── README.md                     # Project documentation
```

## 💡 Why It Stands Out
This project offers a realistic, usable, and easily extensible solution to the growing need for threat aggregation. With a clean architecture and focused utility, it empowers analysts and developers to access IOC data quickly — all without overengineering.

Perfectly suited for SOC teams, educators, researchers, or even individual defenders — the Threat Aggregator proves that even simple tools can drive big impact.

