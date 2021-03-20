def File1 ():    
    file1 = open (input("PLease enter the right name of the file"))
    readFile1 = file1.readlines()
    count = 0
    
    for line in readFile1:
        words = line.split()
        count = count+len(words)
    print(count)


DummyLine = "Python is a language, I am learning it, my name is Ayushman"
print (DummyLine.split(","))
File1()
