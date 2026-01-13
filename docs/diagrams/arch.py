from diagrams import Diagram, Cluster, Edge
from diagrams.onprem.client import User
from diagrams.onprem.compute import Server
from diagrams.onprem.network import Internet

from diagrams.aws.compute import EKS, EC2
from diagrams.aws.network import ELB
from diagrams.aws.management import Cloudwatch

graph_attr = {
    "pad": "0.6",
    "splines": "ortho",
    "nodesep": "0.7",
    "ranksep": "0.9",
    "fontsize": "12",
    "bgcolor": "white",
}

with Diagram(
    "Green-Guard: Argo Rollouts + HPA on EKS",
    show=False,
    filename="docs/diagrams/gg-rollouts-hpa-arch",
    outformat="png",
    direction="LR",
    graph_attr=graph_attr,
):
    you = User("You\n(local)")
    internet = Internet("Internet")

    with Cluster("AWS"):
        with Cluster("EKS [Elastic Kubernetes Service]"):
            eks = EKS("EKS cluster")

            # Worker nodes (EKS managed nodes are EC2 under the hood)
            nodes = EC2("Worker nodes\n(EC2)")

            # Argo Rollouts controller
            argo = Server("Argo Rollouts\ncontroller\n(namespace: argo-rollouts)")

            with Cluster("rollouts-demo namespace"):
                rollout = Server("Rollout\n(kind: Rollout)")
                rs_stable = Server("ReplicaSet\nstable")
                rs_canary = Server("ReplicaSet\ncanary")
                pods = Server("Workload pods\n(stable/canary)")
                svc = ELB("Service\n(type: LoadBalancer)\nExternal IP")
                hpa = Server("HPA\n[Horizontal Pod Autoscaler]\n(target: Rollout)")
                metrics = Cloudwatch("Metrics API\n(Metrics Server)\nrequired for HPA")

            # Control-plane ↔ nodes
            eks >> Edge(label="schedules pods") >> nodes

            # Argo manages rollout
            argo >> Edge(label="reconciles") >> rollout
            rollout >> Edge(label="creates/updates") >> rs_stable
            rollout >> Edge(label="creates/updates") >> rs_canary
            rs_stable >> Edge(label="owns") >> pods
            rs_canary >> Edge(label="owns") >> pods

            # Service routes to pods
            svc >> Edge(label="routes traffic") >> pods

            # HPA scales rollout based on CPU metrics
            metrics >> Edge(label="feeds metrics") >> hpa
            hpa >> Edge(label="scales replicas") >> rollout

            # Where the controller runs
            argo << Edge(label="runs on") << nodes

    # User flow
    you >> Edge(label="kubectl apply\nYAML [YAML Ain't Markup Language]") >> eks
    internet >> Edge(label="HTTP") >> svc
