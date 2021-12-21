import pandas as pd
import pytest
from functions_data.data import read_csv,days_table_cover,departure_cities,relation_manufacter,db_path,haversine
# import data

@pytest.fixture(scope='module')
def df():
    path = 'C:/Users//Rev07/PycharmProjects/data2/test/file/flight.csv'
    df = pd.read_csv(path, sep='\t')
    return df


def test_read_csv():
     path='C:/Users/Rev07/PycharmProjects/data2/test/file/flight.csv'
     df = read_csv(path)
     expected = (3,1)
     assert df.shape == expected

def test_days_table_cover(df):
    expected = 3
    # Act
    result = days_table_cover(df)
    # Assert
    assert result.iloc[0][0] == expected

def test_departure_cities(df):
    expected = 3
    # Act
    result = departure_cities(df)
    # Assert
    assert result[0] == expected



def test_relation_manufacter(df):
    path2 = 'C:/Users/Rev07/PycharmProjects/data2/test/file/planes.csv'
    df2 = pd.read_csv(path2, sep='\t')
    expected = 105.0
    # Act
    result = relation_manufacter(df,df2)
    # Assert
    assert result[0] == expected



def test_db_path():
    expected = 'C:/Users/Rev07/Downloads/data/'
    assert db_path() == expected

def test_haversine():
    #Arrange
    path = 'C:/Users/Rev07/PycharmProjects/data2/test/file/airport.csv'
    df3 = pd.read_csv(path, sep='\t' )
    result = df3.copy()

    expected = 35.04022

    result['tmp'] = 1
    result = pd.merge(result, result, on='tmp')
    result = result[result.CITY_x != result.CITY_y]
    result['dist'] = result.apply(lambda row: haversine(row['LONGITUDE_x'],
                                              row['LATITUDE_x'],
                                              row['LONGITUDE_y'],
                                              row['LATITUDE_y']), axis=1)


    assert result.iloc[0][15] == expected















