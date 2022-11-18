import time
from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 5)

    @task
    def hello_world(self):
        self.client.get("/")
        self.client.get("/predict")

    @task(3)
    def view_items(self):
        self.client.get("/")
        self.client.get("/predict")