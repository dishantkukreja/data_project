import pandas as pd
from math import radians, cos, sin, asin, sqrt
import logging
import os


def read_csv(path: str):
    return pd.read_csv(path)

def days_table_cover(df):
    return df.groupby(['year'], sort=True).sum()

def departure_cities(flight):
    count = flight[["origin"]]
    city =(count.value_counts())
    return city

def relation_manufacter(flight,planes):
    relation = flight.merge(planes, how='inner', on=['tailnum', 'year'])
    most_delay = relation.groupby(['manufacturer'], sort=True).sum().sort_values("dep_delay", ascending=False)
    return most_delay['dep_delay']

def db_path():
    current_file = os.path.abspath(os.path.dirname(__file__))
    csv_filename = 'C:/Users/Rev07/Downloads/data/'
    return os.path.join(current_file, csv_filename)

def haversine(lon1, lat1, lon2, lat2):

    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r



def main():
    # current_file = os.path.abspath(os.path.dirname(__file__))
    # csv_filename = 'C:/Users/Rev07/Downloads/data/'
    # absolute_path = os.path.join(current_file, csv_filename)
    flight_csv = 'flights.csv'
    planes_csv = 'planes.csv'
    airports_csv = 'airports.csv'
    df_path = db_path()

    flight = read_csv(f"{df_path}{flight_csv}")
    planes = read_csv(f"{df_path}{planes_csv}")
    airport = read_csv(f"{df_path}{airports_csv}")
    b = airport.copy()
    logger = logging.getLogger(__name__)

    print(days_table_cover(flight))

    print("5291016 days in the flights table covers")

    print(departure_cities(flight))

    print("EWR, JFK,LGA are departure cities in the flight database covers")

    print(relation_manufacter(flight, planes).head(1))

    print("BOEING is the airplane manufacturer incurred the most delays in the analysis period")

    b['tmp'] = 1
    b = pd.merge(b, b, on='tmp')
    b = b[b.CITY_x != b.CITY_y]
    b['dist'] = b.apply(lambda row: haversine(row['LONGITUDE_x'],
                                              row['LATITUDE_x'],
                                              row['LONGITUDE_y'],
                                              row['LATITUDE_y']), axis=1)
    b = b[b.dist < 500] #distance between 500 km
    # df1 = b.groupby('CITY_x')['CITY_y'].apply(list)
    df2 = b.groupby('CITY_x')['CITY_y'].size()
    connected = (df2.sort_values(ascending=False))
    print(connected.head(2))

    print("Chicago and New York are the two most connected cities between 500 distance km")


if __name__ == '__main__':
    main()
