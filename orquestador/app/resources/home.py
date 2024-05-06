import random
from flask import jsonify
from flask_restful import Resource
from app.services import AtomicProcess

class Home(Resource):
    def get(self):
        resp = jsonify({"order": "3", "status": "ok"})
        resp.status_code = random.choice([200, 404])
        return resp

class AtomicProcessResource(Resource):
    def get(self):
        process = AtomicProcess()
        result = process.execute()
        resp = result.json()
        return resp, result.status_code
