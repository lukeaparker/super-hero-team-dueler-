import random 

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.max_damage = attack_strength
         

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

class Hero():
    def __init__(self, name, starting_health=100):
        self.name = name
        self.starting_health = starting_health
        self.current_health = starting_health
        self.abilities = list()
        self.armors = list()
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

        return damage_val
    def add_armor(self, armor):
        '''Add armor to self.armors
        Armor: Armor Object
        '''
        self.armors.append(armor)
    def defend(self):
        defense_val = 0
        for armor in self.armors:
            blocked = armor.block() + defense_val
            defense_val = blocked 
        return defense_val
    def take_damage(self, damage):
        defend = self.defend() 
        if damage - defend > 0:
            dmg_amount = damage - defend
        else: 
            dmg_amount = 0
        self.current_health = self.current_health - dmg_amount
        return self.current_health
    def is_alive(self):
        if self.current_health <= 0:
            return False
        else:
            return True
    def fight(self, opponent):
        self_alive = True
        opp_alive = True
        draw = False 
        while self_alive == True and opp_alive == True:
            self_alive = self.is_alive()
            opp_alive = opponent.is_alive()
            if self.abilities == [] and opponent.abilities == []:
                print(f"You have run out of abilities")
                return draw == True
            opponent.take_damage(self.attack())
            opp_alive = opponent.is_alive()
            self.take_damage(opponent.attack())
            self_alive = self.is_alive()

        if self_alive == True and opp_alive == False:
            print(self.name, "has won")
        elif self_alive == False and opp_alive == True:
            print(opponent.name, "has won")
        elif self_alive == False and opp_alive == False:
            print("Both dead")







if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    hero1 = Hero("Wonder Woman")
    hero2 = Hero("Dumbledore")
    ability1 = Ability("Super Speed", 3)
    ability2 = Ability("Super Eyes", 1)
    ability3 = Ability("Wizard Wand", 8000)
    ability4 = Ability("Wizard Beard", 2000)
    hero1.add_ability(ability1)
    hero1.add_ability(ability2)
    hero2.add_ability(ability3)
    hero2.add_ability(ability4)
    hero1.fight(hero2)