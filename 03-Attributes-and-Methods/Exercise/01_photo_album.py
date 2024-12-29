class PhotoAlbum:
    def __init__(self, pages):
        self.pages = pages
        self.photos = [[] for _ in range(pages)]

    @classmethod
    def from_photos_count(cls, photos_count):
        return cls(photos_count // 4)

    def add_photo(self, label):
        for page in range(len(self.photos)):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page " \
                       f"{page + 1} slot {self.photos[page].index(label) + 1}"

        return "No more free spots"

    def display(self):
        photos_display = ''
        for page in self.photos:
            photos_display += f"{'-' * 11}\n"
            photos = f"{'[] ' * len(page)}"
            photos_display += f"{photos[:-1]}\n"
        photos_display += f"{'-' * 11}\n"
        return photos_display


album = PhotoAlbum(2)



print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
