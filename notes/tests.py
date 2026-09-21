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
        
class NoteWebViewTests(TestCase):

    def setUp(self):
        self.title = Title.objects.create(
            title_text="Web Test Note"
        )

        self.body = Body.objects.create(
            title=self.title,
            body_text="Body created for the web view tests."
        )

    def test_notes_index_page_loads(self):
        response = self.client.get('/notes/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/index.html')
        self.assertIn(
            self.title,
            response.context['latest_title_list']
        )

    def test_note_detail_page_loads(self):
        response = self.client.get(
            f'/notes/{self.title.id}'
        )

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notes/detail.html')
        self.assertEqual(response.context['title'], self.title)
        self.assertEqual(response.context['body'], self.body)

    def test_make_note_page_loads(self):
        response = self.client.get('/notes/make_note/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/makenote.html')

    def test_create_note_from_web_form(self):
        response = self.client.post(
            '/notes/create/',
            {
                'title': 'Created Through Test',
                'body_text': 'This note was created by an automated test.'
            }
        )

        self.assertEqual(response.status_code, 302)

        created_title = Title.objects.get(
            title_text='Created Through Test'
        )

        self.assertEqual(
            created_title.body.body_text,
            'This note was created by an automated test.'
        )

    def test_delete_note_from_web_form(self):
        response = self.client.post(
            f'/notes/delete/{self.title.id}/'
        )

        self.assertEqual(response.status_code, 302)
        self.assertFalse(
            Title.objects.filter(id=self.title.id).exists()
        )
        self.assertFalse(
            Body.objects.filter(id=self.body.id).exists()
        )
        
     
