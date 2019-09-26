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
        self.max_block = block
    def block(self):
        ''' Return a value between 0 and the 
        value set by self.max_damage.'''
        return random.randint(0, self.max_block)  

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    punch = Ability("punch", 300)
    print(punch.name)
    print(punch.attack())      

