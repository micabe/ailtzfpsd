## This is Proof-of-Concept script that loads Ansible inventory to Zookeeper for service discovery by Prometheus

### INSTALLATION:
```
git clone git@github.com:ngilmitdinov/ailtzfpsd.git
cd ailtzfpsd
pip install -r requirements.txt
```

### USAGE:
```
python inventory-uploader.py $zookeper_host $inventory-name
```

### TESTING:
```
docker-compose up -d
python inventory-uploader.py localhost inventory
```

prometheus-server running on localhost:9090

zookeeper runnig on localhost:2181

node_exporter running on localhost:9100
