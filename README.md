# Wisecow - Containerization & Kubernetes Deployment

A complete containerized DevOps solution for the Wisecow application, featuring automated CI/CD pipelines via GitHub Actions, ephemeral Kubernetes deployments with `kind`, and secure TLS ingress routing.

---

## Project Overview

This repository automates the build, test, and deployment lifecycle of the **Wisecow** application. The project meets all core requirements and includes advanced challenge goals:
* **Dockerization:** Optimized container image built on Ubuntu 22.04 with necessary system utilities (`cowsay`, `fortune-mod`, `netcat-openbsd`).
* **Kubernetes Manifests:** Production-ready Deployment, Service (`NodePort`), and Ingress configurations.
* **CI/CD Automation:** GitHub Actions workflow that builds and pushes images to Docker Hub on every commit to `main`.
* **Continuous Deployment :** Automated cluster spinning and deployment validation using `kind`.
* **TLS Implementation :** Secure ingress routing configuration supporting TLS termination.

---

