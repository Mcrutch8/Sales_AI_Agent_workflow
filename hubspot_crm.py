import json
from security import safe_requests

# Purpose:
#This file retrieves contacts from HubSpot, extracts key details, and stores them in contacts.json. 
#It only needs to run occasionally (e.g., weekly) to refresh the contact list.


# HubSpot Private App Access Token
ACCESS_TOKEN = "pat-na2-29c4e905-5e62-4f68-9e14-545b249c131b"

# HubSpot API endpoint for fetching contacts
url = "https://api.hubapi.com/crm/v3/objects/contacts"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

def fetch_contacts():
    """Fetch contacts from HubSpot and store them in a JSON file."""
    response = safe_requests.get(url, headers=headers)
    
    if response.status_code == 200:
        contacts = response.json().get("results", [])
        
        for contact in contacts:
            contact["day_count"] = 0  # Initialize cadence tracking

        with open("contacts.json", "w") as f:
            json.dump(contacts, f, indent=2)
        
        print(f"✅ {len(contacts)} contacts saved to contacts.json.")
    else:
        print(f"❌ Error: {response.status_code}, {response.text}")
