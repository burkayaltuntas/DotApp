import dota2api
import time
'''
Learn about installing dota2api: https://dota2api.readthedocs.io/en/latest/installation.html
and get your D2_API_KEY from valve: https://steamcommunity.com/dev/apikey
'''
key="API KEY WILL BE HERE"
api = dota2api.Initialise(key)

def GetMatches(matchSeqNum):
    matchList = list()
    for i in range(0,400):
        matchHistory = api.get_match_history_by_seq_num(matchSeqNum) #this gets 100 match everytime * 400 = 40000 i checked here.
        matchList += matchHistory["matches"]
        lastMatchSeqNum = matchList[-1]["match_seq_num"]
        matchSeqNum = lastMatchSeqNum
        time.sleep(10) #dota api have time limits for requests so...
    return matchList

seqNum = "STARTING GAME SEQUENCE NUMBER AS INT"
matchList = GetMatches(seqNum)

listOfWinnerTeamHeroes = list()

for match in matchList:
    players = match["players"]
    winnerTeamPlayers = list()
    if match["radiant_win"]: 
        for player in players:
            if player["player_slot"] in [0,1,2,3,4]: #radiant heroes slot numbers declared by dota 2 api
                winnerTeamPlayers.append(player["hero_id"])
    else:
        for player in players:
            if int(player["player_slot"]) in [128,129,130,131,132]: #dire heroes slot numbers declared by dota 2 api
                winnerTeamPlayers.append(player["hero_id"])

    listOfWinnerTeamHeroes.append(sorted(winnerTeamPlayers,key=int))



for i in listOfWinnerTeamHeroes:
    if len(i) == 5:
        howManyTimesThisHeroSetPicked = listOfWinnerTeamHeroes.count(i)
        if howManyTimesThisHeroSetPicked > 1: #writing it to console is not the best way to see
            print(i)
            print(howManyTimesThisHeroSetPicked)



