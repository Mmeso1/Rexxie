# Dockerfile for Apache Kafka
FROM confluentinc/cp-kafka:7.5.3

# Set environment variables for Kafka
ENV KAFKA_HOME=/usr \
    PATH="${PATH}:/usr/bin"

# Create data directories for custom configurations
RUN mkdir -p /var/lib/kafka/data /var/log/kafka

# Set working directory
WORKDIR /usr

# Expose Kafka ports
# 9092: Kafka broker (external)
# 9093: Kafka broker (internal)
EXPOSE 9092 9093

# Set up volumes for data persistence
VOLUME ["/var/lib/kafka/data", "/var/log/kafka"]

# The base image already contains the startup script
# Default command will be inherited from base image or can be overridden via docker-compose

