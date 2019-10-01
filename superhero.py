import random 
import superhero

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
        self.deaths = 0
        self.kills = 0
    def add_ability(self, ability):
        self.abilities.append(ability)
    def add_weapons(self, weapon):
        self.abilities.append(weapon)

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
    def add_kills(self):
        self.kills += 1
        
    def add_deaths(self):
        self.deaths += 1

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
            self.add_kills()
            opponent.add_deaths()

        elif self_alive == False and opp_alive == True:
            print(opponent.name, "has won")
            opponent.add_kills()
            self.add_deaths()
        elif self_alive == False and opp_alive == False:
            print("Both dead")
class Weapon(Ability):
    def attack(self):
        return random.randint(self.max_damage//2, self.max_damage)  
class Team():
    def __init__(self, name):
        self.name = name
        self.heros = [] 
    def remove_hero(self, name):
        if name in self.heros:
            return self.heros.remove(name)
        else:
            return 0
    def view_all_heros(self):
        for hero in self.heros:
            print(hero.name)
    def add_hero(self, hero):
        self.hero = hero
        self.heros.append(hero)
    def attack(self, other_team):
        self.self_hero = random.choice(self.heros)
        self.opp_hero = random.choice(other_team.heros)
        Hero.fight(self.self_hero, self.opp_hero)
    def revive_heroes(self, health=100):
        current_health = health
    def stats(self):
        for hero in self.heros:
            print(f"Kills: {hero.kills} Deaths: {hero.deaths} k / d : {hero.kills} / {hero.deaths}")
class Arena:
    def __init__(self):
        self.team_one = []
        self.team_two = []
    def create_ability(self):
        '''Prompt for Ability information.
        return Ability with values from user Input
        '''
        ability = Ability(input("Name ability? "), int(input("Strength value?")))
        return ability
    
    def create_weapon(self):
        weapon = Weapon(input("Name weapon? "), int(input("Strength value?")))
        return weapon 

    def create_armor(self):
        armor = Armor(input("Name armor? "), int(input("Strength value?")))
        return armor 

    def create_hero(self):
        hero = Hero(input("Name Hero? "))
        number = int(input("How many abilities?"))
        for i in range(number):
            ability = self.create_ability()
            hero.add_ability(ability)
        number = int(input("How many weapons?"))
        for i in range(number):
            weapon = self.create_weapon()
            hero.add_ability(weapon)
        number = int(input("How much armor?"))
        for i in range(number):
            armor = self.create_armor()
            hero.add_armor(armor)
        return hero 

    def build_team_one(self):
        self.team_one = Team(input("Team name?"))
        
        number = int(input("How many heros do you want?"))
        for i in range(number):
            hero = self.create_hero()
            self.team_one.add_hero(hero)
        return self.team_one

    def build_team_two(self):
        self.team_two = Team(input("Team name?"))
        
        number = int(input("How many heros do you want?"))
        for i in range(number):
            hero = self.create_hero()
            self.team_two.add_hero(hero)
        return self.team_two
    def team_battle(self):
        self.team_one = self.build_team_one()
        self.team_two = self.build_team_two()
        return self.team_one.attack(self.team_two)
    def show_stats(self):
        print(f"{self.team_one.name} stats: ")
        self.team_one.stats()
        print(f"{self.team_two.name} stats: ")
        self.team_two.stats()






    

        








if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    # hero1 = Hero("Wonder Woman")
    # hero2 = Hero("Dumbledore")
    # ability1 = Ability("Super Speed", 3)
    # ability2 = Ability("Super Eyes", 1)
    # ability3 = Ability("Wizard Wand", 8000)
    # ability4 = Ability("Wizard Beard", 2000)
    # hero1.add_ability(ability1)
    # hero1.add_ability(ability2)
    # hero2.add_ability(ability3)
    # hero2.add_ability(ability4)
    # hero1.fight(hero2)

    ''' game test '''
    # arena = Arena()
    # arena.build_team_one()
    # arena.build_team_two()
    # arena.team_battle()
    # arena.show_stats()

    game_is_running = True

    # Instantiate Game Arena
    arena = Arena()

    #Build Teams
    # arena.build_team_one()
    # arena.build_team_two()

    while game_is_running:

        arena.team_battle()
        arena.show_stats()
        play_again = input("Play Again? Y or N: ")

        #Check for Player Input
        if play_again.lower() == "n":
            game_is_running = False

        else:
            #Revive heroes to play again
            arena.team_one.revive_heroes()
            arena.team_two.revive_heroes()
