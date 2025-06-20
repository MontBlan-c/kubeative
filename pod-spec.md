# Kubernetes Pod Specification: All Possible Fields

This list covers all official fields for the `Pod` resource, based on the [Kubernetes API reference (v1.29)](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.29/#podspec-v1-core) and practical usage.  
**Note:** Some fields are advanced/rare or only meaningful in certain contexts.

---

## metadata

| Field                    | Description                                                                                  |
|--------------------------|----------------------------------------------------------------------------------------------|
| `name`                   | Name of the Pod.                                                                             |
| `namespace`              | Namespace for the Pod.                                                                       |
| `labels`                 | Key-value pairs for organizing/selecting the Pod.                                            |
| `annotations`            | Arbitrary metadata.                                                                          |
| `generateName`           | Prefix for generating a unique name.                                                         |
| `finalizers`             | List of finalizers to be executed before Pod is deleted.                                     |
| `ownerReferences`        | References to objects owning this Pod.                                                       |
| `clusterName`            | Name of the cluster this object belongs to.                                                  |
| `managedFields`          | Managed fields info (server-side apply).                                                     |
| `creationTimestamp`      | Timestamp of creation.                                                                       |
| `deletionTimestamp`      | Timestamp when object is scheduled for deletion.                                             |
| `resourceVersion`        | Version for concurrency control.                                                             |
| `uid`                    | Unique ID.                                                                                   |

---

## spec

| Field                                 | Description                                                                               |
|----------------------------------------|-------------------------------------------------------------------------------------------|
| `activeDeadlineSeconds`                | Time (seconds) before Pod is terminated.                                                  |
| `affinity`                            | Node/pod affinity scheduling rules.                                                       |
| `automountServiceAccountToken`         | Mount the default service account token.                                                  |
| `containers`                          | List of containers (required, at least one).                                              |
| `dnsConfig`                           | DNS parameters for the Pod.                                                               |
| `dnsPolicy`                           | DNS policy (`ClusterFirst`, `Default`, etc.).                                             |
| `enableServiceLinks`                   | Inject service environment variables.                                                     |
| `ephemeralContainers`                  | List of ephemeral containers for debugging.                                               |
| `hostAliases`                         | Add custom entries to `/etc/hosts`.                                                       |
| `hostIPC`                             | Use host's IPC namespace.                                                                 |
| `hostNetwork`                         | Use host's network.                                                                       |
| `hostPID`                             | Use host's process namespace.                                                             |
| `hostname`                            | Pod hostname.                                                                             |
| `imagePullSecrets`                     | List of image pull secret names.                                                          |
| `initContainers`                      | List of init containers.                                                                  |
| `nodeName`                            | Schedule Pod to a specific node.                                                          |
| `nodeSelector`                        | Node label selectors.                                                                     |
| `os`                                  | Specify operating system (e.g., Linux, Windows).                                          |
| `overhead`                            | Resource overhead for running a Pod.                                                      |
| `preemptionPolicy`                     | Pod preemption policy.                                                                    |
| `priority`                            | Integer priority value.                                                                   |
| `priorityClassName`                   | Priority class name.                                                                      |
| `readinessGates`                      | Extra readiness gates (custom conditions).                                                |
| `restartPolicy`                       | `Always`, `OnFailure`, `Never`.                                                           |
| `runtimeClassName`                    | Container runtime class.                                                                  |
| `schedulerName`                       | Name of the scheduler to dispatch this Pod.                                               |
| `securityContext`                     | Pod-level security options (run as user, group, SELinux, etc.).                           |
| `serviceAccount`                      | Name of the ServiceAccount to use.                                                        |
| `serviceAccountName`                  | [Deprecated] Use `serviceAccount`.                                                        |
| `setHostnameAsFQDN`                   | Set pod hostname as FQDN.                                                                 |
| `shareProcessNamespace`                | Containers share process namespace.                                                       |
| `subdomain`                           | Pod subdomain for DNS.                                                                    |
| `terminationGracePeriodSeconds`        | Time to wait before forceful kill.                                                        |
| `tolerations`                         | List of node taints this Pod will tolerate.                                               |
| `topologySpreadConstraints`            | Spread pods across topology domains (nodes/zones).                                        |
| `volumes`                             | List of volumes to be mounted by containers.                                              |

---

### spec.containers[] and spec.initContainers[] & spec.ephemeralContainers[]

| Field                     | Description                                                                                 |
|---------------------------|---------------------------------------------------------------------------------------------|
| `name`                    | Name of the container.                                                                     |
| `image`                   | Docker image to use.                                                                       |
| `command`                 | Entrypoint array; overrides Docker ENTRYPOINT.                                              |
| `args`                    | Arguments to the entrypoint.                                                               |
| `workingDir`              | Working directory for the container.                                                       |
| `ports`                   | List of container ports to expose.                                                         |
| `env`                     | List of environment variables.                                                             |
| `envFrom`                 | Populate env from ConfigMap/Secret.                                                        |
| `resources`               | Resource requests/limits (CPU, memory, etc.).                                              |
| `volumeMounts`            | Volumes to mount into the container's filesystem.                                          |
| `livenessProbe`           | Health check; restarts container if fails.                                                 |
| `readinessProbe`          | Readiness check before sending traffic.                                                    |
| `startupProbe`            | Startup check for the container.                                                           |
| `lifecycle`               | Actions before/after container start/stop.                                                 |
| `securityContext`         | Container security settings (user, capabilities, etc.).                                    |
| `stdin`                   | Keep stdin open.                                                                           |
| `stdinOnce`               | Close stdin once the attached client disconnects.                                          |
| `tty`                     | Allocate a TTY for the container.                                                          |
| `terminationMessagePath`  | Path for container termination message.                                                    |
| `terminationMessagePolicy`| Policy for writing termination messages.                                                   |
| `imagePullPolicy`         | `Always`, `IfNotPresent`, `Never`.                                                         |
| `envFrom`                 | Set env from ConfigMap/Secret.                                                             |
| `volumeDevices`           | Map block devices to the container.                                                        |

**ephemeralContainers[]** (special usage):  
- `targetContainerName`: Container to attach to.  
- Used for debugging existing pods.

---

### spec.volumes[] (possible types and fields)

| Type                       | Key Fields/Description                                                                   |
|----------------------------|-----------------------------------------------------------------------------------------|
| `emptyDir`                 | Temporary directory shared among containers.                                            |
| `hostPath`                 | Mount a file or directory from the host node.                                           |
| `configMap`                | Mount a ConfigMap as files or env.                                                      |
| `secret`                   | Mount a Secret as files or env.                                                         |
| `persistentVolumeClaim`    | Attach a PersistentVolumeClaim.                                                         |
| `downwardAPI`              | Expose pod/container fields as files.                                                   |
| `projected`                | Combine multiple volume sources into one.                                               |
| `csi`                      | Mount a CSI volume.                                                                     |
| `awsElasticBlockStore`     | AWS EBS volume.                                                                         |
| `gcePersistentDisk`        | GCE Persistent Disk volume.                                                             |
| `nfs`                      | NFS volume.                                                                             |
| `iscsi`                    | iSCSI volume.                                                                           |
| `rbd`                      | Ceph RBD volume.                                                                        |
| `cinder`                   | OpenStack Cinder volume.                                                                |
| `fc`                       | Fibre Channel volume.                                                                   |
| `azureDisk`                | Azure Disk volume.                                                                      |
| `azureFile`                | Azure File volume.                                                                      |
| `vsphereVolume`            | vSphere volume.                                                                         |
| `photonPersistentDisk`     | Photon Controller volume.                                                               |
| `quobyte`                  | Quobyte volume.                                                                         |
| `flexVolume`               | FlexVolume plugin.                                                                      |
| `flocker`                  | Flocker volume.                                                                         |
| `portworxVolume`           | Portworx volume.                                                                        |
| `scaleIO`                  | ScaleIO volume.                                                                         |
| `storageos`                | StorageOS volume.                                                                       |
| `glusterfs`                | GlusterFS volume.                                                                       |
| `cephfs`                   | CephFS volume.                                                                          |

**Each type has its own required and optional fields.**

---

### spec.dnsConfig

| Field                | Description                          |
|----------------------|--------------------------------------|
| `nameservers`        | List of DNS servers.                 |
| `searches`           | List of DNS search domains.          |
| `options`            | List of DNS options.                 |

---

### spec.affinity

| Field                | Description                          |
|----------------------|--------------------------------------|
| `nodeAffinity`       | Node selection rules.                |
| `podAffinity`        | Pod affinity rules.                  |
| `podAntiAffinity`    | Pod anti-affinity rules.             |

---

### spec.securityContext

| Field                | Description                                      |
|----------------------|--------------------------------------------------|
| `runAsUser`          | User ID.                                         |
| `runAsGroup`         | Group ID.                                        |
| `fsGroup`            | File system group.                               |
| `seLinuxOptions`     | SELinux options.                                 |
| `supplementalGroups` | Extra group IDs.                                 |
| `sysctls`            | Kernel sysctls.                                  |
| `windowsOptions`     | Windows security settings.                       |
| `seccompProfile`     | Seccomp profile.                                 |
| `runAsNonRoot`       | Require running as non-root user.                |

---

### spec.topologySpreadConstraints

| Field                | Description                                      |
|----------------------|--------------------------------------------------|
| `maxSkew`            | Maximum skew across topology domains.            |
| `topologyKey`        | Node label key to spread across.                 |
| `whenUnsatisfiable`  | Scheduling behavior if constraint can't be met.  |
| `labelSelector`      | Selector for pods to spread.                     |

---

### spec.readinessGates

| Field                | Description                                      |
|----------------------|--------------------------------------------------|
| `conditionType`      | Name of the readiness condition.                 |

---

### spec.os

| Field                | Description                                      |
|----------------------|--------------------------------------------------|
| `name`               | OS name (e.g., linux, windows).                  |
| `features`           | OS features (future).                            |

---

## For exhaustive details

- [PodSpec (Kubernetes API Reference)](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.29/#podspec-v1-core)
- [Pod (Kubernetes API Reference)](https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.29/#pod-v1-core)

---

**Tip:**  
Most users only use a subset of these fields. Many are advanced or cloud-provider specific.  
For production, always check the version-specific Kubernetes docs.

