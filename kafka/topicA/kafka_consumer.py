from confluent_kafka import Consumer, KafkaException
import json
import mysql.connector

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'my-kafka-app',
    'group.id': 'my-consumer-group'  # Ensure the consumer group ID is the same as used in Kafka console consumer
}

mysql_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Nitin@123',
    'database': 'kafka'
}

consumer = Consumer(conf)
consumer.subscribe(['topicB'])

mysql_conn = mysql.connector.connect(**mysql_config)
mysql_cursor = mysql_conn.cursor()

def consume_messages():
    try:
        while True:
            msg = consumer.poll(timeout=1.0)
            if msg is None:
                continue
            if msg.error():
                if msg.error().code() == KafkaException._PARTITION_EOF:
                    continue
                else:
                    print(f"Kafka error: {msg.error()}")
                    break

            # Process received message
            json_data = msg.value().decode('utf-8')
            data = json.loads(json_data)

            # Insert JSON data into MySQL table
            insert_query = "INSERT INTO your_table (key_column, json_data) VALUES (%s, %s)"
            insert_values = (data.get('key', ''), json_data)
            mysql_cursor.execute(insert_query, insert_values)
            mysql_conn.commit()

            print(f"Inserted data into MySQL: {data}")

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Exception occurred: {e}")

    finally:
        consumer.close()
        mysql_cursor.close()
        mysql_conn.close()

if __name__ == '__main__':
    consume_messages()
