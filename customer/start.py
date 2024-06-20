from data_generator.fake_data_generator import FakeDataGenerator
import pandas as pd
import os


sample_record_count = 100
fake_data_generator = FakeDataGenerator()
sample_data_df = fake_data_generator.generate_fake_data(sample_record_count)


# Task 1: Write CSV file containing first_name, last_name, address, date_of_birth
file_name = 'sample_source_data.csv'
data_folder = os.path.join(os.getcwd(),  'fake_data')
os.makedirs(data_folder, exist_ok=True)

file_path = os.path.join(data_folder, file_name)

sample_data_df.to_csv(file_path, index=False)
print(f"Source file CSV file successfully created:  '{file_path}' ")


# Task 2 : Load generated CSV in previous step, anomalise sare and output to a different file. 
# Columns to anonymise are first_name, last_name and address

source_data_df = pd.read_csv(file_path)
output_file = 'anonymised_data.csv'
output_file_path =  os.path.join(data_folder, output_file)


shuffle_columns = ['first_name' , 'last_name']
anonymised_df =  fake_data_generator.shuffle_columns(source_data_df, shuffle_columns)

# Uncomment below line to mask the date_of_birth column 
#mask_date_columns = ['date_of_birth']
#anonymised_df = fake_data_generator.mask_dates(anonymised_df, mask_date_columns)


mask_address_colunms = ['address']
anonymised_df = fake_data_generator.mask_address(anonymised_df, mask_address_colunms)


anonymised_df.to_csv(output_file_path, index=False)
print(f"Anonimised CSV file successfully created: '{output_file_path}' ")