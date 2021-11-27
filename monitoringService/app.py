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
            # port = container.labels['port']
            # Get ip from database
            # response = requests.get('http://127.0.0.1:8001/health')
            # if response.status_code == 200:
            #     containerStatus[container.id] = time.time()
            # else:
            #     if containerStatus[container.id] == 0:
            #         # Send request to CSS to restart service
            #         body = {
            #             'action': 'restart',
            #             'id': container.id
            #         }
            #         response = requests.post('http://127.0.0.1:8001/action', json=body)
            #     else:
            #         containerStatus[container.id] = 0
            print('Inside Body')
            body[container.id] = {
                'service': container.labels['service'],
                'cpu_usage': cpuUseage,
                'max_memory': memoryLimit,
                'max_used': memoryMaxUsed,
                'mem_usage': memoryUsed
            }
        else:
            containerStats = container.stats(stream=False)
    print(body)
    requests.post('http://127.0.0.1:8001/updateData', json=body)
    time.sleep(5)