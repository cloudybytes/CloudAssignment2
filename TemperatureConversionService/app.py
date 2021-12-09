from flask import Flask,request
from multiprocessing import Value
app = Flask(__name__)

counter = Value('i', 0)
health = {"health" : "healthy"}

@app.route('/health')
def health_check():
    return health

@app.route('/toggle_health', methods = ['POST'])
def toggle_health():
    health["health"] = request.form.get("health")
    return health

@app.route('/count', methods= ['GET'])
def count_requests():
    return str(counter.value)
    
@app.route('/')
def hello():
    return 'Temperature Converter Service'

@app.route('/<value>')
def temp_conversion(value):
    with counter.get_lock():
        counter.value += 1
    fah = float(value)*1.8 +32
    return str(fah)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8006, debug=True)