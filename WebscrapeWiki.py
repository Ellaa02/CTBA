import pandas as pd        # Import pandas → to handle and analyze tabular data
import requests            # Import requests → to fetch the Wikipedia page from the web

# Wikipedia page containing the population table
url = "https://en.wikipedia.org/wiki/List_of_countries_and_dependencies_by_population"

# Send a request to Wikipedia with a fake browser header (to avoid being blocked)
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
response.raise_for_status()   # If the request fails (404, 500, etc.), raise an error

# Use pandas to read ALL tables from the HTML page into a list of DataFrames
tables = pd.read_html(response.text)

# Find the right table that contains both "Location" and "Population" columns
candidate = None
for t in tables:  
    cols = [c.lower() for c in t.columns.astype(str)]  # standardize column names to lowercase
    if any("location" in c for c in cols) and any("population" in c for c in cols):
        candidate = t    # select this table if it has the right columns
        break

# If no matching table is found, stop the program with an error
if candidate is None:
    raise ValueError("Could not find a suitable table on the page.")

# Rename the columns to consistent names: "Location" and "Population"
col_map = {}
for c in candidate.columns:
    cl = str(c).lower()
    if "location" in cl:
        col_map[c] = "Location"
    elif "population" in cl:
        col_map[c] = "Population"

df_scrape = candidate.rename(columns=col_map)[["Location", "Population"]].copy()

# Clean the Population column so it only contains numbers
df_scrape["Population"] = (
    df_scrape["Population"]
    .astype(str)                           # convert values to strings
    .str.replace(r"\[.*?\]", "", regex=True)   # remove footnotes like [1], [2]
    .str.replace(",", "", regex=False)         # remove commas from large numbers
    .str.extract(r"(\d+)", expand=False)       # extract only the digits
    .astype("Int64")                           # convert back to integer type
)

# Keep only the top 10 most populous countries
df_scrape = (
    df_scrape.dropna(subset=["Population"])          # drop rows with missing population
             .sort_values("Population", ascending=False)  # sort by population, descending
             .head(10)                               # take first 10 rows
             .reset_index(drop=True)                 # reset row index (0–9)
)

# Print the cleaned and sorted DataFrame
print(df_scrape)
