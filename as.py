



# Read the contents of the file
with open(r'C:\Users\Dell\Desktop\da.txt', 'r', encoding='utf-8', errors='ignore') as file:
    sql_queries = file.read()

# Replace commas in the MinutesPlayed field
sql_queries_fixed = sql_queries.replace("','", "'"",").replace("','", "'"",")

# Write the fixed SQL queries back to the file
with open('fixed_insert_queries.txt', 'w', encoding='utf-8') as file:
    file.write(sql_queries_fixed)

print("Commas removed from MinutesPlayed field.")


