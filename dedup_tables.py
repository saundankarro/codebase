import sys
import re

##
#
#
#   Requirements:-
#       1) File with list of tables to parse (preferably txt)
#
#
#   Takes grep output file and outputs two files:
#       1) File with tables only
#       2) File with tables with db and schema info in {db}.{name}.{table} format
#
#
##

filename = sys.argv[1]

with open(filename) as file:
    match_list = []
    unmatch_list = []
    db_list = []
    db_no_match = []
    
    ### Replace schema1/SCHEMA1 in below try/except clauses with actual schema name.
    ### More names can be added using |
    ### ***REMEMBER TO USE LOWER CASE AND UPPER CASE OPTIONS FOR ALL SCHEMAS
    
    for line in file:
        try:
            
            ### First try/except clause searches for schema.table ONLY
            print(f"***************************************************")
            tbl_pattern = r"(schema1|SCHEMA1)([_\w+])+"
            match_line = re.search(tbl_pattern, line).group(0).lower()
            print(f"First Capture Suceeded")
            match_list.append(match_line)
            print(f"***************************************************")
        except Exception:
            print(f"Exception - Tabledoes not start with SCHEMA:-\n{line}")
            unmatch_list.append(line)
            print(f"***************************************************")
        
        try:
            
            ### Second try/except clause searches for db.schema.table ONLY
            print(f"***************************************************")
            print(f"line:- {line}")
            db_pattern = r"([a-zA-Z]{3-5}\.])+(schema1|SCHEMA1)([_\w+])+"
            print(f"db_pattern:- {db_pattern}")
            match_db = re.search(db_pattern, line)
            i = 0
            print(f"match_db:- {match_db}")
            if match_db != None:
                db_list.append(match_db.group(0).lower())
            print("db_list:- {db_list[-1]}")
            print(f"Second Capture Suceeded")
            print(f"***************************************************")
        except Exception as e:
            print(f"Line ({line}) has Exception:- {e}")
            db_no_match.append(line)
            print(f"***************************************************")

### Cleaning up db outputs - can add or remove as needed        
db_list = (s.replace('&','') for s in db_list)
db_list = (s.replace('{','') for s in db_list)
db_list = (s.replace('}','') for s in db_list)

db_list = (s.replace('schema1_db','schema1') for s in db_list)

print(f"***************************************************")
print(f"db_list was formatted")
print(f"***************************************************")

print(f"***************************************************")
### Sorts lists
db_list.sort()
match_list.sort()

print(f"Sorted lists")
print(f"***************************************************")

unique_tables = set(match_list)

unique_db = set(db_list)

del_ext = filename.replace('.txt','')
tbl_output = f"{del_ext}_tables.txt"
db_output = f"{del_ext}_db.txt"

with open(f"{tbl_output}", "w") as f:
    f.write(f"List of tables:- \n")
    for tables in unique_tables:
        f.write(f"{tables}\n")

print(f"Saved list of tables in {tbl_output}")


with open(f"{db_output}", "w") as f:
    f.write(f"List of db and schema:- \n")
    for db in unique_db:
        f.write(f"{db}\n")

print(f"Saved list of db and schema in {db_output}")
  