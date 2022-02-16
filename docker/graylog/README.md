# graylog


```bash
mkdir data
mkdir config
````

copy `./config` files to `config` folder



```bash
chown -R 1100:1100 ./data
chown -R 1100:1100 ./config
```

```bash
docker-compose up -d --force-recreate
```