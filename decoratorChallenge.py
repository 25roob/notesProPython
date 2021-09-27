import random

main_options = ['pizza', 'hot-dogs', 'tacos', 'burgers']

def misteryDinner(func):
    """Funcion decoradora para agregar opciones extra para elegir la cena"""
    def wrapper(options):
        mOptions = ['soup', 'sushi', 'filete', 'quesadillas']
        options.extend(mOptions)
        
        return func(options)

    return wrapper

@misteryDinner
def randomDinner(options):
    "Funcion que nos ayuda a elegir la cena"
    return random.choice(options)
    
print(randomDinner(main_options))