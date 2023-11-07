import csv

# with open("planets.csv") as file:
#     planets = csv.DictReader(file)
#     print(planets.fieldnames)
#     for row in planets:
#         print(row)
# We can do better!!!

with open("planets.csv") as file:
    planet_reader = csv.DictReader(file, skipinitialspace=True)
    
    planets = {
        row["name"]: {
            "type": row["type"],
            "distance": float(row["avg_distance_from_sun_km"]),
            "num_moons": int(row["num_moons"]),
            "earth_mass": float(row["earth_mass"])
        }
        for row in planet_reader
    }
    
    print(planets) # A dictionary of planet dicts