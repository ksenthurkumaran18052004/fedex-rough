# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# # # AQICN API for Weather Data
# # def get_weather_data(location):
# #     api_key = "6de04ebceb5acd7c06226ffb5b8609f44b4dcbe3"
# #     url = f"https://api.waqi.info/feed/{location}/?token={api_key}"
# #     print("Weather API Request URL:", url)  # Debug log

# #     response = requests.get(url)
# #     try:
# #         response_data = response.json()
# #         print("Weather API Raw Response:", response_data)  # Debug log
# #         if response.status_code == 200 and "data" in response_data:
# #             return response_data['data']
# #         else:
# #             return {"error": f"Unexpected response structure: {response_data}"}
# #     except Exception as e:
# #         print("Error parsing weather data:", str(e))  # Debug log
# #         return {"error": str(e)}

# def get_weather_data(location):
#     # Step 1: Geocode the location to get coordinates
#     google_api_key = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"
#     geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={google_api_key}"
#     geocode_response = requests.get(geocode_url)
#     try:
#         geocode_data = geocode_response.json()
#         print("Geocode Data:", geocode_data)  # Debug log
#         if geocode_data["status"] == "OK":
#             lat = geocode_data["results"][0]["geometry"]["location"]["lat"]
#             lng = geocode_data["results"][0]["geometry"]["location"]["lng"]
#             coordinates = f"{lat},{lng}"
#         else:
#             return {"error": f"Failed to geocode location: {location}"}
#     except Exception as e:
#         return {"error": f"Geocoding error: {str(e)}"}

#     # Step 2: Query AQICN API with coordinates
#     aqicn_api_key = "6de04ebceb5acd7c06226ffb5b8609f44b4dcbe3"
#     aqicn_url = f"https://api.waqi.info/feed/geo:{coordinates}/?token={aqicn_api_key}"
#     print("AQICN API URL:", aqicn_url)  # Debug log
#     response = requests.get(aqicn_url)
#     try:
#         response_data = response.json()
#         print("AQICN Response Data:", response_data)  # Debug log
#         if response.status_code == 200 and "data" in response_data and "aqi" in response_data["data"]:
#             return response_data["data"]
#         else:
#             return {"error": f"Unknown station or missing data for coordinates: {coordinates}"}
#     except Exception as e:
#         return {"error": f"Error fetching weather data: {str(e)}"}


# # TomTom API for Traffic Data
# def get_traffic_data(origin, destination):
#     api_key = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
#     url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={api_key}"
#     print("Traffic API Request URL:", url)  # Debug log

#     response = requests.get(url)
#     try:
#         response_data = response.json()
#         print("Traffic API Raw Response:", response_data)  # Debug log
#         if response.status_code == 200 and "routes" in response_data:
#             return response_data['routes']
#         else:
#             return {"error": f"Unexpected response structure: {response_data}"}
#     except Exception as e:
#         print("Error parsing traffic data:", str(e))  # Debug log
#         return {"error": str(e)}


# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/optimize", methods=["POST"])
# def optimize():
#     try:
#         data = request.json
#         print("Received Input Data:", data)  # Debug log

#         origin = data["origin"]
#         destination = data["destination"]
#         fuel_efficiency = float(data["fuel_efficiency"])
#         emission_factor = float(data["emission_factor"])

#         # Step 1: Fetch weather data
#         weather_data = get_weather_data(destination["address"])
#         print("Fetched Weather Data:", weather_data)  # Debug log

#         if "error" in weather_data:
#             print("Weather data error:", weather_data["error"])  # Debug log
#             weather_warning = weather_data["error"]
#             rain = False
#             high_aqi = False
#         else:
#             # Process weather data
#             rain = "rain" in str(weather_data.get("forecast", {})).lower()
#             high_aqi = weather_data.get("aqi", 0) > 100
#             weather_warning = None

#         print(f"Rain: {rain}, High AQI: {high_aqi}")  # Debug log

#         # Step 2: Fetch traffic data
#         traffic_data = get_traffic_data(
#             f"{origin['lat']},{origin['lng']}",
#             f"{destination['lat']},{destination['lng']}",
#         )
#         print("Fetched Traffic Data:", traffic_data)  # Debug log
#         if "error" in traffic_data:
#             return jsonify({"error": f"Traffic data error: {traffic_data['error']}"})

#         # Step 3: Evaluate routes
#         better_routes = []
#         for route in traffic_data:
#             if rain or high_aqi or route["summary"]["trafficDelayInSeconds"] > 600:
#                 continue
#             better_routes.append(route)

#         print("Better Routes:", better_routes)  # Debug log

#         # Step 4: Select the optimal route
#         optimal_route = min(better_routes, key=lambda r: r["summary"]["trafficDelayInSeconds"], default=None)
#         if not optimal_route:
#             return jsonify({"error": "No optimal route found due to adverse conditions"})

#         # Step 5: Calculate emissions
#         distance_km = optimal_route["summary"]["lengthInMeters"] / 1000  # Convert meters to km
#         emissions = (distance_km / fuel_efficiency) * emission_factor

#         return jsonify({
#             "optimal_route": optimal_route,
#             "emissions": emissions,
#             "weather_warning": weather_warning,
#             "weather_conditions": {
#                 "rain": rain,
#                 "high_aqi": high_aqi,
#                 "aqi": weather_data.get("aqi", 0) if weather_warning is None else "N/A",
#                 "forecast": weather_data.get("forecast", {}) if weather_warning is None else "N/A",
#             },
#         })

