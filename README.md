
# Healthcare-Data-Pipeline
End-to-end Python ETL pipeline with FastAPI, PostgreSQL, Docker

An end-to-end data engineering project that demonstrates building a production-style ETL pipeline using Python, Pandas, PostgreSQL, FastAPI, and Docker.

The pipeline ingests public healthcare data, cleans and transforms it, loads it into a relational database, and exposes a REST API for querying.

This project showcases skills in:

- Data pipelines (ETL)
- Backend APIs
- Database design
- Containerization
- Clean code and reproducibility

Tech Stack

Language: Python 3.10
Data: Pandas: NumPy
API: FastAPI: Uvicorn
Database: PostgreSQL
ORM: SQLAlchemy
Containerization: Docker, Docker Compose
Version Control: Git

Architecture

Public Dataset (CVS) -> Extract Script -> Transform Script -> PostgreSQL Database -> FastAPI Service

How to Run (Docker)

Prerequisites
- Docker Desktop installed
- Git installed

Clone the Repository

<--git clone https://github.com/ednasawe/Healthcare-Data-Pipeline.git-->

<--cd Healthcare-Data-Pipeline-->

Start the Pipeline

<--docker-compose up --build-->

Access API Documentation

Open in browser:

<--http://localhost:8000/docs-->

Example API Endpoint

<--GET /health?limit=10-->

Returns a JSON list of healthcare records.

Project Structure

Healthcare-Data-Pipeline/
api/          # FastAPI service
etl/          # Extract, transform, load scripts
data/         # Raw and processed datasets
database/     # Schema and migrations
tests/        # Unit tests
docker-compose.yml
Dockerfile
README.md

Future Improvements

- Add Airflow or Prefect scheduling
- Add CI/CD pipeline
- Add authentication to API
- Add dashboard visualization
- Add cloud deployment

Author

Edna Sawe
Github: https://www.github.com/ednasawe
LinkedIn: https://www.linkedin.com/ednasawe
