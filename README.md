# Hello FastAPI Application

A simple FastAPI application with automated CI/CD deployment to AWS Lightsail.

## 🚀 Quick Start

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Run the application
uvicorn main:app --reload
```

### API Documentation

Once the server is running, you can access:
- Interactive API docs: `http://localhost:8000/docs`
- Alternative API docs: `http://localhost:8000/redoc`

## 📦 Docker

### Build and Run Locally

```bash
# Build the image
docker build -t hello-app .

# Run the container
docker run -d -p 8000:8000 --name hello-container hello-app
```

## 🚢 Deployment

This project includes automated CI/CD deployment to AWS Lightsail via GitHub Actions.

**Pipeline:** Cursor → GitHub → GitHub Actions → AWS Lightsail

### Quick Setup

See `QUICK_START.md` for a step-by-step checklist.

### Detailed Guide

See `DEPLOYMENT_GUIDE.md` for comprehensive deployment instructions.

### Workflow

1. Make changes in Cursor
2. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Your changes"
   git push origin main
   ```
3. GitHub Actions automatically:
   - Builds Docker image
   - Pushes directly to AWS Lightsail
   - Deploys to production
4. Your changes are live in ~3-5 minutes!

## 📁 Project Structure

```
.
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── .github/
│   └── workflows/
│       └── deploy.yml     # GitHub Actions workflow
├── DEPLOYMENT_GUIDE.md    # Detailed deployment guide
└── QUICK_START.md         # Quick setup checklist
```
