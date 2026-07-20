import alchemy

alchemy.elements.create_air()
print(alchemy.create_air())
try:
    create_earth()
except AttributeError as e:
    print(type(e))
