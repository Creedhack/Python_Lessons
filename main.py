playlist = ["Blinding Lights", "Starboy", "Save Your Tears"]
while True:
    print("\n=== THE WEEKND PLAYLIST мәзірі ===")
    print("1. Плэйлистті көру")
    print("2. Жаңа ән қосу")
    print("3. Әнды өшіру")
    print("4. Шығу")
    choice = input("\nТаңдауыңызды енгізіңіз (1-4): ")
    if choice == "1":
        print("\n---СІЗДІҢ ПЛЭЙЛИСТІҢІЗ---")
        num = 1
        for song in playlist: 
            print(f"{num}. {song}")
            num += 1
    elif choice == "2":
        new_song = input("Қосқыңыз келетін әннің атын енгізіңіз: ")
        playlist.append(new_song)
        print(f'"{new_song}" плэйлистке қосылды.\n')
    elif choice == "3":
        remove_song = input("Өшіру үшін әннің атын енгізіңіз: ") 
        if remove_song in playlist:
            playlist.remove(remove_song)
            print(f'"{remove_song}" плэйлисттен өшірілді.\n')
        else:
            print("Мұндай ән плэйлистте табылмады!")
    elif choice == "4":
        print("Музыкалық плеер жабылды. Сау болыңыз!")
        break
    else:
        print("Қате таңдау! 1-ден 4-ке дейінгі санды енгізіңіз.")