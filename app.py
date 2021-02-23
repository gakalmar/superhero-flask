import random

import flask

from superheroes import DCSuperHero, Fight

# Create the application.
APP = flask.Flask(__name__)


def create_heroes():
# list our superheroes here
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
    robin = DCSuperHero("Robin", strength=75, powers=["agility"], damagemin=1, damagemax=2)

    all_superheroes =  [superman, batman, catwoman, robin]

    return all_superheroes

all_superheroes = create_heroes()

# this is a "dictionary comprehension" - it's a one-liner of building a dictionary from another iterable
superheroes = {hero.name.lower(): hero for hero in all_superheroes}

@APP.route("/game/")
def first_hero():
    return flask.render_template("index.html", heroes=all_superheroes)

# this is another form of routing:
# <name> is a variable and can be any superhero name
@APP.route("/game/<name>")
def second_hero(name):
    first_hero = superheroes.get(name)
    heroes = all_superheroes
    return flask.render_template("second_hero.html", heroes=heroes, hero1=first_hero)

@APP.route('/game/<hero1>/<hero2>')
def fight(hero1, hero2):
    hero1 = superheroes.get(hero1)
    hero2 = superheroes.get(hero2)
    return flask.render_template("fight.html", hero1=hero1, hero2=hero2)


@APP.route('/game/fight/<hero1>/<hero2>')
def start_fight(hero1, hero2):
    hero1 = superheroes.get(hero1.lower())
    hero2 = superheroes.get(hero2.lower())

    fight = Fight(hero1, hero2).start()
    return flask.render_template("after_fight.html", hero1=hero1, hero2=hero2)


if __name__ == "__main__":
    APP.debug = True
    APP.run()
