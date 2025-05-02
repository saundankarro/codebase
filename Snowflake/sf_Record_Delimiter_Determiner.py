import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col
from snowflake.snowpark.files import SnowflakeFile
import pandas as pd
import csv

def main(session: snowpark.Session):
    file_loc = "location"
    
    csv_file = SnowflakeFile.open(file_location=csv_stg_url, mode='r', require_scoped_url=False)

    i = 0
    print(f"Printing the first 3 lines of the file\n")

    for line in csv_file:
        i+=1
        print(f"Printing line {i} of the file:- {line}\n")
        if i >= 3:
            break
    csv_file.seek(0)

    sniffer = csv.Sniffer()

    dialect = sniffer.sniff(csv_file.readline())
    header = sniffer.has_header(csv_stg_url)
    if dialect.delimiter == f"\t":
        dlmtr = 'tab'
    elif dialect.delimiter == f" ":
        dlmtr = 'space'
    else:
        dlmtr = dialect.delimiter
    print(f"Delimiter = {dlmtr}\n")
    print(f"Header = {header}\n")

    return print(f"Delimiter determined to be '{dlmtr}")