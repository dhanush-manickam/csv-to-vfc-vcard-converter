import csv 
import os
with open('cont.csv', 'r') as contact:
    reader = csv.reader(contact)
    contact = list(reader)
# To unpack initial list in the contact
for initial in contact:
    first = initial[0].strip()
    second = initial[1].strip()
    numbers = initial[2].strip()
    number = int(numbers)
    with open('contact.txt', 'a+') as f:
        f.write('BEGIN:VCARD\n')
        f.write('VERSION:2.1\n')
        f.write(f'N:;{first}; {second};;\nFN:{first} {second}\nTEL;CELL:{number}\nEND:VCARD\n')
        print('finished converting...')
        print('converting to vcf...')
os.rename('contact.txt', 'contact.vcf')
print('converted to vcf')