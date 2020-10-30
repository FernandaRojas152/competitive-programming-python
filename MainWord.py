word= str(input())
upper=0
lower=0
for i in range (len(word)):
    if(word[i]>='a' and word[i]<='z'):
          lower+=1
    elif (word[i]>='A' and word[i]<='Z'):
        upper+=1

if lower>=upper:
    print(word.lower())
else:
    print(word.upper())