# Kubernetes RBAC with Service Accounts

<p align="center">
  <img src="https://img.shields.io/badge/Kubernetes-RBAC-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white" alt="Kubernetes RBAC" />
  <img src="https://img.shields.io/badge/Cloud_Computing-Lab-0A66C2?style=for-the-badge" alt="Cloud Computing Lab" />
  <img src="https://img.shields.io/badge/Ubuntu-24.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" alt="Ubuntu" />
  <img src="https://img.shields.io/badge/Kubernetes_Cluster-KIND-00ADD8?style=for-the-badge&logo=docker&logoColor=white" alt="KIND" />
</p>

<p align="center">
  <strong>A practical implementation of Kubernetes Role-Based Access Control.</strong>
  <br>
  Demonstrating ServiceAccount identity, namespace-scoped permissions, and least-privilege authorization.
</p>

---

## Project Information

| Field | Details |
|:---|:---|
| Course | Cloud Computing Lab (26ECAC301) |
| Evaluation | Lab Evaluation 2 |
| Problem Statement | 18 — Basic RBAC with Service Accounts |
| Technology | Kubernetes RBAC |
| Operating System | Ubuntu 24.04 |
| Container Platform | Docker |
| Kubernetes Cluster | KIND |
| Development Environment | Visual Studio Code |
| Command-Line Tool | kubectl |

---

## 1. Objective

The objective of this project is to implement and demonstrate Role-Based Access Control (RBAC) in Kubernetes.

Kubernetes RBAC provides a mechanism to regulate access to cluster resources by assigning permissions to identities through Roles and RoleBindings.

In this implementation, a ServiceAccount named `pod-reader` is created inside the `rbac-demo` namespace. It is granted read-only access to Pods through a namespace-scoped Role.

The implementation demonstrates:

- Controlled access to Kubernetes resources.
- Namespace-level permission isolation.
- The relationship between ServiceAccounts, Roles, and RoleBindings.
- Allowed and denied API operations.
- The principle of least privilege.

## 2. Team Members

| Team Member | Student Registration Number |
|:---|:---|
| Mudit Nayak | `01FE24BCI076` |
| Kartik | `01FE24BCI072` |
| Manoj | `01FE24BCI077` |
| Vinayak | To be updated |

---

## 3. Architecture Overview

The implementation follows the Kubernetes RBAC authorization model.

```text
                    KUBERNETES CLUSTER
                            |
                            |
                   Namespace: rbac-demo
                            |
              +-------------+-------------+
              |                           |
              |                           |
       ServiceAccount                    Role
         pod-reader                pod-reader-role
              |                           |
              |                           |
              +-------------+-------------+
                            |
                       RoleBinding
                   pod-reader-binding
                            |
                            |
                  Namespace-Scoped Access
                            |
                 +----------+----------+
                 |                     |
              ALLOWED                DENIED
                 |                     |
             GET PODS              CREATE PODS
             LIST PODS              UPDATE PODS
             WATCH PODS             DELETE PODS
                                    LIST SECRETS
                                    ACCESS OTHER
                                    NAMESPACES
```

### RBAC Components

| Component | Description |
|:---|:---|
| Namespace | Provides a logical scope for Kubernetes resources. |
| ServiceAccount | Represents an identity for workloads or processes running inside the cluster. |
| Role | Defines permissions for accessing resources within a namespace. |
| RoleBinding | Associates a Role with a user, group, or ServiceAccount. |
| kubectl auth can-i | Checks whether an identity is authorized to perform a particular operation. |

---

## 4. Project Structure

```text
basic-rbac-vscode/
│
├── manifests/
│   ├── 01-namespace.yaml
│   ├── 02-serviceaccount.yaml
│   ├── 03-role.yaml
│   ├── 04-rolebinding.yaml
│   └── 05-test-pod.yaml
│
├── scripts/
│   ├── apply.sh
│   ├── verify.sh
│   └── cleanup.sh
│
├── screenshots/
│   ├── Screenshot from 2026-11-17 00-01-05.png
│   └── Screenshot from 2026-11-17 00-01-14.png
│
├── .vscode/
│   └── extensions.json
│
├── .gitignore
└── README.md
```

---

## 5. Prerequisites

The following tools are required:

| Tool | Purpose |
|:---|:---|
| Docker | Runs containerized Kubernetes nodes. |
| KIND | Creates a local Kubernetes cluster using Docker containers. |
| kubectl | Communicates with the Kubernetes API server. |
| Visual Studio Code | Provides the development environment. |

Verify the installations:

```bash
docker --version
kubectl version --client
kind version
code --version
```

---

## 6. Start the Kubernetes Cluster

Check the available KIND clusters:

```bash
kind get clusters
```

Select the existing project cluster:

```bash
kubectl config use-context kind-practical-cluster
```

Verify the cluster:

```bash
kubectl get nodes
```

Check the system Pods:

```bash
kubectl get pods -A
```

All cluster nodes should be in the `Ready` state before proceeding.

---

## 7. Implementation

The project uses separate YAML manifests to define and deploy each Kubernetes resource.

### Step 1 — Create the Namespace

Create an isolated namespace named `rbac-demo`.

```bash
kubectl apply -f manifests/01-namespace.yaml
```

### Step 2 — Create the ServiceAccount

Create the `pod-reader` identity inside the namespace.

```bash
kubectl apply -f manifests/02-serviceaccount.yaml
```

### Step 3 — Define the Role

Create a namespace-scoped Role that grants read-only access to Pods.

The Role contains the following permissions:

| API Group | Resource | Allowed Verbs |
|:---|:---|:---|
| Core API (`""`) | Pods | `get`, `list`, `watch` |

