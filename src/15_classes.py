# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor

# YOUR CODE HERE
class LatLon:
  def __init__(self, lat, lon):
    self.lat = lat
    self.lon = lon

# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

# YOUR CODE HERE
class Waypoint(LatLon):
  def __init__(self, lat, lon, name):
    super().__init__(lat, lon)
    self.name = name

  def __str__(self):
    return f"\n Waypoint: {self.name} can be found at these coordinates: \n {self.lat} latitude and {self.lon} longitude."


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

# YOUR CODE HERE
class Geocache(Waypoint):
  def __init__(self, name, difficulty, size, lat, lon):
    super().__init__(lat, lon, name)
    self.difficulty = difficulty
    self.size = size

  def __str__(self):
    return f"\n Geocache: {self.name}is located at {self.lat} latitude and {self.lon} longitude. \n It's size is {self.size}. \n It has a difficulty rating of {self.difficulty}. \n"

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

# YOUR CODE HERE
waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
print("\n", waypoint.name, "\n", waypoint.lat, "\n", waypoint.lon)
# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

# YOUR CODE HERE
geocache = Geocache("Newberry Views", 1.5, 2, 44.052137, -121.41556)
print("\n", geocache.name, "\n", geocache.difficulty, "\n", geocache.size, "\n",geocache.lat, "\n", geocache.lon, "\n",)

# Print it--also make this print more nicely
print(geocache)
