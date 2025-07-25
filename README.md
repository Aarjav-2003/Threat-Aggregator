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

## Output
1️⃣ **Initial Feed Display (Raw IOC Listing)**
The application demonstrates successful parsing and display of threat intelligence feeds collected from multiple sources. It shows a table with data like IOCs (Indicators of Compromise), threat types, and timestamps. This confirms that the system is effectively fetching and rendering real-time data from platforms like ThreatFox and AlienVault.
<img width="1260" height="764" alt="Screenshot 2025-07-25 054122" src="https://github.com/user-attachments/assets/e1f796f2-105d-43f6-9a38-2fe07b019ead" />


2️⃣ **Enhanced Web UI – IOC Table Display**
This highlights the web interface powered by Django. The data is structured into a clean, searchable table view, styled with modern frontend frameworks. It includes search functionality and sorting capabilities, enabling cybersecurity analysts to sift through large volumes of threat data with ease.
<img width="1237" height="764" alt="Screenshot 2025-07-25 054133" src="https://github.com/user-attachments/assets/c3992811-f914-44ec-afa2-bb63962f9d5b" />


## 💡 Why It Stands Out
This project offers a realistic, usable, and easily extensible solution to the growing need for threat aggregation. With a clean architecture and focused utility, it empowers analysts and developers to access IOC data quickly — all without overengineering.

Perfectly suited for SOC teams, educators, researchers, or even individual defenders — the Threat Aggregator proves that even simple tools can drive big impact.

