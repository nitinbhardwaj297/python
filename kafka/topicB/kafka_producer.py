from confluent_kafka import Producer

conf = {
    'bootstrap.servers': 'localhost:9092',  # Corrected property name
    'client.id': 'my-kafka-app'
}

# Create a Kafka Producer instance
producer = Producer(conf)

topic = 'topicC'

def delivery_report(err, msg):
    if err is not None:
        print(f"Failed to deliver message: {err}")
    else:
        print(f"Message delivered to {msg.topic()} [{msg.partition()}]")

for i in range(5):
    producer.produce(topic, f"message {i}".encode('utf-8'), callback=delivery_report)


producer.flush()
producer.poll(0)

producer.close()
