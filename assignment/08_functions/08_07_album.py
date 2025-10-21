# 08_07_album.py

def make_album(artist, title):
    """Returns a dictionary with album information."""
    album = {
        "artist": artist,
        "title": title
    }
    return album

print(make_album("Bad Bunny", "Un Verano Sin Ti"))
print(make_album("J Balvin", "Colores"))
print(make_album("Kendrick Lamar", "DAMN."))