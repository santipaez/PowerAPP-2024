from flask import jsonify
import requests

class AtomicProcess:

    def execute_user(self):
        result = requests.get('http://localhost:5001')
        if result.status_code != 200:
            result = self.compensation_user()
        return result
    
    def compensation_user(self):
        result = requests.get('http://localhost:5001/compensation')
        return result
    
    def execute_instructor(self):
        result = requests.get('http://localhost:5002')
        if result.status_code != 200:
            result = self.compensation_instructor()
        return result
    
    def compensation_instructor(self):
        result = requests.get('http://localhost:5002/compensation')
        return result
    
    def execute_gym_class(self):
        result = requests.get('http://localhost:5003')
        if result.status_code != 200:
            result = self.compensation_instructor()
        return result
    
    def compensation_gym_class(self):
        result = requests.get('http://localhost:5003/compensation')
        return result

    def execute(self):
        user = self.execute_user()
        instructor = self.execute_instructor()
        gym_class = self.execute_gym_class()
        if user.status_code == 200 and instructor.status_code == 200 and gym_class.status_code == 200:
            return jsonify({"status": "ok"})
        else:
            return jsonify({"status": "not working"})
