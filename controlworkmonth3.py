import flet as ft

def main(page: ft.Page):
    page.title = 'приветствия'

    try:
        with open('history.txt', 'r', encoding='utf-8') as f:
            history = f.readlines()
            
    except FileNotFoundError:
        history = []

    old_history = ft.Text(''.join(history))

    name_input = ft.TextField(label='Имя пользователя')

    def greeting(e):
            name = name_input.value
            if not name:
                 return
            
            new_greeting = f'Привет, {name}!\n'


            history.append(new_greeting)

            if len(history) > 5:
                 history[:] = history[-5:]

            with open('history.txt', 'w', encoding='utf-8') as f:
                f.writelines(history)
              
                
            old_history.value = ''.join(history)
            name_input.value = ''

            page.update()

    name_input.on_submit = greeting


    batton = ft.ElevatedButton('Поприветствовать', on_click=greeting)

    page.add(
        old_history,
        name_input,
        batton
    )


        
ft.app(target=main)







