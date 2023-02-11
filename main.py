from pprint import pprint
import re
from itertools import groupby
import csv

with open("phonebook_raw.csv", "r", encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  contacts_list.sort()

phonebook = []
check = []
count = 0
re_exp = r'(\+7|8)?\s*?\(?(\d{3})\)?[\s*-]?(\d{3})[\s*-]?(\d{2})[\s*-]?(\d{2})[\s,]?\(?(доб.)?\s?(\d{4})?\)?'

for i in contacts_list:
  contact = []
  str_fio = ' '.join(i)
  fio = str_fio.split(' ', 3)
  str = ':'.join(i)
  info = str.split(':')
  contact.append(fio[0])
  contact.append(fio[1])
  contact.append(fio[2])
  contact.append(info[3])
  contact.append(info[4])
  contact.append(info[5])
  contact.append(info[6])
  sub = r'+7(\2)\3-\4-\5 \6\7'
  contact[5] = re.sub(re_exp, sub, contact[5])
  # print(contact[5])
  if count > 0:
    if contact[0] == check[0] and contact[1] == check[1]:
      # print(check)
      # print(contact)
      if check[2] not in contact[2]:
        contact.insert(2, check[2])
      if check[3] not in contact[3]:
        contact.insert(3, check[3])
      if check[4] not in contact[4]:
        contact.insert(4, check[4])
      if check[5] not in contact[5]:
        contact.insert(5, check[5])
      if check[6] not in contact[6]:
        contact.insert(6, check[6])
      # print(f' If true append {contact}')
      check.clear()
      check.extend(contact)
      phonebook.pop()
      phonebook.append(contact)
    else:
      # print(f' Else append {contact}')
      check.clear()
      check.extend(contact)
      phonebook.append(contact)
  else:
    check.clear()
    check.extend(contact)
    phonebook.append(contact)
  count = count + 1

pprint(phonebook)

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(phonebook)