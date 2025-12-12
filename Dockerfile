# Dockerfile for Apache Kafka
FROM openjdk:11-jre-slim

# Set environment variables
ENV KAFKA_VERSION=3.6.1 \
    SCALA_VERSION=2.13 \
    KAFKA_HOME=/opt/kafka \
    PATH="${PATH}:/opt/kafka/bin"

# Install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    wget \
    netcat \
    && rm -rf /var/lib/apt/lists/*

# Download and extract Kafka
RUN wget -q "https://archive.apache.org/dist/kafka/${KAFKA_VERSION}/kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz" -O /tmp/kafka.tgz && \
    tar -xzf /tmp/kafka.tgz -C /opt && \
    mv /opt/kafka_${SCALA_VERSION}-${KAFKA_VERSION} ${KAFKA_HOME} && \
    rm /tmp/kafka.tgz

# Create data directories
RUN mkdir -p /var/lib/kafka/data /var/log/kafka

# Set working directory
WORKDIR ${KAFKA_HOME}

# Copy custom server properties if needed
# COPY server.properties ${KAFKA_HOME}/config/

# Expose Kafka ports
# 9092: Kafka broker
# 9093: Kafka broker (SSL)
EXPOSE 9092 9093

# Set up volumes for data persistence
VOLUME ["/var/lib/kafka/data", "/var/log/kafka"]

# Default command to start Kafka server
CMD ["kafka-server-start.sh", "config/server.properties"]
