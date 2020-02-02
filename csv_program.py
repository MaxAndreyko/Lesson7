import csv


data = [['brand', 'model', 'fuel_cons', 'price'], ['Audi', 'A5', 20, 4500000]]

with open('example.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '&')
    writer.writerows(data)
print('Writing complete!')


with open('example.csv') as f:
    reader = csv.reader(f, delimiter = '&')
    for row in reader:
        print(row)