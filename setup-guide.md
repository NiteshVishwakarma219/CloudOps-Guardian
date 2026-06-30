# 🚀 CloudOps Guardian — Complete Setup Guide

This guide walks you through setting up the entire project from scratch: folder structure, backend, frontend, Docker, CI/CD, and pushing to GitHub.

---

## 📋 Prerequisites

Make sure you have these installed before starting:

- Python 3.11+
- Node.js + npm (only needed if you upgrade to React later)
- Docker & Docker Compose
- Git
- A GitHub account

---

## 1️⃣ Create Project Structure

```bash
mkdir CloudOps-Guardian
cd CloudOps-Guardian

mkdir frontend backend terraform docker database docs screenshots .github

touch README.md docker-compose.yml .gitignore
```

---

## 2️⃣ Initialize Git

```bash
git init
git branch -M main

git remote add origin https://github.com/YOUR_USERNAME/cloudops-guardian.git
```

> Replace `YOUR_USERNAME` with your actual GitHub username, and create the empty repo on GitHub first (without a README, so it doesn't conflict).

---

## 3️⃣ Set Up `.gitignore`

```bash
cat > .gitignore << 'EOF'
# Python
__pycache__/
*.pyc
venv/
.env

# Node
node_modules/
dist/

# Docker
*.log

# OS
.DS_Store
EOF
```

---

## 4️⃣ Backend Setup (FastAPI)

```bash
cd backend
touch main.py requirements.txt

pip install fastapi uvicorn boto3
```

### Fill in `requirements.txt`

```bash
cat > requirements.txt << 'EOF'
fastapi
uvicorn
boto3
EOF
```

### Fill in `main.py`

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/dashboard")
def dashboard():
    return {
        "ec2_total": 5,
        "ec2_running": 3,
        "s3_total": 2,
        "savings": 120
    }

@app.get("/security")
def security():
    return {
        "public_s3": 1,
        "open_sg": 2,
        "mfa_missing": 3
    }

@app.get("/cost")
def cost():
    return {
        "idle_ec2": 2,
        "unused_ebs": 1,
        "savings": 80
    }

@app.get("/drift")
def drift():
    return {
        "missing": 1,
        "modified": 2,
        "deleted": 0
    }
```

### Run the backend

```bash
uvicorn main:app --reload
```

Visit `http://127.0.0.1:8000/docs` to confirm the API is running.

---

## 5️⃣ Frontend Setup

```bash
cd ../frontend

mkdir css js

touch index.html dashboard.html security.html cost.html drift.html
touch css/style.css
touch js/api.js js/dashboard.js js/security.js js/cost.js js/drift.js
```

### Fill in `js/api.js`

```javascript
const BASE_URL = "http://127.0.0.1:8000";

async function fetchData(endpoint) {
    const res = await fetch(BASE_URL + endpoint);
    return await res.json();
}
```

### Fill in `js/dashboard.js`

```javascript
document.addEventListener("DOMContentLoaded", async () => {
    const data = await fetchData("/dashboard");

    document.getElementById("stats").innerHTML = `
        <h2>EC2 Total: ${data.ec2_total}</h2>
        <h2>Running: ${data.ec2_running}</h2>
        <h2>S3 Buckets: ${data.s3_total}</h2>
        <h2>Savings: $${data.savings}</h2>
    `;
});
```

### Fill in `index.html`

```html
<div>
    <h1>CloudOps Guardian</h1>
    <a href="dashboard.html">Dashboard</a>
    <a href="security.html">Security</a>
    <a href="cost.html">Cost</a>
    <a href="drift.html">Drift</a>
</div>
```

### Fill in `dashboard.html`

```html
<div id="stats">Loading...</div>

<script src="js/api.js"></script>
<script src="js/dashboard.js"></script>
```

### Run the frontend

```bash
open frontend/index.html
```

(On Linux: `xdg-open frontend/index.html`. On Windows: just double-click the file.)

---

## 6️⃣ Docker Setup (Backend)

```bash
cd ../backend
touch Dockerfile
```

### Fill in `Dockerfile`

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install fastapi uvicorn boto3

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Build and run the container

```bash
docker build -t cloudops-backend .
docker run -p 8000:8000 cloudops-backend
```

---

## 7️⃣ Docker Compose (Root Level)

```bash
cd ..
touch docker-compose.yml
```

### Fill in `docker-compose.yml`

```yaml
version: "3.8"

services:
  backend:
    build: ./backend
    ports:
      - "8000:8000"

  frontend:
    image: nginx
    volumes:
      - ./frontend:/usr/share/nginx/html
    ports:
      - "3000:80"
```

### Run everything together

```bash
docker-compose up --build
```

Backend will be live at `http://localhost:8000` and frontend at `http://localhost:3000`.

---

## 8️⃣ GitHub Actions (CI/CD)

```bash
mkdir -p .github/workflows
touch .github/workflows/deploy.yml
```

### Fill in `.github/workflows/deploy.yml`

```yaml
name: Deploy Backend

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v3

      - name: Deploy to Server
        uses: appleboy/ssh-action@v1.0.3
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ubuntu
          key: ${{ secrets.EC2_KEY }}
          script: |
            cd cloudops-guardian/backend
            git pull
            pkill -f uvicorn || true
            nohup uvicorn main:app --host 0.0.0.0 --port 8000 &
```

> ⚠️ This workflow assumes you already have an EC2 instance set up with the repo cloned, and that you've added `EC2_HOST` and `EC2_KEY` as repository secrets under **Settings → Secrets and variables → Actions**. Without that setup, this workflow will fail on push.

---

## 9️⃣ Push to GitHub

```bash
git add .
git commit -m "initial cloudops guardian setup"
git push -u origin main
```

---

## 🔟 Running the Project Day-to-Day

### Backend only

```bash
cd backend
uvicorn main:app --reload
```

### Frontend only

```bash
open frontend/index.html
```

### Full stack via Docker

```bash
docker-compose up --build
```

---

## ✅ What You'll Have After This Guide

- ✔ FastAPI backend running with mock data endpoints
- ✔ Basic HTML/JS dashboard fetching from the backend
- ✔ Dockerfile + docker-compose for containerized run
- ✔ GitHub Actions CI/CD skeleton
- ✔ Project pushed and live on GitHub

---

## ⚠️ Known Gaps (Not Yet Implemented)

This setup gets the skeleton running, but these are still stubs and need real implementation before the project matches the full README:

- `boto3` is installed but not actually called — all API responses are hardcoded
- No real Terraform drift detection logic
- No AI assistant endpoint
- No PostgreSQL/SQLAlchemy database wiring
- `security.html`, `cost.html`, `drift.html` and their JS files exist but are empty
- `css/style.css` is empty — no styling applied yet
- No charts (Chart.js) wired in yet
- Frontend is plain HTML/JS, not React (despite README listing React as the stack)

---

## 🚀 Next Level Upgrades (Optional)

- Real AWS integration via `boto3` (live EC2/S3/IAM data)
- Kubernetes deployment (EKS-style)
- Grafana + Prometheus monitoring
- React + Tailwind + Chart.js frontend rebuild
- PostgreSQL database integration
- AI-powered cost assistant endpoint
