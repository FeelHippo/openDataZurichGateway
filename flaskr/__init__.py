import os
import sys
from flask import Flask
from flask_restful import Api
from flasgger import Swagger
from logging.config import dictConfig
from dotenv import load_dotenv

# For relative imports to work in Python 3.6
import os, sys; sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from config import dependencies
from routes import health, zuerivelo

def create_app():
    
    # https://betterstack.com/community/guides/logging/how-to-start-logging-with-flask/
    dictConfig(dependencies.__dictConfig__)
    load_dotenv()
    app = Flask(__name__)
    api = Api(app)
    app.config['SWAGGER'] = dependencies.__swaggerConfig__
    Swagger(app)

    # Task health evaluation
    # https://aws.amazon.com/blogs/containers/a-deep-dive-into-amazon-ecs-task-health-and-task-replacement/
    app.add_url_rule('/health', health.ping)

    api.add_resource(zuerivelo.ZueriVelo, '/view-zuerivelo-publibike')
    
    return app

if __name__ == '__main__':
    create_app().run(debug=True, use_reloader=False)
