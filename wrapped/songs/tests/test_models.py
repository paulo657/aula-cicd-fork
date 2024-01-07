from django.test import TestCase
from ..models import Songs


class SongTest(TestCase):
    """ Test module for Puppy model """

    def setUp(self):
        Songs.objects.create(
            song='Meat Grinder', streamed='2024-01-02', artist='MF DOOM')
        Songs.objects.create(
            song='Prisioner', streamed='2024-01-02', artist='The Weeknd')

    def test_created_song(self):
        song_meat_grinder = Songs.objects.get(song='Meat Grinder')
        song_prisioner = Songs.objects.get(song='Prisioner')
        self.assertEqual(
            song_meat_grinder.get_artist(), "MF DOOM")
