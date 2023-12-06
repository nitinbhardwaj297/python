def personalized_message(names, greet):
    for name in names:
        print(f"{greet},{name}!")
name_list=['nitin', 'mukul']
greet='Hello'
personalized_message(name_list,greet)