players = { 
    "Matt": { "password" : "2312", "cards": ["5", "4", "3"] }
}
cards = []

# user = input("Enter Username: ")
# password = input("Enter Password: ")
# players[user] = {}
# players[user]['password'] = password
# players[user]['cards'] = []

print(players.get('Matt').get('cards'))




# if 'Braydon' in (players.keys()):
#     print('User Exists')
# else:
#     print('User does not Exist')











# for key in players:
#     # print(key)
#     if(user == key):
#         if(password == players[key].get("password")):
#             print("access granted")
#             while True:
#                 print("Current hand: " + str(players[key].get("cards")));
#                 isPlaying = input("Would you like to play card?(Y or N)\n")
#                 if(isPlaying == "Y"):
#                     print("player playing card")
#                     break
#                 else:
#                     print("Player not playing card")
#                     break
#         else:
#             print("access denied")
#         break

