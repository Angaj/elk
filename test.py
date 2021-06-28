from flask import Flask, jsonify
from elasticapm.contrib.flask import ElasticAPM
from elasticapm.handlers.logging import LoggingHandler
app = Flask(__name__)
apm = ElasticAPM(app, server_url='http://20.72.96.106:8200', service_name='flask-app-1', logging=True)
@app.route('/')
def index():
    return jsonify({"message": "response ok"}), 200
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)