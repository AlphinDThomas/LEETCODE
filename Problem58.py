text = input()
text = text.rstrip()

lastword = ""

for ch in text :
  if ch==" ":
    lastword=""
  else :
    lastword += ch

print(len(lastword))


#################  OR  ####################
'''
text = input()
i = len(text)-1

while i>=0 and text[i]==" ":
  i = i -1

i = i+1

lastword = ""

for j in range(i):
    if text[j] == " ":
      lastword=""
    else:
      lastword = lastword + text[j]

lengthoflastword = len(lastword)
print(lengthoflastword) 
'''