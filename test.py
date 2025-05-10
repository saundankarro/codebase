file_stg = '@db.schema.stg/folder/file.xlsx'

csv_nm = file_stg.split('.')[-2].split('/')[-1]
print(f"File Stage:- {file_stg}\ncsv_nm = {csv_nm}") 