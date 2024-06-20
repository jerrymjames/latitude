import pandas as pd
import numpy as np
import pytest
import datetime

from data_generator.fake_data_generator import FakeDataGenerator

print('start')

fakeDataGenerator = FakeDataGenerator ()

def test_generate_fake_data ():
    # check for correct column_names
    sample_record_count = 2
    sample_data_df = fakeDataGenerator.generate_fake_data(sample_record_count)
    expected_columns = {'first_name': str, 'last_name': str, 'address': str, 'date_of_birth': datetime.date}
    actual_columns = sample_data_df.columns
    
    assert set(expected_columns) == set(actual_columns)

    # check for correct record count
    assert sample_data_df.shape[0] == sample_record_count

def test_shuffle_columns():
    # this test checkes whether the values in the given columns are shuffled and the order of record values are changed

    sample_record_count = 10
    sample_data_df = fakeDataGenerator.generate_fake_data(sample_record_count)

    columns_to_be_shuffled = ['first_name','last_name']
    anonymised_df =  fakeDataGenerator.shuffle_columns(sample_data_df, columns_to_be_shuffled)
    print(sample_data_df)
    print('-----------------test_shuffle_columns--------------------')
    print(anonymised_df)
    print('----------------------------------------------------')

    # Ensure that dataframe shape is not changes
    assert sample_data_df.shape == anonymised_df.shape

    # Ensure that the column value is retained and order is not retained. Order of elements doesnt matter for set

    assert set(sample_data_df['first_name']) == set(anonymised_df['first_name'])

    # ensure that the order is not retained i.e data is shuffled '. Order of elements does  matter for array
    assert not np.all(sample_data_df['first_name'] == anonymised_df['first_name'] )


def test_mask_dates():
    sample_record_count = 5
    sample_data_df = fakeDataGenerator.generate_fake_data(sample_record_count)

    date_columns_to_be_masked = ['date_of_birth']
    anonymised_df =  fakeDataGenerator.mask_dates(sample_data_df, date_columns_to_be_masked)
    print('------------------test_mask_dates------------------------')
    print(sample_data_df)
    print('----------------------------------------------------')
    print(anonymised_df)

    # compare shape
    assert sample_data_df.shape == anonymised_df.shape

    # compare columns
    assert all(sample_data_df.columns == anonymised_df.columns)

    # compare data . values for date_of_birth should be changes
    assert not np.all(sample_data_df['date_of_birth'] == anonymised_df['date_of_birth'] )

    # ensure that all columns except date_of_birth are not changed
    assert (sample_data_df.loc[:,['first_name','last_name','address']]).equals(anonymised_df.loc[:,['first_name','last_name','address']])

def test_mask_address():
    sample_data_df = pd.DataFrame({'first_name': ['William', 'Lindsey', 'Philip'],
                                    'last_name': ['Rodriguez', 'Holland','Roberson'],
                                    'address':["85237 Rodriguez Fork Suite 263,Brianside, NE 60362", "36457 Abigail Pass,South Betty, OR 08423", "Unit9059Box1270DPOAE87647"] ,
                                    'date_of_birth':['1908-08-02','2019-01-03','1957-10-19']})
    
    expected_masked_data_df = sample_data_df = pd.DataFrame({'first_name': ['William', 'Lindsey', 'Philip'],
                                    'last_name': ['Rodriguez', 'Holland','Roberson'],
                                    'address':["***** Rodriguez Fork Suite ***,Brianside, ********* *****", "***** Abigail Pass,South Betty, ******* *****", "*************************"] ,
                                    'date_of_birth':['1908-08-02','2019-01-03','1957-10-19']})

    address_columns_to_be_masked = ['address']
    actual_anonymised_df =  fakeDataGenerator.mask_address(sample_data_df, address_columns_to_be_masked)
    print('------------------test_mask_address------------------------')
    print('expected_masked_data_df')
    print(expected_masked_data_df['address'])
    print('----------------------------------------------------')
    print('actual_anonymised_df')
    print(actual_anonymised_df['address'])
    # ensure that actual anomalised data is matching with expected
    assert expected_masked_data_df.equals(actual_anonymised_df)
    



