# This class is for generating fake data  

import pandas as pd
import numpy as np
import re
from  faker import Faker
import logging

class FakeDataGenerator:
    def __init__(self,):
        self.logger = logging.getLogger()
        self.faker = Faker()
        self.logger.info('FakeDataGenerator - object created')
        
    def generate_fake_data(self, sample_record_count):
        #  This function produces a dataframe with random values using faker
        #  Parameters: 
        #      sample_record_count : Number of records required in the ourput dataframe
        #      return: A pandas dataframe with four columns (first_name, last_name, address and date_of_birth)
        #              Data is populated with python package Faker 
        
        self.logger.info(f'Generating {sample_record_count} sample records')
        data = {
                "first_name": [self.faker.first_name() for f_name in range(sample_record_count)],
                "last_name": [self.faker.last_name() for l_name in range(sample_record_count)],
                "address": [self.faker.address().replace('\n', ',') for address in range(sample_record_count)],
                "date_of_birth": [self.faker.date_of_birth().isoformat() for dob in range(sample_record_count)]
                }
        pd_fake_data = pd.DataFrame(data)
        self.logger.info('Fake data generated in dataframe')
        return pd_fake_data
    
    
    def shuffle_columns(self, source_df, shuffle_columns):
        #  This function shuffles the data in column shuffle_column in the dataframe source_df
        #  Parameters: 
        #      source_df : pandas dataframe with source data
        #      shuffle_columns : list of columns  in  source_df where data is shuffled
        #      return: a pandas dataframe with same structure as source_df with data in coumn shuffle_column shuffled
        shuffled_df = source_df.copy()
        for column in shuffle_columns:
            shuffled_df.loc[: , column] = np.random.permutation(source_df[column])
            
        self.logger.info(f'Shuffled columns : {shuffle_columns}')
        
        return shuffled_df

    def mask_dates(self, source_df, mask_date_columns):
        #  This function maskes the date columns in the dataframe source_df by applying a random offset days
        #  Parameters: 
        #      source_df : pandas dataframe with source data
        #      mask_date_columns : list of date columns  in  source_df which should be masked
        #      return: a pandas dataframe with same structure as source_df with columns given are masked
        masked_df = source_df.copy()
        offset_days = np.random.randint(0, 200, size=len(masked_df))
        for column in mask_date_columns:
            #source_df[column] = (pd.to_datetime(source_df[column]) + pd.to_timedelta(offset_days, unit='D')).dt.strftime('%Y-%m-%d')
            masked_df.loc[: , column] = (pd.to_datetime(masked_df[column]) + pd.to_timedelta(offset_days, unit='D')).dt.strftime('%Y-%m-%d')
            
   
        return masked_df

    def mask_address(self, source_df, columns):
        #  This function maskes the string by replacing any digits in the string by * and replacing the first initial few characters with string
        #  Parameters: 
        #      source_df : pandas dataframe with source data
        #      columns : list of  columns  in  source_df which should be masked
        #      return: a pandas dataframe with same structure as source_df
        
        def mask(address):
            address_list =  re.sub(r'\d', '*', address).split(' ')
            self.logger.info (' '.join(address_list))
            if len(address_list) > 2:                
                address_list[-2] =  '*' * len(address_list[1])
                address = ' '.join(address_list)
            else:
                address = '*' * len(address)
            return address
        
        masked_df = source_df.copy()
        for column in columns:
            masked_df.loc[: , column] = masked_df[column].apply(mask)
            
        return masked_df   
    