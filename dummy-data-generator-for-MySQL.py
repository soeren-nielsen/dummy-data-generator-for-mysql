# Importing libraries
import pandas as pd
from faker import Faker
from collections import defaultdict
from sqlalchemy import create_engine

# Initialize Faker instance
fake = Faker()

# Dictionary that creates key-value pairs that are not currently stored within dictionary when accessed
fake_data = defaultdict(list)

# Accesing methods from faker library
# Because defaultdict(list) is used, whenever a key is accessed we did not create, it will automatically be added with an empty list [] as its value.
for _ in range(1000):
    fake_data["first_name"].append(fake.first_name())
    fake_data["last_name"].append(fake.last_name())
    fake_data["occupation"].append(fake.job())
    fake_data["dob"].append(fake.date_of_birth())
    fake_data["country"].append(fake.country())

# The dictionary fake_data contains all the random data generated, but it needs to be packaged into the pandas dataframe
df_fake_data=pd.DataFrame(fake_data)

# Connecting to local database using sqlalchemy library
# Specify username, password and database
engine = create_engine('mysql://[user]:[password]@localhost/[database]', echo=False)

# Saves the pandas dataframe in the specified database and creates a new table called user
df_fake_data.to_sql('user', con=engine,index=False)
