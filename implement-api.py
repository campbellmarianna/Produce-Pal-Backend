import requests

# Set up the parameters we want to pass to the API
parameters = {"lat": "37.774929", "lon": "-122.419418"}

# Make a get request with the parameters.
response = requests.get("http://search.ams.usda.gov/farmersmarkets/v1/data.svc/locSearch?lat=" + parameters["lat"] + "&lng=" + parameters["lon"])

# Get the response data as a python object. Verify that it's a dictionary.
data = response.json()
print(type(data))
print(data)

# Future additions:
    # Create functions to retrieve data from the API
