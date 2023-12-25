# 3. Напишіть функцію, яка приймає на вхід список електронних адрес
# і повертає перелік унікальних поштових серверів з цього переліку
# (множину всіх унікальних доменних імен, які зустрічаються в списку).
def extract_mail_servers(emails):
    unique_servers = set()

    for email in emails:
        _, domain = email.split('@', 1)

        unique_servers.add(domain)

    return list(unique_servers)

email_list = ['user1@example.com', 'user2@gmail.com', 'user3@example.com', 'user4@yahoo.com']
result = extract_mail_servers(email_list)
print("Унікальні сервери електронних адрес:", result)
