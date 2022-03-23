"""Dictionaries of dictionary capabilities."""


# Declaring the type of a dictionary
schools: dict[str, int]

# Initialize into an empty dictionary
schools = dict()

# Set a key value pairing in the dictionary
schools["UNC"] = 19_400
schools["Duke"] = 6_717
schools["NCSU"] = 26_150

# Print a dictionary literal representation
print(schools)

# Access a value by its key -- "look-up"
print(f"UNC has {schools['UNC']} students.")

# Remove a key value pair from a dictionary
# by its key.
schools.pop("Duke")

# Test for existence of a key
# is_duke_present: bool = "Duke" in schools
# print(f"Duke is present: {is_duke_present}")
if "Duke" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update / reassign a key value pair
schools["UNC"] = 20000
# schools["NCSU"] = schools["NCSU"] + 200
schools["NCSU"] += 200

print(schools)

# Demonstration of dictionary literals

# Empty dictionary literal

schools = {}  # Same as dict()
print(schools)

# Alternatively, initialize key-value pairs
schools = {"UNC": 19400, "Dukie": 6717, "NCSU": 26150}
print(schools)


print(schools["UNC"])

for key in schools:
    print(f"key: {key} -> Value: {schools[key]}")