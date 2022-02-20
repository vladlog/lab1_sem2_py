def nameoffile():
    name = input()
    return name


def get_input(name):
    mode = input("If you like to append your input, enter q. Otherwise enter w:")
    if mode == 'q':
        file = open(name, "a")
    if mode == 'w':
        file = open(name, "w")
    while (mode != 'q' and mode != 'w'):
        mode = input('Enter correct letter:')
    print("Enter your text:\n End the line | press --> ENTER\n End the input | press --> Ctrl + X\n")
    while 1:
        line = input()
        if ord(line[0]) == 24:
            break
        file.write(line + "\n")
    file.close()


def output(name):
    file = open(name, "r")
    print(file.read())


def change(name, newname):
    file = open(name, "r")
    lines = file.readlines()
    newtext = ''
    for line in lines:
        for letter in line:
            if letter != '1' and letter != '0':
                newtext += letter
            if letter == '1':
                newtext += '0'
            if letter == '0':
                newtext += '1'
    newfile = open(newname, "w")
    newfile.write(newtext)
    file.close()
    newfile.close()

print("enter name of the input file:")
header = nameoffile()
get_input(header)
print('Entered text:\n')
output(header)
print("enter  name of the output file:")
newheader = nameoffile()
change(header, newheader)
print('Changed text:\n')
output(newheader)
