hero_name = "Eminem" 
hero_hp = 100 
hero_damage = 25
raper_name = "Slim Shady"
raper_hp = 150
raper_damage = 20
print(f"=== ОЙЫН БАСТАЛДЫ ! ===\n")
print(f"Eminem: {hero_name} (HP: {hero_hp}, Damage: {hero_damage})")
print(f"Slim Shady: {raper_name} (HP: {raper_hp}, Damage: {raper_damage})\n")
round = 1 
while hero_hp > 0 and raper_hp > 0:
    print(f"--- Раунд {round} ---")
    raper_hp = raper_hp - hero_damage
    print(f"{hero_name} ұрды ! {hero_damage} залал келтірді.")
    print(f"{raper_name} Денсаулығы: {raper_hp}")
    if raper_hp <= 0:
        print(f"\n{raper_name} жеңілді ! {hero_name} жеңіске жетті !")
        break
    hero_hp = hero_hp - raper_damage
    print(f"{raper_name} ұрды ! {raper_damage} залал келтірді.") 
    print(f"{hero_name} Денсаулығы: {hero_hp}\n")
    if hero_hp <= 0:
        print(f"\n{hero_name} жеңілді ! {raper_name} жеңіске жетті !")
    round = round + 1
print(f"\n=== RAP BATTLE АЯҚТАЛДЫ ! ===") 