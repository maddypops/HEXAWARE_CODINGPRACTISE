import csv
data = [['name','age'],
        ['Madhansai', '18'],
        ['Bob', '19'], ]
with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\hexa.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(data)
with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\hexa.csv",'r')as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)



data = [
    ['Name', 'Age', 'City'],
    ['A', 28, 'Boston'],
    ['B', 35, 'San Francisco']
]


with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\hexa.csv",'w', newline='') as file:
    csv_writer = csv.writer(file)


    csv_writer.writerows(data)


data = [
    ['Name', 'Age', 'City'],
    ['Alice', 28, 'Boston'],
    ['Bob', 35, 'San Francisco']
]


with open(r"C:\HEXAWARE\HEXAWARE-CODINGPRACTISE\hexa.csv",'w', newline='') as file:
    csv_writer = csv.writer(file)


    csv_writer.writerows(data)
    print(csv_writer)

