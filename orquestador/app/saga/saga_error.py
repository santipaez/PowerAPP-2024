class SagaError(Exception):

    def __init__(self, message: str, microservice: str):
        self.message = message
        self.microservice = microservice
        super().__init__(self.message)
    
    def __str__(self):
        return f'{self.microservice} failed with error: {self.message}'
