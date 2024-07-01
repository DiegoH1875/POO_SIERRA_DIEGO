# Programa con una clase con tres atributos y 3 metodos
class Song:
    def __init__(self, name, artist, album, genre):
        self.name = name
        self.artist = artist
        self.album = album
        self.genre = genre
    def artist_name(self):
        print(f"Artist of {self.name} is {self.artist}")
    def sing(self, verse):
        print(f"♫♫ {verse} ♫♫")
    def print_album(self):
        print(f"Album of {self.name}: {self.album}")
    def print_genre(self):
        print(f"Genre of {self.name}: {self.genre}")

def main():
    # Use two objects of the class 
    stiches = Song("stiches", "Shawn Mendez", "Handwritten", "Pop")
    videogames = Song("Videogames", "Lana del Rey", "Born to Die","Pop")
    stiches.artist_name()
    stiches.print_album()
    stiches.sing("And now that i'm without your kisses, i'll be needing stitches")
    videogames.artist_name()
    videogames.print_album()
    videogames.sing("Only worth living if somebody is loving you, baby now you do")

main()