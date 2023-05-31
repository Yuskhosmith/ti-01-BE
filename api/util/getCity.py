from fuzzywuzzy import fuzz
import math, json, os
# To get the city and it's details - getCity does the job

def getCity(query, longitude=None, latitude=None):
    file_path = os.path.join(os.path.dirname(__file__), 'cities5000.txt')
    with open(file_path, 'r', encoding='utf8') as file:
        data = []
        for line in file:
            values = line.split('\t')
            if query in values[1]:
                lat = float({values[4]}.pop())
                lon = float({values[5]}.pop())
                out = {
                    "name": f"{values[1]}, {getDetails(values[8], values[10])}, {values[8]}",
                    "latitude": lat,
                    "longitude": lon,
                    "score": getScore(query, {values[1]}, lat, lon, latitude, longitude)
                }
                data.append(out)
    
    return sorted(data, key=lambda x: x['score'], reverse=True)
                

def getDetails(cc, ac):
    file_path = os.path.join(os.path.dirname(__file__), 'admin1CodesASCII.txt')
    with open(file_path, 'r', encoding='utf8') as file:
        for line in file:
            values = line.split('\t')
            if values[0] == f"{cc}.{ac}":
                return values[1]
            

def relevaceScore(query, city_name):
    score = fuzz.token_set_ratio(query, city_name) / 100.0
    return score

def proximityScore(city_latitude, city_longitude, caller_latitude, caller_longitude):
    lat_diff = city_latitude - caller_latitude
    lon_diff = city_longitude - caller_longitude

    # Using Pythagorean theorem and proximiity as the inverse of the distance
    # added one to the denominator to avoid zero division error
    proximity_score = 1 / (math.sqrt(lat_diff**2 + lon_diff**2) + 1)

    return proximity_score

def getScore(query, city_name, city_latitude, city_longitude, caller_latitude, caller_longitude):
    relevance = relevaceScore(query, city_name)
    if caller_latitude and caller_longitude:
        proximity = proximityScore(city_latitude, city_longitude, caller_latitude, caller_longitude)
    else:
        return relevance
    return (relevance + proximity)/2
