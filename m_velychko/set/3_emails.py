# 3. Напишіть функцію, яка приймає на вхід список електронних адрес
# і повертає перелік унікальних поштових серверів з цього переліку
# (множину всіх унікальних доменних імен, які зустрічаються в списку).

def unique_mail_servers(emails):  
    
    unique_servers = set()

    for email in emails:

        domain = email.split('@')[1]

        unique_servers.add(domain)

    return list(unique_servers)
email_list = ["user1@edu.ugi.ua", "user2@edu.ugi.ua", "user3@example.com", "user4@gmail.com"]

result = unique_mail_servers(email_list)

print("Унікальні поштові сервери:", result)