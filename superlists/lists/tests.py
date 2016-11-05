from django.test import TestCase

class SmokeTest(TestCase):
    def test_bad_maths(self):
        self.assertEquall(1 + 1,3)
