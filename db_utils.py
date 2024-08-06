from sqlalchemy import create_engine
def get_db_conn ():
    # Create a connection to the SQL database
    conn =create_engine('mssql+pyodbc://@DESKTOP-RVTL0C7/claim_analytics?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes')
    print('db has been connected succesfully')
    return conn

