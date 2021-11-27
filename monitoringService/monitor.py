import docker
import time
import json
import requests

client = docker.from_env()

containerStatus = {}

while True:
    containerList = client.containers.list()
    body = {}
    for container in containerList:
        if 'service' in container.labels.keys():
            containerStats = container.stats(stream=False)
            cpuUseage = containerStats['cpu_stats']['cpu_usage']['total_usage']
            memoryLimit = containerStats['memory_stats']['limit']
            memoryMaxUsed = containerStats['memory_stats']['max_usage']
            memoryUsed = containerStats['memory_stats']['usage']
            port = container.labels['port']
            # Get ip from database
            response = requests.get('http://127.0.0.1:8001/health')
            if response.status_code == 200:
                containerStatus[container.id] = time.time()
            else:
                if containerStatus[container.id] == 0:
                    # Send request to CSS to restart service
                else:
                    containerStatus[container.id] = 0
            body[container.id] = {
                'service': container.labels['service'],
                'cpu_usage': cpuUseage,
                'max_memory': memoryLimit,
                'max_used': memoryMaxUsed,
                'mem_usage': memoryUsed
            }
            # Send body to Auto-Scaler
        else:
            containerStats = container.stats(stream=False)
            print(json.dumps(containerStats, indent=3, sort_keys=True))
    time.sleep(5)