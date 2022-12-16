## This is Proof-of-Concept script that loads Ansible inventory to Zookeeper for service discovery by Prometheus

### TESTING:

```
docker-compose up -d
python inventory-uploader.py localhost inventory
```

### Create ZNode:

From zookeeper node execute:

```
zkCli.sh -server zookeeper-headless:2181 create /discovery ''
```
