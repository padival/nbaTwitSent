#====== Team ID's =======

#   === East ===
#raptor id = 1610612761
#celtics id = 1610612738
#cavaliers id = 1610612739
#pacers id = 1610612754
#wizards id = 1610612764

#   === West ===
#rockets id = 1610612745
#warriors id = 1610612744
#pelicans id = 1610612740
#trail blazers id = 1610612757
#timberwolves id = 1610612750

# === team info (wins/losses) ====
#from nba_py import team
#print(team.TeamSummary("1610612761", season = "2017-18").info())

#print(team.TeamSummary("1610612738", season = "2017-18").info())

#print(team.TeamSummary("1610612739", season = "2017-18").info())

#print(team.TeamSummary("1610612754", season = "2017-18").info())

#print(team.TeamSummary("1610612764", season = "2017-18").info())

#print(team.TeamSummary("1610612745", season = "2017-18").info())

#print(team.TeamSummary("1610612744", season = "2017-18").info())

#print(team.TeamSummary("1610612740", season = "2017-18").info())

#print(team.TeamSummary("1610612757", season = "2017-18").info())

#print(team.TeamSummary("1610612750", season = "2017-18").info())

import sqlite3

sqlite_file = 'stats_db2.sqlite'    # name of the sqlite database file
table_name = 'team_stats'   # name of the table to be created
id_column = 'team_id' # name of the PRIMARY KEY column
name_column = 'team_name'  # name of team name column
wins_column = 'team_wins'  # name of wins column
losses_column = 'team_losses'   #name of losses column
column_type = 'TEXT' # E.g., INTEGER, TEXT, NULL, REAL, BLOB
default_val = 'This is a new column' # a default value for the new column rows
field_type = 'INTEGER'  # column data type
default_null = 'NULL'

from nba_py import team
#print(team.TeamGeneralSplits("1610612761", season = "2017-18").wins_losses())
raptor_wins_losses = team.TeamSummary("1610612761", season = "2017-18").info()
#raptor_wins_losses = team.TeamSummary("1610612761", season = "2017-18").season_ranks()
#raptor_wins_losses = team.TeamGeneralSplits(1610612761).wins_losses()
print(raptor_wins_losses)

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

#c.execute("UPDATE {tn} SET {cn}=(raptor_wins_losses) WHERE {idf}=(1610612761)".\
#          format(tn=table_name, cn=wins_column, idf=id_column))

"""try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (1610612761, 'Raptors')".\
              format(tn=table_name, idf=id_column, cn=name_column))
except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))"""

"""
# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
          .format(tn=table_name, nf=id_column, ft=field_type))


# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
          .format(tn=table_name, cn=name_column, ct=column_type))

# B) Adding a wins column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
          .format(tn=table_name, cn=wins_column, ct=column_type))

# B) Adding a losses column with a default row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
          .format(tn=table_name, cn=losses_column, ct=column_type))"""

# A) Inserts an ID with a specific value in a second column
"""try:
    c.execute("INSERT INTO {tn} ({idf}, {cn}) VALUES (1610612761, 'Raptors')".\
    format(tn=table_name, idf=id_column, cn=name_column))
    except sqlite3.IntegrityError:
    print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))"""


# B) Tries to insert an ID (if it does not exist yet)
# with a specific value in a second column
#c.execute("INSERT OR IGNORE INTO {tn} ({idf}, {cn}) VALUES (1610612738, 'Celtics')".\
#          format(tn=table_name, idf=id_column, cn=name_column))

# C) Updates the newly inserted or pre-existing entry
#c.execute("UPDATE {tn} SET {cn}=('52') WHERE {idf}=(1610612761)".\
#          format(tn=table_name, cn=wins_column, idf=id_column))

#c.execute("UPDATE {tn} SET {cn}=('18') WHERE {idf}=(1610612761)".\
#          format(tn=table_name, cn=losses_column, idf=id_column))

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()

#http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
