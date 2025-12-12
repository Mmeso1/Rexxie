from kafka import KafkaProducer
import json
from .config import settings


class FraudKafkaProducer:
    def __init__(self):
        self.producer = KafkaProducer(
            bootstrap_servers=settings.kafka_bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    
    def send_transaction(self, transaction_data: dict):
        """Send transaction to Kafka topic"""
        future = self.producer.send(settings.kafka_topic, transaction_data)
        return future.get(timeout=10)
    
    def close(self):
        self.producer.close()
