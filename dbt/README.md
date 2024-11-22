# bank_demo

## Local setup

1. pip install dbt-core==1.7.3
2. pip install re_data==0.10.9
3. pip install dbt-snowflake==1.7.1

## Install dbt plugins
dbt deps

## Local env check
1. Create a .env file in dbt directory contains credentials to connect to snowflake:
```
DBT_ACCOUNT=
DBT_ENV_SECRET_USER_DEV=
DBT_ENV_SECRET_PASSWORD_DEV=
DBT_DB_ROLE_DEV=
DBT_DB_DEV=
DBT_WH_DEV=
DBT_SCHEMA_DEV=
```
2. source setup_env.sh
3. dbt debug --profiles-dir=config

## Load data from csv
dbt seed --profiles-dir=config 

## Build models
dbt run --select package:bank_demo --profiles-dir=config

## Generate re_data for some time period
re_data run --profiles-dir config --start-date 2023-10-10 --end-date 2023-10-11

## Run tests
dbt test --select package:bank_demo --profiles-dir=config

## Generate dbt docs
dbt docs generate -t snowflake --profiles-dir=config

## DBT docs UI
dbt docs serve --profiles-dir config

## Generate re_data docs for some time period
re_data overview generate --profiles-dir=config --start-date 2023-10-10  --interval days:1

## re_data UI
re_data overview serve


## Resources:
- Learn more about dbt [in the docs](https://docs.getdbt.com/docs/introduction)
- Check out [Discourse](https://discourse.getdbt.com/) for commonly asked questions and answers
- Join the [chat](https://community.getdbt.com/) on Slack for live discussions and support
- Find [dbt events](https://events.getdbt.com) near you
- Check out [the blog](https://blog.getdbt.com/) for the latest news on dbt's development and best practices


