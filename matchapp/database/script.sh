# execute ./script.sh
sqlite3 matchapp/database/matchapp.db < matchapp/database/schema.sql
# sqlite3 matchapp.db < data.sql
sqlite3 matchapp/database/matchapp.db < matchapp/database/InsertUserUS.sql
sqlite3 matchapp/database/matchapp.db < matchapp/database/InsertInterests.sql
sqlite3 matchapp/database/matchapp.db <matchapp/database/InsertActions.sql
sqlite3 matchapp/database/matchapp.db <matchapp/database/InsertLocations.sql