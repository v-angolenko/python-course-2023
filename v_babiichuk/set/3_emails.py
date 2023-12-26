# 3. Напишіть функцію, яка приймає на вхід список електронних адрес
# і повертає перелік унікальних поштових серверів з цього переліку
# (множину всіх унікальних доменних імен, які зустрічаються в списку).
def unique_mail_servers(email_list):
    server_set = set()

    for email in email_list:
        _, domain = email.split('@', 1)
        server_set.add(domain)

    return server_set


print("Введіть електронні адреси. Або введіть порожній рядок для завершення.")

user_emails = []

while True:
    email = input("Введіть електронну адресу: ")
    if not email:
        break
    user_emails.append(email)

result = unique_mail_servers(user_emails)

print("Унікальні поштові сервери:", result)