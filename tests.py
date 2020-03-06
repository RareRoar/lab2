import unittest

from os import remove

from sort import create_file, external_sort
from jsonconvert import to_json, from_json
from vector import Vector
from decorator import cashed


class MyTestCase(unittest.TestCase):
    # sort
    def test_sort_input(self):
        with self.assertRaises(FileNotFoundError):
            external_sort("unexciting.txt", 10, "sorted_test_file")

    def test_sort_correctness(self):
        create_file("test_file", 100, -100, 100)
        external_sort("test_file", 10, "sorted_test_file")
        with open("sorted_test_file.txt", 'r') as sorted_test_file:
            buffer_list = []
            for line in sorted_test_file:
                buffer_list.append(int(line.strip()))
                if not buffer_list:
                    self.assertTrue(buffer_list[-2] <= buffer_list[-1])
        remove("test_file.txt")
        remove("sorted_test_file.txt")

    # jsonconvert
    def test_to_json(self):
        self.assertEqual(to_json((4, "word")), "[4, \"word\"]")
        self.assertEqual(to_json({2.3: [1, 2], 4: True}), "{2.3: [1, 2], 4: true}")
        self.assertEqual(to_json([None, False]), "[null, false]")

    def test_from_json(self):
        self.assertEqual(from_json("{\"key:\": \"value,\"}"), {"key:": "value,"})
        self.assertEqual(from_json("[\"word, another word\", 4.3]"), ["word, another word", 4.3])
        self.assertEqual(from_json("[true, false, null]"), [True, False, None])

    def test_from_json_input(self):
        with self.assertRaises(ValueError):
            from_json("{1: 2, 3: 4]")

    # vector
    def test_multiply(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        with self.assertRaises(ValueError): v1 * v2

    def test_scalar(self):
        v1 = Vector(1, 2)
        v2 = Vector(3, 4)
        self.assertEqual(Vector.scalar(v1, v2), 11)

    # decorator
    def test_usage(self):

        @cashed
        def doubling_func(x) -> int:
            return 2 * int(x)

        with self.assertRaises(TypeError):
            doubling_func(1)

    def test_performance(self):
        @cashed
        def doubling_func(x) -> int:
           return 2 * int(x[0])

        self.assertEqual(doubling_func(1), doubling_func(1))


if __name__ == '__main__':
    unittest.main()
