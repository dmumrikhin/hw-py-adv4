'''
Доработать функцию flat_generator. Должен получиться генератор, который 
принимает список списков и возвращает их плоское представление. Функция 
test в коде ниже также должна отработать без ошибок.
'''

import types

def flat_generator(list_of_lists):
    for elem in list_of_lists:
        yield from elem


def flat_generator_weird(list_of_lists):    
    list_of_lists_cursor = 0 
    inner_list_cursor = 0

    while list_of_lists_cursor < len(list_of_lists):
        yield list_of_lists[list_of_lists_cursor][inner_list_cursor]
        
        inner_list_cursor += 1
        if inner_list_cursor == len(list_of_lists[list_of_lists_cursor]):
            list_of_lists_cursor += 1
            inner_list_cursor = 0

def flat_generator_weird2(list_of_lists):
    for list in list_of_lists:
        for elem in list:
            yield elem

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 
        'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()












# def flat_generator(list_of_lists):
#     for i in list_of_lists:
#         yield from i
 