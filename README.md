# 🚀 CloudOps Guardian  
### AI-Powered Cloud Governance, FinOps & Security Platform

<p align="center">
  <img src="https://img.shields.io/badge/AWS-Cloud-orange?style=for-the-badge&logo=amazon-aws"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi"/>
  <img src="https://img.shields.io/badge/React-Frontend-blue?style=for-the-badge&logo=react"/>
  <img src="https://img.shields.io/badge/Terraform-IaC-purple?style=for-the-badge&logo=terraform"/>
  <img src="https://img.shields.io/badge/Docker-Container-blue?style=for-the-badge&logo=docker"/>
  <img src="https://img.shields.io/badge/DevOps-CI/CD-red?style=for-the-badge&logo=githubactions"/>
</p>

---

## 🧠 Overview

**CloudOps Guardian** is a next-generation **Cloud Governance & FinOps platform** that helps engineers monitor, optimize, and secure AWS infrastructure using automation, AI insights, and real-time analytics.

It detects:
- 💰 Cost inefficiencies  
- 🔐 Security risks  
- ⚠️ Infrastructure drift  
- 📊 Resource usage anomalies  

and provides **AI-powered recommendations** for optimization.

---

## 🎯 Problem Statement

Modern cloud environments suffer from:
- Rising AWS costs due to idle resources
- Misconfigured security groups
- Lack of visibility into infrastructure drift
- Manual monitoring overhead
- No unified governance system

---

## 💡 Solution

CloudOps Guardian provides a **single dashboard** to:

- Optimize cloud cost automatically
- Detect infrastructure drift (Terraform vs AWS)
- Audit security misconfigurations
- Provide AI-based insights
- Monitor AWS resources in real-time

---

## 🏗️ System Architecture

```
                ┌──────────────────────────────┐
                │            USER UI            │
                │   HTML / CSS / JS Dashboard   │
                └─────────────┬────────────────┘
                              │
                              ▼
                ┌──────────────────────────────┐
                │        FRONTEND LAYER        │
                │  - Dashboard Pages           │
                │  - Security UI               │
                │  - Cost UI                   │
                │  - Drift UI                  │
                └─────────────┬────────────────┘
                              │  REST API Calls
                              ▼
                ┌──────────────────────────────┐
                │       FASTAPI BACKEND        │
                │  - /dashboard                │
                │  - /security                 │
                │  - /cost                     │
                │  - /drift                    │
                └─────────────┬────────────────┘
                              │
          ┌───────────────────┼────────────────────┐
          ▼                   ▼                    ▼
┌────────────────┐  ┌────────────────┐  ┌──────────────────┐
│   AWS BOTO3    │  │   TERRAFORM    │  │    AI ENGINE     │
│                │  │  STATE CHECK   │  │ Insights Engine  │
│ EC2 / S3 / IAM │  │  Drift Detect  │  │ Cost Suggestions │
└───────┬────────┘  └───────┬────────┘  └────────┬─────────┘
        │                   │                    │
        └──────────┬────────┴──────────┬────────┘
                   ▼                   ▼
        ┌──────────────────────────────────────┐
        │         DATA PROCESSING LAYER        │
        │  - Security Scan Results             │
        │  - Cost Optimization Data            │
        │  - Drift Comparison Output           │
        └───────────────┬──────────────────────┘
                        ▼
        ┌──────────────────────────────────────┐
        │          RESPONSE FORMAT             │
        │          JSON API OUTPUT             │
        └───────────────┬──────────────────────┘
                        ▼
        ┌──────────────────────────────────────┐
        │        VISUALIZATION LAYER           │
        │   Charts (Chart.js) + UI Cards       │
        │   Alerts + Metrics Dashboard         │
        └──────────────────────────────────────┘
```

---

## ⚙️ Tech Stack

### 🖥️ Frontend
- React.js
- Tailwind CSS
- Chart.js
- Axios

### 🔧 Backend
- FastAPI
- Python (Boto3)
- SQLAlchemy

### ☁️ Cloud & DevOps
- AWS (EC2, S3, IAM, CloudWatch, Lambda)
- Terraform (Infrastructure as Code)
- Docker
- GitHub Actions

### 🗄️ Database
- PostgreSQL

---

## 🔍 Core Features

### 💰 FinOps (Cost Optimization)
- Detect idle EC2 instances
- Identify unused EBS volumes
- Detect orphaned snapshots
- Estimate monthly savings

### 🔐 Security Audit
- Public S3 bucket detection
- Open security groups (0.0.0.0/0)
- IAM users without MFA
- Root account usage tracking
- Encryption checks

### ⚠️ Drift Detection
- Compare Terraform state vs live AWS resources
- Detect:
  - Missing resources
  - Modified configurations
  - Unauthorized changes

### 🤖 AI Cloud Assistant
Ask questions like:
> "Why is my AWS bill high?"

Get insights:
- Idle resources
- Cost breakdown
- Optimization suggestions

### 📊 Dashboard
- AWS resource summary
- Cost analytics
- Security score
- Drift status
- Real-time monitoring graphs

---

## 🧱 Project Structure

```
CloudOps-Guardian/
│
├── frontend/        # React UI
├── backend/         # FastAPI services
├── terraform/       # IaC scripts
├── docker/          # Container configs
├── database/        # DB schema
├── docs/            # Documentation
├── screenshots/     # UI images
├── .github/         # CI/CD pipelines
├── docker-compose.yml
└── README.md
```

---

## ☁️ AWS Services Used

- EC2 – Compute
- S3 – Storage
- IAM – Security
- CloudWatch – Monitoring
- Lambda – Automation
- SNS – Notifications

---

## 📈 Future Enhancements

- Kubernetes integration (EKS)
- Prometheus & Grafana monitoring
- Multi-cloud support (Azure/GCP)
- Slack & Teams alerts
- Advanced AI FinOps engine

---

## 🚀 Getting Started

### 1️⃣ Clone Repository
```bash
git clone https://github.com/your-username/cloudops-guardian.git
cd cloudops-guardian
```

### 2️⃣ Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 3️⃣ Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

### 4️⃣ Run with Docker
```bash
docker-compose up --build
```

---

## 👨‍💻 Author

**Nitesh Vishwakarma**  
Cloud Engineer / DevOps Engineer

🌐 Portfolio: https://securewithnitesh.netlify.app  
💼 LinkedIn: https://linkedin.com/in/nitesh1vishwakarma  
🐙 GitHub: https://github.com/NiteshVishwakarma219
