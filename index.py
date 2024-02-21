# import the python datetime module to help us create a timestamp
from datetime import date
from slithering import Groundhog, Lizard, PrairieDog, Scorpion, Snake
from swimming import Duck, Fish, Frog, Swan, Turtle
from walking import Goat, Horse, Llama, Pig, Rabbit


# //mm PETTING AREA


miss_fuzz = Llama("Miss fuzz", "domestic llama", "morning", "llama chow")
print(
    f"{miss_fuzz.name} the {miss_fuzz.species} is available to pet during the {miss_fuzz.shift} shift."
)
print(miss_fuzz.feed())
print(miss_fuzz)

#####

mister_horse = Horse("Mister Horse", "clydesdale", "midday", "horse chow")
print(
    f"{mister_horse.name} the {mister_horse.species} is available to pet during the {mister_horse.shift} shift."
)
print(mister_horse.feed())
print(mister_horse)

#####

miss_piggy = Pig("Miss Piggy", "wild boar", "afternoon", "pig chow")
print(
    f"{miss_piggy.name} the {miss_piggy.species} is available to pet during the {miss_piggy.shift} shift."
)
print(miss_piggy.feed())
print(miss_piggy)

#####

tin_can = Goat("Tin Can", "billy goat", "morning", "goat chow")
print(
    f"{tin_can.name} the {tin_can.species} is available to pet during the {tin_can.shift} shift."
)
print(tin_can.feed())
print(tin_can)

#####

peter_cottontail = Rabbit(
    "Peter Cottontail", "flemish giant", "afternoon", "rabbit chow"
)
print(
    f"{peter_cottontail.name} the {peter_cottontail.species} is available to pet during the {peter_cottontail.shift} shift."
)
print(peter_cottontail.feed())
print(peter_cottontail)

#####

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
