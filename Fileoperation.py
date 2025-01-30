
# file read method

def readFile(filename):
    file=open(filename,'r')
    for name in file:
        print(name)
    file.close()
readFile('test.txt')

def readFile2(filename):
    with open(filename,'r') as file:
        
        while True:
            line=file.readline()
            if not line:
                break
            print(line)
            
def writeFile(filename, data):
    with open(filename, 'W') as file:
        file.write(data +'\n')
       
def appendFile(filename, data):
    with open(filename, 'a') as file:
        file.write(data +'\n')
appendFile('test.txt','Write to the file agian')
    
    