# 🚀 Unified Sales Analytics Lakehouse | Accenture GTGH Project

[![Databricks](https://img.shields.io/badge/Databricks-FF3621?style=for-the-badge&logo=Databricks&logoColor=white)](https://databricks.com/)
[![Apache Spark](https://img.shields.io/badge/Apache_Spark-FFFFFF?style=for-the-badge&logo=apachespark&logoColor=#E35A16)](https://spark.apache.org/)
[![Microsoft Fabric](https://img.shields.io/badge/Microsoft_Fabric-0078D4?style=for-the-badge&logo=microsoft&logoColor=white)](https://microsoft.com/fabric)
[![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)

> **Team 3 Final Project** for the Accenture "Get Trained - Get Hired" (GTGH) Data Engineering Academy by Code.Hub.

## 📌 Business Context & Problem Statement
This project addresses the data infrastructure challenges of **Multisales**, a mid-size distribution company. The company faced critical analytical limitations due to a fragmented data pipeline, poor data quality (inconsistent data types, invalid dates, missing identifiers, duplicates), and reports that focused only on static totals rather than actionable trends.

**Objective:** Design and implement an end-to-end, scalable analytics pipeline to ingest imperfect operational data (CSV exports), clean and validate it, and serve it through a robust dimensional model for executive reporting.

## 🏗️ Architecture & Tech Stack
The solution implements a **Medallion Lakehouse Architecture** leveraging modern cloud data platforms:

* **Data Processing & Lakehouse:** Databricks, PySpark, Delta Lake
* **Data Integration & Orchestration:** Microsoft Fabric (Data Factory / Dataflow Gen2)
* **Analytics & Visualization:** Power BI (Semantic Models, DAX, Interactive Dashboards)

![Medallion Architecture](https://docs.databricks.com/en/_images/medallion-architecture.png) *(Illustrative Medallion Architecture)*

## ⚙️ Pipeline Implementation Details

### 🥉 Bronze Layer (Raw Ingestion)
* **Goal:** Create an immutable, auditable historical record of the source data.
* **Process:** Raw, imperfect CSV files (Sales transactions, Products, Resellers, Regions, Salespeople, Targets) are ingested directly into Databricks and saved as Bronze Delta tables. No transformations are applied at this stage to preserve data lineage.

### 🥈 Silver Layer (Data Quality & Cleansing)
* **Goal:** Transform Bronze data into a trusted, analytics-ready state applying a "Data Quality Mindset".
* **Process:** 
  * Standardized data types (e.g., parsing dates, casting strings with currency symbols to numeric).
  * Implemented **Data Quality Gates** to handle missing, invalid, or inconsistent values.
  * Applied deduplication logic to ensure reliable primary/foreign keys.
  * Standardized text fields (trimming whitespace, resolving casing variations).

### 🥇 Gold Layer (Dimensional Modeling)
* **Goal:** Serve business-ready metrics using a performant schema.
* **Process:** Modeled the cleansed Silver data into a **Star Schema** (Fact and Dimension tables) optimized for BI tools. Data is stored in Delta format for optimal query performance using Databricks SQL.

### 📊 BI & Consumption (Microsoft Fabric & Power BI)
* **Integration:** Microsoft Fabric Data Factory was utilized to ingest the Gold schema from Databricks into the Fabric Workspace.
* **Semantic Model:** Built a robust Power BI Semantic Model defining core business measures (Sales, Cost, Margin, Target Attainment) using DAX.
* **Reporting:** Developed a 3-page interactive Power BI dashboard featuring KPIs, trend lines, and drill-through capabilities to analyze product, regional, and sales team performance.

# 📁 Repository Structure

```text
📦 Accenture-Final-Project-Team-3
 ┣ 📂 bronze/                 # Scripts/Notebooks for raw data ingestion
 ┣ 📂 silver/                 # Data quality gates and cleansing transformations
 ┣ 📂 gold/                   # Dimensional modeling (Star Schema) for BI
 ┣ 📂 job/                    # Databricks workflow/job configurations and orchestration scripts
 ┣ 📂 models/                 # Architecture diagrams and conceptual data models
 ┣ 📂 power_bi_dashboards/    # Power BI (.pbix) files and dashboard screenshots
 ┣ 📂 reports/                # Final presentation (.pptx) and project documentation
 ┗ 📜 README.md               # Project documentation
--------------------------------------------------------------------------------
This project was developed under the guidance of Code.Hub and Accenture during the GTGH Data Engineering Academy (Feb-Mar 2026).
