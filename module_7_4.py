team1_num = 6
team2_num = 6
score1 = 40
score2 = 42
team1_time = 1552.512
team2_time = 2153.31451

# Выполнено задач всего
tasks_total = score1 + score2

# Среднее время на задачу
time_avg = (team1_time + team2_time) / tasks_total

# Расчет победителя
if score1 > score2 or score1 == score2 and team1_time > team2_time:
    ch_result = 'победа команды "Мастера Кода"'
elif score1 < score2 or score1 == score2 and team1_time < team2_time:
    ch_result = 'победа команды "Волшебники Данных"'
else:
    ch_result = 'ничья'

# Использование %
print('В комнде "Мастера Кода" участников: %s' % team1_num)
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

# Использование format()
print('Команда "Волшебники Данных" решила задач: {}!'.format(score2))
print('Мастера Кода решили задачаи за: {} секнуды.'.format(team1_time))

# Использование f-строк
print(f'Команды решили {score1} и {score2} задач!')
print(f'Результат битвы - {ch_result}!')
print(f'Сегодня было решено {tasks_total}, в среднем по {time_avg} секунды на задачу')