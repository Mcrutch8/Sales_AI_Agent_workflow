from hubspot_crm import fetch_contacts
from sales_cadence import update_sales_cadence, get_outreach_action
from research_ai import get_company_info, generate_email, generate_call_notes

# Step 1: Pull contacts from HubSpot (Run only when necessary)
fetch_contacts()

# Step 2: Update sales cadence and get today's outreach list
outreach_today = update_sales_cadence()

# 🟢 Display outreach summary
print("\n📢 **Outreach Summary**")
print(f"🔹 {len(outreach_today)} contacts require outreach today.\n")

# Step 3: Process outreach actions
for contact in outreach_today:
    name = contact["name"]
    company = contact["company"]
    action = contact["action"]
    day_count = contact["day_count"]

    print(f"🟢 **Processing Outreach for {name} at {company}**")
    print(f"🔹 Action: {action} (Day {day_count})")

    # Fetch company information
    company_info = get_company_info(company)
    print(f"🔍 Company Info: {company_info[:300]}...\n")  # Truncate for readability

    # Generate AI-generated content
    if action.endswith("Email"):
        email_content = generate_email(contact, company_info)
        print(f"📧 **Generated Email for {name}:**\n{email_content}\n")

    elif action == "Phone Call":
        call_notes = generate_call_notes(contact, company_info)
        print(f"📞 **Call Notes for {name}:**\n{call_notes}\n")

print("✅ **Outreach processing completed.**")
