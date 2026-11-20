# Screenshot Index

All screenshots below are extracted directly from the supplied WEBM recording. They are not recreated or synthetically generated.

| Screenshot | Approx. video time | Stage | What it demonstrates |
|:--|--:|:--|:--|
| `01-cluster-and-node-verification.jpg` | ~28 s | Cluster verification | Kind cluster creation completion, three Ready nodes, Metrics Server setup and kubectl context. |
| `02-resource-usage-and-six-replica-deployment.jpg` | ~34 s | Initial metrics and deployment | Node metrics, application of resource-demo, six Nginx Pods and rollout. |
| `03-six-pods-scheduled-across-three-nodes.jpg` | ~38 s | Six-Pod placement | The six Running Pods and their node assignments; two Pods appear on each node. |
| `04-scheduler-events-and-pod-placement.jpg` | ~42 s | Scheduling events | Kubernetes events showing Pod creation and successful scheduling to the three nodes. |
| `05-twelve-replica-scaling-and-service-creation.jpg` | ~58 s | Scaling and Service creation | Scaling to twelve replicas, observed node placement, and creation of nginx-service. |
| `06-nodeport-service-endpoints-and-http-tests.jpg` | ~62 s | Service verification | NodePort 30080, endpoints and EndpointSlice backends, and ten HTTP 200 responses. |
| `07-high-resource-pod-pending.jpg` | ~66 s | Scheduling extension | High-resource Pod remains Pending with no node assignment. |
| `08-high-resource-pod-request-details.jpg` | ~68 s | Pending Pod inspection | Pod description shows CPU request 100, memory request 64Mi, and PodScheduled False. |
| `09-insufficient-cpu-event-and-cleanup.jpg` | ~70 s | Scheduling failure and cleanup | FailedScheduling event reports insufficient CPU; experiment Deployments and Service are deleted. |
