def union(some_set, some_other_set):
    union_sets = some_set.union(some_other_set)

    print('Union = all the items that exist in bouth sets {}'.
            format(union_sets))


def intersection(some_set, some_other_set):
    intersection_sets = some_set.intersection(some_other_set)

    print('Intersection = common items in the both sets {}'.
            format(intersection_sets))


def diference(some_set, some_other_set):
    diference_sets = some_set.difference(some_other_set)

    print('Diference = items that exist in A but do not exist in B {}'.
            format(diference_sets))


def symmetric(some_set, some_other_set):
    symmetric_sets = some_set.symmetric_difference(some_other_set)

    print('Symmetric difference = all the items that do not belong to both ' \
          'sets at the same time {}'.format(symmetric_sets))


def show_sets(some_set, some_other_set):

    print('These are your lists: set A:{} / set B:{}'.
            format(some_set, some_other_set))