```bash
kubectl apply -f manifests/03-role.yaml
```

### Step 4 — Create the RoleBinding

Associate the `pod-reader` ServiceAccount with the `pod-reader-role`.

```bash
kubectl apply -f manifests/04-rolebinding.yaml
```

### Step 5 — Deploy the Test Pod

Deploy an Nginx Pod to provide a resource for testing.

```bash
kubectl apply -f manifests/05-test-pod.yaml
```

Wait for the Pod to become Ready:

```bash
kubectl wait \
  --for=condition=Ready \
  pod/rbac-test-pod \
  -n rbac-demo \
  --timeout=120s
```

### Automated Deployment

All resources can also be deployed using the provided script:

```bash
bash scripts/apply.sh
```

---

## 8. Resource Verification

Verify that all the Kubernetes resources have been created successfully.

### Check the Namespace

```bash
kubectl get namespaces
```

### Check the ServiceAccount

```bash
kubectl get serviceaccounts -n rbac-demo
```

### Check the Role

```bash
kubectl get roles -n rbac-demo
```

### Check the RoleBinding

```bash
kubectl get rolebindings -n rbac-demo
```

### Check the Test Pod

```bash
kubectl get pods -n rbac-demo
```

### View All Project Resources

```bash
kubectl get serviceaccounts,roles,rolebindings,pods -n rbac-demo
```

---

## 9. RBAC Authorization Testing

Authorization is verified using the `kubectl auth can-i` command.

The ServiceAccount identity is specified using Kubernetes impersonation.

```bash
SA="system:serviceaccount:rbac-demo:pod-reader"
```

### 9.1 Allowed Operations

The ServiceAccount should be allowed to perform the following operations:

```bash
kubectl auth can-i get pods \
  --as="$SA" -n rbac-demo

kubectl auth can-i list pods \
  --as="$SA" -n rbac-demo

kubectl auth can-i watch pods \
  --as="$SA" -n rbac-demo
```

Expected output:

```text
yes
yes
yes
```

### 9.2 Denied Operations

The ServiceAccount should not be allowed to perform write operations or access unauthorized resources.

```bash
kubectl auth can-i create pods \
  --as="$SA" -n rbac-demo

kubectl auth can-i update pods \
  --as="$SA" -n rbac-demo

kubectl auth can-i delete pods \
  --as="$SA" -n rbac-demo

kubectl auth can-i list secrets \
  --as="$SA" -n rbac-demo
```

Expected output:

```text
no
no
no
no
```

### 9.3 Namespace Isolation Test

Test whether the ServiceAccount can access Pods in the `default` namespace.

```bash
kubectl auth can-i list pods \
  --as="$SA" -n default
```

Expected output:

```text
no
```

This demonstrates that the RoleBinding grants permissions only within the `rbac-demo` namespace.

### Authorization Summary

| Operation | Expected Result | Description |
|:---|:---:|:---|
| Get Pods | YES | Read individual Pods |
| List Pods | YES | View Pods in the namespace |
| Watch Pods | YES | Monitor Pod changes |
| Create Pods | NO | Cannot create Pods |
| Update Pods | NO | Cannot modify Pods |
| Delete Pods | NO | Cannot delete Pods |
| List Secrets | NO | Cannot access Secrets |
| List Pods in `default` | NO | Cannot access another namespace |

---

## 10. Screenshots and Execution Evidence

The following screenshots document the implementation and authorization testing.

### Screenshot 1 — RBAC Setup and Resource Creation

Shows the creation of the Kubernetes namespace, ServiceAccount, Role, RoleBinding, and test Pod.

![RBAC Setup and Resource Creation](screenshots/Screenshot%20from%202026-11-17%2000-01-05.png)

### Screenshot 2 — RBAC Authorization Validation

Shows the authorization test results demonstrating permitted and denied operations.

![RBAC Authorization Validation](screenshots/Screenshot%20from%202026-11-17%2000-01-14.png)

---

## 11. Cleanup

To remove the resources created by this project:

```bash
bash scripts/cleanup.sh
```

This removes the project resources without deleting the entire Kubernetes cluster.

To stop the KIND cluster, you can stop its Docker containers or use the appropriate KIND cluster-management commands.

**Note:** Do not delete a shared KIND cluster if it is being used by other projects.

---

## 12. Conclusion

This project demonstrates the implementation of Role-Based Access Control in Kubernetes using ServiceAccounts, Roles, and RoleBindings.

A dedicated ServiceAccount is assigned limited permissions to access Pods within a specific namespace. Authorization tests verify that permitted operations succeed while unauthorized operations are restricted.

The implementation demonstrates the principle of least privilege and highlights the importance of identity-based access control in containerized environments.

Through this practical, the fundamental concepts of Kubernetes authentication, authorization, resource isolation, and RBAC policy enforcement are explored.

---

## 13. References

1. [Kubernetes RBAC Documentation](https://kubernetes.io/docs/reference/access-authn-authz/rbac/)
2. [Kubernetes ServiceAccounts](https://kubernetes.io/docs/concepts/security/service-accounts/)
3. [Kubernetes Authorization](https://kubernetes.io/docs/reference/access-authn-authz/authorization/)
4. [KIND Documentation](https://kind.sigs.k8s.io/)
5. [Docker Documentation](https://docs.docker.com/)
6. [kubectl Documentation](https://kubernetes.io/docs/reference/kubectl/)

---

<p align="center">
  <strong>Cloud Computing Lab — Lab Evaluation 2</strong>
  <br>
  Kubernetes Role-Based Access Control with Service Accounts
</p>
