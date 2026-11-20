#!/usr/bin/env bash
set -euo pipefail
ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"
kubectl apply -f manifests/01-namespace.yaml
kubectl apply -f manifests/02-serviceaccount.yaml
kubectl apply -f manifests/03-role.yaml
kubectl apply -f manifests/04-rolebinding.yaml
kubectl apply -f manifests/05-test-pod.yaml
echo
echo "Wait for the test Pod with:"
echo "kubectl wait --for=condition=Ready pod/rbac-test-pod -n rbac-demo --timeout=120s"
