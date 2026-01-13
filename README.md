# gg-rollouts-hpa

Progressive delivery using **Argo Rollouts [Argo Progressive Delivery Controller]** (stable + canary) and **HPA [Horizontal Pod Autoscaler]** on **EKS [Elastic Kubernetes Service]**.

## ✅ What this demo shows
- **Argo Rollouts** managing a **Rollout** (stable + canary)
- A **Service (type: LoadBalancer)** exposing the app
- **HPA** scaling the Rollout based on **CPU [Central Processing Unit]** usage
- Proof via real screenshots in `docs/screenshots/`

## 🧠 Architecture
- Diagram: `docs/diagrams/gg-rollouts-hpa-arch.png`

## 📦 Repo structure
- `k8s/rollouts/rollout.yaml`  → Rollout resource (canary steps)
- `k8s/rollouts/service.yaml`  → LoadBalancer Service
- `k8s/hpa/hpa.yaml`           → HPA targeting the Rollout
- `docs/screenshots/`          → Proof

## ✅ Prerequisites
- A working **EKS [Elastic Kubernetes Service]** cluster
- **kubectl [Kubernetes CLI]**
- Argo Rollouts controller installed (steps below)
- HPA requires Metrics API support (so `kubectl top` works)

## 🚀 Deploy (step-by-step)

### 1) Install Argo Rollouts
```bash
kubectl create namespace argo-rollouts
kubectl apply -n argo-rollouts -f https://github.com/argoproj/argo-rollouts/releases/latest/download/install.yaml
kubectl get pods -n argo-rollouts
