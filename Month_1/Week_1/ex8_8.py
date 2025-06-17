def city_country(name,country):
    return f"{name.title()}, {country.title()}"

city = city_country("nairobi", "kenya")
print(city)
city = city_country("paris", "france")
print(city)
city = city_country("tokyo", "japan")



def make_album(artist_name,album_title,number_of_songs=None):
    '''Return a dictionary containing information about an album'''
    album = {'artist': artist_name, 'title': album_title}
    if number_of_songs:
        album['number_of_songs'] = number_of_songs
    return album
album = make_album("Kamau", "My Life")
print(album)
album = make_album("Kamau", "My Life", 10)
print(album)

while True:
    print("\nPlease enter the artist name and album title: ")
    print("(enter 'q' at any time to quit)")
    artist_name = input("Artist name: ")
    if artist_name == 'q':
        break
    album_title = input("Album title: ")
    if album_title == 'q':
        break
    album = make_album(artist_name, album_title)
print(album)