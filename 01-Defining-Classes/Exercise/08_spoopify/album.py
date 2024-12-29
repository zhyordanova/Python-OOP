class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        return "Song is already in the album."

    def remove_song(self, song_name):
        if not self.published:
            filtered = [s for s in self.songs if s.name == song_name]
            if filtered:
                self.songs.remove(filtered[0])
                return f"Removed song {song_name} from album {self.name}."
            return "Song is not in the album."
        return "Cannot remove songs. Album is published."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        result = f"Album {self.name}\n"
        result += '\n'.join([f"== {s.get_info()}" for s in self.songs])
        return result


