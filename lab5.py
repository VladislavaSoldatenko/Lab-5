import re
import csv

with open('task1-en.txt', 'r', encoding='utf-8') as file:
    content = file.read()

numbers = re.findall(r'\b\d+\.?\d*\b', content)
print("Найденные числа:", numbers)

words_6_8 = re.findall(r'\b\w{6}\b|\b\w{8}\b', content)
print("Слова из 6 и 8 букв:", words_6_8)
print()

with open('task2.html', 'r', encoding='utf-8') as file:
    content = file.read()

pattern = r'content="([^"]*)"'

matches = re.findall(pattern, content)

for match in matches:
    print(match)
print()

with open('task3.txt', 'r') as file:
    data = file.read()

id_pattern = re.compile(r'\b\d+\b')
surname_pattern = re.compile(r'\b[A-Z][a-z]+\b')
email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}')
date_pattern = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
url_pattern = re.compile(r'https?://[^\s]+')

ids = id_pattern.findall(data)
surnames = surname_pattern.findall(data)
emails = email_pattern.findall(data)
dates = date_pattern.findall(data)
urls = url_pattern.findall(data)

min_length = min(len(ids), len(surnames), len(emails), len(dates), len(urls))
ids = ids[:min_length]
surnames = surnames[:min_length]
emails = emails[:min_length]
dates = dates[:min_length]
urls = urls[:min_length]

table = list(zip(ids, surnames, emails, dates, urls))

with open('task3.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['ID', 'Surname', 'Email', 'Registration Date', 'Website'])
    writer.writerows(table)

print("Данные успешно сохранены в файл task3.csv")