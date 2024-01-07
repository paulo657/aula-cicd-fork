from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from datetime import date, datetime
from ..models import Songs

class SongsTests(APITestCase):
    def test_create_songs(self):
        url = reverse('create-song')
        data = {'song': 'dec 11th', 'artist': 'Giveon', "streamed": "2024-01-02"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Songs.objects.count(), 1)
        song_dec_11th = Songs.objects.get(song='dec 11th')
        self.assertEqual(song_dec_11th.get_artist(), "Giveon")
        assert song_dec_11th.get_streamed() == date(2024, 1, 2)