#     except Exception as e:
#         print("Error in /optimize route:", str(e))  # Debug log
#         return jsonify({"error": str(e)})


    
# if __name__ == "__main__":
#     app.run(debug=True)
















































# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# # Function to fetch weather forecast from OpenWeatherMap
# def get_weather_forecast(lat, lon):
#     openweather_api_key = "01fecea7c070babba3ef42c3cb86c9c2"
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={openweather_api_key}"
#     print("OpenWeatherMap Request URL:", url)  # Debug log
#     response = requests.get(url)
#     try:
#         response_data = response.json()
#         print("OpenWeatherMap Response:", response_data)  # Debug log
#         if response.status_code == 200:
#             return response_data
#         else:
#             return {"error": f"Failed to fetch weather forecast: {response_data}"}
#     except Exception as e:
#         return {"error": f"Error fetching weather forecast: {str(e)}"}

# # Function to fetch AQI data from AQICN
# def get_weather_data(location):
#     google_api_key = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"
#     geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={location}&key={google_api_key}"
#     geocode_response = requests.get(geocode_url)
#     try:
#         geocode_data = geocode_response.json()
#         print("Geocode Data:", geocode_data)  # Debug log
#         if geocode_data["status"] == "OK":
#             lat = geocode_data["results"][0]["geometry"]["location"]["lat"]
#             lng = geocode_data["results"][0]["geometry"]["location"]["lng"]
#             coordinates = f"{lat},{lng}"
#         else:
#             return {"error": f"Failed to geocode location: {location}"}
#     except Exception as e:
#         return {"error": f"Geocoding error: {str(e)}"}

#     aqicn_api_key = "6de04ebceb5acd7c06226ffb5b8609f44b4dcbe3"
#     aqicn_url = f"https://api.waqi.info/feed/geo:{coordinates}/?token={aqicn_api_key}"
#     print("AQICN API URL:", aqicn_url)  # Debug log
#     response = requests.get(aqicn_url)
#     try:
#         response_data = response.json()
#         print("AQICN Response Data:", response_data)  # Debug log
#         if response.status_code == 200 and "data" in response_data:
#             return response_data["data"]
#         else:
#             return {"error": f"Failed to fetch AQI data: {response_data}"}
#     except Exception as e:
#         return {"error": f"Error fetching AQI data: {str(e)}"}

# # Function to fetch traffic data from TomTom
# def get_traffic_data(origin, destination):
#     tomtom_api_key = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
#     url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={tomtom_api_key}"
#     print("Traffic API Request URL:", url)  # Debug log
#     response = requests.get(url)
#     try:
#         response_data = response.json()
#         print("Traffic API Raw Response:", response_data)  # Debug log
#         if response.status_code == 200 and "routes" in response_data:
#             return response_data["routes"]
#         else:
#             return {"error": f"Failed to fetch traffic data: {response_data}"}
#     except Exception as e:
#         return {"error": f"Error fetching traffic data: {str(e)}"}

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/optimize", methods=["POST"])
# def optimize():
#     try:
#         data = request.json
#         print("Received Input Data:", data)  # Debug log

#         origin = data["origin"]
#         destination = data["destination"]
#         fuel_efficiency = float(data["fuel_efficiency"])
#         emission_factor = float(data["emission_factor"])

#         # Geocode destination for lat/lon
#         google_api_key = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"
#         geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={destination['address']}&key={google_api_key}"
#         geocode_response = requests.get(geocode_url)
#         geocode_data = geocode_response.json()
#         if geocode_data["status"] != "OK":
#             return jsonify({"error": "Failed to geocode destination"})
#         lat = geocode_data["results"][0]["geometry"]["location"]["lat"]
#         lon = geocode_data["results"][0]["geometry"]["location"]["lng"]

#         # Get weather forecast
#         weather_forecast = get_weather_forecast(lat, lon)
#         rain = "rain" in weather_forecast.get("weather", [{}])[0].get("main", "").lower()

#         # Get AQI
#         aqi_data = get_weather_data(destination["address"])
#         aqi = aqi_data.get("aqi", "N/A") if "aqi" in aqi_data else "N/A"
#         high_aqi = aqi != "N/A" and int(aqi) > 100

#         # Traffic data
#         traffic_data = get_traffic_data(
#             f"{origin['lat']},{origin['lng']}",
#             f"{destination['lat']},{destination['lng']}"
#         )
#         if "error" in traffic_data:
#             return jsonify({"error": f"Traffic data error: {traffic_data['error']}"})

#         # Find optimal route
#         optimal_route = min(traffic_data, key=lambda r: r["summary"]["trafficDelayInSeconds"])
#         distance_km = optimal_route["summary"]["lengthInMeters"] / 1000
#         emissions = (distance_km / fuel_efficiency) * emission_factor

#         return jsonify({
#             "optimal_route": optimal_route,
#             "emissions": emissions,
#             "weather_conditions": {"rain": rain, "aqi": aqi, "high_aqi": high_aqi}
#         })
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == "__main__":
#     app.run(debug=True)








































































# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# # API Keys
# OPEN_WEATHER_API_KEY = "01fecea7c070babba3ef42c3cb86c9c2"
# TOMTOM_API_KEY = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
# GOOGLE_API_KEY = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"

# # Function to fetch weather forecast
# def get_weather_forecast(lat, lon):
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return {"error": "Failed to fetch weather data"}
#     except Exception as e:
#         return {"error": str(e)}

