#.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic topicB
#.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic topicB --from-beginning

from confluent_kafka import Producer
import json

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'my-kafka-app'
}

# Example JSON data
data = {
    'key': 'value',
    'number': 42,
    'nested': {
        'key': 'nested_value'
    }
}

# Serialize JSON to UTF-8 encoded bytes
json_str = json.dumps(data)  # Use json.dumps() to serialize data to a JSON formatted string
json_data = json_str.encode('utf-8')

producer = Producer(conf)

# Produce data to a Kafka topic
producer.produce('topicB', json_data)

producer.flush()
producer.poll(0)
producer.close()







