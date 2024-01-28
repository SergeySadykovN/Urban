'''Использование %'''
team1_num = 5
print("In the first team participate: %d participants" % team1_num)
team2_num = 6
print('Total participants: %d and %d = %d participants' % (team1_num, team2_num, team1_num + team2_num))

'''Использование .format()'''
score1 = 42
score2 = 42
total_score = score1 + score2
team1_time = 18015.2
team2_time = 17021.3
time_avr_per_task = (team1_time + team2_time) / total_score

print("The first team collect {} points, the second team collect {} points".format(score1, score2))
print('The first team collect {} points, in {}  sec.'.format(score1, team1_time))
print('The second team collect {} points, in {} sec.'.format(score2, team2_time))

'''Использование f-строк'''
if score1 > score2 or score1 == score2 and team1_time < team2_time:
    result = 'First team'
elif score1 < score2 or score1 == score2 and team1_time > team2_time:
    result = 'Second team'
else:
    result = 'Friendship!'

print(f'\nTournaments Results: \n'
      f'The winner is the {result}\n'
      f'Teams collect {score1} and {score2} points!\n'
      f'Total score {total_score}\n'
      f'Average time per task {time_avr_per_task:.2f} sec\n')

# форматирование вывода ширины полей
teams_dict = {'The winner is ': result,
              'number of participate first team:': team1_num,
              'number of participate second team:': team2_num,
              'points first team:': score1,
              'points second team:': score2,
              'total points: ': total_score,
              'average time per task': time_avr_per_task}

for key, value in teams_dict.items():
    print(f'{key:34}: {value}')