# # Function to fetch traffic data
# def get_traffic_data(origin, destination):
#     url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={TOMTOM_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json().get("routes", [])
#         else:
#             return []
#     except Exception as e:
#         return {"error": str(e)}

# # Reverse Geocoding for Traffic Locations
# def get_location_name(lat, lon):
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             data = response.json()
#             if data["status"] == "OK" and data["results"]:
#                 return data["results"][0]["formatted_address"]
#         return "Unknown Location"
#     except Exception as e:
#         return "Error Fetching Location"

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/optimize", methods=["POST"])
# def optimize():
#     try:
#         data = request.json
#         origin = data["origin"]
#         destination = data["destination"]
#         fuel_efficiency = float(data["fuel_efficiency"])
#         emission_factor = float(data["emission_factor"])

#         # Fetch traffic data for 3 routes
#         traffic_data = get_traffic_data(
#             f"{origin['lat']},{origin['lng']}",
#             f"{destination['lat']},{destination['lng']}"
#         )
#         if not traffic_data:
#             return jsonify({"error": "No traffic data available"})

#         routes = []
#         for route in traffic_data[:3]:  # Limit to 3 routes
#             route_summary = route.get("summary", {})
#             distance_km = route_summary.get("lengthInMeters", 0) / 1000
#             duration_sec = route_summary.get("travelTimeInSeconds", 0)
#             traffic_delay = route_summary.get("trafficDelayInSeconds", 0)
#             emissions = (distance_km / fuel_efficiency) * emission_factor

#             # Extract traffic delay locations (sample points)
#             traffic_locations = []
#             for leg in route.get("legs", []):
#                 for point in leg.get("points", [])[::100]:  # Sample every 100th point
#                     location_name = get_location_name(point["latitude"], point["longitude"])
#                     traffic_locations.append(location_name)

#             # Fetch weather for the midpoint of the route
#             midpoint = leg.get("points", [])[len(leg.get("points", [])) // 2]
#             weather_data = get_weather_forecast(midpoint["latitude"], midpoint["longitude"])
#             weather_summary = weather_data.get("weather", [{}])[0].get("description", "Unknown")

#             routes.append({
#                 "distance": f"{distance_km:.2f} km",
#                 "duration": f"{duration_sec // 3600} hours {duration_sec % 3600 // 60} mins",
#                 "traffic_delay": f"{traffic_delay // 60} mins" if traffic_delay > 0 else "No delay",
#                 "emissions": f"{emissions:.2f} kg CO2",
#                 "traffic_locations": traffic_locations[:5],  # Limit to 5 locations
#                 "weather_summary": weather_summary
#             })

#         return jsonify({"routes": routes})
#     except Exception as e:
#         return jsonify({"error": str(e)})

# if __name__ == "__main__":
#     app.run(debug=True)
















































# from flask import Flask, render_template, request, jsonify
# import requests

# app = Flask(__name__)

# # API Keys
# OPEN_WEATHER_API_KEY = "01fecea7c070babba3ef42c3cb86c9c2"
# TOMTOM_API_KEY = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
# GOOGLE_API_KEY = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"

# # Function to fetch weather forecast
# def get_weather_forecast(lat, lon):
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return {"error": "Failed to fetch weather data"}
#     except Exception as e:
#         return {"error": str(e)}

# # Function to fetch traffic data
# def get_traffic_data(origin, destination):
#     url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={TOMTOM_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json().get("routes", [])
#         else:
#             return []
#     except Exception as e:
#         return {"error": str(e)}

# # Reverse Geocoding for Traffic Locations
# def get_location_name(lat, lon):
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             data = response.json()
#             if data["status"] == "OK" and data["results"]:
#                 return data["results"][0]["formatted_address"]
#         return "Unknown Location"
#     except Exception as e:
#         return "Error Fetching Location"

# @app.route("/")
# def home():
#     return render_template("index.html")

# # Function to reverse geocode and get city name
# def get_city_name(lat, lon):
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             data = response.json()
#             if data["status"] == "OK" and data["results"]:
#                 # Extract city name from the address components
#                 for component in data["results"][0]["address_components"]:
#                     if "locality" in component["types"]:  # Check for city/locality
#                         return component["long_name"]
#                 # If no city/locality, return formatted address
#                 return data["results"][0]["formatted_address"]
#         return "Unknown Location"
#     except Exception as e:
#         return "Error Fetching City Name"

# # Update the weather data fetching for every 100 km
# def get_weather_forecast_along_route(route_points):
#     weather_data = []
#     for idx, point in enumerate(route_points[::100]):  # Sample every 100th point
#         weather = get_weather_forecast(point["latitude"], point["longitude"])
#         city_name = get_city_name(point["latitude"], point["longitude"])
#         weather_summary = weather.get("weather", [{}])[0].get("description", "Unknown")
#         weather_data.append({"location": city_name, "weather": weather_summary})
#     return weather_data


# # Function to calculate the distance between two points (Haversine formula)
# from math import radians, sin, cos, sqrt, atan2

# def calculate_distance(point1, point2):
#     R = 6371  # Radius of the Earth in km
#     lat1, lon1 = radians(point1["latitude"]), radians(point1["longitude"])
#     lat2, lon2 = radians(point2["latitude"]), radians(point2["longitude"])
#     dlat, dlon = lat2 - lat1, lon2 - lon1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     return R * c
# # Function to fetch traffic locations and reverse geocode
# def get_traffic_locations(points):
#     traffic_locations = []
#     for point in points[::100]:  # Sample every 100th point
#         location_name = get_location_name(point["latitude"], point["longitude"])
#         traffic_locations.append(location_name)
#     return traffic_locations

