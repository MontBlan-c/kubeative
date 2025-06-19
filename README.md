# Kubeitive Imperative-to-YAML Pod Generator

This script converts imperative command-line flags into a full-featured Kubernetes Pod YAML manifest.

## Usage

```sh
python3 Code run <pod-name> --container=<container-flags> [more --container=...] [pod-level flags...]
```

You can specify almost all Pod spec options via flags.

---

## Container Flags (`--container=...`)

- **name**: Required. Container name.
- **image**: Required. Container image.
- **ports**: Ex: `ports=80,443,8080/tcp`
- **env**: Ex: `env=MYVAR=foo,MYVAR2=bar`
- **command**: Ex: `command=/bin/sh -c`
- **args**: Ex: `args=sleep 1000`
- **requests-memory**: Ex: `requests-memory=128Mi`
- **requests-cpu**: Ex: `requests-cpu=100m`
- **limits-memory**: Ex: `limits-memory=256Mi`
- **limits-cpu**: Ex: `limits-cpu=200m`
- **requests**: Ex: `requests=cpu=100m,memory=128Mi`
- **limits**: Ex: `limits=cpu=200m,memory=256Mi`
- **volumeMounts**: Ex: `volumeMounts=mountPath=/data,name=datavol`
  - Multiple: separate with `;` (semicolon)
- **stdin**: `stdin=true` to enable
- **tty**: `tty=true` to enable
- **workingDir**: Ex: `workingDir=/work`

**Example:**
```sh
--container='name=web,image=nginx:1.24.0,ports=80,env=FOO=bar,requests-memory=64Mi,limits-cpu=200m,volumeMounts=mountPath=/data,name=datavol'
```

---

## Volume Flags (`--volume=...`)

- **name**: Required. Volume name.
- **type**: `emptyDir` | `configMap` | `secret` | `hostPath`
- **configMapName**: For configMap volumes.
- **secretName**: For secret volumes.
- **path**, **hostPathType**: For hostPath volumes.

**Examples:**
```sh
--volume='name=datavol,type=emptyDir'
--volume='name=cmvol,type=configMap,configMapName=myconfig'
--volume='name=secretvol,type=secret,secretName=mysecret'
--volume='name=hpvol,type=hostPath,path=/tmp,hostPathType=Directory'
```

---

## Pod-Level Flags

- **--restart-policy**: Always | OnFailure | Never
- **--node-selector**: `key1=val1,key2=val2`
- **--affinity**: JSON string of affinity spec
- **--tolerations**: `key=dedicated,value=db,effect=NoSchedule;key=...`
- **--labels**: `key1=val1,key2=val2`
- **--annotations**: `key1=val1,key2=val2`
- **--service-account**: ServiceAccount name
- **--host-network**: Set hostNetwork: true
- **--dns-policy**: E.g. ClusterFirst, Default, etc.
- **--image-pull-secrets**: Comma-separated names
- **--security-context**: JSON string of pod securityContext

---

## Global Resource Flags (applies to all containers unless overridden)

- **--requests**: Ex: `cpu=100m,memory=64Mi`
- **--limits**: Ex: `cpu=200m,memory=128Mi`
- **--requests-memory**: Ex: `128Mi`
- **--requests-cpu**: Ex: `100m`
- **--limits-memory**: Ex: `256Mi`
- **--limits-cpu**: Ex: `200m`

---

## Example: Full Usage

```sh
python3 Code run mypod \
  --container='name=web,image=nginx:1.24.0,ports=80,env=FOO=bar,requests-memory=64Mi,limits-cpu=200m,volumeMounts=mountPath=/data,name=datavol' \
  --container='name=sidecar,image=busybox,command=sleep,args=1000,env=BAR=foo' \
  --volume='name=datavol,type=emptyDir' \
  --restart-policy=Always \
  --node-selector=disktype=ssd,region=us-east \
  --labels=app=web,tier=frontend \
  --annotations=purpose=test \
  --service-account=mysa \
  --host-network \
  --dns-policy=ClusterFirst \
  --image-pull-secrets=mysecret \
  --tolerations='key=dedicated,value=db,effect=NoSchedule' \
  --requests=cpu=200m,memory=128Mi \
  --limits=cpu=300m,memory=256Mi
```

---

## Tips

- Enclose each `--container` or `--volume` argument in single quotes if using `,` or `=`.
- Use `--container` multiple times for multiple containers.
- Use `--volume` multiple times for multiple volumes.
- For complex affinity or securityContext, pass a JSON string.

---

## Output

The script prints the YAML manifest to standard output.

---

## Requirements

- Python 3
- PyYAML (`pip install pyyaml`)

---

## Limitations

- Not every Pod spec field is covered, but most practical ones are.
- For extremely complex fields (affinity, securityContext), pass as JSON string.
- Not a drop-in replacement for `kubectl run`.

---

## License

MIT
