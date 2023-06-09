'''
Доработать класс FlatIterator в коде ниже. Должен получиться итератор, 
который принимает список списков и возвращает их плоское представление, 
т. е. последовательность, состоящую из вложенных элементов. Функция test 
в коде ниже также должна отработать без ошибок.
'''

class FlatIterator:

    def __init__(self, list_of_lists):
            self.list_of_lists = list_of_lists

    def __iter__(self):
        self.list_of_lists_cursor = 0 
        self.inner_list_cursor = -1  
        return(self)

    def __next__(self):
        self.inner_list_cursor += 1
        
        if self.inner_list_cursor == len(self.list_of_lists[self.list_of_lists_cursor]):
            self.list_of_lists_cursor += 1
            self.inner_list_cursor = 0
        
        if self.list_of_lists_cursor == len(self.list_of_lists):
            raise StopIteration

        return self.list_of_lists[self.list_of_lists_cursor][self.inner_list_cursor]




def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()