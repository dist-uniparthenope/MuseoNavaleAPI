from flask import Flask, Blueprint, url_for, jsonify, current_app, abort
from flask_restplus import Api, Resource, reqparse
from flask_marshmallow import Marshmallow, base_fields
from marshmallow import post_dump
import werkzeug
import os
import tempfile



app = Flask(__name__)


class BaseConfig(object):
    DATA_FOLDER="data_folder"

config = {
    "default": BaseConfig
}


def configure_app(app):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    app.config.from_object(config[config_name]) # object-based default configuration
    app.config.from_pyfile('config.cfg', silent=True) # instance-folders configuration


configure_app(app)


api = Api(app)

@api.route('/info')
class info(Resource):
    def get(self):

        return {'status': 'Done'}
		
@api.route('/boundle', methods=['GET'])
def return_file():
      return send_file('./file', as_attachment=True, attachment_filename="boundle.zip")



if __name__ == '__main__':
    app.run()
