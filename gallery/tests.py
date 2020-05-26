from django.test import TestCase
from .models import Images, Category
# Create your tests here.

# set up method
class ImageTest(TestCase):
    def setUp(self):
     self.flowergirl= Images(name = 'flowergirl', description='Girl holding a flower')
    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.flowergirl,Images))

    def test_save_method(self):
        self.image.save_image()
        images = Images.objects.all()
        self.assertTrue(len(images) > 0)

class CategoryTest(TestCase):
    def setUp(self):
        self.category = Category(name = 'flowers', id=1)

    def test_instance(self):
        self.assertTrue(isinstance(self.category,Category)) 

    