# @app.route("/optimize", methods=["POST"])
# def optimize():
#     try:
#         data = request.json
#         origin = data["origin"]
#         destination = data["destination"]
#         fuel_efficiency = float(data["fuel_efficiency"])
#         emission_factor = float(data["emission_factor"])

#         # Fetch traffic data for up to 3 routes
#         traffic_data = get_traffic_data(
#             f"{origin['lat']},{origin['lng']}",
#             f"{destination['lat']},{destination['lng']}"
#         )
#         if not traffic_data:
#             return jsonify({"error": "No traffic data available"})

#         routes = []
#         for idx, route in enumerate(traffic_data[:3]):  # Limit to 3 routes
#             route_summary = route.get("summary", {})
#             distance_km = route_summary.get("lengthInMeters", 0) / 1000
#             duration_sec = route_summary.get("travelTimeInSeconds", 0)
#             traffic_delay = route_summary.get("trafficDelayInSeconds", 0)
#             emissions = (distance_km / fuel_efficiency) * emission_factor

#             # Extract route points
#             route_points = [{"latitude": point["latitude"], "longitude": point["longitude"]}
#                             for leg in route.get("legs", [])
#                             for point in leg.get("points", [])]

#             # Get traffic locations
#             traffic_locations = get_traffic_locations(route_points)

#             # Fetch weather data for every 100 km
#             # Fetch weather data for the midpoint of the route
#             weather_data = get_weather_forecast_along_route(route_points)


#             routes.append({
#                 "route_index": idx + 1,
#                 "distance": f"{distance_km:.2f} km",
#                 "duration": f"{duration_sec // 3600} hours {duration_sec % 3600 // 60} mins",
#                 "traffic_delay": f"{traffic_delay // 60} mins" if traffic_delay > 0 else "No delay",
#                 "emissions": f"{emissions:.2f} kg CO2",
#                 "traffic_locations": traffic_locations[:5],  # Limit to 5 locations
#                 "weather_data": weather_data,
#                 "route_points": route_points  # Include points for mapping
#             })

#         return jsonify({"routes": routes})
#     except Exception as e:
#         return jsonify({"error": str(e)})


# if __name__ == "__main__":
#     app.run(debug=True)












































# from flask import Flask, render_template, request, jsonify
# import requests
# from math import radians, sin, cos, sqrt, atan2

# app = Flask(__name__)

# # API Keys
# OPEN_WEATHER_API_KEY = "01fecea7c070babba3ef42c3cb86c9c2"
# TOMTOM_API_KEY = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
# GOOGLE_API_KEY = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"

# # Function to fetch weather forecast
# def get_weather_forecast(lat, lon):
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return {"error": "Failed to fetch weather data"}
#     except Exception as e:
#         return {"error": str(e)}

# # Function to fetch traffic data
# def get_traffic_data(origin, destination):
#     url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={TOMTOM_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json().get("routes", [])
#         else:
#             return []
#     except Exception as e:
#         return {"error": str(e)}

# # Function to reverse geocode and get city name
# def get_city_name(lat, lon):
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             data = response.json()
#             if data["status"] == "OK" and data["results"]:
#                 for component in data["results"][0]["address_components"]:
#                     if "locality" in component["types"]:  # Check for city/locality
#                         return component["long_name"]
#                 return data["results"][0]["formatted_address"]
#         return "Unknown Location"
#     except Exception as e:
#         return "Error Fetching City Name"

# # Function to fetch weather data along the route every 100 km
# def get_weather_forecast_along_route(route_points):
#     weather_data = []
#     for idx, point in enumerate(route_points[::100]):  # Sample every 100th point
#         weather = get_weather_forecast(point["latitude"], point["longitude"])
#         city_name = get_city_name(point["latitude"], point["longitude"])
#         weather_summary = weather.get("weather", [{}])[0].get("description", "Unknown")
#         weather_data.append({"location": city_name, "weather": weather_summary})
#     return weather_data

# # Function to fetch traffic locations and reverse geocode
# def get_traffic_locations(points):
#     traffic_locations = []
#     for point in points[::100]:  # Sample every 100th point
#         location_name = get_city_name(point["latitude"], point["longitude"])
#         traffic_locations.append(location_name)
#     return traffic_locations

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/optimize", methods=["POST"])
# def optimize():
#     try:
#         data = request.json
#         origin = data["origin"]
#         destination = data["destination"]
#         fuel_efficiency = float(data["fuel_efficiency"])
#         emission_factor = float(data["emission_factor"])

#         # Fetch traffic data for up to 3 routes
#         traffic_data = get_traffic_data(
#             f"{origin['lat']},{origin['lng']}",
#             f"{destination['lat']},{destination['lng']}"
#         )
#         if not traffic_data:
#             return jsonify({"error": "No traffic data available"})

#         routes = []
#         for idx, route in enumerate(traffic_data[:3]):  # Limit to 3 routes
#             route_summary = route.get("summary", {})
#             distance_km = route_summary.get("lengthInMeters", 0) / 1000
#             duration_sec = route_summary.get("travelTimeInSeconds", 0)
#             traffic_delay = route_summary.get("trafficDelayInSeconds", 0)
#             emissions = (distance_km / fuel_efficiency) * emission_factor

#             # Extract route points
#             route_points = [{"latitude": point["latitude"], "longitude": point["longitude"]}
#                             for leg in route.get("legs", [])
#                             for point in leg.get("points", [])]

