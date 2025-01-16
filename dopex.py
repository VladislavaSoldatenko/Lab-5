import re

with open('task_add.txt', 'r', encoding='utf-8') as file:
    content = file.read()

date_pattern = r'\s\d{1,2}[-/.]\d{1,2}[-/.]\d{2,4}|\s\d{4}[-/.]\d{1,2}[-/.]\d{1,2}'
email_pattern = r'\s[\w\.-]+@[\w\.-]+'
url_pattern = r'\shttps?://[^\s]+'

dates = re.findall(date_pattern, content)
emails = re.findall(email_pattern, content)
urls = re.findall(url_pattern, content)

print("Найденные даты:")
for date in dates:
    print(date.strip())

print("\nНайденные email:")
for email in emails:
    print(email.strip())

print("\nНайденные URL:")
for url in urls:
    print(url.strip())