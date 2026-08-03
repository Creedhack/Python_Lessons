inventory = ["Blinding lights", "Starboy", "Save Your Tears", "In Your Eyes", "Heartless", "Pray For Me"]
print("=== THE WEEKND PLAYLIST ===")
song_number = 1 
for song in inventory:
    print(f"- {song_number}. {song}")
    song_number += 1
print ("\n--------------------------------")
print("Плэйлистке '(Cry For Me)' музыкасын қостыңыз !")
inventory.append("Cry For Me")
print("\n=== ӨҢДЕЛГЕН ПЛЭЙЛИСТ ===")
song_number = 1
for song in inventory:
    print(f"- {song_number}. {song}")
    song_number = song_number + 1