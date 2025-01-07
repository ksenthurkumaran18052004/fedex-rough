// function initMap() {
//     // Initialize the map centered on a default location
//     const map = new google.maps.Map(document.getElementById('map'), {
//         center: { lat: 37.7749, lng: -122.4194 }, // Default location (San Francisco)
//         zoom: 13,
//         mapTypeControl: false,
//     });

//     // Create search boxes for origin and destination
//     const originInput = document.getElementById('origin-input');
//     const destinationInput = document.getElementById('destination-input');

//     const originAutocomplete = new google.maps.places.Autocomplete(originInput);
//     originAutocomplete.bindTo('bounds', map);

//     const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);
//     destinationAutocomplete.bindTo('bounds', map);

//     // Handle form submission
//     document.getElementById('route-form').addEventListener('submit', (e) => {
//         e.preventDefault();

//         const originPlace = originAutocomplete.getPlace();
//         const destinationPlace = destinationAutocomplete.getPlace();

//         if (!originPlace || !originPlace.geometry || !destinationPlace || !destinationPlace.geometry) {
//             alert("Please select valid origin and destination locations.");
//             return;
//         }

//         const originDetails = {
//             address: originPlace.formatted_address,
//             lat: originPlace.geometry.location.lat(),
//             lng: originPlace.geometry.location.lng(),
//         };

//         const destinationDetails = {
//             address: destinationPlace.formatted_address,
//             lat: destinationPlace.geometry.location.lat(),
//             lng: destinationPlace.geometry.location.lng(),
//         };

//         const fuelEfficiency = document.getElementById('fuel-efficiency').value;
//         const emissionFactor = document.getElementById('emission-factor').value;

//         // Send the data to the server
//         fetch('/optimize', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({
//                 origin: originDetails,
//                 destination: destinationDetails,
//                 fuel_efficiency: fuelEfficiency,
//                 emission_factor: emissionFactor,
//             }),
//         })
//             .then((response) => response.json())
//             .then((data) => {
//                 if (data.error) {
//                     alert(`Error: ${data.error}`);
//                 } else {
//                     console.log(data);
//                     alert(`Optimal Route Found!\nEmissions: ${data.emissions} kg CO2`);
//                 }
//             })
//             .catch((error) => {
//                 console.error('Error:', error);
//             });
//     });
// }

// // Initialize the map
// google.maps.event.addDomListener(window, 'load', initMap);
























// function initMap() {
//     // Initialize the map centered on a default location
//     const map = new google.maps.Map(document.getElementById('map'), {
//         center: { lat: 37.7749, lng: -122.4194 }, // Default location (San Francisco)
//         zoom: 7,
//         mapTypeControl: false,
//     });

//     // Create search boxes for origin and destination
//     const originInput = document.getElementById('origin-input');
//     const destinationInput = document.getElementById('destination-input');

//     const originAutocomplete = new google.maps.places.Autocomplete(originInput);
//     originAutocomplete.bindTo('bounds', map);

//     const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);
//     destinationAutocomplete.bindTo('bounds', map);

//     // Set up the Directions service and renderer
//     const directionsService = new google.maps.DirectionsService();
//     const directionsRenderer = new google.maps.DirectionsRenderer();
//     directionsRenderer.setMap(map);

//     // Handle form submission
//     document.getElementById('route-form').addEventListener('submit', (e) => {
//         e.preventDefault();

//         const originPlace = originAutocomplete.getPlace();
//         const destinationPlace = destinationAutocomplete.getPlace();

//         if (!originPlace || !originPlace.geometry || !destinationPlace || !destinationPlace.geometry) {
//             alert("Please select valid origin and destination locations.");
//             return;
//         }

//         const origin = originPlace.geometry.location;
//         const destination = destinationPlace.geometry.location;

//         // Request the directions and display them on the map
//         directionsService.route(
//             {
//                 origin: origin,
//                 destination: destination,
//                 travelMode: google.maps.TravelMode.DRIVING,
//             },
//             (result, status) => {
//                 if (status === google.maps.DirectionsStatus.OK) {
//                     directionsRenderer.setDirections(result);

//                     // Extract distance and duration
//                     const route = result.routes[0];
//                     const distance = route.legs[0].distance.value / 1000; // Convert meters to km
//                     const duration = route.legs[0].duration.text;

//                     // Display distance and duration in an alert
//                     alert(`Route distance: ${distance.toFixed(2)} km\nEstimated duration: ${duration}`);
//                 } else {
//                     alert("Directions request failed due to " + status);
//                 }
//             }
//         );
//     });
// }

