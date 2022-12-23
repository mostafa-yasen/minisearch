from django.test import TestCase
from time import sleep


class IndexTestCase(TestCase):
  def test_key_is_required(self):
    response = self.client.get("/results?key=")
    self.assertEqual(response.status_code, 400, "Empty key should return 400 BAD REQUEST")

  def test_key_not_found(self):
    response = self.client.get("/results?key=TEST_KEY")
    self.assertEqual(response.status_code, 404, "Non existing key did should return 404 NOT FOUND")

  def test_results_is_working(self):
    response = self.client.get("/results?key=ETHYL+CHLORIDE+SPRAY")
    self.assertEqual(response.status_code, 200, "Results view valid request should return 200 OK")
