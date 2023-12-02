# импорт модулей
import time
import random


# класс игрока


class Player:
    # конструктор класса, где задаются все характеристики главного героя
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage
        self.lvl = 1
        self.exp = 0
        self.skill = None  # изначально способности нет

    # функция создания героя
    def create_hero(name, species, prof):
        # создаем временные переменные для вывода в return
        hp = 0
        damage = 0
        # присваиваем характеристики в зависимости от расы
        if species == species_list[0]:
            hp += 100
            damage += 50
        elif species == species_list[1]:
            hp += 50
            damage += 100
        elif species == species_list[2]:
            hp += 70
            damage += 60
        elif species == species_list[3]:
            hp += 90
            damage += 110
        elif species == species_list[4]:
            hp += 20
            damage += 140
        else:
            print('Я не знаю кто ты...')
        # присваиваем характеристики в зависимости от профессии
        if prof == prof_list[0]:
            hp += 100
            damage += 50
        elif prof == prof_list[1]:
            hp += 60
            damage += 100
        elif prof == prof_list[2]:
            hp += 50
            damage += 70
        elif prof == prof_list[3]:
            hp += 30
            damage += 110
        elif prof == prof_list[4]:
            hp += 80
            damage += 50
        else:
            print('Я не знаю такой профессии...')
        return Player(name, hp, damage)  # выводим объект класса Player

    # функция атаки игрока на монстра
    def attack(self, victim):
        max_exp = self.lvl * 100  # максимальное количество очков в уровне
        victim.hp -= self.damage

        if victim.hp <= 0:
            print(f'Поздравляем,{victim.name} повержен! +20 опыта')
            time.sleep(1)
            self.exp += 20  # увеличиваем опыт и повышаем уровень, если нужно
            if self.exp >= max_exp:
                self.levelup(max_exp)

            thing = random.randint(0, 3)  # случайно выдаем дополнение (вещь)
            if thing == 1:
                wpn = self.create_weapon()
                print(f"Вам выпало новое оружие! {wpn[0]}{wpn[1]}.")
                time.sleep(1)
            elif thing == 2:
                armor = self.create_armor()
                print(f"Вам выпала новая броня! {armor[0]} {armor[1]}")
                time.sleep(1)
            elif thing == 3:
                food = self.create_food()
                print(f"Вам выпала вкусняшка! {food}")
                time.sleep(1)
            else:
                print("Награды нет... Повезет в следующий раз.")
                time.sleep(1)

            # присваиваем способность
            self.skill = random.choice(powers)
            print(f"Теперь вы одарены способностью: {self.skill}")
            time.sleep(1)

            return False
        else:  # если враг не повержен, запускаем способность, если она есть и выводим результат
            if self.skill is not None:
                ability()
            print(victim.name, "теперь имеет", victim.hp, "очков здоровья")
            time.sleep(1)
            return True

    # функция повышения уровня
    def levelup(self, max_exp):
        self.exp -= max_exp  # вычитаем максимальное значение, чтобы на новый уровень перешел только остаток
        self.lvl += 1
        self.damage += self.lvl * 5  # добавляем бонусы после повышения уровня
        self.hp += self.lvl * 10
        print(f"self.name, поздравляю с повышением уровня Уровень: {self.lvl}")
        time.sleep(1)

    def create_weapon(self):
        # выбираем рандомное оружие и изменяем характеристики героя в зависимости от оружия
        wpn_type = wearpon_type_list[random.randint(0, 2)]
        wpn_rare = random.choice(list(wearpon_rare_dict.keys()))
        if wpn_type == wearpon_type_list[0]:
            self.damage += 4 * wpn_rare
        elif wpn_type == wearpon_type_list[1]:
            self.damage += 5 * wpn_rare
        elif wpn_type == wearpon_type_list[2]:
            self.damage += 6 * wpn_rare
        return wpn_type, wearpon_rare_dict[wpn_rare]

    def create_armor(self):
        # выбираем рандомную броню и изменяем характеристики героя в зависимости от брони
        armor_type = armor_type_list[random.randint(0, 2)]
        armor_rare = random.choice(list(armor_rare_dict.keys()))
        if armor_type == armor_type_list[0]:
            self.hp += 4 * armor_rare
        elif armor_type == armor_type_list[1]:
            self.hp += 5 * armor_rare
        elif armor_type == armor_type_list[2]:
            self.hp += 6 * armor_rare
        return armor_type, armor_rare_dict[armor_rare]

    def create_food(self):
        # создаём рандомную еду и добавляем к здоровью величину бонуса
        r_heal_size = random.choice(list(heal.keys()))
        self.hp += r_heal_size
        return heal[r_heal_size]


