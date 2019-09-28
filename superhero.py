import random 

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
        pass 

    def attack(self):
        ''' Return a value between 0 and the 
        value set by self.max_damage.'''
        return random.randint(0, self.max_damage)  

class Armor:
    def __init__(self, name, max_block):
        self.name = name
        self.max_block = max_block
    def block(self):
        ''' Return a value between 0 and the 
        value set by self.max_damage.'''
        return random.randint(0, self.max_block)  

class Hero:
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = 100
        self.abilities = list()
        self.armor = list()
    def add_ability(self, ability):
        self.abilities.append(ability)
    def attack(self):
        '''Calculate the total damage from all ability attacks.
        return: total:Int
        '''
        damage_val = 0
        for ability in self.abilities:
            attack = ability.attack() + damage_val
            damage_val = attack
    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        






if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    punch = Ability("punch", 300)
    print(punch.name)
    print(punch.attack()) 
    my_hero = Hero("Grace Hopper", 200)
    print(my_hero.name)
    print(my_hero.current_health) 
    my_hero.add_ability(punch)
    print(my_hero.abilities)
    print(my_hero.attack())
