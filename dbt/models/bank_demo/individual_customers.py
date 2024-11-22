from snowflake.snowpark.functions import col
from snowflake.snowpark import Row
from faker import Faker

def model(dbt, session):
    dbt.config(
        packages = ["faker==8.8.1"]
    )
     
    fake = Faker("en_US")
    Faker.seed(12345)
    
    raw_accounts = dbt.source("raw", "raw_accounts")
    cust_ids = raw_accounts.select(raw_accounts.col("customer_id")).collect()
    individuals = []
    
    for row in cust_ids:
        print(f"Row: {row}")
        individual_row = Row(customer_id=row['CUSTOMER_ID'], full_name=fake.name(), country_of_birth='US', 
                             birth_date=fake.date_between(start_date='-60y'), gender=fake.random_element(('F', 'M')), 
                             social_security_number=fake.ssn(), state=fake.random_element(('NY', 'VT', 'LA')), city=fake.city(), address=fake.street_address(),
                             zip=fake.postcode())
        individuals.append(individual_row)
    
    final_df = session.create_dataframe(individuals)
    
    return final_df