// // Initialize the map
// google.maps.event.addDomListener(window, 'load', initMap);


































// function initMap() {
//     const map = new google.maps.Map(document.getElementById('map'), {
//         center: { lat: 37.7749, lng: -122.4194 }, // Default location (San Francisco)
//         zoom: 7,
//         mapTypeControl: false,
//     });

//     const originInput = document.getElementById('origin-input');
//     const destinationInput = document.getElementById('destination-input');

//     const originAutocomplete = new google.maps.places.Autocomplete(originInput);
//     originAutocomplete.bindTo('bounds', map);

//     const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);
//     destinationAutocomplete.bindTo('bounds', map);

//     const directionsService = new google.maps.DirectionsService();
//     const directionsRenderer = new google.maps.DirectionsRenderer();
//     directionsRenderer.setMap(map);

//     document.getElementById('route-form').addEventListener('submit', (e) => {
//         e.preventDefault();

//         const originPlace = originAutocomplete.getPlace();
//         const destinationPlace = destinationAutocomplete.getPlace();

//         if (!originPlace || !originPlace.geometry || !destinationPlace || !destinationPlace.geometry) {
//             alert("Please select valid origin and destination locations.");
//             return;
//         }

//         const originDetails = {
//             address: originPlace.formatted_address,
//             lat: originPlace.geometry.location.lat(),
//             lng: originPlace.geometry.location.lng(),
//         };

//         const destinationDetails = {
//             address: destinationPlace.formatted_address,
//             lat: destinationPlace.geometry.location.lat(),
//             lng: destinationPlace.geometry.location.lng(),
//         };

//         const fuelEfficiency = document.getElementById('fuel-efficiency').value;
//         const emissionFactor = document.getElementById('emission-factor').value;

//         fetch('/optimize', {
//             method: 'POST',
//             headers: {
//                 'Content-Type': 'application/json',
//             },
//             body: JSON.stringify({
//                 origin: originDetails,
//                 destination: destinationDetails,
//                 fuel_efficiency: fuelEfficiency,
//                 emission_factor: emissionFactor,
//             }),
//         })
//             .then((response) => response.json())
//             .then((data) => {
//                 if (data.error) {
//                     alert(`Error: ${data.error}`);
//                 } else {
//                     console.log(data);
//                     directionsRenderer.setDirections(data.optimal_route);
//                     alert(`Optimal Route Found!\nEmissions: ${data.emissions} kg CO2\nWeather: Rain (${data.weather_conditions.rain}) | AQI: ${data.weather_conditions.aqi}`);
//                 }
//             })
//             .catch((error) => {
//                 console.error('Error:', error);
//             });
//     });
// }

// google.maps.event.addDomListener(window, 'load', initMap);

























// function initMap() {
//     // Initialize the map
//     const map = new google.maps.Map(document.getElementById("map"), {
//         center: { lat: 13.0827, lng: 80.2707 }, // Default location (Chennai)
//         zoom: 7,
//     });

//     // Autocomplete inputs
//     const originInput = document.getElementById("origin-input");
//     const destinationInput = document.getElementById("destination-input");
//     const originAutocomplete = new google.maps.places.Autocomplete(originInput);
//     const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);

//     // Directions and Polyline
//     const directionsService = new google.maps.DirectionsService();
//     const directionsRenderer = new google.maps.DirectionsRenderer();
//     directionsRenderer.setMap(map);

//     const routePolyline = new google.maps.Polyline({
//         path: [],
//         strokeColor: "#FF0000",
//         strokeOpacity: 1.0,
//         strokeWeight: 3,
//     });
//     routePolyline.setMap(map);

//     document.getElementById("route-form").addEventListener("submit", (e) => {
//         e.preventDefault();

//         const originPlace = originAutocomplete.getPlace();
//         const destinationPlace = destinationAutocomplete.getPlace();

//         if (!originPlace || !originPlace.geometry || !destinationPlace || !destinationPlace.geometry) {
//             alert("Please select valid origin and destination locations.");
//             return;
//         }

//         const originDetails = {
//             lat: originPlace.geometry.location.lat(),
//             lng: originPlace.geometry.location.lng(),
//             address: originPlace.formatted_address,
//         };
//         const destinationDetails = {
//             lat: destinationPlace.geometry.location.lat(),
//             lng: destinationPlace.geometry.location.lng(),
//             address: destinationPlace.formatted_address,
//         };