#             # Get traffic locations
#             traffic_locations = get_traffic_locations(route_points)

#             # Fetch weather data for every 100 km
#             weather_data = get_weather_forecast_along_route(route_points)

#             routes.append({
#                 "route_index": idx + 1,
#                 "distance": f"{distance_km:.2f} km",
#                 "duration": f"{duration_sec // 3600} hours {duration_sec % 3600 // 60} mins",
#                 "traffic_delay": f"{traffic_delay // 60} mins" if traffic_delay > 0 else "No delay",
#                 "emissions": f"{emissions:.2f} kg CO2",
#                 "traffic_locations": traffic_locations[:5],  # Limit to 5 locations
#                 "weather_data": weather_data,
#                 "route_points": route_points  # Include points for mapping
#             })

#         return jsonify({"routes": routes})
#     except Exception as e:
#         return jsonify({"error": str(e)})


# if __name__ == "__main__":
#     app.run(debug=True)























# from flask import Flask, render_template, request, jsonify
# import requests
# from math import radians, sin, cos, sqrt, atan2

# app = Flask(__name__)

# # API Keys
# OPEN_WEATHER_API_KEY = "01fecea7c070babba3ef42c3cb86c9c2"
# TOMTOM_API_KEY = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
# GOOGLE_API_KEY = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"

# # Function to fetch weather forecast
# def get_weather_forecast(lat, lon):
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json()
#         else:
#             return {"error": "Failed to fetch weather data"}
#     except Exception as e:
#         return {"error": str(e)}

# # Function to fetch traffic data
# def get_traffic_data(origin, destination):
#     url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={TOMTOM_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json().get("routes", [])
#         else:
#             return []
#     except Exception as e:
#         return {"error": str(e)}

# # Function to reverse geocode and get city name
# def get_city_name(lat, lon):
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             data = response.json()
#             if data["status"] == "OK" and data["results"]:
#                 for component in data["results"][0]["address_components"]:
#                     if "locality" in component["types"]:  # Check for city/locality
#                         return component["long_name"]
#                 return data["results"][0]["formatted_address"]
#         return "Unknown Location"
#     except Exception as e:
#         return "Error Fetching City Name"

# # Function to fetch weather data along the route every 100 km
# def get_weather_forecast_along_route(route_points):
#     weather_data = []
#     total_distance = 0
#     last_point = route_points[0]  # Initialize with the first point

#     for point in route_points:
#         # Calculate the distance from the last point
#         distance = calculate_distance(last_point, point)
#         total_distance += distance

#         # Fetch weather data for every 100 km
#         if total_distance >= 100:
#             weather = get_weather_forecast(point["latitude"], point["longitude"])
#             city_name = get_city_name(point["latitude"], point["longitude"])
#             weather_summary = weather.get("weather", [{}])[0].get("description", "Unknown")
#             weather_data.append({"location": city_name, "weather": weather_summary})
#             total_distance = 0  # Reset after fetching weather
#         last_point = point  # Update last point

#     return weather_data

# # Function to calculate the distance between two points (Haversine formula)
# def calculate_distance(point1, point2):
#     R = 6371  # Radius of the Earth in km
#     lat1, lon1 = radians(point1["latitude"]), radians(point1["longitude"])
#     lat2, lon2 = radians(point2["latitude"]), radians(point2["longitude"])
#     dlat, dlon = lat2 - lat1, lon2 - lon1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     return R * c

# # Function to fetch traffic locations and reverse geocode
# def get_traffic_locations(points):
#     traffic_locations = []
#     for point in points[::100]:  # Sample every 100th point
#         location_name = get_city_name(point["latitude"], point["longitude"])
#         traffic_locations.append(location_name)
#     return traffic_locations

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/optimize", methods=["POST"])
# def optimize():
#     try:
#         data = request.json
#         origin = data["origin"]
#         destination = data["destination"]
#         fuel_efficiency = float(data["fuel_efficiency"])
#         emission_factor = float(data["emission_factor"])

#         # Fetch traffic data for up to 3 routes
#         traffic_data = get_traffic_data(
#             f"{origin['lat']},{origin['lng']}",
#             f"{destination['lat']},{destination['lng']}"
#         )
#         if not traffic_data:
#             return jsonify({"error": "No traffic data available"})

#         routes = []
#         for idx, route in enumerate(traffic_data[:3]):  # Limit to 3 routes
#             route_summary = route.get("summary", {})
#             distance_km = route_summary.get("lengthInMeters", 0) / 1000
#             duration_sec = route_summary.get("travelTimeInSeconds", 0)
#             traffic_delay = route_summary.get("trafficDelayInSeconds", 0)
#             emissions = (distance_km / fuel_efficiency) * emission_factor

#             # Extract route points
#             route_points = [{"latitude": point["latitude"], "longitude": point["longitude"]}
#                             for leg in route.get("legs", [])
#                             for point in leg.get("points", [])]

#             # Get traffic locations
#             traffic_locations = get_traffic_locations(route_points)

#             # Fetch weather data for every 100 km
#             weather_data = get_weather_forecast_along_route(route_points)

#             routes.append({
#                 "route_index": idx + 1,
#                 "distance": f"{distance_km:.2f} km",
#                 "duration": f"{duration_sec // 3600} hours {duration_sec % 3600 // 60} mins",
#                 "traffic_delay": f"{traffic_delay // 60} mins" if traffic_delay > 0 else "No delay",
#                 "emissions": f"{emissions:.2f} kg CO2",
#                 "traffic_locations": traffic_locations[:5],  # Limit to 5 locations
#                 "weather_data": weather_data,
#                 "route_points": route_points  # Include points for mapping
#             })

