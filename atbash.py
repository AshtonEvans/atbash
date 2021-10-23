file=open("secret.txt")
f=file.read()
encrypted=open("encrypted.txt", "w") #will create new encrypted file
e=[] #encrypted array

print("Text to be encrypted:", f)

alph = ["a", "b", "c", "d", "e", "f",
        "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r",
        "s", "t", "u", "v", "w", "x",
        "y", "z"]

#the algorithm
for i in range(0, len(f)):
    try:
        x = alph[alph.index(f[i])-3] #three letter back
        e.append(x) #add to e array
    except(ValueError):
        if f[i] == " ":
            x=" "

#put the spaces back
try:
    space=f.index(" ")
    e.insert(space, " ")
except:
    pass

#convert array to string
e = str(e)

#get rid of the array-y features
e=e.replace("[", "")
e=e.replace("]", "")
e=e.replace(",", "")
e=e.replace("'", "")

#write close all the files
encrypted.write(e)
encrypted.close()
file.close()

print("Encrypted text: ", e)
