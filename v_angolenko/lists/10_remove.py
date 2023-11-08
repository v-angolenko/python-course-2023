# ```
# Тема: Видалення елемента зі списку.

# Завдання: У вас є список з назвою `softwareTools`,
# який містить елементи: ['Git', 'Docker', 'Jenkins', 'Kubernetes', 'Ansible'].
# Ваше завдання - видалити 'Jenkins' з цього списку. Використайте метод `remove()`
# для виконання цієї задачі. Після видалення елементу, виведіть оновлений список `softwareTools` на екран.

# Очікуваний результат: Коли ви виконаєте скрипт, у консолі має бути виведений список `softwareTools`
# без елемента 'Jenkins':
# ```
# ```
# ['Git', 'Docker', 'Kubernetes', 'Ansible']
# ```

tools = ['Git', 'Docker', 'Jenkins', 'Kubernetes', 'Ansible']
tools.remove('Jenkins')
print(tools)
