import random

def main():

# create mark, count and list
    again = True
    count = 0
    mylist = []
# U.S. states and capitals
    U_S = {'alaska': 'juneau', 'arizona': 'phoenix', 'colorado': 'denver', 'delaware': 'dover',
           'idaho': 'boise', 'illinois': 'springfield', 'kansas': 'topeka', 'missouri': 'jefferson city',
           'alabama': 'montgomery', 'arkansas': 'little rock', 'california': 'sacramento', 'florida': 'tallahassee'}

    print("lets play game . rules are simple , if you guess U.S. states capital you won . "
          "u need to guess 10 capitals .")

    while again:
        # to randomize states
        for i in U_S.keys():
            mylist.append(i)
        random.shuffle(mylist)
        # list to str
        state = mylist[1]

        # we need user answer bruh
        user_answer = input(f"{state}'s capital is ")
        # to compare capitals
        right_an = U_S.get(state)
        if user_answer.lower() == right_an:
            count += 1
            if count > 10:
                again = False
                print('gg you won ')
        else:
            again = False
            print(f'total is {count} right answers')

main()