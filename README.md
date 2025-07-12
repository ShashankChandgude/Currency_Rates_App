# Currency Converter & Charting App

A full-stack web application for real-time currency conversion and historical exchange rate visualization.

## 🚀 Features

- **Live Currency Converter** - Convert between ~180 currencies with sub-second updates
- **Interactive Charts** - Line and candlestick charts for multiple time ranges
- **Real-time Updates** - WebSocket feed pushing latest rates every few seconds
- **Historical Data** - View exchange rate trends over time

## 🛠️ Tech Stack

### Backend
- **Python 3.12** + **FastAPI** - High-performance async web framework
- **PostgreSQL** - Primary database for historical data
- **Redis** - Caching and session storage
- **Celery/RQ** - Background task processing

### Frontend
- **React 18** + **TypeScript** - Modern UI framework
- **Recharts** - Interactive charting library
- **Tailwind CSS** + **shadcn/ui** - Styling and component library
- **Zustand** - State management

### DevOps
- **Docker** - Containerization with multi-stage builds
- **GitHub Actions** - CI/CD pipeline
- **K3s** + **Helm** - Kubernetes deployment

## 📋 Project Status

- [x] Phase 0: Project Bootstrap (Current)
- [ ] Phase 1: Domain & Data Modeling
- [ ] Phase 2: Rate Provider Layer
- [ ] Phase 3: Service Layer & Business Rules
- [ ] Phase 4: API Surface
- [ ] Phase 5: React Frontend Skeleton
- [ ] Phase 6: Frontend Realtime & UX Polish
- [ ] Phase 7: CI/CD & Infrastructure
- [ ] Phase 8: Observability & Security Hardening
- [ ] Phase 9: Documentation, Demo, Launch

## 🚀 Quick Start

### Prerequisites
- Python 3.12+
- Node.js 20+
- Docker & Docker Compose
- PostgreSQL
- Redis

### Development Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd currency-rates-app
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   ```

4. **Start Services**
   ```bash
   # Start database and Redis
   docker-compose up -d postgres redis
   
   # Start backend (in backend directory)
   uvicorn app.main:app --reload
   
   # Start frontend (in frontend directory)
   npm run dev
   ```

5. **Run Tests**
   ```bash
   # Backend tests
   cd backend && pytest
   
   # Frontend tests
   cd frontend && npm test
   ```

## 📚 Documentation

- [Architecture Decision Records (ADRs)](docs/adr/)
- [API Documentation](docs/api/)
- [Development Guide](docs/development/)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [exchangerate.host](https://exchangerate.host/) for free currency API
- [shadcn/ui](https://ui.shadcn.com/) for beautiful UI components
- [Recharts](https://recharts.org/) for charting capabilities 