//         const fuelEfficiency = document.getElementById("fuel-efficiency").value;
//         const emissionFactor = document.getElementById("emission-factor").value;

//         // Call the backend
//         fetch("/optimize", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({
//                 origin: originDetails,
//                 destination: destinationDetails,
//                 fuel_efficiency: fuelEfficiency,
//                 emission_factor: emissionFactor,
//             }),
//         })
//             .then((response) => response.json())
//             .then((data) => {
//                 if (data.error) {
//                     alert(`Error: ${data.error}`);
//                     return;
//                 }

//                 // Extract route points
//                 const routePoints = data.optimal_route.legs[0].points.map((point) => ({
//                     lat: point.latitude,
//                     lng: point.longitude,
//                 }));

//                 // Display route on the map
//                 routePolyline.setPath(routePoints);

//                 // Display results
//                 const summary = `
//                     <p><strong>Optimal Route Found!</strong></p>
//                     <p>Emissions: ${data.emissions.toFixed(2)} kg CO2</p>
//                     <p>Weather: Rain (${data.weather_conditions.rain}) | AQI: ${data.weather_conditions.aqi}</p>
//                 `;
//                 document.getElementById("results").innerHTML = summary;
//             })
//             .catch((error) => {
//                 console.error("Error:", error);
//             });
//     });
// }

// google.maps.event.addDomListener(window, "load", initMap);

























































// function initMap() {
//     const map = new google.maps.Map(document.getElementById("map"), {
//         center: { lat: 13.0827, lng: 80.2707 },
//         zoom: 7,
//     });

//     const originInput = document.getElementById("origin-input");
//     const destinationInput = document.getElementById("destination-input");
//     const originAutocomplete = new google.maps.places.Autocomplete(originInput);
//     const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);

//     document.getElementById("route-form").addEventListener("submit", (e) => {
//         e.preventDefault();

//         const originPlace = originAutocomplete.getPlace();
//         const destinationPlace = destinationAutocomplete.getPlace();
//         const fuelEfficiency = document.getElementById("fuel-efficiency").value;
//         const emissionFactor = document.getElementById("emission-factor").value;

//         if (!originPlace || !destinationPlace) {
//             alert("Please select valid origin and destination.");
//             return;
//         }

//         fetch("/optimize", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({
//                 origin: {
//                     lat: originPlace.geometry.location.lat(),
//                     lng: originPlace.geometry.location.lng(),
//                 },
//                 destination: {
//                     lat: destinationPlace.geometry.location.lat(),
//                     lng: destinationPlace.geometry.location.lng(),
//                 },
//                 fuel_efficiency: fuelEfficiency,
//                 emission_factor: emissionFactor,
//             }),
//         })
//             .then((response) => response.json())
//             .then((data) => {
//                 if (data.error) {
//                     alert(`Error: ${data.error}`);
//                     return;
//                 }

//                 const resultsDiv = document.getElementById("results");
//                 resultsDiv.innerHTML = "";
//                 data.routes.forEach((route, index) => {
//                     resultsDiv.innerHTML += `
//                         <h3>Route ${index + 1}</h3>
//                         <p>Distance: ${route.distance}</p>
//                         <p>Duration: ${route.duration}</p>
//                         <p>Traffic Delay: ${route.traffic_delay}</p>
//                         <p>Weather: ${route.weather_summary}</p>
//                         <p>Emissions: ${route.emissions}</p>
//                         <p>Traffic Locations: ${route.traffic_locations.join(", ")}</p>
//                     `;
//                 });
//             })
//             .catch((error) => {
//                 console.error("Error:", error);
//             });
//     });
// }

// google.maps.event.addDomListener(window, "load", initMap);


















































// function initMap() {
//     const map = new google.maps.Map(document.getElementById("map"), {
//         center: { lat: 13.0827, lng: 80.2707 },
//         zoom: 7,
//     });

//     const directionsService = new google.maps.DirectionsService();
//     const directionsRenderers = [
//         new google.maps.DirectionsRenderer({ polylineOptions: { strokeColor: "#FF0000" } }),
//         new google.maps.DirectionsRenderer({ polylineOptions: { strokeColor: "#00FF00" } }),
//         new google.maps.DirectionsRenderer({ polylineOptions: { strokeColor: "#0000FF" } }),
//     ];

//     directionsRenderers.forEach((renderer) => renderer.setMap(map));

//     const originInput = document.getElementById("origin-input");
//     const destinationInput = document.getElementById("destination-input");
//     const originAutocomplete = new google.maps.places.Autocomplete(originInput);
//     const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);

