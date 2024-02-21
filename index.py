# import the python datetime module to help us create a timestamp
from datetime import date
from slithering import Groundhog, Lizard, PrairieDog, Scorpion, Snake
from swimming import Duck, Fish, Frog, Swan, Turtle
from walking import Goat, Horse, Llama, Pig, Rabbit


# //mm PETTING AREA


miss_fuzz = Llama("Miss fuzz", "domestic llama", "morning")
print(
    f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift."
)

mister_horse = Horse("Mister Horse", "clydesdale", "midday")
print(
    f"{mister_horse.name} the {mister_horse.species} is available to pet during the {mister_horse.shift} shift."
)

miss_piggy = Pig("Miss Piggy", "wild boar", "afternoon")
print(
    f"{miss_piggy.name} the {miss_piggy.species} is available to pet during the {miss_piggy.shift} shift."
)

tin_can = Goat("Tin Can", "billy goat", "morning")
print(
    f"{tin_can.name} the {tin_can.species} is available to pet during the {tin_can.shift} shift."
)

peter_cottontail = Rabbit("Peter Cottontail", "flemish giant", "afternoon")
print(
    f"{peter_cottontail.name} the {peter_cottontail.species} is available to pet during the {peter_cottontail.shift} shift."
)


# //mm POND AREA


hoppy = Frog("Hoppy", "bullfrog")

myrtle = Turtle("Myrtle", "box turtle")

nemo = Fish("Nemo", "clownfish")

daffy = Duck("Daffy", "mallard")

swimmy = Swan("Swimmy", "giant swan")


# //mm TANK AREA

kevin = PrairieDog("Kevin", "texas prairie")

stretch = Snake("Stretch", "gardener snake")

stingy = Scorpion("Stingy", "desert scorpion")

larry = Lizard("Larry", "chameleon")

grindhouse = Groundhog("Grindhouse", "grind hog")
