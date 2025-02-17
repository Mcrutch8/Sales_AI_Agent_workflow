# Sales_AI_Agent_workflow

README: AI Sales Agent Workflow
This AI-powered sales agent automates the sales outreach process by:
 Pulling contacts from HubSpot CRM
 Tracking & updating outreach cadence (LinkedIn requests, emails, calls)
 Searching the web for company insights
 Generating AI-powered emails & call notes
 Providing a structured daily outreach list

 1. Project Overview
This project automates and optimizes a structured sales outreach workflow using LangChain, OpenAI (GPT-4), and Google Serper API.

It follows a sales cadence system, where each contact progresses through a sequence of outreach activities:

Day Count	Outreach Action
Day 1	LinkedIn Request + Intro Email
Day 2	Phone Call
Day 3	Follow-up Email
Day 5	Second Phone Call
Day 7	Final Email
At 8 AM PT every day, the system:

Reads contacts.json to check where each contact is in the cadence
Determines today’s outreach actions
Searches the web for company details
Uses GPT-4 to generate emails & call notes
Displays a structured outreach report
 2. Project Structure
bash
Copy
Edit
sales_ai_agent/
│── main.py                   # Runs the full workflow daily
│── hubspot_crm.py             # Fetches contacts from HubSpot CRM
│── sales_cadence.py           # Updates day_count & determines outreach actions
│── research_ai.py             # Searches web for company info & generates emails/call notes
│── .env                        # Stores API keys securely
│── contacts.json               # Stored contact data (updated daily)
│── README.md                   # Project documentation
 3. Installation & Setup
 Prerequisites
Python 3.8+
HubSpot CRM Account
Google Serper API Key (for web search)
OpenAI API Key (for GPT-4 email/call generation)
 Step 1: Clone Repository
bash
Copy
Edit
git clone https://github.com/your-repo/Sales_AI_Agent_workflow.git
cd Sales_AI_Agent_workflow
 Step 2: Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
(If requirements.txt does not exist, manually install:)

bash
Copy
Edit
pip install langchain openai google-search-results python-dotenv requests
 Step 3: Set Up API Keys
Create a .env file in the root directory:

env
Copy
Edit
OPENAI_API_KEY=your_openai_api_key
GOOGLE_SERPER_API_KEY=your_google_serper_api_key
HUBSPOT_API_KEY=your_hubspot_api_key
 4. How It Works
 Step 1: Fetch Contacts from HubSpot
Runs hubspot_crm.py to pull contacts from your HubSpot CRM
Saves them in contacts.json
 Run manually when needed:

bash
Copy
Edit
python hubspot_crm.py
 Step 2: Update Sales Cadence
Runs sales_cadence.py to:  Increment day_count for all contacts
 Determine today’s outreach actions
 Run manually when needed:

bash
Copy
Edit
python sales_cadence.py
 Step 3: Research & AI-Generated Content
Runs research_ai.py to:  Search for company details using Google Serper API
 Generate AI-powered emails or call notes using GPT-4
 Run manually when needed:

bash
Copy
Edit
python research_ai.py
 Step 4: Run Full Outreach Workflow
Run main.py to execute the entire sales workflow:

bash
Copy
Edit
python main.py
 Processes contacts
 Finds company info
 Generates emails & call notes
 Displays a structured outreach report

 5. Example Output
vbnet
Copy
Edit
 **Outreach Summary**
 2 contacts require outreach today.

 **Processing Outreach for John Doe at Acme Corp**
 Action: Phone Call (Day 2)
 Company Info: Acme Corp recently raised $10M in funding and is hiring for AI roles...

 **Call Notes for John Doe:**
- Acme Corp is expanding into AI-driven solutions.
- Mention how our product aligns with their growth strategy.
- Ask about their vendor onboarding process.

 **Processing Outreach for Jane Smith at Tech Innovations**
 Action: Follow-up Email (Day 3)
 Company Info: Tech Innovations recently launched a new SaaS platform...

 **Generated Email for Jane Smith:**
Subject: Quick Follow-up from Our Last Conversation  

Hi Jane,  
I wanted to follow up on our last discussion. Given Tech Innovations' recent expansion, I believe we have some valuable insights to share.  
Would love to set up a call this week!  

Best,  
[Your Name]

 **Outreach processing completed.**
 6. Troubleshooting & FAQs
 1. No contacts are showing up in outreach?
 Run:

bash
Copy
Edit
python hubspot_crm.py
python sales_cadence.py
python main.py
Ensure contacts.json is populated.


 
