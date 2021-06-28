# initialize using environment variables
from elasticapm.contrib.flask import ElasticAPM
from flask import Flask

app = Flask(__name__)
# apm = ElasticAPM(app)

# or configure to use ELASTIC_APM in your application's settings
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'apm-server-1623307401-apm-server',
    'SECRET_TOKEN': 'ZXlKaGJHY2lPaUpTVXpJMU5pSXNJbXRwWkNJNklrdGpPRE5YVWxaVGVrTmhOVmxWT1RSVFJtcDVhRzVSWmxwdU1uaElSVlIzYkVGbGQweElRVWhzVVhjaWZRLmV5SnBjM01pT2lKcmRXSmxjbTVsZEdWekwzTmxjblpwWTJWaFkyTnZkVzUwSWl3aWEzVmlaWEp1WlhSbGN5NXBieTl6WlhKMmFXTmxZV05qYjNWdWRDOXVZVzFsYzNCaFkyVWlPaUprWldaaGRXeDBJaXdpYTNWaVpYSnVaWFJsY3k1cGJ5OXpaWEoyYVdObFlXTmpiM1Z1ZEM5elpXTnlaWFF1Ym1GdFpTSTZJbUZ3YlMxelpYSjJaWEl0TVRZeU16TXdOelF3TVMxaGNHMHRjMlZ5ZG1WeUxYUnZhMlZ1TFRoaVltaHhJaXdpYTNWaVpYSnVaWFJsY3k1cGJ5OXpaWEoyYVdObFlXTmpiM1Z1ZEM5elpYSjJhV05sTFdGalkyOTFiblF1Ym1GdFpTSTZJbUZ3YlMxelpYSjJaWEl0TVRZeU16TXdOelF3TVMxaGNHMHRjMlZ5ZG1WeUlpd2lhM1ZpWlhKdVpYUmxjeTVwYnk5elpYSjJhV05sWVdOamIzVnVkQzl6WlhKMmFXTmxMV0ZqWTI5MWJuUXVkV2xrSWpvaVpESXpPR1psTUdRdFpEVTJaUzAwTlRVNUxXSm1aV1V0TlRNeE16UmpOV1poTURGbElpd2ljM1ZpSWpvaWMzbHpkR1Z0T25ObGNuWnBZMlZoWTJOdmRXNTBPbVJsWm1GMWJIUTZZWEJ0TFhObGNuWmxjaTB4TmpJek16QTNOREF4TFdGd2JTMXpaWEoyWlhJaWZRLnFoRHBvZm9CVzNUMTlIcl9XekFmWU5hZXZwS0UzbXBaWU1KMWhteHJlejdNOU5nQW1pSmpnUmhkNEg3Y2ZCZkFVNnpwSzNidEVLd1FlODVsalpzcHBZTmRQUl9lWXdUc1htUjhORk1DWlZvZWZtZG1Ib3NJSHVGa0VEMG8zOFJBSXlCUFhBWHh1cHdNWmRvWnhOODdMTmVERWp1cm1SUzIwTk9ySUdFSGtxQUlLNEZ4U1VwdkFmVlQ0OEZLNHVzTnVSN3JkZmI5UjBsdVpDTmZjOHNKdHFzUTN4Y01EX1I5TExFUmlQY2Z3cVI2RFgyb24waThyckxpREpIVExZcTRHWllVX09QOVZITFZ6aVdfak1FTWxOM29NS3RzanhLOG03Wlloem54aWpwVlhpU2pFbjFjWl9Id0tMTWluLTI2SExUeDBOR08zT0lKNWJ3bVlDNzJjYjZKZThkVHZwQzRtWHdCeHMyQjVCLXhTSDJ2WEluTVhjYXlrT3B1aTZCNVNLUkF4WUVLY3Z6dmJZREhVTzk1OWtiN1ZpdEhTUldfODFXUFNGdjdkclhlUTNhRUZPZzAtMUdYTnE2bFRWUC1fWExYVFhGZ3ZfVE54bk1JU29GSWowSFFYRWJqR1NBYzNtdlV5QVNiUVVROFF4MVRkbndKQ1RVSmNINzNQNzE0REJnUUNmRjVfcGpJTWU2VGg2bGduR2MyVTBraGFPWEo1cmcyYndqRFlqSU90bkNjY3lpWGlDRWVpUmxDWUhQSl9JMjVDMGFLUmdmQk5rWHRaa09DQ3VXOEQ0SnNWTlN6Y3hBSjE3ZVV5aVlhd2w3eU5EMmRZUlh6QWVPX1g3Mlh2Z1k0WjdLdU5yWWFZVDZmVjMzMENpazRSODhhNnU2MDV0UEtwZTFWLVo0',
    'SERVER_URL': 'http://20.72.96.106:5601',
    # 'ENVIRONMENT': 'production',
}

apm = ElasticAPM(app)