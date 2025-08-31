# 🚀 Real-Time Data Streaming Pipeline: MySQL → ClickHouse Cloud

This project demonstrates a **real-time data streaming pipeline** that captures live changes from **MySQL** and streams them into **ClickHouse Cloud** for lightning-fast analytics.
It uses **Python, Debezium, Kafka, Kafka Connect, and Docker Compose** to build a scalable, containerized solution.

---
## 📸 Architecture Overview  

![Pipeline Architecture](./architecture.jpeg)  

---
## 📌 Project Overview

The pipeline enables **continuous data flow** from source to destination with minimal latency:

1. **Data Simulation** – A Python script generates IoT-like sensor data and inserts it into **MySQL**.
2. **Change Data Capture (CDC)** – **Debezium** monitors MySQL and captures all inserts/updates in real time.
3. **Streaming Transport** – **Apache Kafka** handles event streaming between source and sink.
4. **Sink Integration** – **Kafka Connect** with the **ClickHouse Sink Connector** writes Kafka events into **ClickHouse Cloud** tables.
5. **Containerized Setup** – All components run seamlessly via **Docker Compose**.

---

## 🧩 Tech Stack  

- ✅ **Python** – data generation & insertion into MySQL  
- ✅ **MySQL** – source database  
- ✅ **Debezium** – CDC from MySQL  
- ✅ **Apache Kafka** – event streaming platform  
- ✅ **Kafka Connect** – integration framework  
- ✅ **ClickHouse Sink Connector** – loads data into ClickHouse Cloud  
- ✅ **ClickHouse Cloud** – destination for real-time analytics  
- ✅ **Docker Compose** – container orchestration  

---
