# Menage Repartiter Backend

This is the backend API for the Menage Repartiter application, built with FastAPI and PostgreSQL.

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with the following variables:
```env
POSTGRES_SERVER=localhost
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=menage_repartiter
```

4. Start the PostgreSQL database (using Docker):
```bash
docker run --name postgres -e POSTGRES_PASSWORD=postgres -e POSTGRES_DB=menage_repartiter -p 5432:5432 -d postgres:15
```

5. Run the application:
```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

## API Documentation

Once the application is running, you can access:
- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Development

The project structure is organized as follows:
- `app/`: Main application package
  - `api/`: API endpoints
  - `core/`: Core functionality and configuration
  - `db/`: Database session and connection
  - `models/`: SQLAlchemy models
  - `schemas/`: Pydantic schemas for request/response models

## Docker

To build and run the application using Docker:

```bash
docker build -t menage-repartiter-backend .
docker run -p 8000:8000 menage-repartiter-backend
``` 