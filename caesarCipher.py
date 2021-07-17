#CEASEAR CIPHER
#input cipher text in small letters with no spaces
alphabets = {
    1 : 'a', 2 : 'b', 3 : 'c',  4 : 'd',  5 : 'e',  6 : 'f',  7: 'g',  8 : 'h',
    9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p',
    17 : 'q', 18 : 'r', 19 : 's', 20 : 't', 21 : 'u', 22 : 'v', 23 : 'w',
    24 : 'x', 25 : 'y', 26 : 'z'
}

def get_key(val):
    for key, value in alphabets.items():
         if val == value:
             return key 
    return " "

cipher = 'exxegoexsrgi'
cip = []

for letter in cipher:
    c = get_key(letter)    
    cip.append(c)
print("\n",cip)

for i in range(1,27) :
  for j in cip:
    p = (j + i ) % 26
    print(alphabets.get(p),end='')
  print("\n")
