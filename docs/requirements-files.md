# Requirements Files Documentation

This document explains the different requirements files in the project and their purposes.

## Backend Requirements

### `backend/requirements.txt`
**Purpose**: Production dependencies for the backend API

**Key Categories**:
- **Core Framework**: FastAPI, Uvicorn, Starlette
- **Data Validation**: Pydantic, Pydantic-settings
- **Database**: SQLAlchemy, Alembic, PostgreSQL drivers
- **Caching**: Redis, aioredis
- **Background Tasks**: Celery, Flower
- **HTTP Client**: httpx, aiohttp, requests
- **WebSocket Support**: websockets
- **Logging & Monitoring**: structlog, prometheus-fastapi-instrumentator
- **Security**: python-jose, passlib
- **Rate Limiting**: slowapi
- **Data Processing**: pandas, numpy, python-dateutil
- **Testing**: pytest and related plugins
- **Code Quality**: black, isort, flake8, mypy, bandit

### `backend/requirements-dev.txt`
**Purpose**: Development-only dependencies

**Additional Tools**:
- **Debugging**: ipython, ipdb, debugpy
- **Documentation**: mkdocs, mkdocs-material
- **Advanced Linting**: pylint, autopep8
- **Testing Utilities**: pytest-mock, pytest-xdist, hypothesis
- **Security Scanning**: safety, pip-audit
- **Performance Profiling**: py-spy, memory-profiler
- **Code Complexity**: radon, mccabe

### `backend/env.example`
**Purpose**: Template for environment variables

**Key Variables**:
- Database and Redis connection strings
- API configuration
- External service URLs
- Security settings
- Cache TTL values
- Development settings

## Frontend Requirements

### `frontend/package.json`
**Purpose**: Node.js dependencies for the React frontend

**Key Categories**:
- **Core Framework**: React 18, TypeScript
- **Routing**: react-router-dom
- **State Management**: Zustand, TanStack Query
- **Charts**: Recharts
- **HTTP Client**: axios
- **UI Components**: Radix UI primitives, shadcn/ui
- **Styling**: Tailwind CSS, class-variance-authority
- **Internationalization**: react-intl
- **Testing**: Vitest, Testing Library
- **Build Tools**: Vite
- **Documentation**: Storybook

### `frontend/requirements.txt`
**Purpose**: Python-based tools for frontend pipeline (if needed)

**Note**: Most frontend dependencies are managed via npm/yarn through package.json.

## Installation Commands

### Backend Setup
```bash
# Production dependencies
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt

# Development dependencies (optional)
pip install -r requirements-dev.txt
```

### Frontend Setup
```bash
# Install Node.js dependencies
cd frontend
npm install

# Or using yarn
yarn install
```

### Environment Setup
```bash
# Copy environment template
cd backend
cp env.example .env

# Edit .env with your actual values
nano .env
```

## Dependency Management

### Backend
- **pip-tools**: For managing complex dependency trees
- **pre-commit**: For automated code quality checks
- **Dependabot**: For automated dependency updates

### Frontend
- **npm/yarn**: For package management
- **Husky**: For git hooks
- **Dependabot**: For automated dependency updates

## Security Considerations

### Backend
- **bandit**: Security linting
- **safety**: Vulnerability scanning
- **pip-audit**: Dependency vulnerability checks

### Frontend
- **npm audit**: Security vulnerability scanning
- **ESLint security rules**: Code security checks

## Version Pinning

All dependencies are pinned to specific versions to ensure:
- Reproducible builds
- Consistent behavior across environments
- Security through known-good versions

## Updates

### Backend
```bash
# Update all dependencies
pip install --upgrade -r requirements.txt

# Update specific package
pip install --upgrade package-name
```

### Frontend
```bash
# Update all dependencies
npm update

# Update specific package
npm update package-name
```

## Troubleshooting

### Common Issues

1. **Version Conflicts**: Use `pip-tools` to resolve conflicts
2. **Missing Dependencies**: Check if all requirements are installed
3. **Environment Issues**: Verify `.env` file is properly configured
4. **Node Modules Issues**: Delete `node_modules` and reinstall

### Dependency Resolution

```bash
# Backend
pip install pip-tools
pip-compile requirements.in

# Frontend
npm ls  # Check for dependency conflicts
npm audit fix  # Fix security vulnerabilities
``` 