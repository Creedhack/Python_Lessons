correct_password = "Python2026" 
attempts = 3 
print("=== ҚАУІПСІЗ КІРУ ЖҮЙЕСІ ===")
while attempts > 0:
    user_input = input("Құпия сөзді енгізіңіз: ")
    if user_input == correct_password:
        print("Құпия сөз дұрыс! Қош келдіңіз!")
        break
    else:
        attempts = attempts - 1
        if attempts > 0:
            print(f"ПАРОЛЬ ҚАТЕ! ТАҒЫ {attempts} МҮМКІНДІГІҢІЗ ҚАЛДЫ.\n")
        else:
            print("3 РЕТ ҚАТЕ ЕНГІЗДІҢІЗ! Қауіпсіздік жүйесі бұғатталды.")