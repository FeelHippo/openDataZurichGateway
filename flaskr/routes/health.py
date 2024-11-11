from flask import Flask, jsonify

def ping() -> Flask.response_class:
    health = { 'exit_code': 0 }
    return jsonify(health), 200
