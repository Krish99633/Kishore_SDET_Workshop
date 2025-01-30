import csv

def readDataFrom(filename):
    with open(filename,'r') as file:
        reader = csv.reader(file)
        for data in reader:
            print(data)
            readDataFrom('Data.csv')
#read Data from CSV

def writeDataToCSV(filename):
    with open(filename,'w',newline='') as file:
        writer = csv.writer(file)
        data =[
            ['Name','Age','City'],
            ['Kishore','29','Chennai'],
            ['Kedhar','2','Chennai'],
            ['Yamuna','29','Chennai']
        ]
        header = ['Name','Age','City']
        for row in data:
            writer.writerow(row)
writeDataToCSV('Data.csv')

'''
def writeDataToCSVDict(filename):
    with open(filename,'w',newline='') as file:
        header = ['Name','Age','City']
        writer = csv.DictWriter(file, fieldnames=header)
        data = [
           {'Name':'Kishore1','Age':'29','City':'Chennai'},
           {'Name':'Kedhar1','Age':'2','City':'Chennai'},
           {'Name':'Yamuna1','Age':'29','City':'Chennai'}
        ]
        writer.writeheader()
        for row in data:
            writer.writerow(row)
writeDataToCSVDict('Data.csv')
'''
'''
# Reading text file and updating it in CSV
def readDataFromTxt(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            name, age, city = line.strip().split(',')
            data.append({'Name': name, 'Age': age, 'City': city})
    return data

def writeDataToCSVDict(data, filename):
    with open(filename, 'w', newline='') as file:
        header = ['Name', 'Age', 'City']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

# Read data from text file
data = readDataFromTxt('test.txt')

# Write data to CSV file
writeDataToCSVDict(data, 'Data.csv')
'''

def readDataFromTxt(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split(',')
            if len(values) == 3:
                name, age, city = values
                data.append({'Name': name, 'Age': age, 'City': city})
            else:
                print(f"Skipping line: {line.strip()} (incorrect format)")
    return data

def writeDataToCSVDict(data, filename):
    with open(filename, 'w', newline='') as file:
        header = ['Name', 'Age', 'City']
        writer = csv.DictWriter(file, fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

data = readDataFromTxt('test.txt')

writeDataToCSVDict(data, 'data1.csv')
            