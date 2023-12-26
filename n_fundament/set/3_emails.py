# 3. Напишіть функцію, яка приймає на вхід список електронних адрес
# і повертає перелік унікальних поштових серверів з цього переліку
# (множину всіх унікальних доменних імен, які зустрічаються в списку).

emails = ["work@gmail.com", "last@sadness.website", "im_coder@mail.ua.com"]

def get_unique_domains(emails: list[str]) -> set:
	domains = set()
	for email in emails:
		domains.add(email.split('@')[1])
	return domains

print(get_unique_domains(emails))