from confluent_kafka import Consumer, KafkaException, KafkaError
import json

# Kafka configuration
conf = {'bootstrap.servers': 'localhost:9092',
        'group.id': 'my-group',
        'auto.offset.reset': 'earliest'}

consumer = Consumer(conf)
consumer.subscribe(['topicB'])

try:
    while True:
        msg = consumer.poll(timeout=1.0)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                continue
            else:
                print(msg.error())
                break

        # Process JSON message
        data = json.loads(msg.value().decode('utf-8'))
        print(data)

        # Insert data into database (pseudo code)
        # db.insert(data['user_id'], data['phone_number'], ...)

except KeyboardInterrupt:
    pass

finally:
    consumer.close()
