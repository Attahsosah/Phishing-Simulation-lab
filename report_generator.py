import csv
from collections import Counter

def generate_report():
    print("--- PHISHING SIMULATION: INTERNAL AUDIT REPORT ---")
    try:
        with open('harvested_creds.csv', 'r') as f:
            reader = csv.reader(f)
            data = list(reader)
            
            total_clicks = len(data)
            ips = [row[3] for row in data]
            unique_victims = len(set(ips))
            
            print(f"Total Compromised Credentials: {total_clicks}")
            print(f"Unique Victim IP Addresses: {unique_victims}")
            print("\nIP Address Breakdown:")
            for ip, count in Counter(ips).items():
                print(f" - {ip}: {count} submission(s)")
                
    except FileNotFoundError:
        print("No data captured yet.")

if __name__ == "__main__":
    generate_report()
