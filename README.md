# Phishing Simulation & SOC Triage Lab

A Python-based credential harvesting simulation built to demonstrate the phishing lifecycle and SOC analysis techniques.

## 🔗 Full Technical Write-up
https://medium.com/p/af52916a7e64/edit

## 🛠️ Features
- **Flask Backend:** Handles GET/POST requests for credential capture.
- **Telemetry Logging:** Captures IP addresses and User-Agent strings for triage.
- **SOC Reporting:** Includes a `report_generator.py` for automated log analysis.

## 🚀 Quick Start
1. Clone the repo: `git clone https://github.com/Attahsosah/Phishing-Simulation-lab/tree/main`
2. Setup Venv: `python3 -m venv venv && source venv/bin/activate`
3. Install Flask: `pip install -r requirements.txt`
4. Run the app: `python3 app.py`
