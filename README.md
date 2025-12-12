# Rexxie
Real Time Explainable Fraud Agent

## Overview

Rexxie is a real-time fraud detection system that leverages Apache Kafka for streaming transaction data and identifying fraudulent activities.

## Apache Kafka Setup

This project includes a complete Apache Kafka setup for real-time event streaming. See [KAFKA_SETUP.md](KAFKA_SETUP.md) for detailed instructions on:

- Starting Kafka and Zookeeper
- Creating and managing topics
- Producing and consuming messages
- Monitoring with Kafka UI

### Quick Start

```bash
# Start Kafka ecosystem
docker-compose up -d

# Access Kafka UI at http://localhost:8080
```

For more information, see the [Kafka Setup Guide](KAFKA_SETUP.md).
