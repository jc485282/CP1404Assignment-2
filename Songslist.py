from songs import Song


class SongList:
    def __init__(self, ):
        # empty list for song object
        self.songs = []

    def append_Songs(self, title, artist, year):
        # adding song
        self.songs.append([Song(title, artist, year, 'y')])

    def song_get(self, title):
        # Method to let user selected single song object.
        for song in self.songs:
            if song[0].title == title:
                return song[0]

