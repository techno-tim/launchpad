# gitlab runner

```bash
helm repo add gitlab https://charts.gitlab.io
```

`values.yml` is the default from
https://gitlab.com/gitlab-org/charts/gitlab-runner/blob/main/values.yaml

```bash
helm install --namespace default gitlab-runner -f values.yml gitlab/gitlab-runner
```

update

```bash
helm upgrade --namespace default gitlab-runner -f values.yml gitlab/gitlab-runner 
```
