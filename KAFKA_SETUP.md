# Kafka Apache Setup for Rexxie

This directory contains Docker configurations for running Apache Kafka for the Rexxie fraud detection system.

## Prerequisites

- Docker (20.10+)
- Docker Compose (1.29+)

## Quick Start

### Using Docker Compose (Recommended)

Start the entire Kafka ecosystem (Zookeeper, Kafka, and Kafka UI):

```bash
docker-compose up -d
```

This will start:
- **Zookeeper** on port 2181
- **Kafka Broker** on ports 9092 (external) and 9093 (internal)
- **Kafka UI** on port 8080 (accessible at http://localhost:8080)

### Using Dockerfile Only

Build the Kafka image:

```bash
docker build -t rexxie-kafka .
```

Run Kafka (requires a running Zookeeper instance):

```bash
docker run -d --name kafka \
  -p 9092:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=<zookeeper-host>:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  rexxie-kafka
```

## Kafka Configuration

### Environment Variables

The Dockerfile and docker-compose.yml support the following key configurations:

- `KAFKA_BROKER_ID`: Unique broker identifier (default: 1)
- `KAFKA_ZOOKEEPER_CONNECT`: Zookeeper connection string
- `KAFKA_ADVERTISED_LISTENERS`: How clients connect to Kafka
- `KAFKA_AUTO_CREATE_TOPICS_ENABLE`: Auto-create topics on first use
- `KAFKA_LOG_DIRS`: Directory for Kafka data storage

### Ports

- **9092**: External Kafka broker port
- **9093**: Internal Kafka broker port (for inter-container communication)
- **2181**: Zookeeper client port
- **8080**: Kafka UI web interface

## Usage Examples

### Create a Topic

```bash
docker exec -it rexxie-kafka kafka-topics.sh \
  --create \
  --topic fraud-transactions \
  --bootstrap-server localhost:9092 \
  --partitions 3 \
  --replication-factor 1
```

### List Topics

```bash
docker exec -it rexxie-kafka kafka-topics.sh \
  --list \
  --bootstrap-server localhost:9092
```

### Produce Messages

```bash
docker exec -it rexxie-kafka kafka-console-producer.sh \
  --topic fraud-transactions \
  --bootstrap-server localhost:9092
```

### Consume Messages

```bash
docker exec -it rexxie-kafka kafka-console-consumer.sh \
  --topic fraud-transactions \
  --from-beginning \
  --bootstrap-server localhost:9092
```

## Data Persistence

Data is persisted using Docker volumes:
- `kafka-data`: Kafka message data
- `kafka-logs`: Kafka logs
- `zookeeper-data`: Zookeeper data
- `zookeeper-logs`: Zookeeper logs

## Monitoring

Access the Kafka UI at http://localhost:8080 to:
- View topics and messages
- Monitor consumer groups
- Check broker health
- Manage Kafka configurations

## Stopping Services

```bash
# Stop all services
docker-compose down

# Stop and remove volumes (WARNING: This deletes all data)
docker-compose down -v
```

## For Fraud Detection Use Cases

This Kafka setup is optimized for real-time fraud detection scenarios:

1. **Transaction Events**: Stream transaction data to topics for real-time analysis
2. **Fraud Alerts**: Publish detected fraud events to dedicated topics
3. **Model Updates**: Stream model updates and feature engineering results
4. **Audit Logs**: Maintain audit trails of all fraud detection activities

### Suggested Topics

```bash
# Create fraud detection topics
docker exec -it rexxie-kafka kafka-topics.sh --create --topic transactions --partitions 5 --bootstrap-server localhost:9092
docker exec -it rexxie-kafka kafka-topics.sh --create --topic fraud-alerts --partitions 3 --bootstrap-server localhost:9092
docker exec -it rexxie-kafka kafka-topics.sh --create --topic model-updates --partitions 1 --bootstrap-server localhost:9092
docker exec -it rexxie-kafka kafka-topics.sh --create --topic audit-logs --partitions 2 --bootstrap-server localhost:9092
```

## Troubleshooting

### Check Kafka Logs

```bash
docker logs rexxie-kafka
```

### Check Zookeeper Logs

```bash
docker logs rexxie-zookeeper
```

### Verify Kafka is Running

```bash
docker exec -it rexxie-kafka kafka-broker-api-versions.sh --bootstrap-server localhost:9092
```

## Version Information

- Apache Kafka: 3.6.1
- Scala: 2.13
- Java: OpenJDK 11
- Zookeeper: Confluent Platform 7.5.3
