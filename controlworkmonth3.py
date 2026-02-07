# ### **Добавить сохранение истории в файл**

history = []

try:
    with open('history.txt', 'r', encoding='utf8') as file:
        history = file.read().splitlines()
except FileNotFoundError:
    history = []


print('История посещения:')
for line in  history:
    print(line)  
print("-" * 10)

name = input('enter name: ')
greeting = f'Приветствую, {name}!'
history.append(greeting)
print(greeting)

with open('history.txt', 'a', encoding='utf8') as file:
    file.write(greeting + '\n')  





# ### **4. Добавить ограничение по длине истории **

greetings_history = []

for i in range(10):
    greeting = f'Приветствеий! {i+1}'
    greetings_history.append(greeting)


    greetings_history = greetings_history[-5:]

    print(f'Текущий история: {greetings_history}')








