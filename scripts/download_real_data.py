import requests
import os

# Target Destination
dest = "../data/real_store_transactions.csv"
url = "https://raw.githubusercontent.com/datsoftlyngby/soft2019fall-bi/master/workshops/workshop01/online_retail_subset.csv"

print(f"Downloading real-world baseline dataset (UCI Subset)...")

try:
    response = requests.get(url, timeout=30)
    if response.status_code == 200:
        with open(dest, 'wb') as f:
            f.write(response.content)
        print(f"Success: Real-world data saved to '{dest}'")
    else:
        print(f"Failed to download: Status Code {response.status_code}")
except Exception as e:
    print(f"Error during download: {e}")
