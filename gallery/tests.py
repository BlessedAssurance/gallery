from django.test import TestCase
from .models import Images
# Create your tests here.

# set up method
def setUp(self):
    self.flowergirl= Images(name = 'flowergirl', description='Girl holding a flower')
# Testing  instance
def test_instance(self):
    self.assertTrue(isinstance(self.flowergirl,Images))

def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))
    # Testing Save Method

def test_save_method(self):
        self.image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)