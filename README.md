# Bug Bounty Recon Tool - Premium Edition

This is a Flask-based web application that automates bug bounty reconnaissance tasks.

## Features
✅ **Subdomain Enumeration** → (Subfinder, Amass, Assetfinder API)  
✅ **Port Scanning & Service Detection** → (Nmap, Masscan)  
✅ **Web Crawler & Hidden URLs Finder** → (Gau, Waybackurls, Katana)  
✅ **Automated XSS, SQLi & LFI Detection** → (Nuclei, Dalfox, SQLmap)  
✅ **API Security Testing & Token Leaks Detection** → (GitHub Dorking, Secret Scanning)  
✅ **Burp Suite Integration** → (Live Traffic Analysis & Interception)  
✅ **OSINT Data Collection** → (Email, Social Media, WHOIS Lookup)  
✅ **Custom Dashboard with Reports & Export Option**  
✅ **Dark Web Scan (Tor-based Lookup)**  

## Installation
```bash
pip install -r requirements.txt
python app.py
```

## Usage
1. Open `http://127.0.0.1:5000`  
2. Enter the target URL and select the scan type  
3. View the scan results in JSON format  

## Example Output
```json
{
  "result": "Found subdomain: api.target.com\nFound subdomain: mail.target.com"
}
```

## Premium Features
- **Report Generation in PDF & CSV**  
- **Custom Wordlists & Dictionary Attacks**  
- **Automation with Task Scheduler**  
- **Encrypted Data Storage for Scan Results**  
