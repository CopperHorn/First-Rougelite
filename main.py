import random
import os
# Defining variables, functions, and classes

#Variables
encounter1 = 0
encounter2 = 0
encounter_number = 0
#Stats for all charachters
class Char:
    def __init__(self,name,max_health,health,shield=0,baseDMG=1,items=[], gold=0): 
        self.name = name
        self.max_health = max_health
        self.health = health
        self.shield = shield
        self.baseDMG = baseDMG
        self.items = []
        self.gold = gold
        self.living = True
    def damage_done(self):
        total = self.baseDMG
        for item in self.items:
            total += random.randint(item_list[item]['low'],item_list[item]['high'])
        return total
    def add_item(self,item):
        self.items.append(item)
    def damage_taken(self,damage):
        if self.shield >= damage:
            self.shield -= damage
            return
        elif self.shield < damage:
            total_dmg = damage - self.shield
            self.shield = 0
            if total_dmg > self.health:
                self.living = False
                self.health = 0
            else:
                self.health -= total_dmg
        else:
            print('Error')
        
# Encounter things
#Enemy list
enemy_list = {
    'Goblin': {
        'name':'Goblin',
        'max_health':20,
        'shield':0,
        'baseDMG':4,
        'gold':5
    },
    'Troll': {
        'name':'Troll',
        'max_health':45,
        'shield':0,
        'baseDMG':8,
        'gold':20
    },
    'Kobold': {
        'name':'Kobold',
        'max_health': 10,
        'shield':0,
        'baseDMG': 2,
        'gold':2
    },
    'Suspicious Kobold': {
        'name':'Three Kobolds in a Trench Coat',
        'max_health':30,
        'shield':0,
        'baseDMG':2,
        'gold':6
    }
}

encounter_table = {
    'Goblin':4,
    'Troll':4,
    'Kobold':4,
    'Suspicious Kobold':4,
    'Campfire':1,
    'Shop':2,
    'Item':1,
}
#Item list
item_list = {
    'Sharpening Stone': {
        'low': 1,
        'high': 1,
        'cost': 10
    },
    'An Extra Sword': {
        'low': 0,
        'high': 2,
        'cost': 10
    },
    'Throwing Stone': {
        'low': 1,
        'high': 3,
        'cost': 12
    },
    'Bow String': {
        'low': 3,
        'high': 4,
        'cost': 14
    },
    'Gilded Blade': {
        'low': 0,
        'high': 8,
        'cost': 17
    },
    'Seeing Stone': {
        'low': 4,
        'high': 4,
        'cost': 15
    },
    'D20': {
        'low': 1,
        'high': 20,
        'cost': 23
    },
    'Dragon Scales': {
        'low': 6,
        'high': 6,
        'cost': 19
    },
    'Everlasting Flame': {
        'low': 5,
        'high': 8,
        'cost': 20
    },
    'Something': {
        'low': 200,
        'high': 4000,
        'cost': 0
    },
    'Enemy': {
        'low': 1,
        'high': 5,
    }
}

loot_table = {
    'Sharpening Stone': 70,
    'An Extra Sword': 70,
    'Throwing Stone': 70,
    'Bow String': 30,
    'Gilded Blade': 30,
    'Seeing Stone': 30,
    'D20': 5,
    'Dragon Scales': 9,
    'Everlasting Flame': 9,
    'Something': 1,
}

