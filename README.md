# Ads Data Pipeline Simulation

## 🧭 Overview
The **Ads Data Pipeline Simulation** project replicates a real-world advertising analytics pipeline similar to those used by platforms like Google Ads or Meta Ads. It demonstrates the full **data engineering lifecycle** — from event generation and streaming ingestion to transformation, storage, and visualization.

This project showcases scalable data engineering concepts and cloud integration using **Python, Kafka, PySpark, Airflow, and AWS**.

---

## 🧱 System Architecture

### **High-Level Flow**
```
Python + Faker → Kafka → PySpark → AWS S3 → AWS Glue → AWS Athena → QuickSight
```

### **Components**
| Layer | Tools / Services | Description |
|--------|------------------|--------------|
| **Data Generation** | Python, Faker | Simulate ad events (impressions, clicks, conversions). |
| **Ingestion** | Kafka | Stream data in real-time using producers and consumers. |
| **Processing** | PySpark | Clean, aggregate, and compute metrics (CTR, CPC). |
| **Storage** | AWS S3, Glue, Athena | Store raw and processed data; catalog metadata and enable SQL queries. |
| **Visualization** | AWS QuickSight | Build dashboards showing campaign KPIs. |
| **Orchestration** | Airflow | Schedule and monitor daily ETL workflows. |
| **Infrastructure** | Docker, GitHub Actions | Containerized setup and CI/CD automation. |

---

## ⚙️ Setup Instructions

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/ads-data-pipeline.git
cd ads-data-pipeline
```

### **2. Create Virtual Environment & Install Dependencies**
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### **3. Run Data Simulation Script**
Generate synthetic ad events:
```bash
python scripts/generate_ads_data.py
```
This creates a CSV file in `data/raw/` containing simulated ad event data.

### **4. Start Kafka Services**
Use Docker Compose or a local setup to run Kafka:
```bash
docker-compose up -d
```

### **5. Run the Spark Processing Job**
Execute the ETL job to clean and aggregate data:
```bash
spark-submit scripts/spark_processor.py
```

### **6. Deploy to AWS (Optional)**
- Upload processed data to **S3**
- Run **Glue Crawler** to catalog datasets
- Query via **Athena**
- Visualize in **QuickSight**

---

## 📊 Metrics Computed
| Metric | Formula | Description |
|---------|----------|--------------|
| **CTR (Click-Through Rate)** | clicks / impressions | Measures ad engagement. |
| **CPC (Cost Per Click)** | cost / clicks | Measures advertising efficiency. |
| **Conversion Rate** | conversions / clicks | Measures ad effectiveness. |

---

## 🚀 Future Enhancements
- Real-time Lambda triggers for instant data updates.
- REST API for retrieving campaign-level metrics.
- Integration with Snowflake or Redshift for advanced analytics.
- Monitoring dashboards using Grafana.

---

## 🧩 Folder Structure
```
ads-data-pipeline/
│
├── scripts/
│   ├── generate_ads_data.py
│   ├── kafka_producer.py
│   ├── kafka_consumer.py
│   ├── spark_processor.py
│
├── airflow_dags/
│   └── daily_pipeline_dag.py
│
├── data/
│   ├── raw/
│   └── processed/
│
├── docs/
│   ├── PRD.md
│   └── architecture_diagram.png
│
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

## 📈 Success Metrics
| Objective | Target |
|------------|---------|
| Event Generation | ≥ 1 million/day |
| ETL Runtime | ≤ 5 minutes |
| Dashboard Latency | < 5 seconds/query |
| Uptime | 99% |

---

## 🧑‍💻 Author
**Parth Kharkar**  
Data Engineer & Full Stack Developer  
[LinkedIn](https://www.linkedin.com/in/parrthhkharkar) · [GitHub](https://github.com/Parrthh) · [Portfolio](https://parthkharkar.lovable.app/?)

---

## 📄 License
This project is open source and available under the [MIT License](LICENSE).

