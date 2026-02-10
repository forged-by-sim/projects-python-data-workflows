import urllib.request as ur
import json

# Prompt for URL
url = input("Enter location: ").strip()

print("Retrieving", url)
data = ur.urlopen(url).read().decode()
print("Retrieved", len(data), "characters")

# Parse JSON
info = json.loads(data)

# Sum the counts
total_sum = 0
total_count = 0

for item in info["comments"]:
    total_sum += int(item["count"])
    total_count += 1

print("Count:", total_count)
print("Sum:", total_sum)

