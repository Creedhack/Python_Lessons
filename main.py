secret_number = 7
print("=== САНДЫ ТАП ОЙЫНЫ ===!") 
guess = int(input("1-ден 10-ға дейінгі санды енгізіңіз: ")) 
if guess == secret_number:
    print("Құттықтаймыз! Сіз дұрыс санды таптыңыз!") 
elif guess < secret_number: 
    print("Тым кішкентай! құпия сан бұдан үлкенірек.") 
else:
    print("Тым үлкен! құпия сан бұдан кіші.")  