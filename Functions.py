def swapFileData():
    file1 = input('enter file 1 : ')
    file2 = input('enter file 2 : ')
    with open(file1) as a:
        dataA=a.read()
    
    with open(file2) as a:
        dataB=a.read()
    
    with open(file1,'w') as a:
        a.write(dataB)
    
    with open(file2,'w') as b:
        b.write(dataA)

swapFileData()