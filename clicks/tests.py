from django.test import TestCase
from .models import Category,Image

class CategoryTestClass(TestCase):
    def setUp(self):
        self.francis = Category(category='Adventure')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.francis,Category))   
        
    def test_save_method(self):
        self.francis.save_category()
        categories = Category.objects.all()
        self.assertTrue(len(categories)>0)