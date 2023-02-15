import requests

# API endpoint for player information
endpoint = "https://www.balldontlie.io/api/v1/players/"


# API key

# player id
player_id = 237

# API request
response = requests.get(endpoint + str(player_id))

# Get JSON data
data = response.json()

# Print player information
print("Name:", data["first_name"], data["last_name"])
print("Team:", data["team"]["full_name"])
print("Position:", data["position"])
print("Height:", data["height_feet"], "feet", data["height_inches"], "inches")
print("Weight:", data["weight_pounds"], "pounds")


