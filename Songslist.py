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


    def load_to_csv(self):

        filereader = open('Songs.csv', 'r')
        for song in filereader:
            song_string = song.split(",")
            self.songs.append(
                [Song(song_string[0], song_string[1], int(song_string[2]), song_string[3].strip())])

        filereader.close()

    def sorting(self, sort_method):
        if sort_method == "Artist":
            self.songs.sort(key=lambda i: (i[0].artist, i[0].title))
        elif sort_method == "Title":
            self.songs.sort(key=lambda i: i[0].title)
        elif sort_method == "Year":
            self.songs.sort(key=lambda i: (i[0].year, i[0].title))
        else:
            self.songs.sort(key=lambda i: (i[0].status, i[0].title))








