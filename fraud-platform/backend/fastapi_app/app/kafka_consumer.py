from kafka import KafkaConsumer
import json
from .config import settings


class FraudKafkaConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            settings.kafka_topic,
            bootstrap_servers=settings.kafka_bootstrap_servers,
            value_deserializer=lambda m: json.loads(m.decode('utf-8')),
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='fraud-detection-group'
        )
    
    def consume_messages(self):
        """Consume messages from Kafka topic"""
        for message in self.consumer:
            yield message.value
    
    def close(self):
        self.consumer.close()
