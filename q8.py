import re

# Sample data
data = [
    {"Device_Type": "Desktop", "Stats_Access_Link": "<a href=\"http://www.example.com\">Example</a>"},
    {"Device_Type": "Mobile", "Stats_Access_Link": "<a href=\"https://m.example.com\">Mobile Example</a>"},
    {"Device_Type": "Tablet", "Stats_Access_Link": "<a href=\"http://tablet.example.com\">Tablet Example</a>"}
]

# Regular expression pattern to extract the URL
pattern = r'<a\s+href="(https?://[\w\.\/]+)"'

# Loop through the data and extract the URLs for each device type
for d in data:
    device_type = d["Device_Type"]
    access_link = d["Stats_Access_Link"]

    # Convert the access link to lower case as per the rules
    access_link = access_link.lower()

    # Extract the URL using the regular expression pattern
    urls = re.findall(pattern, access_link)

    # Print the device type and the extracted URLs
    print(device_type, urls)

