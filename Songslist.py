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

    def tolearn_songs_count(self):

        song_tolearn = 0
        for song in self.songs:
            if song[0].status == 'y':
                song_tolearn += 1
        return song_tolearn

    def learned_songs_count(self):

        learned_songs = 0
        for song in self.songs:
            if song[0].status == 'n':
                learned_songs += 1
        return learned_songs


    def load_songs(self):

        filereader = open('song.csv', 'r')
        for song in filereader:
            song_string = song.split(",")
            self.songs.append(
                [Song(song_string[0], song_string[1], int(song_string[2]), song_string[3].strip())])

        filereader.close()






