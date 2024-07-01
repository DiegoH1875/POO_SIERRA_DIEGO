class Artist:
    def __init__(self, name, musical_genre, record_label):
        self.name = name
        self.musical_genre = musical_genre
        self.record_label = record_label
        self.albums = []
    def show_info(self):
        print(f"Artist: {self.name}")
        print(f"Genre: {self.musical_genre}")
        print(f"Record Label: {self.record_label}")
    def show_albums(self):
        # Function to show the albums of the artist
        # Asociation function
        ''' La clase Album actualiza la lista de artistas, cada que un album es inicializado
        se agregra el objeto de la clase album a la lista self.albums de la clase Artista
        '''
        for album in self.albums:
            print(f"{album.name}")

class Album:
    def __init__(self, name, artist, launch_date, number_songs):
        self.name = name
        self.artist = artist #An object of the class Artist
        self.launch_date = launch_date
        try:
            self.number_songs = int(number_songs)
        except ValueError:
            raise ValueError(f"Error in datatype conversion, {number_songs} should be type integer")
        self.artist.albums.append(self) # Asociation, when the album is initialized it actualizes the list of albums of the self.artist
    def show_artist_info(self):
        self.artist.show_info()
    def show_album_info(self):
        print(f"Album name: {self.name} ")
        print(f"Launch Date: {self.launch_date}")
        print(f"Number of songs {self.number_songs}")
        self.artist.show_info()

def main():
    lana_del_rey = Artist("Lana del Rey", "Indie Pop", "Interscope Records")
    born_to_die = Album("Born to die", lana_del_rey, "12/10/2012", 23)
    ultraviolence = Album("Ultraviolence", lana_del_rey, "01/01/2014", 14)
    lana_del_rey.show_albums()

if __name__ == "__main__":
    main()
