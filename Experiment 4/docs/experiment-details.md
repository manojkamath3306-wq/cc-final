# Experiment 4 — Source and Implementation Details

## Sources used
- Experiment 4 lab manual: `kubernetes_resource_allocation_scheduling_load_balancing.pdf` (4 pages).
- Experiment recording: `Screencast from 2026-11-03 14-27-11.webm` (approximately 73.9 seconds).
- Experiment 2 reference archive: `CC-LAB-EXP2-DOCKER-master.zip`, used for README structure, level of detail, tables, screenshots, and repository presentation only.

## Source alignment
The lab manual defines the aim, required Kubernetes concepts, eleven procedural steps, observation table, expected outcomes, result, and suggested high-CPU scheduling extension. The recording supplies the concrete environment and observed outputs documented in README.md.

## Recorded environment
- Ubuntu 24.04.4 LTS host.
- Kind cluster `practical-cluster`.
- Three nodes: `practical-cluster-control-plane`, `practical-cluster-worker`, `practical-cluster-worker2`.
- Kubernetes node version v1.37.0.
- Debian GNU/Linux 13 (trixie) node image.
- Kernel 7.0.0-34-generic.
- containerd 2.3.4.
- Nginx image `nginx:latest`.

## Confirmed recorded results
- Six Pods: two per node in the captured placement.
- Twelve Pods: four per node in the captured placement.
- NodePort Service `nginx-service`, ClusterIP 10.96.195.29, port 80, NodePort 30080.
- Ten `curl` requests returned HTTP 200.
- High-resource Pod remained Pending; request displayed as CPU 100 and memory 64Mi.
- Scheduler event: `0/3 nodes are available: 3 Insufficient cpu`.
- Cleanup removed the two Deployments and the Service.

## Deliberate omissions
The high-resource YAML contents were not recovered from the source files; only the applied filename and the Pod's observed request/condition were visible. Therefore, no high-resource YAML is fabricated. The recording does not show a browser window, a per-Pod request distribution measurement, or a complete before/after resource-utilization table. These are explicitly identified as evidence limitations in the README.