def view_status():
    user_profile()
    while True:
        yes = input('Would you like to view items? (y/n) ')
        print('')
        if yes != 'y' and yes != 'n':
            os.system('clear')
            print('Please write y/n')
            print('')
            continue
        elif yes == 'n':
            os.system('clear')
            break
        elif yes == 'y':
            if user.items == []:
                os.system('clear')
                print('')
                print('You have no Items')
                break
            else:
                x = 1
                os.system('clear')
                
                for item in user.items:
                    print(f'{x}.) '+item)
                    x += 1
                print('')
                while True:
                    try:
                        num = int(input('Please enter number to view Item: ')) - 1
                        try:
                            os.system('clear')
                            num = user.items[num]
                            print('')
                            print('')
                            print('      //═══════════════════════════════════════\\')
                            print('      ║ Name: '+num)
                            if item_list[num]['low'] == item_list[num]['high']:
                                print(f'[≡]═══╣ Damage: {item_list[num]['low']}')
                            else:
                                print(f'[≡]═══╣ Damage: {item_list[num]['low']} - {item_list[num]['high']}')
                            print('      ║')
                            print('      \\\\═══════════════════════════════════════/')
                            print('')
                            print('')
                            yes = input('Would you like to view another item? (y/n) ')
                            print('')
                            if yes != 'y' and yes != 'n':
                                print('Please write y/n')
                                print('')
                                continue
                            elif yes == 'n':
                                os.system('clear')
                                break
                            elif yes == 'y':
                                os.system('clear')
                                if user.items == []:
                                    print('You have no Items')
                                    break
                                else:
                                    os.system('clear')
                                    x = 1
                                    for item in user.items:
                                        print(f'{x}.) '+item)
                                        x += 1
                                    print('')
                                continue
                            
                                
                        except:
                            print('')
                            print('Please enter a valid number.')
                            print('')
                            x = 1
                            for item in user.items:
                                print(f'{x}.) '+item)
                                x += 1
                            print('')
                            continue
                    except:
                        os.system('clear')
                        print('Please enter a number')
                        print('')
                        x = 1
                        for item in user.items:
                                print(f'{x}.) '+item)
                                x += 1
                        print('')
                        continue
        break

def encounter_ran():
    return random.choices(list(encounter_table.keys()), weights=list(encounter_table.values()))[0]
# Encounter Function
def encounter():
    enemy = 0
    print('Before you lie two paths:')
    encounter1 = encounter_ran()
    while True:
        encounter2 = encounter_ran()
        if encounter1 == encounter2:
            encounter1 = encounter_ran()
            continue
        else:
            break
    
    while True:
        try:
            while True:
                print('1.) '+encounter1)
                print('2.) '+encounter2)
                print('3.) View items and status')
                print('')
                direction = int(input('Which direction? (1-3): '))
                os.system("clear")
                if direction != 1 and direction != 2 and direction != 3:
                    print('Please enter 1, 2, or 3')
                    continue
                else:
                    if direction == 3:
                        view_status()
                        continue
                    else:
                        break
            break
        except:
            os.system("clear")
            print('Please enter a number')
    if direction == 1:
        enemy = encounter1
    elif direction == 2:
        enemy = encounter2
    if enemy == 'Item' or enemy == 'Shop' or enemy == 'Campfire':
        return enemy 
    else:
        enemy = list(enemy_list[enemy].values())
        return enemy
# Acii art for Profiles
def user_profile():
    print('')
    print('')
    print('   .::[ '+user.name.upper()+'\'S CHARACTER PROFILE ]::.')
    print(' \\\\══════════════════════════════════//')
    print(f'  | Remaining HP:     {user.health}/{user.max_health}')
    print(f'  | Remaining Shield: {user.shield}')
    print('  | Items in Bag:')
    if user.items == []:
        print('  |  - No Items')
    else:
        for item in user.items:
            print('  |  - '+item)
    print(f'  | Gold: {user.gold}')
    print(' //══════════════════════════════════\\\\')
    print('')
    print('')

def item_profile():
    print('     ()')
    print('     )(')
    print('     )(')
    print('  o======o')
    print('     ||')
    print('     ||')
    print('     ||')
    print('  ..-||--..')
    print('.\'  ^      ;')
    print('\'-.______.-\'')

def enemy_profile(num):
    if num == -1:
        next_damage = enemy.damage_done()
    else:
        next_damage = num
    print('')
    print('')
    print('   _/[ '+enemy.name.upper()+' ]\\_')
    print(' \\\\^^^^^^^^^^^^^^^^^^^^^^^^^//')
    print(f'  < Remaining HP:     {enemy.health}/{enemy.max_health}')
    print(f'  < Remaining Shield: {enemy.shield}')
    if enemy.living == True:
        print(f'  < Next Damage:      {next_damage}')
    print(' //^^^^^^^^^^^^^^^^^^^^^^^^^\\\\')
    print('')
    print('')
    return next_damage


