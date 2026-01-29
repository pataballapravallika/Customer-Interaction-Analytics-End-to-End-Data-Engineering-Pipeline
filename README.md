# Customer Interaction Analytics – End-to-End Data Engineering Pipeline

## 📌 Overview
This project implements a complete end-to-end Data Engineering pipeline to ingest, transform, and analyze multi-source customer interaction data such as sales calls, CRM leads, and agent information. The pipeline processes raw data into an analytics-ready PostgreSQL data warehouse using a star schema and enables business insights through SQL analytics queries.

This project focuses on **ETL pipelines, data modeling, and analytics**, aligning with real-world data engineering workflows.

---

## 🏗️ Architecture
Raw Data → ETL (Python) → PostgreSQL Data Warehouse → Analytics SQL Queries

---

## 🛠️ Tech Stack
- **Language:** Python  
- **Data Processing:** Pandas  
- **Database:** PostgreSQL  
- **SQL:** Star Schema, Analytics Queries  
- **Version Control:** Git & GitHub  

---


---

## 🔄 ETL Pipeline Description

### 1️⃣ Extract
- Ingests raw CSV data from multiple sources:
  - Sales calls
  - CRM leads
  - Agent master data

### 2️⃣ Transform
- Cleans and deduplicates data
- Creates dimension and fact datasets
- Generates a date dimension
- Prepares analytics-ready data

### 3️⃣ Load
- Loads transformed data into PostgreSQL
- Enforces primary and foreign key constraints

---

## 🗄️ Data Warehouse Design
The warehouse follows a **star schema**:

- **Fact Table:** `fact_calls`
- **Dimension Tables:**
  - `dim_agent`
  - `dim_customer`
  - `dim_lead`
  - `dim_date`

---

## 📊 Analytics & Business Insights
Example insights generated using SQL:
- Total calls handled by each agent
- Agent-wise conversion rate
- Average call duration per agent
- Monthly call volume trends
- Lead source performance

---

## 📸 Screenshots
Screenshots demonstrating successful execution and outputs are included below:
- PostgreSQL tables created
- <img width="1509" height="1009" alt="image" src="https://github.com/user-attachments/assets/aae9bddf-8550-4422-81f9-cccc9221a2ca" />

- Data loaded into fact and dimension tables
- <img width="922" height="566" alt="image" src="https://github.com/user-attachments/assets/700b385e-37f7-4ed4-97c3-02276eda37df" />

- Sample analytics SQL query results
- <img width="1056" height="905" alt="image" src="https://github.com/user-attachments/assets/3d5d5c04-a1f7-46af-8312-c6a92be0cdc2" />
- <img width="460" height="439" alt="image" src="https://github.com/user-attachments/assets/b5437da8-4ef2-456c-96e7-65c117081501" />
- <img width="565" height="203" alt="image" src="https://github.com/user-attachments/assets/43692f55-30ee-4f3a-ba0f-0b592b4c0220" />


---

## 🎯 Outcome
The final output is an analytics-ready PostgreSQL data warehouse that can be directly consumed by BI tools, analysts, or downstream machine learning models.

---

## 💬 Interview Explanation
"I built an end-to-end data engineering pipeline where I ingested raw CRM and sales call data, transformed it into dimension and fact tables using Python, loaded it into PostgreSQL with a star schema, and wrote analytical SQL queries to generate business insights."

