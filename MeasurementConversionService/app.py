from flask import Flask, request
import time

app = Flask(__name__)

health = {"health" : "healthy"}

@app.route('/health')
def health_check():
    return health

@app.route('/toggle_health', methods = ['POST'])
def toggle_health():
    health["health"] = request.form.get("health")
    return health


@app.route('/')
def hello():
    return 'Measurement Converter Service from Kg to g'

@app.route('/<int:kg>')
def temp_conversion(kg):
    g = kg*1000
    time.sleep(5)
    return str(g)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8007, debug=True)