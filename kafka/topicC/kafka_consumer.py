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

def insert_into_mysql(data):
    try:
        # Assuming 'data' is a JSON object or dictionary received from Kafka
        query = "INSERT INTO your_table_name (column1, column2, ...) VALUES (%s, %s, ...)"
        values = (data['column1_value'], data['column2_value'], ...)  # Adjust according to your JSON structure
        
        mysql_cursor.execute(query, values)
        mysql_conn.commit()
        logger.info("Inserted into MySQL database successfully")
    except mysql.connector.Error as err:
        logger.error(f"Error inserting into MySQL: {err}")

# Create Kafka consumer
consumer = Consumer(conf)
consumer.subscribe(['topicC'])

# Connect to MySQL
mysql_conn = mysql.connector.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor()

# Consume messages from Kafka
try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                logger.error(f"Consumer error: {msg.error()}")
                break
        
        # Process message
        try:
            # Assuming messages are JSON strings
            data = json.loads(msg.value().decode('utf-8'))
            insert_into_mysql(data)
        except json.JSONDecodeError as e:
            logger.error(f"Error decoding JSON: {e}")
        except Exception as e:
            logger.error(f"Error processing message: {e}")
except KeyboardInterrupt:
    pass
finally:
    consumer.close()
    mysql_cursor.close()
    mysql_conn.close()




























# def consume_messages():
#     try:
#         while True:
#             msg = consumer.poll(timeout=1.0)
#             if msg is None:
#                 continue
#             if msg.error():
#                 if msg.error().code() == KafkaException._PARTITION_EOF:
#                     continue
#                 else:
#                     logger.error(f"Kafka error: {msg.error()}")
#                     break

#             # Process received message
#             try:
#                 json_data = msg.value().decode('utf-8')
#                 data = json.loads(json_data)
#             except json.JSONDecodeError as e:
#                 logger.error(f"Error decoding JSON: {e}")
#                 continue

#             # Insert JSON data into MySQL table
#             insert_query = "INSERT INTO your_table (key_column, json_data) VALUES (%s, %s)"
#             insert_values = (data.get('key', ''), json_data)
#             mysql_cursor.execute(insert_query, insert_values)
#             mysql_conn.commit()

#             logger.info(f"Inserted data into MySQL: {data}")

#     except KeyboardInterrupt:
#         pass
#     except Exception as e:
#         logger.error(f"Exception occurred: {e}")

#     finally:
#         consumer.close()
#         mysql_cursor.close()
#         mysql_conn.close()