#Functions for the options
def fight():
    while enemy.living == True:
        incoming_damage = enemy_profile(-1)
        while True:
            try:
                while True:
                    print('1.) Attack')
                    print('2.) Shield')
                    print('3.) View items and status')
                    print('')
                    direction = int(input('Pick a direction: '))
                    os.system("clear")
                    if direction != 1 and direction != 2 and direction != 3:
                        print('Please enter 1, 2, or 3')
                        continue
                    else:
                        if direction == 3:
                            view_status()
                            enemy_profile(incoming_damage)
                            continue
                        else:
                            break
                break
            except:
                os.system('clear')
                enemy_profile(incoming_damage)
                print('Please enter a number')
        if direction == 1:
            damage_done = user.damage_done()
            enemy.health -= damage_done
            if enemy.health <= 0:
                enemy.health = 0
                enemy.living = False
                print('you killed the '+enemy.name)
                user.gold += enemy.gold
            else:
                print('')
                print(f'you did {damage_done} damage!')
            
        elif direction == 2:
            
            shielded = random.randint(4,9)
            user.shield += shielded
            print(f'You gained a shield of {shielded}')
        if enemy.living:
            user.damage_taken(incoming_damage)
            print(f'You took {incoming_damage} damage!')
        if user.health == 0:
            user.living = False
            break
        user_profile()
    enemy_profile(-1)
    user.shield = 0

def item_recieved():
    item_gotten = random.choices(list(loot_table.keys()), weights=list(loot_table.values()), )[0]
    user.add_item(item_gotten)
    item_profile()
    print('You got ['+item_gotten+']')

def shop_profile():
    print('     \':.')
    print('         []_____')
    print('        /\\      \\')
    print('    ___/  \\__/\\__\\__')
    print('   /\\___\\ |[Shop] |__\\')
    print('   ||   | |  ||   |  |')
    print('   ``***`*`**))**`**`')
    print('')

def shop():
    
    x = 1
    items_offered = []
    num_items = random.choices([2,3,4,5],[14,36,36,14])[0]
    shop_profile()
    for i in range(num_items):
        item = random.choices(list(loot_table.keys()), list(loot_table.values()))[0]
        items_offered.append(item)
        print(f'{i+1}.) '+item+ f' ${item_list[item]["cost"]}')
    print('0.) Leave')
    print(f'You have {user.gold} gold')
    while True:
        try:
            item_view = int(input('Which Item would you like to view?: '))
            os.system("clear")
            if item_view == 0:
                break
            try:
                item_view = items_offered[item_view - 1]
                print('')
                print('')
                print('      //═══════════════════════════════════════\\')
                print('      ║ Name: '+item_view)
                if item_list[item_view]['low'] == item_list[item_view]['high']:
                    print(f'[≡]═══╣ Damage: {item_list[item_view]['low']}')
                else:
                    print(f'[≡]═══╣ Damage: {item_list[item_view]['low']} - {item_list[item_view]['high']}')
                print(f'      ║ Cost: {item_list[item_view]['cost']}')
                print('      \\\\═══════════════════════════════════════/')
                print('')
                print('')
                print(f'You have {user.gold} gold')
                
                while True:
                    yes = input("Would you like to buy this? (y/n) ")
                    if yes != 'y' and yes != 'n':
                        print('Enter y or n')
                        continue
                    else:
                        if yes == 'y':
                            if user.gold >= item_list[item_view]['cost']:
                                user.gold -= item_list[item_view]['cost']
                                user.add_item(item_view)
                                items_offered.remove(item_view)
                                os.system('clear')
                                print('You bought ['+item_view+']')
                                x = 1
                                shop_profile()
                                for i in items_offered:
                                    print(f'{x}.) {i} ${item_list[i]["cost"]}')
                                    x += 1
                                print('0.) Leave')
                                print(f'You have {user.gold} gold')
                                break
                            else:
                                os.system('clear')
                                print('You don\'t have enough gold')
                                x = 1
                                shop_profile()
                                for i in items_offered:
                                    print(f'{x}.) {i} ${item_list[i]["cost"]}')
                                    x += 1
                                print('0.) Leave')
                                print(f'You have {user.gold} gold')
                                break
                        else:
                            os.system('clear')
                            x = 1
                            shop_profile()
                            for i in items_offered:
                                print(f'{x}.) {i} ${item_list[i]["cost"]}')
                                x += 1
                            print('0.) Leave')
                            print(f'You have {user.gold} gold')
                            break

            except:
                print('Enter a number that is offered.')
                x = 1
                shop_profile()
                for i in items_offered:
                    print(f'{x}.) {i} ${item_list[i]["cost"]}')
                    x += 1
                print('0.) Leave')
                print(f'You have {user.gold} gold')


        except ValueError:
            os.system("clear")
            print('Please enter a number')
            x = 1
            shop_profile()
            for i in items_offered:
                print(f'{x}.) {i} ${item_list[i]["cost"]}')
                x += 1
            print('0.) Leave')
            print(f'You have {user.gold} gold')

