'''
5. Write a program that takes as input a string and checks whether the string entered is the name of a town
or city known to the program. The towns and cities should include: Dublin, Belfast, Cork, Limerick, Derry,
Galway, Lisburn, Kilkenny, Waterford and Sligo. If the name of one of these towns or cities is entered, the
program should print out the string “You entered x. x is in y.”, where x is the name of the town or city and
y is the province (Ulster, Munster, Leinster or Connacht) in which the town or city is situated. If the string
entered is not recognised, the message “Sorry, I didn’t recognise that name.” should be printed out.
Save this program as p5p5.py.

'''
try_again = True

while try_again == True:
    places_by_province = {
        'Leinster' : ['Dublin', 'Kilkenny', 'Waterford'],
        'Munster' : ['Cork', 'Limerick'],
        'Ulster' : ['Belfast', 'Derry', 'Lisburn'],
        'Connacht' : ['Galway', 'Sligo']}

    input_place = input('Please input a place in Ireland: ')
    place_found = False

    for province, place in places_by_province.items():
        if input_place in place:
            print(f'You entered {input_place}. {input_place} is in {province}')
            place_found = True

    if place_found == False:
        print(f'Sorry, I didn\'t recognise the name. ({input_place})')

    if input('Would you like to try again? (y/n) ').lower() not in ['yes', 'y', 'yeah']:
        try_again = False
        print('Thanks for using my place finder!')