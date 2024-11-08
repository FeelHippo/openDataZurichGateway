from flask import Flask, request, jsonify
from flasgger import swag_from, Swagger
from logging.config import dictConfig
from dotenv import load_dotenv
import xmltodict, json
import collections.abc
import urllib.request
import logging
import sys
import os

try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections

def create_app():
    
    # https://betterstack.com/community/guides/logging/how-to-start-logging-with-flask/
    dictConfig(
        {
            "version": 1,
            "formatters": {
                "default": {
                    "format": "[%(asctime)s] %(levelname)s in %(module)s: %(message)s",
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "stream": "ext://sys.stdout",
                    "formatter": "default",
                }
            },
            "root": {"level": "DEBUG", "handlers": ["console"]},
        }
    )
    load_dotenv()
    app = Flask(__name__)
    Swagger(app)

    LOGGER = logging.getLogger("root")

    # Task health evaluation
    # https://aws.amazon.com/blogs/containers/a-deep-dive-into-amazon-ecs-task-health-and-task-replacement/
    @app.route('/health')
    def health() -> Flask.response_class:
        health = { 'exit_code': 0 }
        return jsonify(health), 200

    @app.get('/view-zuerivelo-publibike')
    # @swag_from('specs/view_zuerivelo_publibike.yml', validation=True)
    def view_zuerivelo_publibike() -> Flask.response_class:

        uri = os.environ['BASE_URL'] + os.environ['ZUERI_VELO'] + '?' + 'SERVICE=' + os.environ['SERVICE'] + '&' + 'REQUEST=' + os.environ['REQUEST'] + '&' + 'VERSION=' + os.environ['VERSION'] + '&' + 'TYPENAME=' + os.environ['TYPENAME']

        # fetch raw XML
        try:
            response = urllib.request.urlopen(uri).read()
        except Exception as e:
            return jsonify({ 'message': e }), 500

        LOGGER.info(response)

        jsonified_response = xmltodict.parse(response)
        feature_members = jsonified_response['wfs:FeatureCollection']['gml:featureMember']
        
        if not isinstance(feature_members, collectionsAbc.Iterable):
            return jsonify({ 'message': 'Invalid input, should be a valid list' }), 400

        
        
        return jsonify(list(map(format_zuerivelo_publibike, feature_members))), 200

    def format_zuerivelo_publibike(data):
        view = data['qgs:view_zuerivelo_publibike']
        return {
            'id': view['qgs:id_publibike'],
            'address': view['qgs:adresse'],
            'lat': view['qgs:lat'],
            'lon': view['qgs:lon'],
            'name': view['qgs:name'],
            'plz': view['qgs:plz'],
            'stadt': view['qgs:stadt'],
            'status': view['qgs:status'],
        }
    
    return app

if __name__ == '__main__':
    create_app().run(debug=True, use_reloader=False)
