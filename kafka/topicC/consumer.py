from confluent_kafka import Consumer, KafkaException
import json
import mysql.connector
import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'my-app',
    'group.id': 'my-consumer-group'
}

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Indialends@12345',
    'database': 'kafka'
}

consumer = Consumer(conf)
consumer.subscribe(['topicC'])

mysql_conn = mysql.connector.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor()
mysql_cursor.execute("")
# Consume messages
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            raise KafkaException(msg.error())

        # Decode message value from byte array
        data = json.loads(msg.value().decode('utf-8'))

        # Validate JSON structure
        if 'key' in data and 'number' in data:
            # Insert into database (example: MySQL)
            mysql_cursor.execute("INSERT INTO example_table (key_field, number_field) VALUES (%s, %s)", (data['key'], data['number']))
            db.commit()
            print(f"Inserted: {data}")
        else:
            print("Invalid JSON data received")

except KeyboardInterrupt:
    pass

finally:
    # Close Kafka consumer
    consumer.close()