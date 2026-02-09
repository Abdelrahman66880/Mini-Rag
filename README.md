# Mini-RAG: A Lightweight Retrieval-Augmented Generation Framework

<div align="center">

![FastAPI](https://img.shields.io/badge/FastAPI-0.110.2-009688?style=flat-square&logo=fastapi)
![Python](https://img.shields.io/badge/Python-3.8+-3776ab?style=flat-square&logo=python)
![MongoDB](https://img.shields.io/badge/MongoDB-7-13aa52?style=flat-square&logo=mongodb)
![Qdrant](https://img.shields.io/badge/Qdrant-VectorDB-1a3d5c?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

A modular, production-ready Retrieval-Augmented Generation (RAG) framework designed for scalable document processing, semantic search, and intelligent query responses.

[Documentation](#documentation) • [Quick Start](#quick-start) • [API Reference](#api-endpoints) • [Architecture](#architecture)

</div>

---

## 📋 Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Prerequisites](#prerequisites)
- [Quick Start](#quick-start)
- [Installation](#installation)
- [Configuration](#configuration)
- [API Endpoints](#api-endpoints)
- [Project Structure](#project-structure)
- [Development](#development)
- [Docker Deployment](#docker-deployment)
- [Contributing](#contributing)
- [License](#license)

---

## 🎯 Overview

**Mini-RAG** is a lightweight yet powerful framework for building Retrieval-Augmented Generation systems. It enables organizations to integrate their documents with Large Language Models (LLMs), providing accurate, context-aware responses grounded in specific data sources.

### Use Cases
- **Document Intelligence**: Extract insights from large document repositories
- **Knowledge Base Systems**: Build intelligent search and Q&A systems
- **Content Analysis**: Process and analyze multi-format documents at scale
- **Enterprise Search**: Context-aware search with semantic understanding

---

## ✨ Key Features

### 🔄 Multi-LLM Support
- **OpenAI**: GPT-3.5, GPT-4 integration
- **Cohere**: Alternative LLM provider with competitive pricing
- Extensible provider factory pattern for easy integration of new LLM services

### 🧠 Advanced Vector Database Integration
- **Qdrant**: High-performance vector database for semantic search
- Efficient embedding management and similarity search
- Scalable storage for millions of document chunks

### 📁 Document Processing
- Multi-format support (PDF, TXT, and extensible to other formats)
- Intelligent chunking with configurable overlap
- Automatic extraction and metadata preservation
- Built-in validation and error handling

### 📊 Data Management
- **MongoDB** integration for persistent metadata storage
- Project-based organization for multi-tenant scenarios
- Asset tracking with versioning capabilities
- Comprehensive audit trails

### 🎨 Flexible Templating
- Multi-language support for prompts and responses
- Locale-aware response generation
- Customizable prompt templates for various use cases
- Dynamic language fallback mechanisms

### 🔌 RESTful API
- Clean, RESTful endpoint design
- Comprehensive error handling
- Request validation with Pydantic
- Async/await for high-performance I/O

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                      FastAPI Application                    │
├─────────────────────────────────────────────────────────────┤
│                      Routes Layer                           │
│        ┌──────────────┬──────────────┬─────────────┐        │
│        │   Base API   │  Data Routes │ NLP Routes  │        │
│        └──────────────┴──────────────┴─────────────┘        │
├─────────────────────────────────────────────────────────────┤
│                    Controllers Layer                        │
│    ┌────────────┬──────────────┬────────────────┐           │
│    │   Data     │  Project     │  Processing    │           │
│    │ Controller │ Controller   │ Controller     │           │
│    └────────────┴──────────────┴────────────────┘           │
├─────────────────────────────────────────────────────────────┤
│                     Models/Schemas Layer                    │
│    ┌──────────┬──────────┬──────────┬─────────┐            │
│    │ Project  │ Chunk    │ Asset    │  Data   │            │
│    │ Model    │ Model    │ Model    │ Scheme  │            │
│    └──────────┴──────────┴──────────┴─────────┘            │
├─────────────────────────────────────────────────────────────┤
│                   Storage & Integration Layer               │
│    ┌─────────────────────┬──────────────────────┐           │
│    │  Vector Database    │   Relational DB      │           │
│    │  (Qdrant, VectorDB) │  (MongoDB)           │           │
│    └─────────────────────┴──────────────────────┘           │
│    ┌─────────────────────┬──────────────────────┐           │
│    │   LLM Providers     │  File Storage        │           │
│    │  (OpenAI, Cohere)   │  (Local Filesystem)  │           │
│    └─────────────────────┴──────────────────────┘           │
└─────────────────────────────────────────────────────────────┘
```

---

## 📋 Prerequisites

- **Python 3.8+**
- **Docker & Docker Compose** (for containerized deployment)
- **MongoDB 7.x** (for metadata storage)
- **API Keys**:
  - OpenAI API Key (for GPT models)
  - Cohere API Key (for Cohere models)

---

## 🚀 Quick Start

### Option 1: Local Development

```bash
# Clone the repository
git clone https://github.com/yourusername/Mini-Rag.git
cd Mini-Rag

# Create Python virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
cd src
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings and API keys

# Run the application
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Option 2: Docker Deployment

```bash
# Navigate to docker directory
cd docker

# Build and start services
docker-compose up -d

# Check service status
docker-compose ps

# View logs
docker-compose logs -f
```

---

## ⚙️ Installation

### Detailed Setup Instructions

```bash
# 1. Install system dependencies (Ubuntu/Debian)
sudo apt-get update
sudo apt-get install python3.11 python3-pip python3-venv

# 2. Clone repository
git clone <repository-url>
cd Mini-Rag

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install Python dependencies
cd src
pip install -r requirements.txt

# 5. Create .env file with required variables
cat > .env << EOF
# Application
APP_NAME=Mini-RAG
APP_VERSION=1.0.0

# Database
MONGODB_URL=mongodb://localhost:27017
MONGODB_DATABASE=mini_rag

# LLM Configuration
GENERATION_BACKEND=openai  # or cohere
GENERATION_MODEL_ID=gpt-3.5-turbo
EMBEDDING_BACKEND=openai
EMBEDDING_MODEL_ID=text-embedding-3-small
EMBEDDING_MODEL_SIZE=1536

# API Keys
OPENAI_API_KEY=sk-your-key-here
COHERE_API_KEY=your-cohere-key-here

# Vector Database
VECTOR_DB_BACKEND=qdrant
VECTOR_DB_PATH=./assets/database/qdrant_db
VECTOR_DB_DISTANCE_METHOD=cosine

# File Processing
FILE_ALLOWED_TYPES=['pdf', 'txt']
FILE_MAX_SIZE=52428800  # 50MB in bytes
FILE_DEFAULT_CHUNK_SIZE=8192

# Language
DEFAULT_LANG=en
PRIMARY_LANG=en
EOF

# 6. Start the application
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

---

## 🔧 Configuration

### Environment Variables

| Variable | Type | Default | Description |
|----------|------|---------|-------------|
| `APP_NAME` | str | Mini-RAG | Application name |
| `APP_VERSION` | str | 1.0.0 | Application version |
| `MONGODB_URL` | str | - | MongoDB connection string |
| `MONGODB_DATABASE` | str | mini_rag | Database name |
| `GENERATION_BACKEND` | str | openai | LLM provider for generation (openai, cohere) |
| `GENERATION_MODEL_ID` | str | gpt-3.5-turbo | Model ID for generation |
| `EMBEDDING_BACKEND` | str | openai | LLM provider for embeddings |
| `EMBEDDING_MODEL_ID` | str | text-embedding-3-small | Model for embeddings |
| `EMBEDDING_MODEL_SIZE` | int | 1536 | Embedding vector dimension |
| `OPENAI_API_KEY` | str | - | OpenAI API key |
| `COHERE_API_KEY` | str | - | Cohere API key |
| `VECTOR_DB_BACKEND` | str | qdrant | Vector database backend |
| `VECTOR_DB_PATH` | str | ./assets/database/qdrant_db | Vector DB storage path |
| `VECTOR_DB_DISTANCE_METHOD` | str | cosine | Distance metric (cosine, euclidean, manhattan) |
| `FILE_MAX_SIZE` | int | 52428800 | Max upload file size (bytes) |
| `FILE_DEFAULT_CHUNK_SIZE` | int | 8192 | Document chunk size (bytes) |
| `PRIMARY_LANG` | str | en | Primary language for responses |
| `DEFAULT_LANG` | str | en | Fallback language |

---

## 🔌 API Endpoints

### Base Endpoints

#### GET `/api/v1/`
Retrieve application information and version.

**Response:**
```json
{
  "app_name": "Mini-RAG",
  "app_version": "1.0.0"
}
```

---

### Data Management Endpoints

#### POST `/api/v1/data/upload/{project_id}`
Upload a document to a specific project.

**Parameters:**
- `project_id` (path): Unique project identifier
- `file` (form-data): Document file (PDF, TXT, etc.)

**Request:**
```bash
curl -X POST "http://localhost:8000/api/v1/data/upload/project123" \
  -F "file=@document.pdf"
```

**Response (200):**
```json
{
  "signal": "FILE_UPLOAD_SUCCESS",
  "file_id": "507f1f77bcf86cd799439011",
  "project_id": "507f1f77bcf86cd799439010"
}
```

**Response (400):**
```json
{
  "signal": "FILE_UPLOAD_FAILED"
}
```

---

#### POST `/api/v1/data/process/{project_id}`
Process uploaded documents: chunk, embed, and index.

**Request Body:**
```json
{
  "chunk_size": 512,
  "overlap_size": 50,
  "do_reset": false
}
```

**Parameters:**
- `chunk_size`: Size of text chunks (characters)
- `overlap_size`: Overlap between chunks (characters)
- `do_reset`: Whether to reset processing before starting

**Response (200):**
```json
{
  "signal": "PROCESSING_COMPLETED",
  "total_chunks": 250,
  "processing_time_seconds": 45.2
}
```

---

### NLP/Query Endpoints

#### POST `/api/v1/nlp/query`
Submit a natural language query and receive RAG-enhanced responses.

**Request Body:**
```json
{
  "query": "What are the key findings?",
  "project_id": "project123",
  "top_k": 5,
  "temperature": 0.7
}
```

**Response (200):**
```json
{
  "signal": "QUERY_SUCCESS",
  "response": "Based on the documents, the key findings are...",
  "sources": [
    {
      "document_id": "507f1f77bcf86cd799439011",
      "chunk_id": "507f1f77bcf86cd799439012",
      "relevance_score": 0.95,
      "excerpt": "..."
    }
  ]
}
```

---

## 📂 Project Structure

```
Mini-Rag/
├── README.md                          # Project documentation
├── docker/
│   └── docker-compose.yml             # Container orchestration
├── src/
│   ├── main.py                        # FastAPI application entry point
│   ├── requirements.txt               # Python dependencies
│   ├── assets/
│   │   ├── database/                  # Vector DB storage
│   │   │   └── qdrant_db/             # Qdrant instance
│   │   └── files/                     # Uploaded documents
│   │       └── {project_id}/          # Project-organized files
│   │
│   ├── controllers/                   # Business logic layer
│   │   ├── BaseController.py          # Base controller with utilities
│   │   ├── DataController.py          # File handling logic
│   │   ├── ProjectController.py       # Project management
│   │   ├── ProcessController.py       # Document processing
│   │   └── NLPController.py           # Query/NLP operations
│   │
│   ├── models/                        # Data models and schemas
│   │   ├── BaseDataModel.py           # Base model class
│   │   ├── ProjectModel.py            # Project data model
│   │   ├── AssetModel.py              # Asset/file model
│   │   ├── ChunkModel.py              # Document chunk model
│   │   ├── db_schemes/                # MongoDB schemas
│   │   │   ├── project.py
│   │   │   ├── asset.py
│   │   │   └── data_chunk.py
│   │   └── enums/                     # Enumeration definitions
│   │       ├── AssetTypeEnum.py
│   │       ├── DataBaseEnum.py
│   │       ├── ProcessingEnum.py
│   │       └── ResponseEnums.py
│   │
│   ├── routes/                        # API route handlers
│   │   ├── base.py                    # Base API routes
│   │   ├── data.py                    # Data management routes
│   │   ├── nlp.py                     # NLP/query routes
│   │   └── schemes/                   # Pydantic request schemas
│   │       ├── data.py                # Data processing schemas
│   │       └── nlp.py                 # NLP request schemas
│   │
│   ├── stores/                        # External service integrations
│   │   ├── llms/                      # LLM provider abstraction
│   │   │   ├── LLMInterface.py        # LLM base interface
│   │   │   ├── LLMProviderFactory.py  # LLM factory pattern
│   │   │   ├── LLMEnums.py            # LLM type enums
│   │   │   ├── providers/             # Specific LLM implementations
│   │   │   │   ├── OpenAIProvider.py
│   │   │   │   └── CohereProvider.py
│   │   │   └── templates/             # Prompt templates
│   │   │       └── locales/           # Multi-language support
│   │   │           └── en/
│   │   │               └── rag.py     # RAG prompt templates
│   │   │
│   │   └── vectordb/                  # Vector DB provider abstraction
│   │       ├── VectorInterface.py     # VectorDB base interface
│   │       ├── VectorProviderFactory.py # VectorDB factory
│   │       ├── VectorDBEnums.py       # VectorDB type enums
│   │       └── providers/             # Specific VectorDB implementations
│   │           └── QdrantProvider.py
│   │
│   └── helper/                        # Utility modules
│       └── config.py                  # Configuration management

```

---

## 🛠️ Development

### Local Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt
pip install pytest pytest-asyncio black flake8 mypy

# Format code
black src/

# Run linter
flake8 src/

# Run type checking
mypy src/

# Run tests
pytest tests/ -v
```

### Environment Setup for Different Providers

#### OpenAI Configuration
```bash
export GENERATION_BACKEND=openai
export GENERATION_MODEL_ID=gpt-3.5-turbo
export EMBEDDING_BACKEND=openai
export EMBEDDING_MODEL_ID=text-embedding-3-small
export OPENAI_API_KEY=sk-...
```

#### Cohere Configuration
```bash
export GENERATION_BACKEND=cohere
export GENERATION_MODEL_ID=command
export EMBEDDING_BACKEND=cohere
export EMBEDDING_MODEL_ID=embed-english-v3.0
export COHERE_API_KEY=...
```

### Common Development Tasks

```bash
# Start development server with auto-reload
uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

# Start with specific Python version
python3.11 -m uvicorn src.main:app --reload

# Generate API documentation
# Available at http://localhost:8000/docs (Swagger UI)
# Available at http://localhost:8000/redoc (ReDoc)
```

---

## 🐳 Docker Deployment

### Docker Compose Services

The project includes a pre-configured `docker-compose.yml` with MongoDB:

```yaml
# Services included:
# - MongoDB 7 (metadata storage)
# - Configurable networking and volumes
```

### Running with Docker

```bash
# Start all services
cd docker
docker-compose up -d

# Check service status
docker-compose ps

# View MongoDB connection
# Connection: mongodb://mongodb:27017
# From host: mongodb://localhost:27007

# Stop services
docker-compose down

# Remove volumes (WARNING: deletes all data)
docker-compose down -v
```

### Building Custom Docker Image

```bash
# Create Dockerfile in project root
FROM python:3.11-slim

WORKDIR /app
COPY src/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

# Build image
docker build -t mini-rag:latest .

# Run container
docker run -d \
  --name mini-rag \
  -p 8000:8000 \
  -e MONGODB_URL=mongodb://host.docker.internal:27017 \
  -e OPENAI_API_KEY=sk-... \
  mini-rag:latest
```

---

## 📝 Logging

The application uses Python's built-in logging module:

```python
import logging

logger = logging.getLogger("uvicorn.error")

# Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
logger.info("Processing started")
logger.error("An error occurred", exc_info=True)
```

Access logs are available through:
- Console output during development
- Docker logs: `docker-compose logs -f`

---

## 🔐 Security Considerations

- **API Keys**: Store sensitive keys in `.env` file, never commit to version control
- **CORS**: Configure appropriate CORS policies in production
- **MongoDB**: Enable authentication in production environments
- **File Uploads**: Validate file types and sizes server-side
- **Rate Limiting**: Implement rate limiting on API endpoints for production
- **HTTPS**: Use HTTPS in production environments

---

## 🚨 Troubleshooting

### MongoDB Connection Issues

```bash
# Check MongoDB is running
docker-compose ps

# Verify connection string
# Format: mongodb://[username:password@]host[:port]/[database]

# Test connection
python -c "import pymongo; print(pymongo.MongoClient('mongodb://localhost:27017'))"
```

### LLM API Errors

```bash
# Verify API key
echo $OPENAI_API_KEY

# Check API key format
# OpenAI: sk-...
# Cohere: Must be valid token
```

### Vector Database Issues

```bash
# Check Qdrant is accessible
curl http://localhost:6333/health

# Verify vector DB path exists
ls -la ./assets/database/qdrant_db/
```

### File Upload Failures

- Check `FILE_MAX_SIZE` configuration
- Verify file format is in `FILE_ALLOWED_TYPES`
- Ensure `assets/files/` directory is writable

---

## 🤝 Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes and commit (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Standards
- Follow PEP 8 style guide
- Add type hints to functions
- Write unit tests for new features
- Update documentation

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support & Contact

For issues, questions, or suggestions:
- Open an Issue on GitHub
- Check existing documentation
- Review API documentation at `/docs` endpoint

---

## 🙏 Acknowledgments

- FastAPI for the excellent async web framework
- MongoDB for reliable data storage
- Qdrant for high-performance vector search
- OpenAI and Cohere for LLM capabilities

---

**Last Updated**: February 2026  
**Version**: 1.0.0
