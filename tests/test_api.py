import unittest
import json
from api.views import app
from . import (incident)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create_incident(self):
        with self.client as client:
            response = client.post("/api/v1/incidents", data=json.dumps(incident), content_type='application/json')
            self.assertEqual(response.status_code, 201)

    def test_fetch_all_incidents(self):
        with self.client as client:
            response = client.get("/api/v1/incidents")
            self.assertEqual(response.status_code, 200)
    
    def test_fetch_single_incident(self):
        with self.client as client:
            response = client.get("/api/v1/incidents/1")
            self.assertEqual(response.status_code, 200)

    def test_fetch_single_incident(self):
        with self.client as client:
            response = client.delete("/api/v1/incidents/1")
            self.assertEqual(response.status_code, 200)
if __name__ == "__main__":
    unittest.main()
            


 