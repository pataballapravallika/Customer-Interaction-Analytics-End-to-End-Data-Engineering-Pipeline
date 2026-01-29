import pandas as pd

def extract_data():
    sales_calls = pd.read_csv("data/raw/sales_calls/sales_calls.csv")
    crm_leads = pd.read_csv("data/raw/crm_leads/crm_leads.csv")
    agents = pd.read_csv("data/raw/agents/agents.csv")

    return sales_calls, crm_leads, agents
