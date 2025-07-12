.PHONY: help install test lint format clean up down logs

# Default target
help:
	@echo "Available commands:"
	@echo "  install    - Install dependencies for backend and frontend"
	@echo "  test       - Run tests for backend and frontend"
	@echo "  lint       - Run linting for backend and frontend"
	@echo "  format     - Format code for backend and frontend"
	@echo "  up         - Start all services with Docker Compose"
	@echo "  down       - Stop all services"
	@echo "  logs       - Show logs for all services"
	@echo "  clean      - Clean up containers, volumes, and cache"
	@echo "  setup      - Initial setup (install + up)"

# Development setup
setup: install up

# Install dependencies
install:
	@echo "Installing backend dependencies..."
	cd backend && python -m venv venv
	cd backend && source venv/bin/activate && pip install -r requirements.txt
	@echo "Installing frontend dependencies..."
	cd frontend && npm install
	@echo "Installation complete!"

# Docker commands
up:
	@echo "Starting services with Docker Compose..."
	docker-compose up -d postgres redis
	@echo "Waiting for database to be ready..."
	@until docker-compose exec -T postgres pg_isready -U currency_user -d currency_app; do sleep 2; done
	@echo "Services started successfully!"

down:
	@echo "Stopping services..."
	docker-compose down

logs:
	docker-compose logs -f

# Testing
test:
	@echo "Running backend tests..."
	cd backend && source venv/bin/activate && pytest
	@echo "Running frontend tests..."
	cd frontend && npm test

test-backend:
	@echo "Running backend tests..."
	cd backend && source venv/bin/activate && pytest

test-frontend:
	@echo "Running frontend tests..."
	cd frontend && npm test

# Linting and formatting
lint:
	@echo "Linting backend..."
	cd backend && source venv/bin/activate && flake8 app tests
	@echo "Linting frontend..."
	cd frontend && npm run lint

lint-backend:
	@echo "Linting backend..."
	cd backend && source venv/bin/activate && flake8 app tests

lint-frontend:
	@echo "Linting frontend..."
	cd frontend && npm run lint

format:
	@echo "Formatting backend..."
	cd backend && source venv/bin/activate && black app tests
	cd backend && source venv/bin/activate && isort app tests
	@echo "Formatting frontend..."
	cd frontend && npm run format

format-backend:
	@echo "Formatting backend..."
	cd backend && source venv/bin/activate && black app tests
	cd backend && source venv/bin/activate && isort app tests

format-frontend:
	@echo "Formatting frontend..."
	cd frontend && npm run format

# Cleanup
clean:
	@echo "Cleaning up..."
	docker-compose down -v
	docker system prune -f
	cd backend && rm -rf venv __pycache__ .pytest_cache .coverage htmlcov
	cd frontend && rm -rf node_modules .next dist
	@echo "Cleanup complete!"

# Database commands
db-migrate:
	@echo "Running database migrations..."
	cd backend && source venv/bin/activate && alembic upgrade head

db-reset:
	@echo "Resetting database..."
	docker-compose down -v
	docker-compose up -d postgres redis
	@until docker-compose exec -T postgres pg_isready -U currency_user -d currency_app; do sleep 2; done
	cd backend && source venv/bin/activate && alembic upgrade head

# Development server commands
dev-backend:
	@echo "Starting backend development server..."
	cd backend && source venv/bin/activate && uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

dev-frontend:
	@echo "Starting frontend development server..."
	cd frontend && npm run dev

# Production build
build:
	@echo "Building production images..."
	docker-compose -f docker-compose.prod.yml build

# Security checks
security:
	@echo "Running security checks..."
	cd backend && source venv/bin/activate && bandit -r app
	cd frontend && npm audit

# Coverage
coverage:
	@echo "Running coverage report..."
	cd backend && source venv/bin/activate && pytest --cov=app --cov-report=html
	cd frontend && npm run test:coverage 