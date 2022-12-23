from django.test import TestCase
# from time import sleep

class IndexTestCase(TestCase):
  def test_index_is_working(self):
    response = self.client.get("/")
    self.assertEqual(response.status_code, 200, "Index page did not return 200 OK")

  # # Commented this out because unittest by default 
  # # use prallel processes.
  # def test_throtling(self):
  #   for i in range(6):
  #     response = self.client.get("/")
  #     if i == 5:
  #       self.assertEqual(response.status_code, 403, "Index should return 403 FORBIDDEN "
  #         "after 5 requests per minute")

  #     else:
  #       self.assertEqual(response.status_code, 200, "Index should return 200 OK in first "
  #         "5 requests per minute")
    
  #   sleep(60)
  #   response = self.client.get("/")
  #   self.assertEqual(response.status_code, 200, "Index should return 200 OK after 1 minute")
