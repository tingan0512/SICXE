def LOAD(filename):
    f = open(filename, 'r')
    line = f.read()
    f.close()
    return line

def LIST(name):
    print(name)

while True:
    command = input("<SICXE> ")

    tokens = command.split()
    if len(tokens) == 2 and tokens[0] == "LOAD":
        filename = tokens[1]
        name = LOAD(filename)

    elif tokens[0] == "LIST":
        LIST(name)

    else:
        print("Invalid command:", command)



