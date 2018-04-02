# NBA Team Statistics Collector
import sqlite3
import json
from nba_py import team
from nba_py.constants import TEAMS

season = '2017-18'
team_ids = []

for k,v in TEAMS.items():
    team_ids.append(k)

def populate_teams():
    print('Retrieving team stats')
    conn = sqlite3.connect('../data/data_team.db')
    c = conn.cursor()

    c.execute('DELETE FROM teams') # remove old entries
    conn.commit()

    for team_id in team_ids:
        tid = TEAMS[team_id]['id']
        team_stats = dict(team.TeamSummary(tid, season).json)

        team_name = team_id 
        team_conf = team_stats['resultSets'][0]['rowSet'][0][5]
        team_wins = team_stats['resultSets'][0]['rowSet'][0][8]
        team_loss = team_stats['resultSets'][0]['rowSet'][0][9]
        team_pct = team_stats['resultSets'][0]['rowSet'][0][10]

        row = (team_name, team_conf, team_wins, team_loss, team_pct)
        c.execute('INSERT INTO teams VALUES (?,?,?,?,?)', row)
        conn.commit()

    conn.close()
    print('Done')

def populate_players():
    print('Retrieving players stats')
    conn = sqlite3.connect('../data/data_team.db')
    c = conn.cursor()

    c.execute('DELETE FROM players')
    conn.commit()

    for team_id in team_ids:
        tid = TEAMS[team_id]['id']
        player_stats = dict(team.TeamCommonRoster(tid, season).json)

        for player in player_stats['resultSets'][0]['rowSet']:
            num = player[4]
            name = player[3]
            pos = player[5]
            height = player[6]
            weight = player[7]

            row = (team_id, num, name, pos, height, weight)
            c.execute('INSERT INTO players VALUES (?,?,?,?,?,?)', row)
            conn.commit()

    conn.close()
    print('Done')

if __name__ == '__main__':
    populate_teams()
    populate_players()

