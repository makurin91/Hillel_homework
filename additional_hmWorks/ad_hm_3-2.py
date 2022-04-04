import random

"""
1) Write a function that emulates the game "rock, scissors, paper"
At the entrance, your function accepts your version printed from the console, the computer makes a decision randomly.
"""


def play_game(element):
    game_configurations = ('rock', 'scissors', 'paper')
    if element not in game_configurations:
        return 'Wrong element, enter the correct element'
    else:
        comp_choose = random.choice(game_configurations)
        print('Computer chose: ' + comp_choose)
        my_element_index = game_configurations.index(element)
        comp_element_index = game_configurations.index(comp_choose)
        if game_configurations[my_element_index] == game_configurations[comp_element_index]:
            return 'Computer choose the same element, Try again!'
        elif game_configurations[my_element_index] == game_configurations[comp_element_index - 1]:
            return 'You Win!'
        else:
            return 'You Lose...'


print(play_game(input('Enter your element for playing: ')))

"""
2)Try to imagine a world in which you might have to stay home for (Corona virus) 14 days at any given time.
Do you have enough toilet paper(TP) to make it through?
Although the number of squares per roll of TP varies significantly, we'll assume each roll has 500 sheets,
and the average person uses 57 sheets per day.

Create a function that will receive a dictionary with two key/values:
"people" ⁠— Number of people in the household.
"tp" ⁠— Number of rolls.
Return a statement telling the user if they need to buy more TP!
"""


data = {
    'people': 4,
    'tp': 10
}


def counting_tp(info):
    people, tp = info.get('people'), info.get('tp')
    return 'Need to buy more TP' if people * 57 * 14 > tp * 500 else 'Enough toilet paper, everything is fine'


print(counting_tp(data))
