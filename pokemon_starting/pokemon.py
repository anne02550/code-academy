
weaknesses = {
    "Fire" : "Water",
    "Water" : "Grass",
    "Grass" : "Fire"
}

class Pokemon:
    def __init__(self, name, pokemon_type, level, is_knocked_out = False):
      self.name = name
      self.level = level 
      self.type = pokemon_type

      self.max_health = level * 5
      self.is_knocked_out = is_knocked_out
      self.health = 0 if is_knocked_out else self.max_health

    def revive(self):
        self.is_knocked_out = False
        if self.health == 0:
             self.health = 1
        print("{name} pokemon has been revived!".format(name = self.name))

    def knock_out(self):
        self.is_knocked_out == True
        self.health = 0
        print("{name} pokemon has been knocked down!".format(name = self.name))

    def lose_health(self, amount):
        if amount >= self.health:
            self.knock_out()
        else:
            self.health -= amount
            print("{name} lost {amount} hp and now has {health} hp".format(name = self.name, amount = amount, health =  self.health))
        
    def gain_health(self, amount):
        if self.health ==0:
            self.revive()
        self.health = min(self.max_health, self.health + amount)
        print("{name} pokemon has gained {health} health".format(name = self.name, health = self.health))


    def attack(self, other_pokemon):
        if self.is_knocked_out:
            print("{name} pokemon can not attack because it has been knocked out".format(name = self.name))

        damage = round(self.level * 0.5)

        other_weakness = weaknesses[other_pokemon.type]
        if other_weakness == self.type:
            print("{name} is weak to {type}".format(name=other_pokemon.name, type=self.type))
            damage *= 2

        print("{our_name} hit {other_name} for {damage}".format(our_name = self.name, other_name = other_pokemon.name, damage = damage))
        other_pokemon.lose_health(damage)

class Grass_Pokemon(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Grass Pokemon", "Grass", level)

class Fire_Pokemon(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Fire Pokemon", "Fire", level)

class Water_Pokemon(Pokemon):
    def __init__(self, level = 5):
        super().__init__("Water Pokemon", "Water", level)

# a = Grass_Pokemon()
# b = Fire_Pokemon(10)

# a.attack(b)

# b.attack(a)
# b.attack(a)
# b.attack(a)
# b.attack(a)
# b.attack(a)

class Trainer:
    def __init__(self, pokemon_list, num_potions, name):
        self.pokemon = pokemon_list
        self.potions = num_potions
        self.current_pokemon = 0
        self.name = name

    def switch_active_pokemon(self, new_active):
        if new_active >= len(self.pokemon) or new_active < 0:
            print("Invalid index. Can't switch the pokemon.")
            return
        

        selected = self.pokemon[new_active]     
        if selected.is_knocked_out:
            print("{name} is knocked out. You can't make it your active pokemon".format(name = selected.name))
        elif new_active == self.current_pokemon:
            print("{name} is already your active pokemon".format(name = selected.name))
        else:
            self.current_pokemon = new_active
            print("Go {name}, it's your turn!".format(name = selected.name))

    def use_potion(self):
        if self.potions > 0:
            print("You used a potion on {name}.".format(name = self.pokemon[self.current_pokemon].name))
            self.pokemon[self.current_pokemon].gain_health(20)
            self.potions -= 1
        else:
            print("You don't have any more potions")

    def attack_other_trainer(self, other_trainer):
        print("{trainer} attack {other_trainer}".format(trainer = self.name, other_trainer = other_trainer.name))
        my_pokemon = self.pokemon[self.current_pokemon]
        their_pokemon = other_trainer.pokemon[other_trainer.current_pokemon]
        my_pokemon.attack(their_pokemon)

g1 = Grass_Pokemon()
g2 = Grass_Pokemon()
g3 = Grass_Pokemon()

f1 = Fire_Pokemon()
f2 = Fire_Pokemon()
f3 = Fire_Pokemon()

w1 = Water_Pokemon()
w2 = Water_Pokemon()

t1 = Trainer([g1, g2, f1, w1], 5, "Anne")
t2 = Trainer([g3, f2, f3, w2], 5, "An Thanh")

t2.attack_other_trainer(t1)
t1.switch_active_pokemon(3)
t2.attack_other_trainer(t1)
t1.use_potion()