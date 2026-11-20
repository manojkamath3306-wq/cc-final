#!/usr/bin/env bash
set -euo pipefail
SA="system:serviceaccount:rbac-demo:pod-reader"
echo "=== Expected ALLOWED checks (yes) ==="
for verb in get list watch; do
  printf "%-8s pods: " "$verb"
  kubectl auth can-i "$verb" pods --as="$SA" -n rbac-demo
done
echo
echo "=== Expected NOT-GRANTED checks (no, unless other bindings grant them) ==="
for verb in create update delete; do
  printf "%-8s pods: " "$verb"
  kubectl auth can-i "$verb" pods --as="$SA" -n rbac-demo
done
printf "%-8s secrets: " "list"
kubectl auth can-i list secrets --as="$SA" -n rbac-demo
echo
echo "=== Namespace-scope check (expected no, unless other bindings grant it) ==="
kubectl auth can-i list pods --as="$SA" -n default
