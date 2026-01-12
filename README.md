# gg-rollouts-hpa

Progressive delivery on AWS EKS [Elastic Kubernetes Service] using Argo Rollouts [Argo Progressive Delivery Controller] (canary) plus HPA [Horizontal Pod Autoscaler].

## ✅ What this demonstrates
- **Argo Rollouts** installed and running
- **Canary rollout** reaching **Healthy**
- **HPA autoscaling** from **min 3** to **max 10** pods under CPU load
- **Service LoadBalancer** exposure for the demo app

## 🧱 Repo structure
- `k8s/rollouts/rollout.yaml` → Rollout resource (canary strategy)
- `k8s/rollouts/service.yaml` → LoadBalancer service
- `k8s/hpa/hpa.yaml` → HPA for the Rollout
- `docs/screenshots/` → Proof screenshots (CloudShell outputs)

## 🚀 Deploy steps (commands used)
### 1) Create namespace
```bash
kubectl create ns rollouts-demo

