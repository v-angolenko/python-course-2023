# 3. Напишіть функцію, яка приймає на вхід список електронних адрес
# і повертає перелік унікальних поштових серверів з цього переліку
# (множину всіх унікальних доменних імен, які зустрічаються в списку).


def unique_email(emails):
    domains = set()
    for email in emails:
        user_email, domain = email.split('@')
        domains.add(domain)
    return domains 


emails = ["email@gmail.com",
        "email@test.com",
        "email@example.com",
        "email@tempmail.com",]


result = unique_email(emails)
print(result)   





