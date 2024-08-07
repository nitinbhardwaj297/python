#.\bin\windows\kafka-console-producer.bat --broker-list localhost:9092 --topic topicC
#.\bin\windows\kafka-console-consumer.bat --bootstrap-server localhost:9092 --topic topicC --from-beginning


from confluent_kafka import Producer, KafkaException
import json
import logging

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

conf = {
    'bootstrap.servers': 'localhost:9092',
    'client.id': 'my-app'
}

def delivery_report(err, msg):
    """Called once for each message produced to indicate delivery result."""
    if err is not None:
        logger.error(f'Message delivery failed: {err}')
    else:
        logger.info(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# Example JSON data
data = {
    'key': 'nitin',
    'number': 50,
}

# Serialize JSON to UTF-8 encoded bytes
json_str = json.dumps(data)
json_data = json_str.encode('utf-8')

producer = Producer(conf)

# Produce data to a Kafka topic
try:
    producer.produce('topicC', json_data, callback=delivery_report)
    producer.flush()
except KafkaException as e:
    logger.error(f'Failed to produce message: {e}')
except Exception as e:
    logger.error(f'Exception occurred: {e}')
finally:
    # Close the producer
    producer.poll(0)

logger.info('Producer finished execution')
