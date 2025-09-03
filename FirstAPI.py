import requests        # imports the requests library → used to send HTTP requests (talk to APIs)
import pandas          # imports pandas library → used to handle tabular data (tables, DataFrames)


# 5 sample cities in Virginia with lat/lon
cities_va = {                              # creates a dictionary called cities_va
    "Williamsburg": (37.2707, -76.7075),   # key = city name, value = (latitude, longitude)
    "Richmond": (37.5407, -77.4360),    
    "Virginia Beach": (36.8529, -75.9780),
    "Roanoke": (37.2709, -79.9414),
    "Charlottesville": (38.0293, -78.4767),
    } 

url = "https://api.open-meteo.com/v1/forecast"

result = [] # Empty list → will collect the weather data for all cities

# Loop through each city and its coordinates
for city, (lat, lon) in cities_va.items():  
    params = {                              
        "latitude": lat,           # Tell API which latitude to use
        "longitude": lon,          # Tell API which longitude to use
        "current_weather": True,   # Request current weather info only
    }
    
    # Send request to API with the given parameters
    response = requests.get(url, params=params)  
    data = response.json()   # Convert the JSON response into a Python dictionary

    # If the API returned weather info, extract and save it
    if "current_weather" in data:  
        weather = data["current_weather"]  # Pull out the weather details
        
        result.append({                   # Add a dictionary of city + weather data to results
            "City": city,
            "Temperature (°C)": weather["temperature"],   # Current temperature
            "Wind Speed (km/h)": weather["windspeed"],    # Current wind speed
            "Time": weather["time"]                       # Time of data reading
        })
    # If no weather data is available, save None values for this city
    else:
        result.append({
            "City": city, 
            "Temperature (°C)": None, 
            "Wind Speed (km/h)": None, 
            "Time": None
        }) 

# Turn the list of weather results into a pandas DataFrame (table) and print it
df = pandas.DataFrame(result)  
print(df)
