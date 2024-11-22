# data-mesh-bank-demo Release 1

This demo has some fake bank customer money transactions.

# streamlit

## Prerequisites
* Install snowflake connector
```
pip install snowflake-connector-python
```

* Install pandas for snowflake connector
```
pip install "snowflake-connector-python[pandas]"
```

* Install python-dotenv for snowflake connector
```
pip install python-dotenv
```

* Install streamlit
```
pip install streamlit
```

## Local run
* Set env variables in dbt/.env:

* cp ../dbt/.env ./

* Run 
```
streamlit run app.py
```
