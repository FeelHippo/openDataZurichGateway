from flask import Flask, jsonify, make_response
from flask_restful import Resource

class Ping(Resource):
    def get(self) -> Flask.response_class:
        health = { 'exit_code': 0 }
        return make_response(jsonify(health), 200)