# класс врага
class Enemy:
    def __init__(self, name, hp, damage):
        self.name = name
        self.hp = hp
        self.damage = damage

    def create_enemy():
        # назначаем рандомные характеристики врагу
        rnd_name = random.choice(enemy_name)
        rnd_hp = random.randint(10, 50)
        rnd_damage = random.randint(30, 70)
        return Enemy(rnd_name, rnd_hp, rnd_damage)

    def attack(self, victim):
        # монстр бьёт героя, выводим результат
        victim.hp -= self.damage
        if victim.hp <= 0:
            print('Ты повержен! Игра окончена!')
            time.sleep(1)
            quit()
        else:
            print(f'{victim.name}, оставшееся здоровье: {victim.hp}')
            time.sleep(1)


# функция битвы
def fight_choice():
    answer = input(f"Готов сразиться с {enemy.name}? (ответ 'да' или 'нет')").lower()
    # если выбрано сражение
    if answer == "да":
        rezult = hero.attack(enemy)  # находим результат от удара героя по монстру
        if rezult:
            enemy.attack(hero)  # монстр бьет в ответ
            fight_choice()  # перезапускаем выбор
    elif answer == "нет":  # попытка сбежать
        plan = random.randint(0, 1)
        if plan == 0:
            print("Побег не удался. Вы подвергаетесь нападению монстра")
            time.sleep(1)
            enemy.attack(hero)
            fight_choice()  #
        elif plan == 1:
            print("Вы сбежали от монстра")
            time.sleep(1)
    else:  # исключаем неверный ввод
        print("Будь внимательнее, ибо у меня нет такого варианта действий")
        time.sleep(1)
        fight_choice()


# использование способности
def ability():
    if hero.skill == "Замораживание":
        print("Вы заморозили монстра! Теперь он не атакует тебя)")
        time.sleep(1)
        enemy.damage = 0
    elif hero.skill == "Отравление":
        print("Вы отравили монстра в этой схватке,-10 здоровья у врага!")
        time.sleep(1)
        enemy.hp -= 10
    elif hero.skill == "Лечение":
        print("Твоё оружие вылечило тебя. + 10 здоровья")
        time.sleep(1)
        hero.hp += 10


# игровые списки
enemy_name = ['Баба Яга', 'Кощей', 'Волк']  # имена монстров
species_list = ['эльф', 'гном', 'человек', 'тролль', 'пандарен']  # расы героя
prof_list = ['лучник', 'воин', 'маг', 'жрец', 'друид']  # профессии героя
wearpon_type_list = ["Меч", "Лук", "Посох"]  # названия оружий
wearpon_rare_dict = {1: "Обычный", 2: "Редкий", 3: "Эпический"}  # коэффициент улучшения оружия и название редкости
armor_type_list = ["Шлем", "Барьер", "Щит"]  # названия защиты
armor_rare_dict = {1: "Обычный", 2: "Редкий", 3: "Эпический"}  # коэффициент улучшения брони и название редкости
heal = {5: "Апельсин", 10: "Каша Геркулес", 15: "Творожная запеканка"}  # емкость и название бонуса еды
powers = ["Замораживание", "Отравление", "Лечение"]  # названия способностей

# настройка главного героя
my_name = input("Введите имя для своего героя: ")
print(f"Доступные расы:{species_list}")
my_species = input("Выберите расу: ").lower()
print(f'Доступные професси: {prof_list}')
my_prof = input('Выберите профессию: ').lower()
hero = Player.create_hero(my_name, my_species, my_prof)
print(f"Характеристики {hero.name}: Здоровье: {hero.hp}, Урон: {hero.damage}, Уровень: {hero.lvl}, Опыт: {hero.exp}")

# главный цикл — движок
while True:
    event = random.randint(1, 2)  # выбираем событие
    if event == 1:
        print("Тебе никто не встретился")
        time.sleep(1)  # просто пропускаем это событие
    elif event == 2:
        enemy = Enemy.create_enemy()  # создаём монстра
        print(f"Тебе встретился {enemy.name}!")  # выводим имя монстра
        print(f"Здоровье: {enemy.hp}\nУрон: {enemy.damage}")  # выводим характеристики монстра
        print(f"Характеристики {hero.name}:\nЗдоровье: {hero.hp}\nУрон: {hero.damage}\nУровень: {hero.lvl}"
              f"\nОпыт: {hero.exp}")  # выводим характеристики игрока
        time.sleep(2)
        fight_choice()  # запускаем бой
