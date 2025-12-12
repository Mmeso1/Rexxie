# Fraud Detection Platform

A real-time fraud detection platform powered by AI and event-driven architecture.

## Architecture

This platform consists of:

### Backend Services

#### FastAPI App (`backend/fastapi_app`)
- Main API service for handling fraud detection requests
- Kafka integration for event streaming
- Transaction processing and validation

**Key Components:**
- `main.py`: FastAPI application entry point
- `config.py`: Configuration management
- `schemas.py`: Pydantic models for data validation
- `kafka_consumer.py`: Kafka consumer for processing events
- `kafka_producer.py`: Kafka producer for publishing events

#### AI Service (`backend/ai_service`)
- AI-powered fraud analysis using Google Gemini
- Explainable AI for fraud detection decisions

**Key Components:**
- `main.py`: FastAPI service for AI operations
- `gemini_client.py`: Google Gemini API integration

### Frontend

#### Next.js App (`frontend/nextjs-app`)
- User interface for monitoring and analyzing transactions
- Real-time dashboard for fraud detection

### Infrastructure

#### Docker Compose (`infra/docker-compose.yml`)
- Orchestrates all services
- Includes Kafka and Zookeeper for event streaming
- Manages service dependencies and networking

## Getting Started

### Prerequisites
- Docker and Docker Compose
- Google Gemini API key (for AI service)

### Environment Variables
Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key_here
KAFKA_BOOTSTRAP_SERVERS=localhost:9092
KAFKA_TOPIC=fraud-transactions
```

### Running the Platform

1. Navigate to the infrastructure directory:
```bash
cd fraud-platform/infra
```

2. Start all services:
```bash
docker-compose up -d
```

3. Access the services:
- FastAPI Backend: http://localhost:8000
- AI Service: http://localhost:8001
- Next.js Frontend: http://localhost:3000

### Development

Each service can be developed independently:

#### FastAPI App
```bash
cd backend/fastapi_app
pip install -r requirements.txt
uvicorn app.main:app --reload
```

#### AI Service
```bash
cd backend/ai_service
pip install -r requirements.txt
uvicorn app.main:app --port 8001 --reload
```

#### Next.js App
```bash
cd frontend/nextjs-app
npm install
npm run dev
```

## Features

- **Real-time Fraud Detection**: Process transactions in real-time
- **Explainable AI**: Get clear explanations for fraud predictions
- **Event-Driven Architecture**: Scalable Kafka-based messaging
- **Modern Stack**: FastAPI, Next.js, and Google Gemini AI

## License

MIT
