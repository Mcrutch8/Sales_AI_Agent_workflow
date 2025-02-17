AI Sales Agent Workflow

This project automates sales outreach using HubSpot CRM, LangChain, OpenAI (GPT-4), and Google Serper API. It follows a structured sales cadence to determine daily outreach actions, generate AI-powered emails and call notes, and provide company insights.

Project Structure

main.py - Runs the full workflow

hubspot_crm.py - Fetches contacts from HubSpot

sales_cadence.py - Updates outreach actions

research_ai.py - Searches for company info and generates content

.env - Stores API keys

contacts.json - Stores contact data