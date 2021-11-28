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
class ImageTestClass(TestCase):
    def setUp(self):
        self.category = Category(category='love')
        self.category.save_category()
    def test_instance(self):
        self.assertTrue(isinstance(self.synthia,Image))        
        
    def test_save_method(self):
        self.synthia.save_image()
        images = Image.objects.all()
        self.assertTrue(len(images)>0)             

    def test_delete_image(self):
        self.synthia.delete_image()
        image = Image.objects.all()
        self.assertTrue(len(image)==0)

        self.assertTrue(len(image)==0)

    def test_update_image(self):
        self.synthia.save_image()
        self.synthia.update_image(self.synthia.id,'rabbit.jpg')    
        image = Image.objects.filter(photo_image='rabbit.jpg')
        self.assertTrue(len(image)>0)  
    def test_get_image_by_id(self):
        image=self.synthia.get_image_by_id(self.synthia.id)
        image=Image.objects.filter(id=self.synthia.id)    
        self.assertTrue(image.query,image.query)
    def tearDown(self):
        Image.objects.all().delete()
        Category.objects.all().delete()     