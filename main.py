from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy1 = Character("Goblin", 20, 3)
    enemy2 = Character("Orc", 25, 4)

    print(hero)
    print(enemy1)
    print(enemy2)
    print()


    for enemy in [enemy1, enemy2]:
        print(f"A wild {enemy.name} appears!\n")

        while hero.is_alive() and enemy.is_alive():
            hero.attack(enemy)
            if enemy.is_alive():
                enemy.attack(hero)
            print(hero)
            print(enemy)
            print()

        if not hero.is_alive():
            print(f"{enemy.name} wins!")
            break
        else:
            print(f"{enemy.name} is defeated!\n")

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins all battles!")
    else:
        print(f"{hero.name} was defeated!")

if __name__ == "__main__":
    main()
