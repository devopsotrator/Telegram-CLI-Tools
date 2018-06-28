from random import randint

text_file = open("card.vcf", "w")
text_file2 = open("nums.txt", "w")
text = ''
text2 = ''

i = 0
while i != 500:
    num = randint(000000000000,000000000000) #range from XXX to XXX
    
    text += 'BEGIN:VCARD\n'
    text += 'VERSION:2.1\n'
    text += 'N:{}{};{};;;\n'.format("Deanon", i, "Telegram")
    text += 'FN:{} {}{}\n'.format("Telegram", "Deanon", i)
    text += 'TEL;CELL:{}\n'.format(num)
    text += 'END:VCARD\n'

    text2 += '{}\n'.format(num)
        
    i += 1
    print(i)

text_file.write(text)
text_file2.write(text2)
text_file.close()
text_file2.close()