#         return jsonify({"routes": routes})
#     except Exception as e:
#         return jsonify({"error": str(e)})


# if __name__ == "__main__":
#     app.run(debug=True)










# from flask import Flask, render_template, request, jsonify
# import requests
# from math import radians, sin, cos, sqrt, atan2

# app = Flask(__name__)

# # API Keys
# OPEN_WEATHER_API_KEY = "01fecea7c070babba3ef42c3cb86c9c2"
# TOMTOM_API_KEY = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
# GOOGLE_API_KEY = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"

# # Function to fetch weather forecast
# def get_weather_forecast(lat, lon):
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print(f"Weather API Error: {response.status_code}, {response.json()}")
#             return {"error": "Failed to fetch weather data"}
#     except Exception as e:
#         print(f"Weather API Exception: {str(e)}")
#         return {"error": str(e)}

# # Function to fetch traffic data
# def get_traffic_data(origin, destination):
#     url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={TOMTOM_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json().get("routes", [])
#         else:
#             print(f"Traffic API Error: {response.status_code}, {response.json()}")
#             return []
#     except Exception as e:
#         print(f"Traffic API Exception: {str(e)}")
#         return {"error": str(e)}

# # Function to reverse geocode and get city name
# def get_city_name(lat, lon):
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             data = response.json()
#             if data["status"] == "OK" and data["results"]:
#                 for component in data["results"][0]["address_components"]:
#                     if "locality" in component["types"]:  # Check for city/locality
#                         return component["long_name"]
#                 return data["results"][0]["formatted_address"]
#         print(f"Geocoding API Error: {response.json()}")
#         return "Unknown Location"
#     except Exception as e:
#         print(f"Geocoding API Exception: {str(e)}")
#         return "Error Fetching City Name"

# # Function to fetch weather data along the route every 100 km
# def get_weather_forecast_along_route(route_points):
#     weather_data = []
#     total_distance = 0
#     last_point = route_points[0]  # Initialize with the first point

#     for point in route_points:
#         # Calculate the distance from the last point
#         distance = calculate_distance(last_point, point)
#         total_distance += distance

#         # Fetch weather data for every 100 km
#         if total_distance >= 100:
#             weather = get_weather_forecast(point["latitude"], point["longitude"])
#             city_name = get_city_name(point["latitude"], point["longitude"])
#             weather_summary = weather.get("weather", [{}])[0].get("description", "Unknown")
#             weather_data.append({"location": city_name, "weather": weather_summary})
#             print(f"Weather Data Added: {city_name} - {weather_summary}")
#             total_distance = 0  # Reset after fetching weather
#         last_point = point  # Update last point

#     return weather_data

# # Function to calculate the distance between two points (Haversine formula)
# def calculate_distance(point1, point2):
#     R = 6371  # Radius of the Earth in km
#     lat1, lon1 = radians(point1["latitude"]), radians(point1["longitude"])
#     lat2, lon2 = radians(point2["latitude"]), radians(point2["longitude"])
#     dlat, dlon = lat2 - lat1, lon2 - lon1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     return R * c

# # Function to fetch traffic locations and reverse geocode
# def get_traffic_locations(points):
#     traffic_locations = []
#     for point in points[::100]:  # Sample every 100th point
#         location_name = get_city_name(point["latitude"], point["longitude"])
#         traffic_locations.append(location_name)
#     return traffic_locations

# @app.route("/")
# def home():
#     return render_template("index.html")

# @app.route("/optimize", methods=["POST"])
# def optimize():
#     try:
#         data = request.json
#         origin = data["origin"]
#         destination = data["destination"]
#         fuel_efficiency = float(data["fuel_efficiency"])
#         emission_factor = float(data["emission_factor"])

#         # Fetch traffic data for up to 3 routes
#         traffic_data = get_traffic_data(
#             f"{origin['lat']},{origin['lng']}",
#             f"{destination['lat']},{destination['lng']}"
#         )
#         if not traffic_data:
#             return jsonify({"error": "No traffic data available"})

#         routes = []
#         for idx, route in enumerate(traffic_data[:3]):  # Limit to 3 routes
#             route_summary = route.get("summary", {})
#             distance_km = route_summary.get("lengthInMeters", 0) / 1000
#             duration_sec = route_summary.get("travelTimeInSeconds", 0)
#             traffic_delay = route_summary.get("trafficDelayInSeconds", 0)
#             emissions = (distance_km / fuel_efficiency) * emission_factor

#             # Extract route points
#             route_points = [{"latitude": point["latitude"], "longitude": point["longitude"]}
#                             for leg in route.get("legs", [])
#                             for point in leg.get("points", [])]

#             # Get traffic locations
#             traffic_locations = get_traffic_locations(route_points)

#             # Fetch weather data for every 100 km
#             weather_data = get_weather_forecast_along_route(route_points)

#             routes.append({
#                 "route_index": idx + 1,
#                 "distance": f"{distance_km:.2f} km",
#                 "duration": f"{duration_sec // 3600} hours {duration_sec % 3600 // 60} mins",
#                 "traffic_delay": f"{traffic_delay // 60} mins" if traffic_delay > 0 else "No delay",
#                 "emissions": f"{emissions:.2f} kg CO2",
#                 "traffic_locations": traffic_locations[:5],  # Limit to 5 locations
#                 "weather_data": weather_data,
#                 "route_points": route_points  # Include points for mapping
#             })

