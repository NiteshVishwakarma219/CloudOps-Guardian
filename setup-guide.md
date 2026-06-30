# ================================================
# 🚀 CLOUDOPS GUARDIAN — COMPLETE SETUP & GITHUB PUSH
# ================================================

# ---------- 1. CREATE PROJECT STRUCTURE ----------
mkdir CloudOps-Guardian
cd CloudOps-Guardian

mkdir frontend backend terraform docker database docs screenshots
mkdir -p .github/workflows
mkdir frontend/css frontend/js

touch README.md docker-compose.yml .gitignore
touch backend/main.py backend/requirements.txt backend/Dockerfile
touch frontend/index.html frontend/dashboard.html frontend/security.html frontend/cost.html frontend/drift.html
touch frontend/css/style.css
touch frontend/js/api.js frontend/js/dashboard.js frontend/js/security.js frontend/js/cost.js frontend/js/drift.js
touch .github/workflows/deploy.yml


# ---------- 2. INITIALIZE GIT ----------
git init
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/cloudops-guardian.git


# ---------- 3. CREATE .gitignore ----------
cat > .gitignore << 'EOF'
__pycache__/
*.pyc
venv/
.env
node_modules/
.DS_Store
*.log
.terraform/
*.tfstate
*.tfstate.backup
EOF


# ---------- 4. BACKEND SETUP (FASTAPI) ----------
cd backend

cat > requirements.txt << 'EOF'
fastapi
uvicorn
boto3
EOF

pip install -r requirements.txt

# Open backend/main.py and paste your FastAPI code (dashboard, security, cost, drift endpoints)

# Run backend locally to test
uvicorn main:app --reload

cd ..


# ---------- 5. FRONTEND SETUP ----------
# Open frontend/index.html, dashboard.html, etc. and paste your HTML
# Open frontend/js/api.js, dashboard.js etc. and paste your JS code
# Open frontend/css/style.css and add your styling

# Test frontend locally by opening in browser
open frontend/index.html
# (on Linux: xdg-open frontend/index.html)
# (on Windows: start frontend/index.html)


# ---------- 6. DOCKER SETUP ----------
cat > backend/Dockerfile << 'EOF'
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
EOF

cat > docker-compose.yml << 'EOF'
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
EOF

# Test docker build
docker-compose up --build


# ---------- 7. GITHUB ACTIONS (CI/CD) ----------
cat > .github/workflows/deploy.yml << 'EOF'
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
EOF
# Note: this step requires EC2_HOST and EC2_KEY secrets set in
# GitHub repo → Settings → Secrets and variables → Actions


# ---------- 8. ADD README ----------
# Paste your final README.md content into README.md


# ---------- 9. PUSH TO GITHUB ----------
git add .
git commit -m "Initial CloudOps Guardian setup"
git push -u origin main


# ---------- 10. VERIFY ON GITHUB ----------
# Go to https://github.com/YOUR_USERNAME/cloudops-guardian
# Confirm README renders, folder structure is correct, and Actions tab shows the workflow


# ---------- 11. FUTURE COMMITS ----------
git add .
git commit -m "Describe your change here"
git push