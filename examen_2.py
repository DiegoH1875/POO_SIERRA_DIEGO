# Music Database

import os
from time import sleep

def clear_terminal():
    # A function to clear the terminal
    os.system('cls' if os.name == 'nt' else 'clear')

def list_empty(list_sample) -> bool:
    # Function that return True if a list has no elements, False if it has
    if not isinstance(list_sample, list):
        raise ValueError(f"{list_sample} is not a List") 
    if len(list_sample) == 0:
        return True
    else:
        return False
    
def get_int(promtp):
    # Function to get an int from the user
    while True:
        try:
            new_int = int(input(promtp))
            break
        except ValueError:
            continue
    return new_int

    
def print_list(list_sample, message_empty): # Function to print in order the elements of a list
    if list_empty(list_sample):
        print(message_empty)
    else:
        for element in list_sample:
            print(element)

class Artist:
    def __init__(self, name, musical_band=False):
        self.name = name
        # If no errors detected then
        self.record_label = None
        self.musical_genre = None
        self.manager = None
        self.musical_band = musical_band
        if self.musical_band:
            self.members = []
        # Establish the lists for asosiation with other classes
        self.albums = [] 
        self.concerts = []
        self.songs = []

    def __str__(self) -> str:
        return f"Artist: {self.name}"
    
    def show_info(self):
        print(f"Artist: {self.name}")
        if self.musical_genre != None:
            print(f"Genre: {self.musical_genre}")
        if self.record_label != None:
            print(f"Record Label: {self.record_label}")
        if self.manager != None:
            print(f"Manager: {self.manager}")

    def show_albums(self):
        print(f"{self.name}'s albums")
        for album in self.albums:
            print(f"{album.name}")
    
    def show_songs(self):
        for song in self.songs:
            print(song)
    def add_album(self,album_name, number_songs,launch_date):
        self.albums.append(Album(album_name, self,launch_date, number_songs))  # Composition

    def add_musical_genre(self, musical_genre):
        if not isinstance (musical_genre, Musical_genre):
            raise ValueError(f"{musical_genre} should be object of the class Musical_genre")
        else:
            self.musical_genre = musical_genre
            self.musical_genre.artists.append(self) # Asociation
    def show_concerts(self):
        print_list(self.concerts, "There are no concerts programed for that artist")



class Musical_band(Artist): # For the inheritance
    def __init__(self,name,members):
        if type(members) is not list:
            raise ValueError(f"{members} is not of type list")
        super().__init__(name, musical_band=True)
        self.members.extend(members) # Asociation

    def __str__(self) -> str:
        return super().__str__()
    
    def show_members(self):
        for member in self.members:
            print(member)
    
    def show_info(self):
        super().show_info()
        print("Members of the band")
        self.show_members()

# Class album and class song for the composition
class Album: 
    def __init__(self, name, artist, launch_date, number_songs):
        self.name = name
        if not isinstance(artist,Artist): # Agregation
            raise ValueError(f"{artist} is not an object of class Artist")
        self.artist = artist #An object of the class Artist
        self.launch_date = launch_date
        try:
            self.number_songs = int(number_songs)
        except ValueError:
            raise ValueError(f"Error in datatype conversion, {number_songs} should be type integer")
        self.songs = [] # Lists for the composition relation, with the class song

    def __str__(self) -> str:
        return f"Album: {self.name} of {self.artist}"
    
    def show_artist_info(self):
        self.artist.show_info()

    def show_album_info(self):
        print(f"Album name: {self.name} ")
        print(f"Launch Date: {self.launch_date}")
        print(f"Number of songs {self.number_songs}")
        self.artist.show_info()

    def add_song(self, song_name):
        new_song = Song(song_name, self.artist, self)
        self.songs.append(new_song) # Composition

    def show_songs(self):
        print(f"Songs of the Album {self.name}")
        print_list(self.songs, "There are no registred songs in that album")

