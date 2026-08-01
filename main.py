import random 
secret_number = random.randint(1, 10) 
guess = 0  
print("=== ШЕКСІЗ САНДЫ ТАП ОЙЫНЫ ===")
while guess != secret_number:
    guess = int(input("1 мен 10 аралығындағы санды болжаңыз: "))
    if guess < secret_number:
        print("Кіші сан. Тағы бір рет көріңіз.")
    elif guess > secret_number:
        print("Үлкен сан. Тағы бір рет көріңіз.")
    else:
        print("УРА-А-А! Сіз құпия санды таптыңыз!")