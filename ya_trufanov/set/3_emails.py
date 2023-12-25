# 3. Напишіть функцію, яка приймає на вхід список електронних адрес
# і повертає перелік унікальних поштових серверів з цього переліку
# (множину всіх унікальних доменних імен, які зустрічаються в списку).


def get_unique_email(emails):
    mail_server = set()

    for email in emails:
        user_email, domain_name = email.split("@")

        mail_server.add(domain_name)

    return mail_server


emails = [
    "user_email1@gmail.com",
    "user2@catdog.com",
    "user3@example.com",
    "user_email4@example.com",
]

result = get_unique_email(emails)
print(result)