class Song:
    def __init__(self, name,artist,album) -> None:
        if not isinstance(artist, Artist):
            raise ValueError(f"{artist} is not object of class Artist")
        if not isinstance(album, Album):
            raise ValueError(f"{album} is not an object of the class Album")
        self.name = name
        self.artist = artist
        self.artist.songs.append(self)
        self.album = album 
        self.lyrics = None
        self.album.songs.append(self)
    def __str__(self):
        return f"{self.name}" 
    
    def assign_lyrics(self, lyrics):
        self.lyrics = lyrics
    
    def sing_song(self):
        if self.lyrics == None:
            print("No lyrics available for that song")
        else:
            print(f"♫♫♫ {self.lyrics} ♫♫♫")

    def associate_song(self):
        self.album.songs.append(self)
        self.artist.songs.append(self)

    def show_song_info(self):
        print(f"Info of {self.name}")
        print(f"Artist: {self.artist}")
        print(f"{self.album}")




class Concert:
    def __init__(self, artist, date, place, city) -> None:
        if not isinstance(artist, Artist):
            raise ValueError(f"{artist} should be an object of the class Artist")
        else:
            self.artist = artist
        self.date = date
        self.place = place
        self.city = city
        self.artist.concerts.append(self)
        self.zones = []

    def __str__(self) -> str:
        return f"Concert of artist {self.artist}, programmed on {self.date} at {self.place}"
    
    def stablish_zones(self):
        # Composition, insert the zones
        self.zones.append(Zone_concert("Floor A", 2500))
        self.zones.append(Zone_concert("Floor B", 1800))
        self.zones.append(Zone_concert("Stand C", 900))
        self.zones.append(Zone_concert("Stand B", 1200))
        self.zones.append(Zone_concert("Stand A", 1550)) # Composition

    def show_zones(self):
        # Show the prices of the zone
        print("Zones of the concert with its price")
        print_list(self.zones)

    def buy_ticket(self):
        self.show_zones()
        # Function to buy a ticket, using the class Client with a relation of dependency
        while True:
            zone_selected = input("Select your zone: ")
            zone_found = False
            for zone in self.zones:
                if zone_selected == zone.name:
                    zone_found = True
                    break
            if zone_found:
                break
            else:
                continue


class Zone_concert: # Class for composition
    def __init__(self, name, price):
        self.name = name
        try:
            self.price = float(price)
        except ValueError:
            raise ValueError(f"{price} should be float type")
        
    def __str__(self) -> str:
        return f"Zone: {self.name} which has a cost of {self.price}"

    def change_prince(self, new_price):
        if isinstance(new_price, float):
            self.price = new_price
        else:
            raise ValueError(f"{new_price} is not float") 
    

class Client_concert: # Class for dependence
    def __init__(self) -> None:
        self.name = input("Introduce tu nombre: ")

    def __str__(self) -> str:
        return self.name

    def buy_ticket(self,concert):
        if not isinstance(concert, Concert):
            print(f"There is no concert named: {concert}")
            raise ValueError
        else:
            concert.buy_ticket() # It depends on the class Concert


class Manager:
    def __init__(self, name) -> None:
        self.name = str(name)
        self.artists_represented = []
        self.record_label = None

    def __str__(self) -> str:
        if self.record_label != None:
            return f"{self.name} associated with {self.record_label}"
        else:
            return self.name
        
    def negotiate(self):
        print("Deal or no deal")

    def associate_RecordLabel(self, record_label):
        # Function to asociate with a Record_label
        if isinstance(record_label, Record_label):
            self.record_label = record_label
            self.record_label.artists_asociated.append(self) # Asociation

    def show_artists(self):
        print(f"Artist associated with manager {self.name}")
        print_list(self.artists_represented, "There are no artists associated with that manager")

    def associate_Artist(self, artist):
        if isinstance(artist,Artist):
            self.artists_represented.append(artist)
            artist.manager = self
        else:
            raise ValueError(f"{artist} is not an object of class Artist")
    
class Musical_genre:
    def __init__(self, name) -> None:
        self.name = str(name)
        self.artists = []

    def __str__(self) -> str:
        return self.name
        
    def show_artists(self):
        print("Artists")
        print_list(self.artists, "That genre doesn't have artists registred")

    def add_artist(self, artist):
        if isinstance(artist,Artist):
            self.artists.append(artist)
            artist.musical_genre = self
        else:
            raise ValueError(f"{artist} should be an instance of class Artist")

