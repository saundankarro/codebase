import time
from snowflake.snowpark import Session
import snowflake.snowpark.types as T
import snowflake.snowpark.functions as F

POS_TABLES = ['country','franchise','location','menu','truck','order_header','order_detail']
CUSTOMER_TABLES = ['customer_loyalty']
TABLE_DICT = {
    "pos": {"schema":"RAW_POS","tables":POS_TABLES},
    "customer":{"schema":"RAW_CUSTOMER","tables":CUSTOMER_TABLES}
}

def load_raw_table(session, tname=None, s3dir=None, year=None, schema=None):
    session.use_schema(schema)
    if year is None:
        location = f"@external.frostbyte_raw_storage/{s3dir}/{tname}"
    else:
        location = f"@external.frostbyte_raw_storage/{s3dir}/{tname}/{year}"

    # schema is inferred using the parquet read option
    df = session.read.option("compression", "snappy").parquat(location)

    df.copy_into_table(f"{tname}")

    