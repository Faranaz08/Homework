#to find vowels and consonants in string
Name=str(input('enter your name:'))
count=0
consonant=0
for letter in Name:
    if letter== 'a' or letter=='e' or letter=='i' or letter=='o' or letter=='u':
        count +=1
    else:
        consonant +=1
print('vowels'+str(count))
print('consonants'+str(consonant))