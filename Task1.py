#Напишите программу, удаляющую из текста все слова, содержащие "абв".
my_text = 'Напишите абв программу, удаляющую из этого абв текста все  слова, содержащие "абв"'

def del_abc(my_text):
    my_text = list(filter(lambda x: 'абв' not in x, my_text.split()))
    return " ".join(my_text)

my_text = del_abc(my_text)
print(my_text)