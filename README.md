# Wisecow - Containerization & Kubernetes Deployment

A complete containerized DevOps solution for the Wisecow application, featuring automated CI/CD pipelines via GitHub Actions, ephemeral Kubernetes deployments with `kind`, and secure TLS ingress routing.

---

## Project Overview

This repository automates the build, test, and deployment lifecycle of the **Wisecow** application. The project meets all core requirements and includes advanced challenge goals:
* **Dockerization:** Optimized container image built on Ubuntu 22.04 with necessary system utilities (`cowsay`, `fortune-mod`, `netcat-openbsd`).
* **Kubernetes Manifests:** Production-ready Deployment, Service (`NodePort`), and Ingress configurations.
* **CI/CD Automation:** GitHub Actions workflow that builds and pushes images to Docker Hub on every commit to `main`.
<<<<<<< HEAD
* **Continuous Deployment :** Automated cluster spinning and deployment validation using `kind`.
* **TLS Implementation :** Secure ingress routing configuration supporting TLS termination.

---

=======
* **Continuous Deployment:** Automated cluster spinning and deployment validation using `kind`.
* **TLS Implementation:** Secure ingress routing configuration supporting TLS termination.

---

## Problem Statement 2: Health Check & Automation Script

### Overview
A robust health-check automation script was developed to continuously monitor the availability and uptime of the Wisecow web application endpoint. It queries the endpoint, validates the HTTP response code (`200 OK`), and handles downtime or connection errors gracefully.

## Problem Statement 3: Zero-Trust KubeArmor Policy

### Overview
To secure the Kubernetes workload against unauthorized container privilege escalations and system access, a zero-trust security policy was implemented using KubeArmor (defined in `k8s/kubearmor-policy.yaml`).

### Verification & Evidence
./screenshots 
>>>>>>> 74566da (feat: complete health check, monitoring scripts, and KubeArmor zero-trust policy with documentation)
