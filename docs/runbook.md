# Runbook: gg-rollouts-hpa

## ✅ Deploy
1) Install Argo Rollouts controller
2) Apply Rollout + Service
3) Apply HPA

## 🔍 Verify
- Argo pods:
  - `kubectl get pods -n argo-rollouts`
- Demo namespace:
  - `kubectl get all -n rollouts-demo`
- Rollout health:
  - `kubectl argo rollouts get rollout rollout-canary -n rollouts-demo`
- External IP:
  - `kubectl get svc -n rollouts-demo`
- HPA:
  - `kubectl get hpa -n rollouts-demo`
- Metrics:
  - `kubectl top nodes`

## 🧹 Cleanup
- `kubectl delete namespace rollouts-demo`
- `kubectl delete namespace argo-rollouts`