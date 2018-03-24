from defs import union, intersection, diference, symmetric, show_sets


def menu(some_set, some_other_set):
    while True:
        try:
            user_sets = int(input('''
                            What do yo want to do whit your lists?
                            1 Union
                            2 Intersection
                            3 Diference
                            4 Simetric diference
                            0 Out
                            '''))

            if user_sets == 1:
                show_sets(some_set, some_other_set)
                union(some_set, some_other_set)

            elif user_sets == 2:
                intersection(some_set, some_other_set)
                show_sets(some_set, some_other_set)

            elif user_sets == 3:
                show_sets(some_set, some_other_set)
                diference(some_set, some_other_set)

            elif user_sets == 4:
                show_sets(some_set, some_other_set)
                symmetric(some_set, some_other_set)

            elif user_sets == 0:
                print('Ok, se you around...')
                break

            else:
                print('Give me a valid option')
        
        except ValueError:
            print('Write just integer numbers')
