def calculate_pairs(book_list, pairs=[]):
    book_list = list(filter(lambda a: a != 0, book_list))
    if len(book_list) != 0:
        pairs.append(len(book_list))
        book_list = list(map(lambda a: a-1, book_list))
        calculate_pairs(book_list, pairs)
    return pairs

def reevaluate_pairs(pairs):
    threes = len(list(filter(lambda a: a == 3, pairs)))
    fives = len(list(filter(lambda a: a == 5, pairs)))
    leftover = list(filter(lambda a: a != 5 and a!= 3, pairs))
    diff = fives - threes
    if diff < 0:
        leftover.extend([3]*-diff)
        fours = fives
    else:
        leftover.extend([5]*diff)
        fours = threes
    leftover.extend([4]*fours*2)
    return leftover

def calc_price(pairs):
    price = 0
    for pair in pairs:
        if pair == 1:
            price+= 8
        elif pair == 2:
            price+= 15.2
        elif pair == 3:
            price+= 21.6
        elif pair == 4:
            price+= 25.6
        elif pair == 5:
            price+= 30.0
    return price

# def cost():
#     b1 = int(input('Enter quantity of first book: '))
#     b2 = int(input('Enter quantity of second book: '))
#     b3 = int(input('Enter quantity of third book: '))
#     b4 = int(input('Enter quantity of fourth book: '))
#     b5 = int(input('Enter quantity of fifth book: '))
#     book_list = [b1, b2, b3, b4, b5]
#     pairs = calculate_pairs(book_list)
#     print("pairs",pairs)
#     reevaluated_pairs = reevaluate_pairs(pairs)
#     print("reevaluated_pairs",reevaluated_pairs)
#     price = calc_price(reevaluated_pairs)
#
#     print('The discounted price of the basket is: {} EUR'.format(price))
#
#
# if __name__ == '__main__':
#     cost()

import unittest

class TestSumAferDiscount(unittest.TestCase):

    def test_one(self):
        book_list = [1, 2, 3, 4, 5]
        pairs = calculate_pairs(book_list, pairs=[])
        reevaluated_pairs = reevaluate_pairs(pairs)
        price = calc_price(reevaluated_pairs)
        self.assertEqual(price, 100.0)

    def test_two(self):
        book_list = [2, 2, 2, 1, 1]
        pairs = calculate_pairs(book_list, pairs=[])
        reevaluated_pairs = reevaluate_pairs(pairs)
        price = calc_price(reevaluated_pairs)
        self.assertEqual(price, 51.20)

    def test_three(self):
        book_list = [0, 1, 1, 2, 0]
        pairs = calculate_pairs(book_list, pairs=[])
        reevaluated_pairs = reevaluate_pairs(pairs)
        price = calc_price(reevaluated_pairs)
        self.assertEqual(price, 29.6)

    def test_four(self):
        book_list = [0, 1, 0, 0, 0]
        pairs = calculate_pairs(book_list, pairs=[])
        reevaluated_pairs = reevaluate_pairs(pairs)
        price = calc_price(reevaluated_pairs)
        self.assertEqual(price, 8)

if __name__ == '__main__':
    unittest.main()