//     document.getElementById("route-form").addEventListener("submit", (e) => {
//         e.preventDefault();

//         const originPlace = originAutocomplete.getPlace();
//         const destinationPlace = destinationAutocomplete.getPlace();
//         const fuelEfficiency = document.getElementById("fuel-efficiency").value;
//         const emissionFactor = document.getElementById("emission-factor").value;

//         if (!originPlace || !destinationPlace) {
//             alert("Please select valid origin and destination.");
//             return;
//         }

//         fetch("/optimize", {
//             method: "POST",
//             headers: { "Content-Type": "application/json" },
//             body: JSON.stringify({
//                 origin: {
//                     lat: originPlace.geometry.location.lat(),
//                     lng: originPlace.geometry.location.lng(),
//                 },
//                 destination: {
//                     lat: destinationPlace.geometry.location.lat(),
//                     lng: destinationPlace.geometry.location.lng(),
//                 },
//                 fuel_efficiency: fuelEfficiency,
//                 emission_factor: emissionFactor,
//             }),
//         })
//             .then((response) => response.json())
//             .then((data) => {
//                 if (data.error) {
//                     alert(`Error: ${data.error}`);
//                     return;
//                 }

//                 const resultsDiv = document.getElementById("results");
//                 resultsDiv.innerHTML = "";

//                 data.routes.forEach((route, index) => {
//                     const routeDetails = `
//                         <h3>Route ${index + 1}</h3>
//                         <p>Distance: ${route.distance}</p>
//                         <p>Duration: ${route.duration}</p>
//                         <p>Traffic Delay: ${route.traffic_delay}</p>
//                         <p>Emissions: ${route.emissions}</p>
//                         <p>Traffic Locations: ${route.traffic_locations.join(", ")}</p>
//                         <p>Weather Data:</p>
//                         <ul>
//                             ${route.weather_data
//                                 .map((weather) => `<li>${weather.location}: ${weather.weather}</li>`)
//                                 .join("")}
//                         </ul>
//                     `;
//                     resultsDiv.innerHTML += routeDetails;

//                     // Display the route on the map
//                     const routePath = route.route_points.map(
//                         (point) => new google.maps.LatLng(point.latitude, point.longitude)
//                     );
//                     directionsRenderers[index].setDirections({
//                         routes: [
//                             {
//                                 legs: [{ start_location: routePath[0], end_location: routePath.slice(-1)[0] }],
//                                 overview_path: routePath,
//                             },
//                         ],
//                     });
//                 });
//             })
//             .catch((error) => {
//                 console.error("Error:", error);
//             });
//     });
// }

// google.maps.event.addDomListener(window, "load", initMap);



































// function initMap() {
//     // Initialize the map
//     const map = new google.maps.Map(document.getElementById("map"), {
//         center: { lat: 13.0827, lng: 80.2707 }, // Default location (Chennai)
//         zoom: 7,
//     });

//     const originInput = document.getElementById("origin-input");
//     const destinationInput = document.getElementById("destination-input");
//     const originAutocomplete = new google.maps.places.Autocomplete(originInput);
//     const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);

//     document.getElementById("route-form").addEventListener("submit", async (e) => {
//         e.preventDefault();

//         const originPlace = originAutocomplete.getPlace();
//         const destinationPlace = destinationAutocomplete.getPlace();
//         const fuelEfficiency = document.getElementById("fuel-efficiency").value;
//         const emissionFactor = document.getElementById("emission-factor").value;

//         if (!originPlace || !destinationPlace) {
//             alert("Please select valid origin and destination.");
//             return;
//         }

//         const requestData = {
//             origin: {
//                 lat: originPlace.geometry.location.lat(),
//                 lng: originPlace.geometry.location.lng(),
//             },
//             destination: {
//                 lat: destinationPlace.geometry.location.lat(),
//                 lng: destinationPlace.geometry.location.lng(),
//             },
//             fuel_efficiency: fuelEfficiency,
//             emission_factor: emissionFactor,
//         };

//         try {
//             const response = await fetch("/optimize", {
//                 method: "POST",
//                 headers: { "Content-Type": "application/json" },
//                 body: JSON.stringify(requestData),
//             });

//             const data = await response.json();
//             if (data.error) {
//                 alert(`Error: ${data.error}`);
//                 return;
//             }

//             const resultsDiv = document.getElementById("results");
//             resultsDiv.innerHTML = "";

