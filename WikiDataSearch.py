import requests               # Import requests → lets Python send HTTP requests (to APIs)
import pandas as pd           # Import pandas → used to create and manage tables (DataFrames)

# SPARQL query: get the 10 most populous countries from Wikidata
query = """
SELECT ?countryLabel ?population WHERE {
  ?country wdt:P31 wd:Q6256 .             # P31 = "instance of", Q6256 = "country"
  ?country wdt:P1082 ?population .        # P1082 = population property
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
ORDER BY DESC(?population)                # Sort results by population, descending
LIMIT 10                                  # Limit results to top 10
"""

# API endpoint for Wikidata SPARQL queries
endpoint = "https://query.wikidata.org/sparql"

# Headers → identify yourself with a User-Agent (best practice to avoid blocking)
headers = {"User-Agent": "MSBA-class-example/1.0 (xpan02@wm.edu)"}

# Send GET request to Wikidata API with query parameters
resp = requests.get(endpoint, params={"query": query, "format": "json"}, headers=headers)

resp.raise_for_status()  # If request fails (e.g., 404/500), raise an error
data = resp.json()["results"]["bindings"]  # Parse JSON response → extract "results"

# Convert the API results into a pandas DataFrame
df_api = pd.DataFrame([
    {
        "Country": r["countryLabel"]["value"],         # Extract country name
        "Population": int(r["population"]["value"])    # Extract population and convert to integer
    }
    for r in data
])

# Print the DataFrame (table of top 10 most populous countries)
print(df_api)
