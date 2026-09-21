from django.test import TestCase

from .models import Title, Body

class NoteModelTests(TestCase):
    def setUp(self):
        self.title = Title.objects.create(
            title_text="Test Note"
        )
        
        self.body = Body.objects.create(
            title=self.title,
            body_text="This is the body of the test note."
        )
        
    def test_title_is_created(self):
        self.assertEqual(self.title.title_text, "Test Note")
        
    def test_title_string_representation(self):
        self.assertEqual(str(self.title), "Test Note")
        
    def test_body_is_linked_to_title(self):
        self.assertEqual(self.body.title, self.title)
        self.assertEqual(self.title.body, self.body)
    
    def test_deleting_title_deletes_body(self):
        self.title.delete()
        self.assertEqual(Body.objects.count(),0)
        
     