#         return jsonify({"routes": routes})
#     except Exception as e:
#         print(f"Optimize Route Exception: {str(e)}")
#         return jsonify({"error": str(e)})


# if __name__ == "__main__":
#     app.run(debug=True)










# from flask import Flask, render_template, request, jsonify
# import requests
# from math import radians, sin, cos, sqrt, atan2

# app = Flask(__name__)

# # API Keys
# OPEN_WEATHER_API_KEY = "01fecea7c070babba3ef42c3cb86c9c2"
# TOMTOM_API_KEY = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
# GOOGLE_API_KEY = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"

# # Function to fetch weather forecast
# def get_weather_forecast(lat, lon):
#     url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json()
#         else:
#             print(f"Weather API Error: {response.status_code}, {response.json()}")
#             return {"error": "Failed to fetch weather data"}
#     except Exception as e:
#         print(f"Weather API Exception: {str(e)}")
#         return {"error": str(e)}

# # Function to fetch traffic data
# def get_traffic_data(origin, destination):
#     url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={TOMTOM_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             return response.json().get("routes", [])
#         else:
#             print(f"Traffic API Error: {response.status_code}, {response.json()}")
#             return []
#     except Exception as e:
#         print(f"Traffic API Exception: {str(e)}")
#         return {"error": str(e)}

# # Function to reverse geocode and get city name
# def get_city_name(lat, lon):
#     url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
#     response = requests.get(url)
#     try:
#         if response.status_code == 200:
#             data = response.json()
#             if data["status"] == "OK" and data["results"]:
#                 for component in data["results"][0]["address_components"]:
#                     if "locality" in component["types"]:  # Check for city/locality
#                         return component["long_name"]
#                 return data["results"][0]["formatted_address"]
#         print(f"Geocoding API Error: {response.json()}")
#         return "Unknown Location"
#     except Exception as e:
#         print(f"Geocoding API Exception: {str(e)}")
#         return "Error Fetching City Name"

# # Function to fetch weather data along the route every 100 km
# def get_weather_forecast_along_route(route_points):
#     weather_data = []
#     total_distance = 0
#     last_point = route_points[0]  # Initialize with the first point

#     for point in route_points:
#         # Calculate the distance from the last point
#         distance = calculate_distance(last_point, point)
#         total_distance += distance

#         # Fetch weather data for every 100 km
#         if total_distance >= 100:
#             weather = get_weather_forecast(point["latitude"], point["longitude"])
#             city_name = get_city_name(point["latitude"], point["longitude"])
#             if "weather" in weather and len(weather["weather"]) > 0:
#                 weather_summary = weather["weather"][0].get("description", "Unknown")
#             else:
#                 weather_summary = "Unknown"
#             weather_data.append({"location": city_name, "weather": weather_summary})
#             print(f"Weather Data Added: {city_name} - {weather_summary}")
#             total_distance = 0  # Reset after fetching weather
#         last_point = point  # Update last point

#     return weather_data

# # Function to calculate the distance between two points (Haversine formula)
# def calculate_distance(point1, point2):
#     R = 6371  # Radius of the Earth in km
#     lat1, lon1 = radians(point1["latitude"]), radians(point1["longitude"])
#     lat2, lon2 = radians(point2["latitude"]), radians(point2["longitude"])
#     dlat, dlon = lat2 - lat1, lon2 - lon1
#     a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
#     c = 2 * atan2(sqrt(a), sqrt(1 - a))
#     return R * c

# # Function to fetch traffic locations and reverse geocode
# def get_traffic_locations(points):
#     traffic_locations = []
#     for point in points[::100]:  # Sample every 100th point
#         location_name = get_city_name(point["latitude"], point["longitude"])
#         traffic_locations.append(location_name)
#     return traffic_locations

# @app.route("/")
# def home():
#     return render_template("index.html")

# # Function to fetch weather data along the route every 100 km
# def get_weather_forecast_along_route(route_points):
#     weather_data = []
#     total_distance = 0
#     last_point = route_points[0]  # Initialize with the first point

#     for point in route_points:
#         # Calculate the distance from the last point
#         distance = calculate_distance(last_point, point)
#         total_distance += distance

#         # Fetch weather data for every 100 km
#         if total_distance >= 100:
#             weather = get_weather_forecast(point["latitude"], point["longitude"])
#             city_name = get_city_name(point["latitude"], point["longitude"])
            
#             # Check if weather data is valid
#             if "weather" in weather and len(weather["weather"]) > 0:
#                 weather_summary = weather["weather"][0].get("description", "Unknown")
#             else:
#                 weather_summary = "No Data"

#             # Append weather data with city name
#             weather_data.append({"location": city_name, "weather": weather_summary})
#             print(f"Weather at {city_name}: {weather_summary}")  # Debugging log
#             total_distance = 0  # Reset after fetching weather
#         last_point = point  # Update last point

#     return weather_data

# # Update the optimize route function to include debugging logs
# @app.route("/optimize", methods=["POST"])
# def optimize():
#     try:
#         data = request.json
#         origin = data["origin"]
#         destination = data["destination"]
#         fuel_efficiency = float(data["fuel_efficiency"])
#         emission_factor = float(data["emission_factor"])

#         # Fetch traffic data for up to 3 routes
#         traffic_data = get_traffic_data(
#             f"{origin['lat']},{origin['lng']}",
#             f"{destination['lat']},{destination['lng']}"
#         )
#         if not traffic_data:
#             return jsonify({"error": "No traffic data available"})

