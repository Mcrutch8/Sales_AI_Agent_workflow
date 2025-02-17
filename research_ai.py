import os
from langchain.chat_models import ChatOpenAI
from langchain_community.utilities import GoogleSerperAPIWrapper
from langchain_core.tools import Tool
from dotenv import load_dotenv

# Load API keys
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_SERPER_API_KEY = os.getenv("GOOGLE_SERPER_API_KEY")

# Initialize AI tools
llm = ChatOpenAI(
    openai_api_key=OPENAI_API_KEY,
    model_name="gpt-4",
    temperature=0.7
)
search = GoogleSerperAPIWrapper(serper_api_key=GOOGLE_SERPER_API_KEY)

# Get company info
def get_company_info(company_name):
    if not company_name:
        return "No company information available."
    search_query = f"{company_name} company profile"
    results = search.run(search_query)
    return results[:500] if results else "No relevant company details found."

def generate_email(contact, company_info):
    """Generate a personalized outreach email."""
    name = contact.get("name", "Unknown Contact")
    company = contact.get("company", "No Company")

    prompt = f"""
    You are a sales representative reaching out to {name} at {company}.

    Here is some company information:
    {company_info}

    The outreach is on day {contact['day_count']}. Craft an appropriate email.
    """

    return llm.invoke(prompt)  # Fix: Use .invoke() instead of llm(prompt)



# Generate call notes
def generate_call_notes(contact, company_info):
    prompt = f"""
    You have a sales call with {contact['firstname']} {contact['lastname']} at {contact['company']}.
    
    Here is some company information:
    {company_info}

    Summarize key talking points and insights for the call.
    """
    return llm.invoke(prompt)  # Fix: Use .invoke() instead of llm(prompt)
