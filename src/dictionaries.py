"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""

waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
waypoints.append({
    "lat": 41,
    "lon": 71,
    "name": "nowhere"
})

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
place = waypoints[0]
place["lon"] = -130
place["name"] = "not a real place"

# Write a loop that prints out all the field values for all the waypoints
for waypoint in waypoints:
    place_lat = waypoint["lat"]
    place_lon = waypoint["lon"]
    place_name = waypoint["name"]
    print(f'{place_name}:  {place_lat}° {place_lon}°')