//             // Create separate directions renderers for each route
//             const colors = ["#FF0000", "#00FF00", "#0000FF"]; // Colors for the routes
//             data.routes.forEach((route, index) => {
//                 resultsDiv.innerHTML += `
//                     <h3>Route ${index + 1}</h3>
//                     <p>Distance: ${route.distance}</p>
//                     <p>Duration: ${route.duration}</p>
//                     <p>Traffic Delay: ${route.traffic_delay}</p>
//                     <p>Weather Data: ${route.weather_summary}</p>
//                     <p>Emissions: ${route.emissions}</p>
//                     <p>Traffic Locations: ${route.traffic_locations.join(", ")}</p>
//                 `;

//                 // Plot route on the map
//                 const directionsService = new google.maps.DirectionsService();
//                 const directionsRenderer = new google.maps.DirectionsRenderer({
//                     map,
//                     polylineOptions: {
//                         strokeColor: colors[index],
//                         strokeWeight: 4,
//                     },
//                     suppressMarkers: false,
//                 });

//                 const waypoints = route.traffic_locations.map((location) => ({
//                     location,
//                     stopover: false,
//                 }));

//                 directionsService.route(
//                     {
//                         origin: requestData.origin,
//                         destination: requestData.destination,
//                         waypoints,
//                         travelMode: google.maps.TravelMode.DRIVING,
//                         provideRouteAlternatives: true,
//                     },
//                     (result, status) => {
//                         if (status === google.maps.DirectionsStatus.OK) {
//                             directionsRenderer.setDirections(result);
//                         } else {
//                             console.error("Directions request failed due to", status);
//                         }
//                     }
//                 );
//             });
//         } catch (error) {
//             console.error("Error:", error);
//         }
//     });
// }

// google.maps.event.addDomListener(window, "load", initMap);

































function initMap() {
    const map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 13.0827, lng: 80.2707 },
        zoom: 7,
    });

    const directionsRenderers = [
        new google.maps.Polyline({ strokeColor: "#FF0000", strokeWeight: 4, map }),
        new google.maps.Polyline({ strokeColor: "#00FF00", strokeWeight: 4, map }),
        new google.maps.Polyline({ strokeColor: "#0000FF", strokeWeight: 4, map }),
    ];

    const originInput = document.getElementById("origin-input");
    const destinationInput = document.getElementById("destination-input");
    const originAutocomplete = new google.maps.places.Autocomplete(originInput);
    const destinationAutocomplete = new google.maps.places.Autocomplete(destinationInput);

    document.getElementById("route-form").addEventListener("submit", (e) => {
        e.preventDefault();

        const originPlace = originAutocomplete.getPlace();
        const destinationPlace = destinationAutocomplete.getPlace();
        const fuelEfficiency = document.getElementById("fuel-efficiency").value;
        const emissionFactor = document.getElementById("emission-factor").value;

        if (!originPlace || !destinationPlace) {
            alert("Please select valid origin and destination.");
            return;
        }

        fetch("/optimize", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                origin: {
                    lat: originPlace.geometry.location.lat(),
                    lng: originPlace.geometry.location.lng(),
                },
                destination: {
                    lat: destinationPlace.geometry.location.lat(),
                    lng: destinationPlace.geometry.location.lng(),
                },
                fuel_efficiency: fuelEfficiency,
                emission_factor: emissionFactor,
            }),
        })
            .then((response) => response.json())
            .then((data) => {
                if (data.error) {
                    alert(`Error: ${data.error}`);
                    return;
                }

                const resultsDiv = document.getElementById("results");
                resultsDiv.innerHTML = "";

                data.routes.forEach((route, index) => {
                    const routePath = route.route_points.map(
                        (point) => new google.maps.LatLng(point.latitude, point.longitude)
                    );
                    directionsRenderers[index].setPath(routePath);

                    const routeDetails = `
                        <h3>Route ${index + 1}</h3>
                        <p>Distance: ${route.distance}</p>
                        <p>Duration: ${route.duration}</p>
                        <p>Traffic Delay: ${route.traffic_delay}</p>
                        <p>Emissions: ${route.emissions}</p>
                        <p>Traffic Locations: ${route.traffic_locations.join(", ")}</p>
                        <p>Weather Data:</p>
                        <ul>
                            ${route.weather_data
                                .map((weather) => `<li>${weather.location}: ${weather.weather}</li>`)
                                .join("")}
                        </ul>
                    `;
                    resultsDiv.innerHTML += routeDetails;
                });
            })
            .catch((error) => {
                console.error("Error:", error);
            });
    });
}

google.maps.event.addDomListener(window, "load", initMap);
