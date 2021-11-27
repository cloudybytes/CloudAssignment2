from flask import Flask
from flask import request

app = Flask(__name__)

# 1- Threshold Based
# 2- Queuing Theory
# 3- Control Theory
# 4- Time Series Analysis
scalingType = 1

thresholdMemory=512

@app.route('/')
def hello():
    return 'Auto_Scaler Service'

@app.route('/updateData', methods=['POST'])
def updateData():
    if request.method == 'POST':
        body = request.json
        for containerId in body.keys():
            print(containerId)
            data = {}
            if body[containerId]['max_used'] > 0.9 * thresholdMemory:
                data ['service'] = body[containerId]['service']
                data['action'] = '+1'
                requests.post('http://127.0.0.1:8002/schedule', json=data)
            elif body[containerId]['max_used'] > 0.9 * thresholdMemory:
                data ['service'] = body[containerId]['service']
                data['action'] = '+1'
                requests.post('http://127.0.0.1:8002/schedule', json=data)
    return 'Hello'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001, debug=True)