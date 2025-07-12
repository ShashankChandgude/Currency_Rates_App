# ADR-001: Technology Stack Selection

## Status
Accepted

## Context
We need to select a technology stack for the Currency Converter & Charting App that provides:
- High performance for real-time currency conversion
- Scalability for handling multiple concurrent users
- Modern development experience with good tooling
- Cost-effective deployment and maintenance
- Strong ecosystem and community support

## Decision
We will use the following technology stack:

### Backend
- **Python 3.12** - Latest stable Python version with excellent async support
- **FastAPI** - High-performance async web framework with automatic OpenAPI documentation
- **PostgreSQL** - Robust relational database with JSON support and excellent performance
- **Redis** - In-memory cache for session storage and rate caching
- **Celery/RQ** - Background task processing for rate fetching and data processing

### Frontend
- **React 18** - Latest React with concurrent features and improved performance
- **TypeScript** - Type safety and better developer experience
- **Recharts** - Lightweight and flexible charting library
- **Tailwind CSS** - Utility-first CSS framework for rapid UI development
- **shadcn/ui** - High-quality component library built on Radix UI
- **Zustand** - Lightweight state management with TypeScript support

### DevOps & Infrastructure
- **Docker** - Containerization with multi-stage builds for optimization
- **GitHub Actions** - CI/CD pipeline with automated testing and deployment
- **K3s** - Lightweight Kubernetes for production deployment
- **Helm** - Kubernetes package manager for deployment automation

## Consequences

### Positive
- **Performance**: FastAPI provides excellent async performance, PostgreSQL handles complex queries efficiently
- **Developer Experience**: TypeScript, modern tooling, and comprehensive documentation
- **Scalability**: Containerized deployment with Kubernetes enables horizontal scaling
- **Cost-Effective**: All technologies are open-source with free tiers available
- **Community**: Strong ecosystems with extensive documentation and community support

### Negative
- **Learning Curve**: Team needs to be familiar with multiple technologies
- **Complexity**: Microservices architecture requires more operational overhead
- **Resource Usage**: Multiple services require more infrastructure resources

### Risks
- **Technology Lock-in**: Dependency on specific frameworks and tools
- **Maintenance Overhead**: Multiple technologies require ongoing maintenance and updates
- **Debugging Complexity**: Distributed system can be harder to debug

## Alternatives Considered

### Backend Alternatives
- **Django**: Too heavy for our use case, better for content-heavy applications
- **Flask**: Lacks built-in async support and automatic API documentation
- **Node.js/Express**: Good choice but Python ecosystem better for data processing
- **Go**: Excellent performance but steeper learning curve for team

### Database Alternatives
- **MongoDB**: Good for document storage but lacks ACID compliance for financial data
- **MySQL**: Good choice but PostgreSQL has better JSON support and performance
- **SQLite**: Too limited for production use with multiple concurrent users

### Frontend Alternatives
- **Vue.js**: Good framework but React has larger ecosystem for our needs
- **Angular**: Too heavy and complex for our application
- **Svelte**: Promising but smaller ecosystem and community

### Infrastructure Alternatives
- **AWS/GCP/Azure**: More expensive, vendor lock-in concerns
- **Heroku**: Simpler but less control and higher costs at scale
- **Vercel/Netlify**: Good for frontend but limited for full-stack applications

## Implementation Notes
- Start with monorepo structure for easier development
- Use Docker Compose for local development
- Implement comprehensive testing strategy from the beginning
- Set up monitoring and logging infrastructure early
- Document all API endpoints with OpenAPI/Swagger

## References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React 18 Features](https://react.dev/blog/2022/03/29/react-v18)
- [PostgreSQL Performance](https://www.postgresql.org/docs/current/performance.html)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/) 