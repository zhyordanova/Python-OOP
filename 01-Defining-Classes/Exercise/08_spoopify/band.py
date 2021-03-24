class Band:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album in self.albums:
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name):
        filter_published = [a for a in self.albums if a.published]
        if not filter_published:
            filtered = [a for a in self.albums if a.name == album_name]
            if filtered:
                self.albums.remove(filtered[0])
                return f"Album {album_name} has been removed."
            return f"Album {album_name} is not found."
        return "Album has been published. It cannot be removed."

    def details(self):
        result = f"Band {self.name}\n"
        result += '\n'.join([f"{a.details()}" for a in self.albums])
        return result
