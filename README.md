# OurPlant – DevOps Capstone Project

## Project Overview
OurPlant is a plant management application built to showcase modern DevOps practices, delivering fully automated CI/CD pipelines, secure containerized deployments, Kubernetes governance, and end-to-end observability.

Key Features:
- RESTful API using **FastAPI**
- Frontend using **Nginx** serving static content
- Persistent data storage via **MySQL**
- Kubernetes deployment using **Helm charts**
- Automated CI/CD pipelines (GitHub Actions + ArgoCD)
- Security enforced via RBAC and NetworkPolicies
- Monitoring with Prometheus & Grafana
- Horizontal Pod Autoscaler (HPA)

## Project Goals
- Develop a fully functional RESTful API for plant management
- Containerize services with Docker
- Deploy on Kubernetes with Helm
- Implement automated CI/CD pipelines
- Enforce security best practices
- Implement monitoring and observability
- Ensure scalability with HPA and governance via ResourceQuotas & LimitRanges

## Architecture Overview
- Client → Ingress Controller (TLS) → Frontend (Nginx) → Backend (FastAPI) → MySQL
- HPA scales services dynamically
- NetworkPolicies enforce Zero Trust
- RBAC ensures least privilege
- Prometheus & Grafana for monitoring

## Development Workflow
1. Backend development (FastAPI, CRUD endpoints, tests)
2. Frontend development (Nginx, static content)
3. Containerization (Docker multi-stage, non-root)
4. Local development with Docker Compose
5. Kubernetes deployment using Helm (StatefulSet, Deployments, Services, Ingress, NetworkPolicies)
6. CI/CD implementation (GitHub Actions, ArgoCD)
7. Monitoring & Security (Prometheus, Grafana)

## Key Achievements
- Fully functional plant CRUD API
- Automated CI/CD pipelines with build, test, scan, and deploy
- Secure Kubernetes deployment with NetworkPolicies
- Horizontal Pod Autoscaler configured and tested
- Monitoring dashboards and alerts in place
- Runbooks and documentation completed
