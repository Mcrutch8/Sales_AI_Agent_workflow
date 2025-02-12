import requests
import json

# HubSpot API Key (replace with your actual key)
HUBSPOT_API_KEY = "your_api_key_here"

# HubSpot API URL
HUBSPOT_CONTACTS_URL = "https://api.hubapi.com/crm/v3/objects/contacts"

# Headers for API request
HEADERS = {
    "Authorization": f"Bearer {HUBSPOT_API_KEY}",
    "Content-Type": "application/json"
}

# Function to fetch contacts
def fetch_contacts():
    params = {
        "limit": 100,  # Adjust as needed
        "properties": ["firstname", "lastname", "email", "phone", "company"]
    }
    
    response = requests.get(HUBSPOT_CONTACTS_URL, headers=HEADERS, params=params)
    
    if response.status_code == 200:
        contacts = response.json().get("results", [])
        
        customer_data = []
        for contact in contacts:
            customer_data.append({
                "name": f"{contact.get('properties', {}).get('firstname', '')} {contact.get('properties', {}).get('lastname', '')}",
                "email": contact.get("properties", {}).get("email", ""),
                "phone": contact.get("properties", {}).get("phone", ""),
                "company": contact.get("properties", {}).get("company", ""),
                "day_count": 15  # Initialize day count
            })
        
        # Save to JSON file
        with open("customers.json", "w") as file:
            json.dump(customer_data, file, indent=4)
        
        print("Customer data saved successfully.")
    else:
        print(f"Error fetching contacts: {response.status_code} - {response.text}")

# Run the function
fetch_contacts()