import requests
import pandas as pd

# Read the Excel file into a DataFrame
df = pd.read_excel(r'File_location')

# Iterate through the DataFrame
for index, website in df.iterrows():
    try:
        # Send a GET request to the website
        response = requests.get(website["WEBSITE'S NAMES:"])
        # Update the status_code column with the response status code
        df.at[index, "status_code"] = "site is ok {}".format(response.status_code)
    except:
        # If an exception occurs, mark the status_code column with a message
        df.at[index, "status_code"] = "site is not available"

# Print the DataFrame
print(df)
