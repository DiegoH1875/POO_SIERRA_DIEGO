class Artist:
    def __init__(self, name, musical_genre, record_label):
        self.name = name
        self.muscial_genre = musical_genre
        self.record_label = record_label
    def show_info(self):
        print(f"Artist: {self.name}")
        print(f"Genre: {self.muscial_genre}")
        print(f"Record Label: {self.record_label}")
class Album:
    def __init__(self, name, artist, launch_date, number_songs):
        self.name = name
        self.artist = artist #An object of the class Artist
        self.launch_date = launch_date
        try:
            self.number_songs = int(number_songs)
        except ValueError:
            raise ValueError(f"Error in datatype conversion, {number_songs} should be type integer")
    def show_artist_info(self):
        self.artist.show_info()
    def show_album_info(self):
        print(f"Album name: {self.name} ")
        print(f"Launch Date: {self.launch_date}")
        print(f"Number of songs {self.number_songs}")
        self.artist.show_info()

def main():
    tigres_del_norte = Artist("Los Tigres del Norte", "Regional Mexicano", "Fonovisa")
    mi_buena_suerte = Album("Mi buena suerte", tigres_del_norte, "01/01/2001", 12)
    mi_buena_suerte.show_album_info()


main()
