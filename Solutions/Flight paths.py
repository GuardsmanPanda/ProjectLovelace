from math import radians, sqrt, asin, sin, cos

def haversine_distance(lat1, lon1, lat2, lon2):
    lat1, lon1, lat2, lon2 = radians((lat1)), radians(lon1), radians(lat2), radians(lon2)
    inner = sin(lat2/2-lat1/2)**2 + cos(lat1)*cos(lat2)*sin(lon2/2-lon1/2)**2
    return 2 * 6372.1 * asin(sqrt(inner))


print(haversine_distance(46.283, 86.667, -48.877, -123.393))