#!/usr/bin/env bash
set -euo pipefail
kubectl delete namespace rbac-demo --ignore-not-found=true
echo "Project namespace removed. The Minikube cluster remains available."
