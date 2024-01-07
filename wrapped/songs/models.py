from django.db import models

class Songs(models.Model):
    song = models.CharField("Song", max_length=240)
    artist = models.CharField("artist", max_length=240)
    streamed = models.DateField()
    time = models.TimeField(auto_now_add=True)

    def get_artist(self):
        return self.artist
    
    def get_streamed(self):
        return self.streamed

    def get_time(self):
        return self.time

    def get_song(self):
        return self.song