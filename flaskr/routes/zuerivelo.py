from flask import Flask, jsonify, make_response
from flask_restful import Resource
from flasgger import swag_from
from ..config import constants
import collections.abc
import xmltodict, json
import urllib.request
import logging

try:
    collectionsAbc = collections.abc
except AttributeError:
    collectionsAbc = collections

class ZueriVelo(Resource):
  @swag_from('specs/view_zuerivelo_publibike.yml')
  def get(self) -> Flask.response_class:

      LOGGER = logging.getLogger('root')

      uri = constants.zuerivelo_uri()
      LOGGER.debug(uri)

      # fetch raw XML
      try:
          response = urllib.request.urlopen(uri).read()
      except Exception as e:
          return jsonify({ 'message': e }), 500

      LOGGER.debug(response)

      jsonified_response = xmltodict.parse(response)
      feature_members = jsonified_response['wfs:FeatureCollection']['gml:featureMember']
      
      if not isinstance(feature_members, collectionsAbc.Iterable):
          return jsonify({ 'message': 'Invalid input, should be a valid list' }), 400
      
      return make_response(
          jsonify(
            list(map(format_zuerivelo_publibike, feature_members)),
          ),
          200,
        )

def format_zuerivelo_publibike(data):
    view = data[constants.data]
    return {
        'id': int(view[constants.id_publibike]),
        'lat': float(view[constants.lat]),
        'lng': float(view[constants.lng]),
        'name': view[constants.name],
        'address': view[constants.address],
        'zip': view[constants.zip],
        'city': view[constants.city],
        'is_active': view[constants.status] == constants.active,
    }
