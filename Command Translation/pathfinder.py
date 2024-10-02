import requests
import polyline  # Library to decode polylines
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def get_route_coordinates(origin, destination):
    # Get the Google API key from the environment variable
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        raise ValueError("API key not found. Please check your .env file.")
    
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

# # Example usage
# origin = "Museum of Fine Arts, Boston, MA"
# destination = "Newbury Street, Boston, MA"

# coordinates = get_route_coordinates(origin, destination)

# if coordinates:
#     print("Coordinates of the route:")
#     for coord in coordinates:
#         print(coord)
