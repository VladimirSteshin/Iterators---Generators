from more_itertools import collapse


class FlatList:
    def __init__(self, lst):
        self.list = lst

    def __iter__(self):
        it = iter(self.list)
        self.flat = collapse(it)
        return self

    def __next__(self):
        el = next(self.flat)
        return el


def flat_generator(lst):
    for arr in lst:
        for item in arr:
            yield item


if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None]
    ]

    for item in FlatList(nested_list):
        print(item)

    flat_list = [item for item in FlatList(nested_list)]
    print(flat_list)

    for item in flat_generator(nested_list):
        print(item)
