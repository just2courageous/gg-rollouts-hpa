# gg-rollouts-hpa

[![Architecture](https://github.com/just2courageous/gg-rollouts-hpa/blob/main/docs/architecture.png?raw=true)](https://github.com/just2courageous/gg-rollouts-hpa/blob/main/docs/architecture.png?raw=true)


Progressive delivery using **Argo Rollouts (Argo Progressive Delivery Controller)** (stable + canary) and **HPA (Horizontal Pod Autoscaler)** on **EKS (Elastic Kubernetes Service)**.

## ✅ What this demo shows
- **Argo Rollouts (Argo Progressive Delivery Controller)** managing a **Rollout** (stable + canary)
- A **Service (type: LoadBalancer)** exposing the app
- **HPA (Horizontal Pod Autoscaler)** scaling the Rollout based on **CPU (Central Processing Unit)** usage
- Proof via real screenshots in **[docs/screenshots](docs/screenshots/)**

## 🧠 Architecture
- Diagram: **[docs/architecture.png](https://github.com/just2courageous/gg-rollouts-hpa/blob/main/docs/architecture.png?raw=true)**

## 📦 Repo structure
- **[k8s/rollouts/rollout.yaml](k8s/rollouts/rollout.yaml)** → Rollout resource (canary steps)
- **[k8s/rollouts/service.yaml](k8s/rollouts/service.yaml)** → LoadBalancer Service
- **[k8s/hpa/hpa.yaml](k8s/hpa/hpa.yaml)** → HPA targeting the Rollout
- **[docs/runbook.md](docs/runbook.md)** → Deploy, verify, cleanup
- **[docs/evidence.md](docs/evidence.md)** → Proof list
- **[docs/screenshots](docs/screenshots/)** → Screenshots

## 🎥 Demo (YouTube (video platform))
- Demo video: (add link)

## ✅ Prerequisites
- A working **EKS (Elastic Kubernetes Service)** cluster
- **kubectl (Kubernetes command line tool)**
- **Metrics Server (Kubernetes metrics)** so `kubectl top` works

## 🚀 Deploy (step by step)

### 1) Install Argo Rollouts (Argo Progressive Delivery Controller)
```bash
kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
kubectl get pods -n argo-rollouts
