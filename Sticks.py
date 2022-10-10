import random

# initial list
sticks = ['-', '--', '---', '----']

#shuffling the list
def mix_listed(ori_list):
    random.shuffle(ori_list)
    return ori_list

#choose your number
def luck_trying():
    my_trial = ''
    while my_trial not in ['1', '2', '3', '4']:
        my_trial = input("Choosing a number: ")

    return int(my_trial)

try1 = luck_trying()
print(try1)

#checking the trials of the players
def verify_try(alist, a_try):
    if alist[a_try -1] == '-':
        print("Wash the dishes")
    else:
        print("This time your safe")
    print(f"You got {alist[a_try - 1]}")

mixed_sticks = mix_listed(sticks)
selection = luck_trying()
verify_try(mixed_sticks, selection)
