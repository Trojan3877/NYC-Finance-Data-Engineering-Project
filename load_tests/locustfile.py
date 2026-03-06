from locust import HttpUser, task

class FinanceUser(HttpUser):
    @task
    def fetch_pipeline(self):
        self.client.get("/etl/run")
