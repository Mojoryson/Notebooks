from rich import print
import pandas as pd

# This function will take an address and return a Google Maps link
def create_google_maps_link(address):
  """
  Generates a Google Maps link for a given address.
  """
  formatted_address = address.replace(" ", "+")
  return f"https://www.google.com/maps/place/{formatted_address}"


# Fake data with valid US addresses
data = [
    {"Name": "John Smith", "Address": "123 Main St, Springfield, IL, 62701", "Phone": "555-123-4567"},
    {"Name": "Jane Doe", "Address": "456 Elm St, Columbus, OH, 43215", "Phone": "555-234-5678"},
    {"Name": "Mike Johnson", "Address": "789 Oak St, Austin, TX, 73301", "Phone": "555-345-6789"},
    {"Name": "Emily Davis", "Address": "321 Maple Ave, Denver, CO, 80202", "Phone": "555-456-7890"},
    {"Name": "Chris Wilson", "Address": "654 Pine St, Seattle, WA, 98101", "Phone": "555-567-8901"},
    {"Name": "Jessica Brown", "Address": "987 Cedar Dr, Boston, MA, 02110", "Phone": "555-678-9012"},
    {"Name": "David Miller", "Address": "135 Walnut St, Miami, FL, 33101", "Phone": "555-789-0123"},
    {"Name": "Sophia Martinez", "Address": "246 Cherry Ln, Nashville, TN, 37201", "Phone": "555-890-1234"},
    {"Name": "Daniel Anderson", "Address": "357 Birch Rd, Chicago, IL, 60601", "Phone": "555-901-2345"},
    {"Name": "Olivia Taylor", "Address": "468 Aspen Way, Los Angeles, CA, 90001", "Phone": "555-012-3456"},
]

# List to hold the processed data
processed_data = []

for row in data:
    name = row['Name']
    address = row['Address']
    phone = row['Phone']

    maps_link = create_google_maps_link(address)
    
    # Add the processed data to the list
    processed_data.append({
        "Name": name,
        "Address": address,
        "Phone": phone,
        "Google Maps Link": maps_link
    })
    
# Create a DataFrame from the processed data
df = pd.DataFrame(processed_data)
    
# Display the DataFrame
pd.set_option('display.max_colwidth', None) 
print(df)
