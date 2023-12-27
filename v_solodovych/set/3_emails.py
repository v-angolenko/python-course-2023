# 3. Напишіть функцію, яка приймає на вхід список електронних адрес
# і повертає перелік унікальних поштових серверів з цього переліку
# (множину всіх унікальних доменних імен, які зустрічаються в списку).

def server_collector(emails):
    server_set = set()
    temp = None
    counter = 0
    
    for _ in emails:
        temp = emails[counter].split('@')
        server_set.add(temp[1])
        counter += 1

    return server_set

emails_list = ['qwert2000@ukr.net', 'lazylow@gmail.com', 'sethome@i.ua', 'micha2003@gmail.com']
server_list = list(server_collector(emails_list))

print(server_list)