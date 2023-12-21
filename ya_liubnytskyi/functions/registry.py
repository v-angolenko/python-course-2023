# Тема: Реєстрація користувачів на заході
# Завдання: Напишіть функцію `register_user`, яка запитує у користувача його ім'я та email,
# а потім додає цю інформацію до словника `user_registry`.
#
# Ключем у словнику повинен бути email, а значенням - ім'я користувача.
# Створіть другу функцію `display_users`, яка виводить список всіх зареєстрованих користувачів.
# Організуйте цикл, в якому користувач може ввести декілька разів команду 'register' для реєстрації або 'display'
# для відображення зареєстрованих користувачів. Цикл завершується, коли користувач вводить 'exit'.

# Очікуваний результат: Якщо користувач вводить 'register',
# вказує своє ім'я та email, а потім вводить 'display',
# програма виводить список усіх зареєстрованих користувачів.

# Послідовність виконання:
# 1. Визначте функцію `register_user`, яка запитує ім'я та email користувача та додає ці дані
# до словника `user_registry`.
# 2. Визначте функцію `display_users` для виводу інформації про зареєстрованих користувачів.
# 3. Організуйте головний цикл, який читає команди від користувача ('register', 'display', 'exit').
# 4. Використовуйте умовні оператори для визначення дій, які потрібно виконати в залежності від введеної команди.


user_registry = {}


def register_user():
    user_name = input("Введіть ім'я: ")
    user_email = input("Введіть email: ")
    user_registry[user_email] = user_name
    return user_registry


def display_users(): 
    if not user_registry:
        print("Реєстр користувачів порожній.")
    else:
        print("Реєстр користувачів:")
        for email,name in user_registry.items():
            print(f"Email: {email}, Ім'я :{name}")
            
            
    
  
  
while True:
 user_input = input("Введіть команду (register, display, exit): ")
 if user_input == "register":
    register_user()

 elif user_input == "display":
      display_users()   
      
 elif user_input == "exit":
     break
 
 else:
     print("Доступні команди: register, display, exit.: ")
