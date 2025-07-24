import os
import json
import csv
import re
from datetime import datetime

# Paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FEEDS_DIR = os.path.join(BASE_DIR, 'feeds')
OUTPUT_DIR = os.path.join(BASE_DIR, 'parsed_feeds')
OUTPUT_CSV = os.path.join(OUTPUT_DIR, 'aggregated_iocs.csv')

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# CSV Headers
fields = ['source', 'ioc_type', 'value', 'timestamp']

# Store parsed rows
parsed_data = []

# 1. Parse ThreatFox JSON Files
for filename in os.listdir(FEEDS_DIR):
    if filename.startswith('threatfox') and filename.endswith('.json'):
        filepath = os.path.join(FEEDS_DIR, filename)
        with open(filepath, 'r') as f:
            try:
                data = json.load(f)
                for entry in data.get('data', []):
                    parsed_data.append({
                        'source': 'ThreatFox',
                        'ioc_type': entry.get('ioc_type', 'N/A'),
                        'value': entry.get('ioc', 'N/A'),
                        'timestamp': entry.get('last_seen', 'N/A')
                    })
            except Exception as e:
                print(f"[!] Failed to parse {filename}: {e}")

# 2. Parse AlienVault TXT Files (IPs/domains in plain text)
ioc_regex = re.compile(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b|\b(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,}\b')

for filename in os.listdir(FEEDS_DIR):
    if filename.startswith('alienvault') and filename.endswith('.txt'):
        filepath = os.path.join(FEEDS_DIR, filename)
        with open(filepath, 'r') as f:
            for line in f:
                line = line.strip()
                matches = ioc_regex.findall(line)
                for match in matches:
                    parsed_data.append({
                        'source': 'AlienVault',
                        'ioc_type': 'ip/domain',
                        'value': match,
                        'timestamp': datetime.now().isoformat()
                    })

# 3. Write to CSV
with open(OUTPUT_CSV, 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)
    writer.writeheader()
    writer.writerows(parsed_data)

print(f"[+] Parsed {len(parsed_data)} IOCs and saved to {OUTPUT_CSV}")

