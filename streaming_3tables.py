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

# Sample data sources
sensors = ['temperature', 'humidity', 'pressure', 'vibration']
statuses = ['online', 'offline', 'maintenance']
alert_types = ['threshold_exceeded', 'device_error', 'disconnected']

def insert_sensor_data():
    sensor = random.choice(sensors)
    reading = round(random.uniform(10.0, 100.0), 2)
    reading_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute(
        "INSERT INTO sensor_data (sensor_name, reading, reading_time) VALUES (%s, %s, %s)",
        (sensor, reading, reading_time)
    )
    print(f"[sensor_data] Inserted: {sensor}, {reading}, {reading_time}")

def insert_device_status():
    device_id = f"dev-{random.randint(1, 10)}"
    status = random.choice(statuses)
    updated_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute(
        "INSERT INTO device_status (device_id, status, updated_at) VALUES (%s, %s, %s)",
        (device_id, status, updated_at)
    )
    print(f"[device_status] Inserted: {device_id}, {status}, {updated_at}")

def insert_alert():
    sensor = random.choice(sensors)
    alert_type = random.choice(alert_types)
    severity = random.randint(1, 5)
    created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cursor.execute(
        "INSERT INTO alerts (sensor_name, alert_type, severity, created_at) VALUES (%s, %s, %s, %s)",
        (sensor, alert_type, severity, created_at)
    )
    print(f"[alerts] Inserted: {sensor}, {alert_type}, {severity}, {created_at}")

try:
    while True:
        insert_sensor_data()
        insert_device_status()
        insert_alert()
        conn.commit()
        time.sleep(2)  # Wait 2 seconds between inserts
except KeyboardInterrupt:
    print("Stopped.")
finally:
    cursor.close()
    conn.close()
