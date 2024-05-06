from flask import jsonify
import requests

class AtomicProcess:

    def execute_user(self):
        result = requests.get('http://host.docker.internal:5001')
        if result.status_code != 200:
            result = self.compensation_user()
        return result
    
    def compensation_user(self):
        result = requests.get('http://host.docker.internal:5001/compensation')
        return result
    
    def execute_instructor(self):
        result = requests.get('http://host.docker.internal:5002')
        if result.status_code != 200:
            result = self.compensation_instructor()
        return result
    
    def compensation_instructor(self):
        result = requests.get('http://host.docker.internal:5002/compensation')
        return result

    def execute(self):
        user = self.execute_user()
        instructor = self.execute_instructor()
        if user.status_code == 200 and instructor.status_code == 200:
            return jsonify({"status": "ok"})
        else:
            return jsonify({"status": "not working"})
