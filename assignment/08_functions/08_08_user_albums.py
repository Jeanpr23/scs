# 08_08_user_albums.py

def make_album(artist, title):
    """Returns a dictionary with album information."""
    return {
        "artist": artist,
        "title": title
    }

while True:
    print("\nEnter album information (or type 'q' to quit):")

    artist_name = input("Artist name: ")
    if artist_name.lower() == 'q':
        break

    album_title = input("Album title: ")
    if album_title.lower() == 'q':
        break

    album = make_album(artist_name, album_title)
    print(f"Album created: {album}")
