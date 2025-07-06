def add(song, playlist):
      playlist.append(song)
      print(f"Successfully added {song}")
      print(f"Your Current Playlist: {playlist}")

def remove(song, playlist):
    try:
      playlist.remove(song)
      print(f"Removed {song}")
      print(f"Your Current Playlist: {playlist}")
    except:
      print("invalid selection")

def play(playlist):
      try:
          print(f"Currently Playing: {playlist[0]}")
          playlist.pop(0)
          print(f"Your Remaining Playlist: {playlist}")

      except:
          print("No song list")

def show_all(playlist):
       print(f"Your Current Playlist: {playlist}")

def save(playlist, filepath):
    with open(filepath, "w") as file:
             for song in playlist:
              file.write(song)
              file.write('\n')
    print(f"Successfully saved in {filepath}")

def load(filepath):
    with open(filepath, "r") as file:
        file_contents = file.read().splitlines()
        print("Your saved playlist",file_contents)


def playlist_app():
    playlist = []
    end = False

    while not end:
        print()
        print("Menu: \t\t\n Add \t\t\n Remove \t\t\n Play \t\t\n Show \t\t\n Save \t\t\n Load \n")
        user_choice_first = input("Select command: ")
        user_choice = user_choice_first.lower().strip()

        if user_choice == "add":
            new_song = input("Enter song name: ")
            add(new_song, playlist)
        elif user_choice == "remove":
            song_to_remove = input("Song to remove: ")
            remove(song_to_remove, playlist)
        elif user_choice == "play":
            play(playlist)
        elif user_choice == "show":
            show_all(playlist)
        elif user_choice == "save":
            save(playlist, "playlist.txt")
        elif user_choice == "load":
            load("playlist.txt")
        elif user_choice == "exit":
            end = True

        else:
            print("Invalid input")
playlist_app()