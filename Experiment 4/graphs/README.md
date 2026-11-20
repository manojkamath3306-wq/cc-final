# Graphs for the Kubernetes Experiment

This folder contains a few concise comparison charts derived from the recorded experiment results.

## Included charts

- `node-resource-usage.svg` — CPU usage across the three nodes before scaling.
- `node-memory-usage.svg` — memory usage across the three nodes before scaling.
- `pod-distribution.svg` — pod placement comparison between 6 and 12 replicas.
- `service-success.svg` — success/failure breakdown for the HTTP checks through the NodePort Service.

## Interpretation

- The control-plane node carried the highest baseline CPU and memory load.
- The workload was spread evenly across all three nodes, with two pods per node at 6 replicas and four pods per node at 12 replicas.
- The service check showed 100% success rate for the tested HTTP requests.

These charts are intentionally simple and based on the observed values from the experiment recording and the lab documentation.
