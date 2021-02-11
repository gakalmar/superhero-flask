import random

# this is a class
class SuperHero:
    # this is the "constructor" method - the __init__ method
    def __init__(self, name, powers, strength, damagemin, damagemax, legal_name=None):
        self.name = name
        self.powers = powers
        self.legal_name = legal_name
        self.strength = strength
        self.life = 20
        self.max_life = 20
        self.damagemin = damagemin
        self.damagemax = damagemax

        self.description = (
            self.name + " has the following powers: " + ", ".join(self.powers)
        )
        if self.legal_name is not None:
            self.description += " and their legal name is " + self.legal_name

    # this is an "instance method"
    def get_description(self):
        return self.description

    # the hero should say something
    def speak(self):
        intros = [f"Hi, I'm {self.name} and I will kick your ass!", "I am darkness!"]
        print(random.choice(intros))

    # this function should reset the hero's life back to it's maximum level
    def go_to_hospital(self):
        print(f"{self.name} went to the hospital, now he feels ready to fight again!")
        self.life = self.max_life


# another approach is to create a Fight class:
class Fight:
    def __init__(self, player_one, player_two):
        self.p1 = player_one
        self.p2 = player_two
        self.has_ended = False
        self.result = None

    def start(self):
        if self.has_ended:
            print("This fight is over. If you want to fight again, start a new fight!")
            return

        def check_if_anyone_is_sick():
            result = None
            if self.p1.life <= self.p1.max_life // 5:
                result = self.p1
            elif self.p2.life <= self.p2.max_life // 5:
                result = self.p2
            return result

        sick_hero = check_if_anyone_is_sick()

        if sick_hero is not None:
            print(f"They will not fight - {sick_hero.name} is too sick ☹️ ")
            print("They will have to go to the hospital 🏥 🚑 👩‍⚕️")
            return

        print(f"Friendly fight: {self.p1.name} VS {self.p2.name}")
        print("----------------------------------------------------------")

        # Fight scene starts here:
        round_number = 1
        print(f"{self.p1.name} will start the battle!")
        while (self.p1.strength and self.p2.strength) > 0:
            self.p1.damage = random.randint(self.p1.damagemin, self.p1.damagemax)
            self.p2.damage = random.randint(self.p2.damagemin, self.p2.damagemax)

            print(f"----------------------------------------------------------")
            print(f"Round {round_number}... FIGHT!!")

            self.p2.life -= self.p1.damage
            print(
                f"{self.p1.name} damages {self.p1.damage}. {self.p2.name} now has {self.p2.life} lifepoints left..."
            )
            if self.p2.life <= 0:
                return f"{self.p1.name} has won the battle!!! It's time for someone to take {self.p2.name} to the hospital!"

            self.p1.life -= self.p2.damage
            print(
                f"{self.p2.name} damages {self.p2.damage}. {self.p1.name} now has {self.p1.life} lifepoints left..."
            )
            if self.p1.life <= 0:
                return f"{self.p2.name} has won the battle!!! It's time for someone to take {self.p2.name} to the hospital!"

            self.print_health_points()

            keep_fighting = input(
                "Press 'n' to give up, press any other key to continue"
            )
            if keep_fighting == "n":
                print("It's getting too dangerous, the fight has been postponed!")
                self.has_ended = True
                break
            else:
                round_number += 1

    def print_health_points(self):
        print(f"{self.p1.name} has {self.p1.life} health points left")
        print(f"{self.p1.life * '💚'}{(self.p1.max_life - self.p1.life) * '💔'}")
        print()
        print(f"{self.p2.name} has {self.p2.life} health points left")
        print(f"{self.p2.life * '💚'}{(self.p2.max_life - self.p2.life) * '💔'}")


# a class can inherit from another class:
# in this case, the DCSuperHero class inherits from the SuperHero class
class DCSuperHero(SuperHero):
    def get_description(self):
        return self.description + " and they are part of the DC universe"


if __name__ == "__main__":
    superman = DCSuperHero(
        "Superman",
        strength=93,
        powers=["x-ray vision", "flying", "super strength"],
        damagemin=3,
        damagemax=8,
    )
    batman = DCSuperHero(
        "Batman", strength=85, powers=["lots of money"], damagemin=4, damagemax=6
    )
    catwoman = DCSuperHero(
        "Catwoman", strength=88, powers=["speed", "agility"], damagemin=1, damagemax=8
    )
    robin = DCSuperHero(
        "Robin", strength=75, powers=["agility"], damagemin=1, damagemax=2
    )


# https://realpython.com/python3-object-oriented-programming/
