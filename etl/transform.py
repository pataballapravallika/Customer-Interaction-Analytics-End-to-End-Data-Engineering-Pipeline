import pandas as pd
from extract import extract_data

def transform_data():
    sales_calls, crm_leads, agents = extract_data()

    # ---------------- DIM AGENT ----------------
    dim_agent = agents.drop_duplicates(subset=["agent_id"])

    # ---------------- DIM CUSTOMER ----------------
    dim_customer = pd.DataFrame(
        sales_calls["customer_id"].drop_duplicates(),
        columns=["customer_id"]
    )

    # ---------------- DIM LEAD ----------------
    dim_lead = crm_leads[["lead_id", "lead_source", "lead_status"]].drop_duplicates()

    # ---------------- DIM DATE ----------------
    sales_calls["call_date"] = pd.to_datetime(sales_calls["call_date"])

    dim_date = sales_calls[["call_date"]].drop_duplicates()
    dim_date["day"] = dim_date["call_date"].dt.day
    dim_date["month"] = dim_date["call_date"].dt.month
    dim_date["year"] = dim_date["call_date"].dt.year
    dim_date.rename(columns={"call_date": "date_id"}, inplace=True)

    # ---------------- FACT CALLS ----------------
    fact_calls = sales_calls.merge(
        crm_leads[["lead_id", "customer_id"]],
        on="customer_id",
        how="left"
    )

    fact_calls = fact_calls[[
        "call_id",
        "agent_id",
        "customer_id",
        "lead_id",
        "call_duration",
        "call_outcome",
        "call_date"
    ]]

    fact_calls.rename(columns={"call_date": "call_date_id"}, inplace=True)

    # ---------------- SAVE TRANSFORMED DATA ----------------
    dim_agent.to_csv("data/processed/dim_agent.csv", index=False)
    dim_customer.to_csv("data/processed/dim_customer.csv", index=False)
    dim_lead.to_csv("data/processed/dim_lead.csv", index=False)
    dim_date.to_csv("data/processed/dim_date.csv", index=False)
    fact_calls.to_csv("data/processed/fact_calls.csv", index=False)

    print("Transformation completed successfully")

if __name__ == "__main__":
    transform_data()
