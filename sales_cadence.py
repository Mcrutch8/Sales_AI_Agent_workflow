import json
import datetime

# Load contacts from the JSON file
def load_contacts(filename="contacts.json"):
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

# Save contacts back to JSON
def save_contacts(contacts, filename="contacts.json"):
    with open(filename, "w") as f:
        json.dump(contacts, f, indent=2)

# Determine outreach action based on `day_count`
def get_outreach_action(day_count):
    cadence = {
        1: "LinkedIn request + Intro Email",
        2: "Phone Call",
        3: "Follow-up Email",
        5: "Second Phone Call",
        7: "Final Email"
    }
    return cadence.get(day_count, None)  # Returns action if day_count matches, else None

# Process and update contacts for daily outreach
def update_sales_cadence():
    contacts = load_contacts()
    today = datetime.date.today().strftime("%Y-%m-%d")

    outreach_list = []

    for contact in contacts:
        contact["day_count"] += 1  # Increment the outreach day count
        action = get_outreach_action(contact["day_count"])

        if action:
            outreach_list.append({
                "id": contact["id"],
                "name": f"{contact['properties'].get('firstname', 'Unknown')} {contact['properties'].get('lastname', 'Unknown')}",
                "email": contact["properties"].get("email", "No Email"),
                "company": contact["properties"].get("company", "No Company"),
                "day_count": contact["day_count"],
                "action": action,
                "date": today
            })

    # Save updated contacts back to JSON
    save_contacts(contacts)

    return outreach_list


