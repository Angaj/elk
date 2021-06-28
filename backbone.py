from flask import Flask
from elasticapm.contrib.flask import ElasticAPM
import elasticapm

app = Flask(__name__)

server_url = 'http://20.72.96.106:8200/'
service_name = 'apm-server'
environment = 'dev'
secret_token= '39b703cc418f928462fb322138e8827b07181150'

apm = ElasticAPM(app, server_url=server_url, service_name=service_name, environment=environment, secret_token=secret_token)


@app.route('/')
def index():
    return "Hello World!"
if __name__ == '__main__':
    app.run(debug=True)