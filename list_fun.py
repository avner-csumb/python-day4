fave_video_games = ['Overwatch', 'League of Legends', 'Smash Bros']

# print(fave_video_games[0])
#
# print(fave_video_games[-1])

# print(fave_video_games[0:2])
#
# print(fave_video_games[1:3])

fave_video_games.append('Civ V')

# print(fave_video_games)

fave_video_games.append('Leisure Suit Larry')

# print(fave_video_games)

# del fave_video_games[4]
fave_video_games.remove('Leisure Suit Larry')

# print(fave_video_games)

anitas_games = ["Tony Hawk Pro Skater", "Street Fighter", "Sims", "Sim City", "Colore"]

fave_video_games.extend(anitas_games)

# print(fave_video_games)
# print(len(fave_video_games))
#
# for game in fave_video_games:
#     print('I really like ' + game + '.')


if 'Where in the World is Carmen San Diego' in fave_video_games:
    print('This is going to be a good list')
else:
    print('I hate this list, it is bad.')
