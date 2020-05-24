from django.test import TestCase
from .models import Images
# Create your tests here.

# set up method
def setUp(self):
    self.flowergirl= Images(name = 'flowergirl', description='Girl holding a flower')
# Testing  instance
def test_instance(self):
    self.assertTrue(isinstance(self.flowergirl,Images))
