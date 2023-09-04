import csv 
import os
# Opening the csv file into python
# Make sure csv file is in the same folder and named as "cont.csv"
with open('cont.csv', 'r') as contact:
    reader = csv.reader(contact)
    contact = list(reader)
# To unpack initial list in the contact
for initial in contact:
    # unpacking the values and assigning it appropriate variables
    first = initial[0].strip()
    second = initial[1].strip()
    numbers = initial[2].strip()
    number = int(numbers)
    # creating and appending the file format
    with open('contact.txt', 'a+') as f:
        # standard vcard 2.1 format
        f.write('BEGIN:VCARD\n')
        f.write('VERSION:2.1\n')
        f.write(f'N:;{first}; {second};;\nFN:{first} {second}\nTEL;CELL:{number}\nEND:VCARD\n')
        print('finished converting...')
        print('converting to vcf...')
        # renaming the extension of the created file to vcf
os.rename('contact.txt', 'contact.vcf')
# Done!
print('converted to vcf')
