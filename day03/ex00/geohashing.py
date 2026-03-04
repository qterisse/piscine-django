import sys
import antigravity

def main(latitude, longitude, datedow):
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except:
        print("Latitude and longitude need to be a float values")
        return
    
    try:
        datedow = datedow.encode("utf-8")
    except:
        print("Date needs to be a string")
        return
    
    antigravity.geohash(latitude, longitude, datedow)


if __name__ == "__main__":
    if (len(sys.argv) != 4):
        print("Correct usage is: python3 geoashing.py <latitude> <longitude> <datedow>")
        exit()
    
    main(sys.argv[1], sys.argv[2], sys.argv[3])