class Record_label:
    def __init__(self, name,ceo_name) -> None:
        self.ceo_name = str(ceo_name)
        self.name = str(name)
        self.artists_asociated = []
        self.managers_asociated = []
    def __str__(self) -> str:
        return f"{self.name}"
    
    def add_artist(self, artist):
        if isinstance(artist, Artist):
            self.artists_asociated.append(artist)
            artist.record_label = self
        else:
            raise ValueError(f"{artist} should be object of class Artist")
        
    def artists_of_label(self):
        print(f"Artists of label {self.name}")
        print_list(self.artists_asociated, "There are no artists associated with the label")

    def show_managers(self):
        print(f"Managers of label {self.name}")
        print_list(self.managers_asociated)

class Database:
    def __init__(self) -> None:
        self.artists = {}
        self.record_labels = {}
        self.musical_genres = {}
        self.managers = {}

    def build_sample(self):
        self.record_labels["amazon records"] = Record_label("Amazon Records", "Francisco Puentes Perez")
        self.record_labels["warner records"] = Record_label("Warner Records", "Warner Brothers")
        self.artists = {
            "The Killers": Musical_band("The Killers", ["Brandon Flowers", "Joe Barry"]),
            "The Beatles": Musical_band("The Beatles", ["Paul McCartney", "John Lennon", "George Harrison", "Ringo Starr"]),
            "Los Tigres del Norte": Musical_band("Los Tigres del Norte", ["Jorge Hernández", "Hernán Hernández", "Eduardo Hernández", "Luis Hernández", "Óscar Lara"]),
            "Kings of Leon": Musical_band("Kings of Leon", ["Caleb Followill", "Nathan Followill", "Jared Followill", "Matthew Followill"]),
            "Weezer": Musical_band("Weezer", ["Rivers Cuomo", "Patrick Wilson", "Brian Bell", "Scott Shriner"]),
            "Coldplay": Musical_band("Coldplay", ["Chris Martin", "Jonny Buckland", "Guy Berryman", "Will Champion"]),
            "Daddy Yankee": Artist("Daddy Yankee"),
            "Olivia Rodrigo": Artist("Olivia Rodrigo"),
            "Lady Gaga": Artist("Lady Gaga"),
            "Katy Perry": Artist("Katy Perry"),
            "My Chemical Romance": Musical_band("My Chemical Romance", ["Gerard Way", "Ray Toro", "Frank Iero", "Mikey Way"]),
            "Muse": Musical_band("Muse", ["Matthew Bellamy", "Chris Wolstenholme", "Dominic Howard"]),
            "Kanye West": Artist("Kanye West"),
            "Taylor Swift": Artist("Taylor Swift"),
            "Radiohead": Musical_band("Radiohead", ["Thom Yorke", "Jonny Greenwood", "Colin Greenwood", "Ed O'Brien", "Philip Selway"]),
            "Oasis": Musical_band("Oasis", ["Liam Gallagher", "Noel Gallagher", "Paul Arthurs", "Paul McGuigan", "Alan White"])
            }
        self.musical_genres = {
            "Indie Rock": Musical_genre("Indie Rock"),
            "Clasic Rock": Musical_genre("Clasic Rock"),
            "Metal": Musical_genre("Metal"),
            "Alternative Rock": Musical_genre("Alternative Rock"),
            "K-POP": Musical_genre("K-POP"),
            "POP": Musical_genre("POP"),
            "Indie Pop": Musical_genre("Indie Pop"),
            "Hip Hop": Musical_genre("Hip Hop"),
            "Electronic": Musical_genre("Electronic"),
            "Regional Mexicano": Musical_genre("Regional Mexicano"),
            "Reggaeton": Musical_genre("Reggaeton")
        }


        self.musical_genres["Clasic Rock"].add_artist(self.artists["The Beatles"])
        self.musical_genres["Clasic Rock"].add_artist(self.artists["Oasis"])
        self.musical_genres["POP"].add_artist(self.artists["Katy Perry"])

        # Add the rest of the artists to their respective genres
        self.musical_genres["Indie Rock"].add_artist(self.artists["The Killers"])
        self.musical_genres["Indie Rock"].add_artist(self.artists["Kings of Leon"])
        self.musical_genres["Indie Rock"].add_artist(self.artists["Coldplay"])
        self.musical_genres["Indie Rock"].add_artist(self.artists["Radiohead"])

        self.musical_genres["Alternative Rock"].add_artist(self.artists["My Chemical Romance"])
        self.musical_genres["Alternative Rock"].add_artist(self.artists["Muse"])

        self.musical_genres["Regional Mexicano"].add_artist(self.artists["Los Tigres del Norte"])

        self.musical_genres["POP"].add_artist(self.artists["Olivia Rodrigo"])
        self.musical_genres["POP"].add_artist(self.artists["Lady Gaga"])
        self.musical_genres["POP"].add_artist(self.artists["Taylor Swift"])

        self.musical_genres["Hip Hop"].add_artist(self.artists["Kanye West"])

        self.musical_genres["Reggaeton"].add_artist(self.artists["Daddy Yankee"])

        self.musical_genres["Alternative Rock"].add_artist(self.artists["Weezer"])

        # Add some albums and some songs
        self.artists["The Killers"].add_album("Sam's Town", 14, "27/09/2006")
        self.artists["The Beatles"].add_album("Abbey Road", 17, "26/09/1969")
        self.artists["Los Tigres del Norte"].add_album("Jefe de Jefes", 15, "17/06/1997")
        self.artists["Kings of Leon"].add_album("Only by the Night", 13, "19/09/2008")
        self.artists["Weezer"].add_album("Weezer (Blue Album)", 10, "10/05/1994")
        self.artists["Coldplay"].add_album("A Rush of Blood to the Head", 11, "26/08/2002")
        self.artists["Daddy Yankee"].add_album("Barrio Fino", 21, "13/07/2004")
        self.artists["Olivia Rodrigo"].add_album("SOUR", 11, "21/05/2021")
        self.artists["Lady Gaga"].add_album("The Fame", 17, "19/08/2008")
        self.artists["Katy Perry"].add_album("Teenage Dream", 12, "24/08/2010")
        self.artists["My Chemical Romance"].add_album("The Black Parade", 14, "23/10/2006")
        self.artists["Muse"].add_album("Black Holes and Revelations", 11, "03/07/2006")
        self.artists["Kanye West"].add_album("The College Dropout", 21, "10/02/2004")
        self.artists["Taylor Swift"].add_album("Fearless", 13, "11/11/2008")
        self.artists["Radiohead"].add_album("OK Computer", 12, "21/05/1997")
        self.artists["Oasis"].add_album("(What's the Story) Morning Glory?", 13, "02/10/1995")

        # Add some songs
        self.artists["The Killers"].albums[0].add_song("When You Were Young")
        self.artists["The Beatles"].albums[0].add_song("Come Together")
        self.artists["Los Tigres del Norte"].albums[0].add_song("Jefe de Jefes")
        self.artists["Kings of Leon"].albums[0].add_song("Sex on Fire")
        self.artists["Weezer"].albums[0].add_song("Buddy Holly")
        self.artists["Coldplay"].albums[0].add_song("Clocks")
        self.artists["Daddy Yankee"].albums[0].add_song("Gasolina")
        self.artists["Olivia Rodrigo"].albums[0].add_song("drivers license")
        self.artists["Lady Gaga"].albums[0].add_song("Just Dance")
        self.artists["Katy Perry"].albums[0].add_song("Firework")
        self.artists["My Chemical Romance"].albums[0].add_song("Welcome to the Black Parade")
        self.artists["Muse"].albums[0].add_song("Supermassive Black Hole")
        self.artists["Kanye West"].albums[0].add_song("Jesus Walks")
        self.artists["Taylor Swift"].albums[0].add_song("Love Story")
        self.artists["Radiohead"].albums[0].add_song("Paranoid Android")
        self.artists["Oasis"].albums[0].add_song("Wonderwall")

        # Add the lyrics of some examples
        self.artists["The Killers"].songs[0].assign_lyrics("Talks like a gentleman, like you imagined, when you were young")
        self.artists["The Beatles"].songs[0].assign_lyrics("Here come old flat top, he come groovin' up slowly")
        self.artists["Los Tigres del Norte"].songs[0].assign_lyrics("Jefe de jefes, señores, me respetan a todos niveles")
        self.artists["Kings of Leon"].songs[0].assign_lyrics("Your sex is on fire")
        self.artists["Weezer"].songs[0].assign_lyrics("What's with these homies, dissing my girl?")
        self.artists["Coldplay"].songs[0].assign_lyrics("Lights go out and I can't be saved")
        self.artists["Daddy Yankee"].songs[0].assign_lyrics("Dame más gasolina")
        self.artists["Olivia Rodrigo"].songs[0].assign_lyrics("And I just can't imagine how you could be so okay now that I'm gone")
        self.artists["Lady Gaga"].songs[0].assign_lyrics("Just dance, gonna be okay")
        self.artists["Katy Perry"].songs[0].assign_lyrics("Cause baby you're a firework")
        self.artists["My Chemical Romance"].songs[0].assign_lyrics("When I was a young boy, my father took me into the city")
        self.artists["Muse"].songs[0].assign_lyrics("You set my soul alight")
        self.artists["Kanye West"].songs[0].assign_lyrics("Jesus walks with me")
        self.artists["Taylor Swift"].songs[0].assign_lyrics("We were both young when I first saw you")
        self.artists["Radiohead"].songs[0].assign_lyrics("When I am king, you will be first against the wall")
        self.artists["Oasis"].songs[0].assign_lyrics("You're my wonderwall")

        # Add all the artist to the supreme manager
        self.managers['Jesus Christ'] = ( Manager("Jesus Christ"))
        for artist in self.artists:
            self.managers['Jesus Christ'].associate_Artist(self.artists[artist])
            self.record_labels["amazon records"].add_artist(self.artists[artist])

        # Add a concert for some bands
        self.concerts = []
        self.concerts.append(Concert(self.artists["The Killers"], "03/10/2024", "Estadio Banorte", "Guadalajara, Mex"))
        self.concerts.append( Concert(self.artists["Taylor Swift"], "21/08/2023", "Foro Sol", "Ciudad de Mexico, Mex"))
        self.concerts.append( Concert(self.artists["Muse"], "16/01/2023","Foro Pegaso", "Toluca, Mexico")) 

        # Class dependency
        #client1 = Client_concert()
        #client1.buy_ticket(self.concerts[0])
        
        

    def add(self, class_to_handle):
        clear_terminal()
        print(f"You have chosen to add a new {class_to_handle}")
        match class_to_handle:
            case "Song":
                # Chose the name of the song
                song_name = input("Name of the new song: ")

                # Look for the name of the artist
                artist_name = input("Name of the artist: ")
                try:
                    artist_of_song = self.artists[f"{artist_name}"]
                except KeyError:
                    print("That artist is not in the database")
                    print("Firstly, add the artist to the database")
                    sleep(3)
                    return

                # Ask the name of the album
                album_name = input("Album: ")
                song_album = None
                album_found = False
                for album in artist_of_song.albums:
                    if album_name == album.name:
                        song_album = album
                        album_found = True
                if album_found == True:
                    song_album.add_song(song_name)
                else:
                    print(f"{artist_name} doesn't have an album called {album_name} in the database")
                    print(f"First, add the album to the database")
                    sleep(3)
                    return
    

            case "Artist":
                # Name of the artist
                new_artist_name = input("Name of the new artist: ")
                self.artists[new_artist_name] = Artist(new_artist_name)


            case "Manager":
                name_manager = input("Name of the new manager: ")
                self.managers[name_manager] = Manager(name_manager)

            case "Musical genre":
                new_musical_genre = input("Name of the musical genre: ")
                self.musical_genres[new_musical_genre] = Musical_genre(new_musical_genre)


            case "Album":
                album_name = input("Name of the new album: ")
                # Look if the artist is on the database
                album_artist = input("Name of the artist: ")
                if self.artist_in_database(album_artist):
                    album_artist = self.artists[album_artist]
                else:
                    print("The album is not in the database")
                    print("Try to add the album to the database firstly")
                    sleep(3)
                    return
                launch_date = input("Launch date: ")
                number_songs = get_int("Number of songs: ")
                album_artist.add_album(album_name, number_songs, launch_date)
            
            case "Record label":
                new_label_name = input("New record label name: ")
                new_ceo_name = input("Name of the CEO: ")
                self.record_labels[new_label_name] = Record_label(new_label_name, new_ceo_name)

            case "Concert":
                concert_artist = input("Artist of the concert: ")
                if self.artist_in_database(concert_artist):
                    concert_artist = self.artists[concert_artist]
                else:
                    print("That artist is not in the database")
                    print("Try to add  the artist to the database firstly")
                    sleep(3)
                    return
                date = input("Date of the concert: ")
                place = input("Place of the concert: ")
                city = input("City of the concert: ")
                new_concert = Concert(concert_artist, date, place,city)
                new_concert.stablish_zones()

            case "Musical band":
                new_name = input("Musical Band's name: ")
                members = []
                i = 1
                # Ask for the members of the band
                while True:
                    print("Enter 0 to get out")
                    new_member = input(f"Member {i}:  ")
                    if new_member == "0":
                        break
                    else:
                        members.append(new_member)
                        i += 1
                # Initialize the new band
                self.artists[new_name] = Musical_band(new_name,members)

            case _:
                print("A class to handle was not provided")
                sleep(2)
                return
        print(f"{class_to_handle}  was succesfully added")
        sleep(2)
        return
    
    def show(self, class_to_handle):
        clear_terminal()
        print(f"You have chosen the show menu for the {class_to_handle}")
        match class_to_handle:
            case "Song":
                # Ask for one song
                song_to_look = input("Introduce the name of the song: ")
                song_elected = self.song_in_database(song_to_look)
                if song_elected == None:
                    print(f"The song {song_to_look} is not in the database")
                    print("Add it firstly to the database")
                    sleep(3)
                    return
                indications = [
                    "[S] for sing", "[I] for song info", "[E] for exit"
                ]
                options = ["S", "I","E"]

                while True:
                    clear_terminal()
                    self.print_menu_indications(indications,options)
                    user_choice = get_valid_option(options)
                    match user_choice:
                        case "S":
                            # Sing
                            print(f"Sing {song_elected}")
                            song_elected.sing_song()
                            sleep(4)
                        case "I":
                            song_elected.show_song_info()
                            sleep(4)
                        case "E":
                            return

            case "Artist":
                # First show a list with all the artist of the database
                print("LIST OF ALL THE ARTIST OF THE DATABASE")
                for artist in self.artists:
                    print(self.artists[artist])
                sleep(8)

                artist_to_look = input("Artist to look: ")
                try:
                    artist_elected = self.artists[artist_to_look]
                    print("Artist found in the database")
                except KeyError:
                    print(f"{artist_to_look} is not in the database")
                    sleep(3)
                    return
                indications = [
                    "[A] for show the albums of the artist",
                    "[S] for show all the songs of the artist",
                    "[I] for show the information of the artist",
                    "[C] for show the concerts",
                    "[E] for exit",
                ]
                options = ["A", "S","I", "C", "E"]
                while True:
                    clear_terminal()
                    self.print_menu_indications(indications,options)
                    user_choice = get_valid_option(options)
                    match user_choice:
                        case "A":
                            artist_elected.show_albums()
                        case "S":
                            artist_elected.show_songs()
                        case "I":
                            artist_elected.show_info()
                        case "C":
                            artist_elected.show_concerts()
                        case "E":
                            return
                        case _:
                            continue
                    sleep(5)

            case "Manager":
                # Show all the managers
                print("List of all the managers")
                for manager in self.managers:
                    print(manager)
                sleep(5)
                manager_to_look = input("Manager to look: ")
                try:
                    manager_to_handle = self.managers[manager_to_look]
                except KeyError:
                    print(f"{manager_to_look} is not in the database")
                    sleep(3)
                    return
                indications = ["[I] for show info", "[A] for show artists", "[N] for negotiate", "[E] for exit"]
                options = ["I","A", "N", "E"] 
                while True:
                    clear_terminal()
                    self.print_menu_indications(indications,options)
                    user_choice = get_valid_option(options)
                    match user_choice:
                        case "A":
                            manager_to_handle.show_artists()
                        case "I":
                            print(manager_to_handle)
                        case "N":
                            manager_to_handle.negotiate()
                        case "E":
                            return
                        case _:
                            continue
                    sleep(5)

                
            case "Musical genre":
                # Show all the musical genres
                print("Musical Genre")
                for musical_genre in self.musical_genres:
                    print(musical_genre)
                sleep(6)
                genre_to_look = input("Musical Genre to look: ")
                try:
                    genre_to_handle = self.musical_genres[genre_to_look]
                except KeyError:
                    print(f"{genre_to_look} is not in the database")
                    sleep(3)
                    return
                indications = ["[I] for show info", "[A] for show artists", "[E] for exit"]
                options = ["I","A","E"] 
                while True:
                    clear_terminal()
                    self.print_menu_indications(indications,options)
                    user_choice = get_valid_option(options)
                    match user_choice:
                        case "A":
                            genre_to_handle.show_artists()
                        case "I":
                            print(genre_to_handle)
                        case "E":
                            return
                        case _:
                            continue
                    sleep(5)

                
            case "Album": 
                # First show a list with all the artist of the database
                print("LIST OF ALL THE ALBUMS IN THE DATABASE")
                for artist in self.artists:
                    self.artists[artist].show_albums()
                sleep(5)

            case "Record label":
                # Show all the record labels
                print("Record Labels in the database")
                for record_label in self.record_labels:
                    print(record_label)
                sleep(5)

            case "Concert":
                # Show all the concerts
                print("Concerts stored in the database")
                for concert in self.concerts:
                    print(concert)
                sleep(5)

            case "Musical band":
                # Show all the musical bands
                print("LIST OF ALL THE MUSICAL BANDS ON THE DATABASE")
                for artist in self.artists:
                    if self.artists[artist].musical_band == True:
                        print(self.artists[artist])
                sleep(5)

            case _:
                print("A class to handle was not provided. Error in programming")
                sleep(2)
                return
        sleep(3)

    def print_menu_indications(self, indications, options):
        # Function that implements a small menu, to show the options available for each class in the self.add function
        if not isinstance(indications, list):
            raise ValueError(f"{indications} must be of type List")
        if not isinstance(options, list):
            raise ValueError(f"{options} must be of type options")
        print("INDICATIONS")
        print_list(indications,"")
        print("Make your choice")

        
    def song_in_database(self, song_to_look):
        # Not recomended with largers amount of data
        for artist in self.artists:
            for song in self.artists[artist].songs:
                if song.name.upper() == song_to_look.upper():
                    return song
        # If the song was not found
        return None
    
    def artist_in_database(self, artist_to_look) -> bool:
        # Function that checks if the artist is on the database
        artist_found = None
        try:
            artist_found = self.artists[artist_to_look]
            return True
        except KeyError:
            return False
        

            


                    
