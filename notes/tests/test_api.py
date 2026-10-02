from rest_framework.test import APITestCase
from rest_framework import status
from notes.models import Title, Body
    
class NoteAPITests(APITestCase):

    def setUp(self):
        self.title = Title.objects.create(
            title_text="API Test Note"
        )

        self.body = Body.objects.create(
            title=self.title,
            body_text="Body created for API testing."
        )

    def test_get_notes_list(self):
        response = self.client.get('/api/log/')

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(len(response.data), 1)
        self.assertEqual(
            response.data[0]['title_text'],
            'API Test Note'
        )

    def test_create_note_through_api(self):
        response = self.client.post(
            '/api/makenote/',
            {
                'title': 'Created Through API Test',
                'body_text': 'Created by an automated API test.'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        created_title = Title.objects.get(
            title_text='Created Through API Test'
        )

        self.assertEqual(
            created_title.body.body_text,
            'Created by an automated API test.'
        )

    def test_update_note_through_api(self):
        response = self.client.put(
            f'/api/updatenote/{self.title.id}/',
            {
                'title_text': 'Updated Through API Test'
            },
            format='json'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.title.refresh_from_db()

        self.assertEqual(
            self.title.title_text,
            'Updated Through API Test'
        )

    def test_delete_note_through_api(self):
        response = self.client.delete(
            f'/api/noteDelete/{self.title.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        self.assertFalse(
            Title.objects.filter(id=self.title.id).exists()
        )

        self.assertFalse(
            Body.objects.filter(id=self.body.id).exists()
        ) 
