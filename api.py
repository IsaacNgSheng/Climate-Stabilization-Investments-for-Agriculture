import urllib.request
import sys
import json

# Define the API endpoint and parameters
url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/chicago?unitGroup=us&key=TRX5UZ3LZ4G73ZLHQXT9AUGQG&contentType=json"

try:
    # Fetch the data from the API
    ResultBytes = urllib.request.urlopen(url)
    
    # Parse the results as JSON
    jsonData = json.load(ResultBytes)
    
    # Check and extract the required data
    if 'days' in jsonData:
        temperature_data = jsonData['days']
        for day in temperature_data:
            print(f"Date: {day['datetime']}, Temperature: {day['temp']}°F")
    else:
        print("No temperature data found")
        
except urllib.error.HTTPError as e:
    ErrorInfo = e.read().decode()
    print('Error code:', e.code, ErrorInfo)
    sys.exit()
except urllib.error.URLError as e:
    ErrorInfo = e.read().decode()
    print('Error code:', e.code, ErrorInfo)
    sys.exit()
