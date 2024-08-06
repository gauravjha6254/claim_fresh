import os
from csv_utils import read_csv_file
file_path = r'D:\personal\GAURAV\Project\mma_claims\walmart_claims\walmart_claims_data.csv'
df= read_csv_file(file_path)
from db_utils import get_db_conn
db_conn= get_db_conn()
# Save the DataFrame into the "claims_data" table
df.to_sql('claims_data', db_conn, if_exists='append', index=False)
print("walmart data saved successfully into  table claims_data")