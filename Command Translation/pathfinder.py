# The pathfinder seeks to make a path for the drone to fly between two locations using google map directions API. 

import requests
import polyline  # Library to decode polylines

def get_route_coordinates(origin, destination, api_key):
    # API endpoint
    url = f"https://maps.googleapis.com/maps/api/directions/json?origin={origin}&destination={destination}&key={api_key}"
    
    # Make the API request
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse the response JSON
        data = response.json()
        
        # Check if routes are available
        if len(data['routes']) > 0:
            # Extract the overview polyline
            polyline_str = data['routes'][0]['overview_polyline']['points']
            
            # Decode the polyline into a list of (latitude, longitude) tuples
            coordinates = polyline.decode(polyline_str)
            
            return coordinates
        else:
            print("No routes found.")
            return None
    else:
        print(f"Error fetching directions: {response.status_code}")
        return None

# Example usage
api_key = "YOUR_GOOGLE_API_KEY"
origin = "San Francisco,CA"
destination = "Los Angeles,CA"

coordinates = get_route_coordinates(origin, destination, api_key)

if coordinates:
    print("Coordinates of the route:")
    for coord in coordinates:
        print(coord)
