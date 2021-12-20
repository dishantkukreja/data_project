import pandas as pd
import pytest
from functions_data.data import read_csv,days_table_cover,departure_cities,relation_manufacter,db_path
# import data

@pytest.fixture(scope='module')
def df():
    path = 'C:/Users//Rev07//PycharmProjects//data2//test//file//flight.csv'
    df = pd.read_csv(path, sep='\t')
    return df


def test_read_csv():
     path='C:/Users//Rev07//PycharmProjects//data2//test//file//flight.csv'
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
    path2 = 'C:/Users//Rev07//PycharmProjects//data2//test//file//planes.csv'
    df2 = pd.read_csv(path2, sep='\t')
    expected = 105.0
    # Act
    result = relation_manufacter(df,df2)
    # Assert
    assert result[0] == expected



def test_db_path():
    expected = 'C:/Users/Rev07/Downloads/data/'
    assert db_path() == expected
