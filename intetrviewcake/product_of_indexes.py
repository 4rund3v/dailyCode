"""
You have a list of integers, and for each index you want to find the product of every integer except the integer at that index.

Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Here's the catch: You can't use division in your solution!
"""

import unittest


def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

        # We make a list with the length of the input list to
        # hold our products

    products_of_all_ints_except_at_index = [None] * len(int_list)
    # Make a list with the products

    product_so_far = 1
    for i in xrange(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in xrange(len(int_list) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]
    return products_of_all_ints_except_at_index

"""
Breakdown
A brute force approach would use two loops to multiply the integer at every index by the integer at every nested_index, unless index == nested_index.

This would give us a runtime of O(n^2). Can we do better?

Well, we’re wasting a lot of time doing the same calculations. As an example, let's take:

  # Input list
[1, 2, 6, 5, 9]

# List of the products of all integers
# except the integer at each index:
[540, 270, 90, 108, 60]  # [2 * 6 * 5 * 9,  1 * 6 * 5 * 9,  1 * 2 * 5 * 9,  1 * 2 * 6 * 9,  1 * 2 * 6 * 5]

We're doing some of the same multiplications two or three times!

When we calculate [2*6*5*9, 1*6*5*9, 1*2*5*9, 1*2*6*9, 1*2*6*5], we're calculating 5*9 three times: at indices 0, 1, and 2.
Or look at this pattern:

When we calculate [2*6*5*9, 1*6*5*9, 1*2*5*9, 1*2*6*9, 1*2*6*5], we have 1 in index 1, and we calculate 1*2 at index 2,
 1*2*6 at index 3, and 1*2*6*5 at index 4.
We’re redoing multiplications when instead we could be storing the results! This would be a great time to use a greedy ↴ approach. We could store the results of each multiplication highlighted in blue, then just multiply by one new integer each time.

So in the last highlighted multiplication, for example, we wouldn’t have to multiply 1*2*6 again.
 If we stored that value (12) from the previous multiplication, we could just multiply 12*5.

Can we break our problem down into subproblems so we can use a greedy approach?

Let's look back at the last example:

When we calculate [2*6*5*9, 1*6*5*9, 1*2*5*9, 1*2*6*9, 1*2*6*5], we have 1 in index 1, and we calculate 1*2 at index 2, 1*2*6 at index 3, and 1*2*6*5 at index 4.
What do all the highlighted multiplications have in common?

They are all the integers that are before each index in the input list ([1, 2, 6, 5, 9][1,2,6,5,9]). For example, the highlighted multiplication at index 3 (1*2*61∗2∗6) is all the integers before index 3 in the input list.

In the pattern where we calculate 1*2 at index 2, 1*2*6 at index 3, and 1*2*6*5 at index 4, each calculation is the product of all the numbers before the number at that index. For example, 5 is at index 3, and 1*2*6 is the product of all the numbers before 5 in the input array.
Do all the multiplications that aren't highlighted have anything in common?

Yes, they're all the integers that are after each index in the input list!

Knowing this, can we break down our original problem to use a greedy approach?

The product of all the integers except the integer at each index can be broken down into two pieces:

the product of all the integers before each index, and
the product of all the integers after each index.
To start, let's just get the product of all the integers before each index.

How can we do this? Let's take another example:

  # Input list
[3, 1, 2, 5, 6, 4]

# Multiplication of all integers before each index
# (we give index 0 a value of 1 since it has no integers before it)
[1, 3,  3 * 1,  3 * 1 * 2, 3 * 1 * 2 * 5,  3 * 1 * 2 * 5 * 6]

# Final list of the products of all the integers before each index
[1, 3, 3, 6, 30, 180]

Notice that we're always adding one new integer to our multiplication for each index!

So to get the products of all the integers before each index, we could greedily store each product so far and multiply that by the next integer. Then we can store that new product so far and keep going.

So how can we apply this to our input list?

Let’s make a list products_of_all_ints_before_index:

  products_of_all_ints_before_index = [None] * len(int_list)

# For each integer, find the product of all the integers
# before it, storing the total product so far each time
product_so_far = 1
for i in xrange(len(int_list)):
    products_of_all_ints_before_index[i] = product_so_far
    product_so_far *= int_list[i]

So we solved the subproblem of finding the products of all the integers before each index. Now, how can we find the products of all the integers after each index?

It might be tempting to make a new list of all the values in our input list in reverse, and just use the same function we used to find the products before each index.

Is this the best way?

This method will work, but:

We'll need to make a whole new list that's basically the same as our input list. That's another O(n)O(n) memory cost!
To keep our indices aligned with the original input list, we'd have to reverse the list of products we return. That's two reversals, or two O(n)O(n) operations!
Is there a cleaner way to get the products of all the integers after each index?

We can just walk through our list backwards! So instead of reversing the values of the list, we'll just reverse the indices we use to iterate!

  products_of_all_ints_after_index = [None] * len(int_list)

product_so_far = 1
for i in xrange(len(int_list) - 1, -1, -1):
    products_of_all_ints_after_index[i] = product_so_far
    product_so_far *= int_list[i]

Now we've got products_of_all_ints_after_index, but we’re starting to build a lot of new lists. And we still need our final list of the total products. How can we save space?

Let’s take a step back. Right now we’ll need three lists:

products_of_all_ints_before_index
products_of_all_ints_after_index
products_of_all_ints_except_at_index
To get the first one, we keep track of the total product so far going forwards, and to get the second one, we keep track of the total product so far going backwards. How do we get the third one?

Well, we want the product of all the integers before an index and the product of all the integers after an index. We just need to multiply every integer in products_of_all_ints_before_index with the integer at the same index in products_of_all_ints_after_index!

Let's take an example. Say our input list is [2, 4, 10][2,4,10]:

We'll calculate products_of_all_ints_before_index as:

If the input list is [2, 4, 10], the product of all the numbers before each index is [1, 2, 8]
And we'll calculate products_of_all_ints_after_index as:

If the input list is [2, 4, 10], the product of all the numbers after each index is [40, 10, 1]
If we take these lists and multiply the integers at the same indices, we get:

The product of all the numbers before an index times the product of all the numbers after an index is the product of the numbers at all other indices: 1*40=40, 2*10=20, 8*1=8.
And this gives us what we're looking for—the products of all the integers except the integer at each index.

Knowing this, can we eliminate any of the lists to reduce the memory we use?

Yes, instead of building the second list products_of_all_ints_after_index, we could take the product we would have stored and just multiply it by the matching integer in products_of_all_ints_before_index!

So in our example above, when we calculated our first (well, "0th") "product after index" (which is 40), we’d just multiply that by our first "product before index" (1) instead of storing it in a new list.

How many lists do we need now?

Just one! We create a list, populate it with the products of all the integers before each index, and then multiply those products with the products after each index to get our final result!

products_of_all_ints_before_index now contains the products of all the integers before and after every index, so we can call it products_of_all_ints_except_at_index!

Almost done! Are there any edge cases we should test?

What if the input list contains zeroes? What if the input list only has one integer?

We'll be fine with zeroes.

But what if the input list has fewer than two integers?

Well, there won't be any products to return because at any index there are no “other” integers. So let's raise an exception.

Solution
To find the products of all the integers except the integer at each index, we'll go through our list greedily ↴ twice. First we get the products of all the integers before each index, and then we go backwards to get the products of all the integers after each index.

When we multiply all the products before and after each index, we get our answer—the products of all the integers except the integer at each index!

  def get_products_of_all_ints_except_at_index(int_list):
    if len(int_list) < 2:
        raise IndexError('Getting the product of numbers at other '
                         'indices requires at least 2 numbers')

    # We make a list with the length of the input list to
    # hold our products
    products_of_all_ints_except_at_index = [None] * len(int_list)

    # For each integer, we find the product of all the integers
    # before it, storing the total product so far each time
    product_so_far = 1
    for i in xrange(len(int_list)):
        products_of_all_ints_except_at_index[i] = product_so_far
        product_so_far *= int_list[i]

    # For each integer, we find the product of all the integers
    # after it. since each index in products already has the
    # product of all the integers before it, now we're storing
    # the total product of all other integers
    product_so_far = 1
    for i in xrange(len(int_list) - 1, -1, -1):
        products_of_all_ints_except_at_index[i] *= product_so_far
        product_so_far *= int_list[i]

    return products_of_all_ints_except_at_index

Complexity
O(n)O(n) time and O(n)O(n) space. We make two passes through our input a list, and the list we build always has the same length as the input list.

Bonus
What if you could use division? Careful—watch out for zeroes!

What We Learned
Another question using a greedy ↴ approach. The tricky thing about this one: we couldn't actually solve it in one pass. But we could solve it in two passes!

This approach probably wouldn't have been obvious if we had started off trying to use a greedy approach.

Instead, we started off by coming up with a slow (but correct) brute force solution and trying to improve from there. We looked at what our solution actually calculated, step by step, and found some repeat work. Our final answer came from brainstorming ways to avoid doing that repeat work.

So that's a pattern that can be applied to other problems:

Start with a brute force solution, look for repeat work in that solution, and modify it to only do that work once.

"""
# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)