#!/bin/bash

# Bug Bounty Recon Full Setup Script for Linux

echo "🔹 Updating System & Installing Dependencies..."
sudo apt update && sudo apt upgrade -y
sudo apt install python3 python3-pip git nmap sqlmap subfinder -y

# Clone the repository (if needed)
if [ ! -d "BugBountyRecon" ]; then
    git clone https://github.com/your-repo/BugBountyRecon.git
fi

cd BugBountyRecon

echo "🔹 Creating Virtual Environment..."
python3 -m venv venv
source venv/bin/activate

echo "🔹 Installing Python Requirements..."
pip3 install -r requirements.txt

echo "🔹 Setting Permissions for Execution..."
chmod +x app.py

# Running the Application
echo "🔹 Running the Application..."
python3 app.py