def main():
    # Main Menu
    database = Database()
    database.build_sample()
    while True:
        clear_terminal()
        print("MAIN MENU")
        print("Select One Option: ")
        indications = [
            "[A] artists",
            "[M] for musical genres",
            "[N] for managers",
            "[S] for songs",
            "[B] for musical bands",
            "[R] for record labels",
            "[C] for concerts",
            "[L] for albums",
            "[E] for exit",
        ]
        print_list(indications, "")
        user_option = get_valid_option(["A","M","N","S", "B", "R", "C", "L","E"])
        class_to_handle = ""
        match user_option:
            case "A":
                class_to_handle = "Artist"
            case "M":
                class_to_handle = "Musical genre"
            case "N":
                class_to_handle = "Manager"
            case "S":
                class_to_handle = "Song"
            case "B":
                class_to_handle = "Musical band"
            case "R":
                class_to_handle = "Record label"
            case "C":
                class_to_handle = "Concert"
            case "L":
                class_to_handle = "Album"
            case "E":
                return
            case _:
                continue
        menu_database(database,class_to_handle)
        continue
        

def menu_database(database, class_to_handle):
    if not isinstance(database, Database):
        raise ValueError(f"{database} should be instance of class Database")
    while True:
        clear_terminal()
        print("MENU DATABASE")
        indications = [
            "[A] for add",
            "[S] for show",
            "[E] for exit"
        ]
        print_list(indications, "")
        user_option = get_valid_option(["A", "S", "E"])
        match user_option:
            case "A":
                database.add(class_to_handle)
            case "S":
                database.show(class_to_handle)
            case "D":
                ...
            case "E":
                return
            case _:
                continue
        


def get_valid_option(options, upper=True):
    while True:
        user_option = input("Select a valid option: ")
        if upper == True:
            user_option = user_option.upper()
        if user_option not in options:
            print("That's not a valid option")
            continue
        break
    return user_option


        

if __name__=="__main__":
    main()