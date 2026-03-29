import requests
import os
import time
from dotenv import load_dotenv

load_dotenv()

BRIGHT_DATA_API_KEY = os.getenv("BRIGHT_DATA_API_KEY")

def scrape_candidates(linkedin_urls):
    headers = {
        "Authorization": f"Bearer {BRIGHT_DATA_API_KEY}",
        "Content-Type": "application/json"
    }
    
    payload = [{"url": url} for url in linkedin_urls]
    
    trigger_url = "https://api.brightdata.com/datasets/v3/trigger?dataset_id=gd_l1viktl72bvl7bjuj0&format=json"
    response = requests.post(trigger_url, headers=headers, json=payload)
    
    if response.status_code != 200:
        return {"error": response.text}
    
    snapshot_id = response.json().get("snapshot_id")
    print(f"Scrape triggered! Snapshot ID: {snapshot_id}")
    
    snapshot_url = f"https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}?format=json"
    
    for _ in range(20): 
        time.sleep(10)
        snap_response = requests.get(snapshot_url, headers={"Authorization": f"Bearer {BRIGHT_DATA_API_KEY}"})
        
        if snap_response.status_code == 200:
            print("Data is ready :)")
            return snap_response.json()  
        else:
            print("Not ready yet, waiting :(")
    
    return {"error": "Timed out waiting for data"}