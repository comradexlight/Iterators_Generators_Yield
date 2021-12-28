nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None],
]


# 1. Написать итератор, который принимает список списков, и возвращает их плоское представление, т.е последовательность состоящую из вложенных элементов.

class FlatIterator:
    def __init__(self, nested_lst):
        self.main_list = [el for lst in nested_lst for el in lst]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        if self.cursor == len(self.main_list) - 1:
            raise StopIteration

        self.cursor += 1
        return self.main_list[self.cursor]


for x in FlatIterator(nested_list):
    print(x)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


# 2. Написать генератор, который принимает список списков, и возвращает их плоское представление.

def flat_generator(nested_lst):
    for item in nested_lst:
        for lst in item:
            yield lst


for item in flat_generator(nested_list):
    print(item)


# 3.* Написать итератор аналогичный итератору из задания 1, но обрабатывающий списки с любым уровнем вложенности

class FlatIterator:
    def __init__(self, nested_lst):
        self.nested_lst = nested_lst

    def __iter__(self):
        self.iter_items_stack = [iter(self.nested_lst)]
        return self

    def __next__(self):
        while self.iter_items_stack:
            try:
                item = next(self.iter_items_stack[-1])
            except StopIteration:
                self.iter_items_stack.pop()
                continue
            if isinstance(item, list):
                self.iter_items_stack.append(iter(item))
                continue
            else:
                return item
        raise StopIteration


for x in FlatIterator(nested_list):
    print(x)
flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)


# 4.* Написать генератор аналогичный генератор из задания 2, но обрабатывающий списки с любым уровнем вложенности

def flat_really_generator(nested_lst):
    for item in nested_lst:
        if isinstance(item, list):
            for lst in flat_really_generator(item):
                yield lst
        else:
            yield item


for item in flat_really_generator(nested_list):
    print(item)
