# class definition
class Song:
   def __init___(self,performer,title,album,year):
      self.performer = performer
      self.title = title
      self.album = album
      self.year = year
   def __str__(self):
      print(f"Performer: {self.performer}")
      print(f"Title: {self.title}")
      print(f"Album: {self.album}")
      print(f"Year: {self.year}")

# object creation
song1 = Song("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Song("Queen", "Bohemian Rhapsody", "A Night at the Opera", 1975)
song1 = self.__str__(song1)
song2 = self.__str__(song1)
## object usage
print(song1)
print(song2)