# execute ./script.sh
sqlite3 matchapp.db < schema.sql
# sqlite3 matchapp.db < data.sql
sqlite3 matchapp.db < InsertUserUS.sql
sqlite3 matchapp.db < InsertInterests.sql
sqlite3 matchapp.db <InsertActions.sql
sqlite3 matchapp.db <InsertLocations.sql