import json

import requests


def test_prometheus_is_available():
    response = requests.get("http://localhost:9090")
    assert response.ok


def test_targets_connected_to_prometheus():
    response = requests.get("http://localhost:9090/api/v1/targets")
    data = json.loads(json.dumps(response.json()))
    assert(
        data["data"]["activeTargets"][0]["labels"]["instance"] == "node_exporter:9100"
    )
    assert data["data"]["activeTargets"][0]["health"] == "up"
