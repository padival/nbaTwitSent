#https://nba-py.readthedocs.io/en/latest/team/
#https://stats.nba.com/scores/03/05/2018

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



#====== search for team id =======

#==template==
#from nba_py import player
#print (player.get_player("", last_name = ""))
#print(player.PlayerSummary("").info())

#from nba_py import team
#print(team.TeamSummary("", season = "2017-18").info())

#======== Eastern Conference ========
#print (player.get_player("DeMar", last_name = "DeRozan"))
#print(player.PlayerSummary("201942").info())
#raptor id = 1610612761

#from nba_py import player
#print (player.get_player("Kyrie", last_name = "Irving"))
#print(player.PlayerSummary("202681").info())
#celtics id = 1610612738

#print (player.get_player("LeBron", last_name = "James"))
#print(player.PlayerSummary("2544").info())
#cavaliers id = 1610612739

#print (player.get_player("Victor", last_name = "Oladipo"))
#print(player.PlayerSummary("203506").info())
#pacers id = 1610612754

#print (player.get_player("John", last_name = "Wall"))
#print(player.PlayerSummary("202322").info())
#wizards id = 1610612764

#========== Western Conference ========
from nba_py import player
#print (player.get_player("James", last_name = "Harden"))
#print(player.PlayerSummary("201935").info())
#rockets id = 1610612745

#print (player.get_player("Stephen", last_name = "Curry"))
#print(player.PlayerSummary("201939").info())
#warriors id = 1610612744

#print (player.get_player("Anthony", last_name = "Davis"))
#print(player.PlayerSummary("203076").info())
#pelicans id = 1610612740

#print (player.get_player("Damian", last_name = "Lillard"))
#print(player.PlayerSummary("203081").info())
#trail blazers id = 1610612757

#print (player.get_player("Derrick", last_name = "Rose"))
#print(player.PlayerSummary("201565").info())
#timberwolves id = 1610612750

# === team info (wins/losses) ====
from nba_py import team
print(team.TeamSummary("1610612761", season = "2017-18").info())

#print(team.TeamSummary("1610612738", season = "2017-18").info())

#print(team.TeamSummary("1610612739", season = "2017-18").info())

#print(team.TeamSummary("1610612754", season = "2017-18").info())

#print(team.TeamSummary("1610612764", season = "2017-18").info())

#print(team.TeamSummary("1610612745", season = "2017-18").info())

#print(team.TeamSummary("1610612744", season = "2017-18").info())

#print(team.TeamSummary("1610612740", season = "2017-18").info())

#print(team.TeamSummary("1610612757", season = "2017-18").info())

#print(team.TeamSummary("1610612750", season = "2017-18").info())


#
