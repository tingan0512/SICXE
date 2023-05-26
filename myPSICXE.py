while 1:   
    fun,doc= input("<SICXE>").split()
    def LOAD(doc):
        f = open(doc,'r')
        line = f.read()
        f.close()
        return line

    def LIST(name):
        print(name)


    if (fun=='LOAD'):
        name=LOAD(doc)
        print("-----------")
    elif (fun=="LIST"):
        LIST(name)
print("end")


    





