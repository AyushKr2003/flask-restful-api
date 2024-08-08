# Flask Store API

This project is a RESTful API for managing stores, items, tags, and users using Flask, SQLAlchemy, and JWT authentication.

## Features

- User registration and authentication
- CRUD operations for stores, items, and tags
- JWT token-based authentication
- Admin privileges for certain operations
- Database migrations using Flask-Migrate
- API documentation with Swagger UI

## Requirements

See `requirements.txt` for a full list of dependencies. Key requirements include:

- Flask
- Flask-Smorest
- Flask-SQLAlchemy
- Flask-JWT-Extended
- Flask-Migrate

## Installation

1. Clone the repository
2. Create a virtual environment: `python -m venv .venv`
3. Activate the virtual environment:
   - Windows: `.venv\Scripts\activate`
   - macOS/Linux: `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`

## Configuration

The application uses environment variables for configuration. You can set these in a `.env` file or directly in your environment.

Key configuration options:

- `DATABASE_URL`: Database connection string (default: `sqlite:///data.db`)
- `JWT_SECRET_KEY`: Secret key for JWT encoding/decoding

## Running the Application

1. Set the Flask application: `export FLASK_APP=app` (Linux/macOS) or `set FLASK_APP=app` (Windows)
2. Run database migrations: `flask db upgrade`
3. Start the server: `flask run`

The API will be available at `http://localhost:5000`.

## API Documentation

Once the server is running, you can access the Swagger UI documentation at `http://localhost:5000/swagger-ui`.

## Docker

A Dockerfile is provided for containerization. To build and run the Docker image:

1. Build the image: `docker build -t flask-store-api .`
2. Run the container: `docker run -p 5000:5000 flask-store-api`

## Project Structure

- `app.py`: Main application file
- `db.py`: Database initialization
- `models/`: Database models
- `resources/`: API route handlers
- `schemas.py`: Marshmallow schemas for serialization/deserialization
- `migrations/`: Database migration files

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open-sourced under the MIT License.