import mysql.connector
import random
import time
from datetime import datetime

# Connect to MySQL
# MySQL connection config
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='root',
    database='mydb',
    port='3305'
)

cursor = conn.cursor()

try:
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS sensor_data(
        id INT AUTO_INCREMENT PRIMARY KEY,
        sensor_name VARCHAR(50),
        reading FLOAT,
        reading_time DATETIME
    )""")


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS device_status(
        id INT AUTO_INCREMENT PRIMARY KEY,
        device_id VARCHAR(20),
        status VARCHAR(20),
        updated_at DATETIME
    )
    """)


    cursor.execute("""

    CREATE TABLE IF NOT EXISTS alerts(
        id INT AUTO_INCREMENT PRIMARY KEY,
        sensor_name VARCHAR(50),
        alert_type VARCHAR(50),
        severity INT,
        created_at DATETIME
    )
    """)

    cursor.execute("SELECT * FROM sensor_data")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
except Exception as e :
    print(f"Stopped.{e}")

finally:
    cursor.close()
    conn.close()



