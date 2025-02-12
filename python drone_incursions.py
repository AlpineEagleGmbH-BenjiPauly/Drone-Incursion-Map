import folium

# List of drone incursion locations with updated details
locations = [
    # Military Bases
    {"type": "Military Bases", "name": "Schwesing Airbase, Germany", "lat": 54.5200, "lon": 9.1400, "details": "Six drone sightings in January 2025 over Patriot system training site"},
    {"type": "Military Bases", "name": "Ramstein Air Base, Germany", "lat": 49.4369, "lon": 7.6000, "details": "Multiple unauthorized drones observed; varied in size and configuration"},
    {"type": "Military Bases", "name": "Manching Air Base, Germany", "lat": 48.7569, "lon": 11.4900, "details": "Up to 10 drones spotted over Eurofighter jet development site"},
    {"type": "Military Bases", "name": "Wright-Patterson AFB, Ohio, USA", "lat": 39.8278, "lon": -84.0483, "details": "Airspace closed due to advanced drones disrupting operations"},
    {"type": "Military Bases", "name": "Vandenberg Space Force Base, California", "lat": 34.7483, "lon": -120.5522, "details": "Chinese national arrested for flying drone into restricted airspace"},
    {"type": "Military Bases", "name": "Camp Pendleton, California", "lat": 33.3189, "lon": -117.3536, "details": "Sophisticated drones suspected of surveillance; disrupted operations"},
    {"type": "Military Bases", "name": "Picatinny Arsenal, New Jersey", "lat": 40.9444, "lon": -74.5297, "details": "11 unauthorized drone flights confirmed over military R&D site"},
    {"type": "Military Bases", "name": "Naval Weapons Station Earle, New Jersey", "lat": 40.2964, "lon": -74.0614, "details": "Drones observed near ammunition storage; FBI investigation ongoing"},
    {"type": "Military Bases", "name": "Langley AFB, Virginia", "lat": 37.0821, "lon": -76.3605, "details": "Repeated swarm activity near F-22 fighter jet facilities"},
    {"type": "Military Bases", "name": "Hill AFB, Utah", "lat": 41.1236, "lon": -111.9731, "details": "Drones spotted near base; no confirmed overflights"},
    {"type": "Military Bases", "name": "RAF Lakenheath, UK", "lat": 52.4098, "lon": 0.5610, "details": "F-15E jets scrambled to investigate drones near nuclear-capable base"},
    {"type": "Military Bases", "name": "RAF Mildenhall/Feltwell, UK", "lat": 52.3636, "lon": 0.4860, "details": "Drones monitored by US/UK forces; no operators identified"},
    {"type": "Military Bases", "name": "RAF Fairford, UK", "lat": 51.6833, "lon": -1.7833, "details": "Bomber Task Force base targeted; drones disrupted flight operations"},
    
    # Sports Events
    {"type": "Sports Events", "name": "M&T Bank Stadium, Baltimore", "lat": 39.2779, "lon": -76.6227, "details": "NFL game paused in January 2024 after drone flew near play"},
    {"type": "Sports Events", "name": "Paris Olympics 2024", "lat": 48.8566, "lon": 2.3522, "details": "Canadian soccer teams sanctioned for spying via drones"},
    {"type": "Sports Events", "name": "UEFA Champions League Final 2023", "lat": 41.0082, "lon": 28.9784, "details": "Drone disrupted match; neutralized with counter-drone tech"},
    {"type": "Sports Events", "name": "Tokyo Olympics 2021", "lat": 35.6895, "lon": 139.6917, "details": "Unauthorized drones near venues prompted counter-drone measures"},
    {"type": "Sports Events", "name": "US Open 2015", "lat": 40.7498, "lon": -73.8476, "details": "Drone crashed into stadium seating, disrupting play"},
    {"type": "Sports Events", "name": "Levi’s Stadium & Oakland Coliseum", "lat": 37.4033, "lon": -121.9700, "details": "Anti-media leaflets dropped on NFL crowds via drone (2017)"},
    
    # Airports
    {"type": "Airports", "name": "Riga International Airport", "lat": 56.9236, "lon": 23.9711, "details": "Multiple disruptions in 2023/2025 due to drones in restricted airspace"},
    {"type": "Airports", "name": "Stockholm Arlanda Airport", "lat": 59.6519, "lon": 17.9186, "details": "Flights halted for two hours in September 2024"},
    {"type": "Airports", "name": "Frankfurt Airport", "lat": 50.0379, "lon": 8.5622, "details": "Near misses with commercial aircraft in December 2024"},
    
    # Critical Infrastructure
    {"type": "Critical Infrastructure", "name": "Brunsbüttel Chemical Park", "lat": 53.8895, "lon": 9.1372, "details": "Suspected espionage via drones over sensitive facilities (Summer 2024)"},
    {"type": "Critical Infrastructure", "name": "New Jersey Reservoirs & Rail Stations", "lat": 40.0583, "lon": -74.4057, "details": "Drones spotted over water/energy infrastructure (Late 2024)"},
    
    # Prisons
    {"type": "Prisons", "name": "Collins Bay Institution, Canada", "lat": 44.2473, "lon": -76.5711, "details": "Contraband deliveries via drones detected (Early 2023)"},
    {"type": "Prisons", "name": "South Carolina Prisons", "lat": 33.8361, "lon": -81.1637, "details": "Drones used for smuggling drugs/weapons (Early 2023)"},
    
    # Borders
    {"type": "Borders", "name": "Rio Grande Valley Sector", "lat": 26.1906, "lon": -98.1553, "details": "25,000+ cartel-linked drone sightings in one year"},
    {"type": "Borders", "name": "India-Pakistan Border", "lat": 32.1877, "lon": 75.0000, "details": "Arms/narcotics smuggling via drones (2023-2024)"},
    
    # Residential Areas
    {"type": "Residential Areas", "name": "New York & New Jersey", "lat": 41.0000, "lon": -72.0000, "details": "\"Car-sized\" drone swarms observed over neighborhoods (Late 2024)"}
]

# Create a map centered to include global locations
m = folium.Map(location=[40, 0], zoom_start=3)

# Define marker colors based on location type
color_map = {
    "Military Bases": "red",
    "Sports Events": "orange",
    "Airports": "blue",
    "Critical Infrastructure": "green",
    "Prisons": "purple",
    "Borders": "darkred",
    "Residential Areas": "cadetblue"
}

# Add markers to the map
for loc in locations:
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=f"<b>{loc['name']}</b><br>{loc['details']}",
        icon=folium.Icon(color=color_map.get(loc["type"], "gray"), icon="info-sign")
    ).add_to(m)

# Save the map to an HTML file
m.save("drone_incursions_map.html")

print("Map has been generated and saved as 'drone_incursions_map.html'. Open this file in a browser to view it.")
