#!/bin/bash

# Get the directory where this script is located
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Go one level up to reach the main project directory
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

# Define feeds directory relative to project
FEEDS_DIR="$PROJECT_DIR/feeds"
mkdir -p "$FEEDS_DIR"

# Get timestamp
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

# ----------------------
# THREATFOX
# ----------------------
echo "[*] Downloading from ThreatFox..."
THREATFOX_URL="https://threatfox.abuse.ch/export/json/recent/"
THREATFOX_FILE="$FEEDS_DIR/threatfox_$TIMESTAMP.json"
curl -s "$THREATFOX_URL" -o "$THREATFOX_FILE"

if [ -s "$THREATFOX_FILE" ]; then
    echo "✅ ThreatFox feed downloaded successfully: $THREATFOX_FILE"
else
    echo "❌ Failed to download ThreatFox feed."
fi

# ----------------------
# ALIENVAULT
# ----------------------
echo "[*] Downloading from AlienVault..."
ALIENVAULT_URL="https://reputation.alienvault.com/reputation.generic"
ALIENVAULT_FILE="$FEEDS_DIR/alienvault_$TIMESTAMP.txt"
curl -s "$ALIENVAULT_URL" -o "$ALIENVAULT_FILE"

if [ -s "$ALIENVAULT_FILE" ]; then
    echo "✅ AlienVault feed downloaded successfully: $ALIENVAULT_FILE"
else
    echo "❌ Failed to download AlienVault feed."
fi
