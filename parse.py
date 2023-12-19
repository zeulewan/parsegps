# Parsing the provided GPS coordinates

def parse_gps_coordinates(lat, lat_dir, lon, lon_dir):
    # Convert the latitude
    lat_deg = int(lat[:2])
    lat_min = float(lat[2:])
    lat_decimal = lat_deg + lat_min / 60

    # Convert the longitude
    lon_deg = int(lon[:3])
    lon_min = float(lon[3:])
    lon_decimal = lon_deg + lon_min / 60

    # Adjust for direction (N/S, E/W)
    if lat_dir == 'S':
        lat_decimal *= -1
    if lon_dir == 'W':
        lon_decimal *= -1
    return lat_decimal, lon_decimal

# Coordinates to parse
latitude = "4410.8910"
latitude_direction = "N"
longitude = "07646.5707"
longitude_direction = "W"

# Parsing
parsed_latitude, parsed_longitude = parse_gps_coordinates(latitude, latitude_direction, longitude, longitude_direction)
print(parsed_latitude, parsed_longitude)