# gg-rollouts-hpa

[![Architecture](https://raw.githubusercontent.com/just2courageous/gg-rollouts-hpa/main/docs/architecture.png)](https://raw.githubusercontent.com/just2courageous/gg-rollouts-hpa/main/docs/architecture.png)

Progressive delivery using **Argo Rollouts (Argo Progressive Delivery Controller)** (stable + canary) and **HPA (Horizontal Pod Autoscaler)** on **EKS (Elastic Kubernetes Service)**.

## ✅ What this demo shows
- **Argo Rollouts (Argo Progressive Delivery Controller)** managing a **Rollout** (stable + canary)
- A **Service (type: LoadBalancer)** exposing the app
- **HPA (Horizontal Pod Autoscaler)** scaling the Rollout based on **CPU (Central Processing Unit)** usage
- Proof via real screenshots in **[docs/screenshots](docs/screenshots/)**

## 🧠 Architecture
- Diagram: [docs/architecture.png](https://raw.githubusercontent.com/just2courageous/gg-rollouts-hpa/main/docs/architecture.png)

## 📦 Repo structure
- **[k8s/rollouts/rollout.yaml](k8s/rollouts/rollout.yaml)** → Rollout resource (canary steps)
- **[k8s/rollouts/service.yaml](k8s/rollouts/service.yaml)** → LoadBalancer Service
- **[k8s/hpa/hpa.yaml](k8s/hpa/hpa.yaml)** → HPA targeting the Rollout
- **[docs/runbook.md](docs/runbook.md)** → Deploy, verify, cleanup
- **[docs/evidence.md](docs/evidence.md)** → Proof list
- **[docs/screenshots](docs/screenshots/)** → Screenshots

## 🧾 Evidence table (claim → proof)
| Claim | Proof (click) |
| --- | --- |
| Argo Rollouts (Argo Progressive Delivery Controller) installed | [p10-argo-install.png](docs/screenshots/p10-argo-install.png) |
| Cluster nodes are running | [p10-nodes.png](docs/screenshots/p10-nodes.png) |
| Rollout created (canary object exists) | [p10-rollout-created.png](docs/screenshots/p10-rollout-created.png) |
| Service has External IP (LoadBalancer) | [p10-svc-external-ip.png](docs/screenshots/p10-svc-external-ip.png) |
| HPA (Horizontal Pod Autoscaler) is working | [p10-hpa-success.png](docs/screenshots/p10-hpa-success.png) |
| Rollout ends stable/healthy | [p10-final-stable.png](docs/screenshots/p10-final-stable.png) |
| Final pods state captured | [p10-final-pods.png](docs/screenshots/p10-final-pods.png) |
| Metrics pipeline works (`kubectl top`) | [p10-top-nodes.png](docs/screenshots/p10-top-nodes.png) |

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
