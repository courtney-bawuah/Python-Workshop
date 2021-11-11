#!/Users/courtney.bawuah/.pyenv/shims/python

planets = ["Mercury", "Venus", "Earth", "Mars"]

# Dictionaries
distance_from_sun = {
    "Mercury" : 0.4,
    "Venus" : 0.7,
    "Earth" : 1,
    "Mars" : 1.5
}

print(distance_from_sun ["Mercury"])
for key in distance_from_sun:
    print(key + "-->" + str(distance_from_sun[key]))