def campfire_profile():
    print('  .(')
    print('  /%/\\')
    print(' (%(%))')
    print('.-\'..`-.')
    print('`-\'.\'`-\'')

def campfire():
    os.system('clear')
    campfire_profile()
    user.health = user.max_health
    print('You healed to full!')
    user_profile()
    print('')

#Game loop
print('Welcome to the wide world of NotEarth, here you can\'t do much because I\'m bad at game design')
print('')
print('To Start,')
user_name = input('What is your Characters name? ')
os.system("clear")
user = Char(name=user_name, max_health=100, health=100, shield=0, baseDMG=7, items=None)
user_profile()  
while encounter_number < 10:
    choice = encounter()
    if choice == 'Item':
        item_recieved()
    elif choice == 'Campfire':
        campfire()
    elif choice == 'Shop':
        shop()
    else:
        enemy = choice
        enemy = Char(name=enemy[0], max_health=enemy[1], health=enemy[1], shield=enemy[2], baseDMG=enemy[3], gold=enemy[4])
        enemy.add_item('Enemy')
        print('Infront of you, you see a '+enemy.name)
        fight()
        if user.living == False:
            os.system('clear')
            print('You died. Loser')
            break
        print('Would you like: \n1.) 20 Health\n2.) 15 Gold')
        while True:
            try:
                answer = int(input('Pick an option (1/2): '))
                if answer != 1 and answer != 2:
                    print('Please 1 or 2')
                    continue
                else:
                    os.system('clear')
                    if answer == 1:
                        if user.health <= user.max_health - 20:
                            total_healed = 20
                            user.health += 20
                        else:
                            total_healed = user.max_health - user.health
                            user.health = user.max_health
                        print(f'you healed {total_healed} health')
                        break
                    else:
                        user.gold += 15
                        print('You got 15 gold')
                        break
            
            except:
                print('Please enter a number')       
        user_profile()        
        
    encounter_number += 1

#Final path
while True:
    os.system('clear')
    user_profile()
    print('You see one final stop before the end: \n1.) Shop \n2.) Item \n2.) Campfire')
    try:
        answer_last_stop = int(input('Choose one (1-3): '))
        if answer_last_stop == 1:
            os.system('clear')
            shop()
            break
        elif answer_last_stop == 2:
            os.system('clear')
            item_recieved()
            break
        elif answer_last_stop == 3:
            os.system('clear')
            campfire()
            break
        else:
            continue
    except:
        print('Enter a number')
        continue
while True:
    finish_game = input('Continue to boss? (y/n): ')
    if finish_game == 'y':
        break
    elif finish_game == 'n':
        os._exit(0)
    else:
        os.system('clear')
        print('Enter y or n')
        continue
enemy = Char(name='Achra, the forgotten', max_health=200, health=200, baseDMG=12, items=None)
enemy.add_item('Enemy')
fight()
if user.living == True:
    os.system('clear')
    print('You won. Hurray!')
else:
    os.system('clear')
    print('You died. Loser')