#         routes = []
#         for idx, route in enumerate(traffic_data[:3]):  # Limit to 3 routes
#             route_summary = route.get("summary", {})
#             distance_km = route_summary.get("lengthInMeters", 0) / 1000
#             duration_sec = route_summary.get("travelTimeInSeconds", 0)
#             traffic_delay = route_summary.get("trafficDelayInSeconds", 0)
#             emissions = (distance_km / fuel_efficiency) * emission_factor

#             # Extract route points
#             route_points = [{"latitude": point["latitude"], "longitude": point["longitude"]}
#                             for leg in route.get("legs", [])
#                             for point in leg.get("points", [])]

#             # Get traffic locations
#             traffic_locations = get_traffic_locations(route_points)

#             # Fetch weather data for every 100 km
#             weather_data = get_weather_forecast_along_route(route_points)

#             routes.append({
#                 "route_index": idx + 1,
#                 "distance": f"{distance_km:.2f} km",
#                 "duration": f"{duration_sec // 3600} hours {duration_sec % 3600 // 60} mins",
#                 "traffic_delay": f"{traffic_delay // 60} mins" if traffic_delay > 0 else "No delay",
#                 "emissions": f"{emissions:.2f} kg CO2",
#                 "traffic_locations": traffic_locations[:5],  # Limit to 5 locations
#                 "weather_data": weather_data,
#                 "route_points": route_points  # Include points for mapping
#             })

#         return jsonify({"routes": routes})
#     except Exception as e:
#         print(f"Error in optimize function: {str(e)}")  # Debugging log
#         return jsonify({"error": str(e)})



# if __name__ == "__main__":
#     app.run(debug=True)
































from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# API Keys
OPEN_WEATHER_API_KEY = "01fecea7c070babba3ef42c3cb86c9c2"
TOMTOM_API_KEY = "NzorxSPM5oGMeLV4G8LCLXOgbTaj05mP"
GOOGLE_API_KEY = "AIzaSyCtG6ml7N5iNN6cPKOz5li8mjewsNxSiH0"

# Function to fetch weather forecast and city name
def get_weather_forecast(lat, lon):
    try:
        # Fetch weather data
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=metric"
        weather_response = requests.get(weather_url).json()

        # Fetch city name using reverse geocoding
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
        geocode_response = requests.get(geocode_url).json()
        city_name = "Unknown Location"
        if geocode_response["status"] == "OK" and geocode_response["results"]:
            city_name = geocode_response["results"][0]["formatted_address"]

        # Combine weather and city data
        weather_description = weather_response.get("weather", [{}])[0].get("description", "Unknown")
        return {"location": city_name, "weather": weather_description}
    except Exception as e:
        return {"location": "Error", "weather": str(e)}

# Function to fetch traffic data
def get_traffic_data(origin, destination):
    url = f"https://api.tomtom.com/routing/1/calculateRoute/{origin}:{destination}/json?traffic=true&key={TOMTOM_API_KEY}"
    response = requests.get(url)
    try:
        if response.status_code == 200:
            return response.json().get("routes", [])
        else:
            return []
    except Exception as e:
        return {"error": str(e)}

# Function to reverse geocode for traffic locations
def get_location_name(lat, lon):
    try:
        url = f"https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{lon}&key={GOOGLE_API_KEY}"
        response = requests.get(url).json()
        if response["status"] == "OK" and response["results"]:
            return response["results"][0]["formatted_address"]
        return "Unknown Location"
    except Exception as e:
        return "Error Fetching Location"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/optimize", methods=["POST"])
def optimize():
    try:
        data = request.json
        origin = data["origin"]
        destination = data["destination"]
        fuel_efficiency = float(data["fuel_efficiency"])
        emission_factor = float(data["emission_factor"])

        # Fetch traffic data for up to 3 routes
        traffic_data = get_traffic_data(
            f"{origin['lat']},{origin['lng']}",
            f"{destination['lat']},{destination['lng']}"
        )
        if not traffic_data:
            return jsonify({"error": "No traffic data available"})

        routes = []
        for idx, route in enumerate(traffic_data[:3]):  # Limit to 3 routes
            route_summary = route.get("summary", {})
            distance_km = route_summary.get("lengthInMeters", 0) / 1000
            duration_sec = route_summary.get("travelTimeInSeconds", 0)
            traffic_delay = route_summary.get("trafficDelayInSeconds", 0)
            emissions = (distance_km / fuel_efficiency) * emission_factor

            # Extract route points
            route_points = [{"latitude": point["latitude"], "longitude": point["longitude"]}
                            for leg in route.get("legs", [])
                            for point in leg.get("points", [])]

            # Get traffic locations
            traffic_locations = [get_location_name(point["latitude"], point["longitude"]) for point in route_points[::100]]

            # Fetch weather data for every 100 km
            weather_data = [get_weather_forecast(point["latitude"], point["longitude"]) for point in route_points[::100]]

            routes.append({
                "route_index": idx + 1,
                "distance": f"{distance_km:.2f} km",
                "duration": f"{duration_sec // 3600} hours {duration_sec % 3600 // 60} mins",
                "traffic_delay": f"{traffic_delay // 60} mins" if traffic_delay > 0 else "No delay",
                "emissions": f"{emissions:.2f} kg CO2",
                "traffic_locations": traffic_locations[:5],  # Limit to 5 locations
                "weather_data": weather_data,
                "route_points": route_points  # Include points for mapping
            })

        return jsonify({"routes": routes})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
