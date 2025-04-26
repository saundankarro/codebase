import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import lit, current_date
from snowflake.snowpark.types import DataType
import pandas as pd
import numpy as np
import fsspec
import s3fs

'''
    Sample Code to read an Excel file from an external stage and write each sheet to a csv in the defined external stage
    Tested and confirmed with S3 while running the code on Snowflake's worksheets
'''

def main(session: snowpark.Session):

    # Sample file to read
    input_file = "test.xlsx"

    # Sample stage holding the input excel file. Does not need a folder to store, but included as example (based on permissions)
    input_stg = "@database.schema.input_stage/folder/"

    # Sample stage holding the output csv file.
    # Can also be stored in a folder within the stage
    # (i.e. if the stage points to an s3 bucket and the s3 bucket has sub-folders, then the stage can also access it, based on permissions)
    output_stg = "@database.schema.output_stg"

    file_stg = f"{input_stg}{input_file}"

    # Reading the excel file as a stream
    excel_file = pd.ExcelFile(session.file.get_stream(file_stg))

    # Getting a dataframe containing sheet names from the excel file
    sp_df = session.create_DataFrame(excel_file.sheet_names, schema=["Sheet Names"])
    sp_df = sp_df.to_pandas()
    
    # Creating an empty list to store the sheets read from the excel file
    sheet_list = []

    # Parsing through each sheet of the excel file
    for i in sp_df["Sheet Names"]:
        print(f"Reading in Sheet{i} from {input_file}\n")
        
        # Loading the data from the current sheet into a dataframe
        data_df = pd.read_excel(excel_file, sheet_name=i)
        print(f"Excel Dataframe Columns:-\n{data_df.columns}\n")

        # Creating a variable to store the csv name. 
        # Adding the sheet name to the end of the file name to write unique files
        csv_nm = input_file.split('.')[0]+'_'+i

        # Creating the output csv location, including the csv name
        # Extension is not needed
        output_csv = f"{output_stg}{csv_nm}"

        # Converting pandas dataframe to snowpark dataframe to write to the stage
        data_df = session.create_dataframe(data_df)

        # Writing the dataframe into csv
        # Header = True means the file has headers
        # Overwrite = True means to overwrite the file if it exists in output stage location
        # file_format = 'Sample_File_Format' provides a sample file format to follow when writing the csv
        # write.csv automatically provides the .csv extension, therefore .csv is not needed to include when defining the csv name earlier
        data_df.write.csv(output_csv, header=True, overwrite=True, file_format='Sample_File_Format')

        sheet_list.append(i)

    result = f"Successfully saved data from the following sheets of the {config_file_nm} to csv:"
    print(result)
    print('\n'.join(str(p) for p in sheet_list))

    return print(result)