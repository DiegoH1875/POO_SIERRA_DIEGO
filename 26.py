# Composicion
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

    def add_album(self, album_name, launch_date, number_songs):
        # Composition function
        self.albums.append(Album(album_name,self,launch_date,number_songs))

    def show_albums(self):
        # Function to show the albums of the artist
        print(f"Albums of {self.name}")
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
    def show_artist_info(self):
        self.artist.show_info()
    def show_album_info(self):
        print(f"Album name: {self.name} ")
        print(f"Launch Date: {self.launch_date}")
        print(f"Number of songs {self.number_songs}")
        self.artist.show_info()

def main():
    the_killers = Artist("The Killers", "Indie_Rock", "Mercury Records")
    the_killers.add_album("HotFuss", "15/06/2024",14)
    the_killers.add_album("Day&Age", "18/10/2008", 12)
    the_killers.add_album("Sam's Town", "27/09/2006", 12) 
    the_killers.show_albums()

if __name__=="__main__":
    main()  