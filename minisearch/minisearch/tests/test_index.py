from django.test import TestCase


class IndexTestCase(TestCase):
  def setUp(self) -> None:
    self.index = self.client.get("/")

  def test_index_is_working(self):
    self.assertEqual(self.index.status_code, 200, "Index page did not return 200 OK")
