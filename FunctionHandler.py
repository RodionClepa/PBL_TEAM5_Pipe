import sys

class FunctionHandler:
    def __init__(self):
        self.function_map = {
            "removeAllZero": self.removeAllZero,
            "filterPositive": self.filterPositive,
            "filterNegative": self.filterNegative,
            "filterEven": self.filterEven,
            "filterOdd": self.filterOdd,
            "squareAll": self.square,
            "doubleAll": self.double,
            "toString": self.toString,
            "sum": self.sum,
            "average": self.average,
            "findMin": self.findMin,
            "findMax": self.findMax,
            "arr2Str": self.arr2Str,
            "abs": self.abs,
            "increment": self.increment,
            "decrement": self.decrement,
            "multiply": self.multiply,
            "division": self.division,
            "sortAscending": self.sortAscending,
            "sortDescending": self.sortDescending,
            # ------------------------------------- String ------------------------------------------
            "split": self.split,
            "substring": self.substring,
            "replaceAll": self.replaceAll,
            "replaceFirst": self.replaceFirst,
            "toLowerCase": self.toLowerCase,
            "toUpperCase": self.toUpperCase,
            "capitalize": self.capitalize,
            "trim": self.trim,
            "trimStart": self.trimStart,
            "trimEnd": self.trimEnd
        }

        self.added_functions_map = {}

    def add_function(self, function_name, function):
        self.added_functions_map[function_name] = function

    def execute(self, var, function_name, args):
        if function_name in self.function_map:
            function = self.function_map[function_name]
            expected_args = function.__code__.co_argcount - 2
            if expected_args != len(args):
                raise Exception(f"Expected {expected_args} arguments, but got {len(args)}")
            if args:
                return function(var, *args)
            return function(var)

        if function_name in self.added_functions_map:
            function = self.added_functions_map[function_name]
            expected_args = function.__code__.co_argcount - 1
            if expected_args != len(args):
                raise Exception(f"Expected {expected_args} arguments, but got {len(args)}")
            if args:
                return function(var, *args)
            return function(var)

        raise Exception(f"Function {function_name} not found")

    def removeAllZero(self, arr):
        if isinstance(arr, list):
            return [x for x in arr if x != 0]
        raise Exception("Input must be an array")

    def filterPositive(self, arr):
        if isinstance(arr, list):
            return [x for x in arr if x > 0]
        raise Exception("Input must be an array")

    def filterNegative(self, arr):
        if isinstance(arr, list):
            return [x for x in arr if x < 0]
        raise Exception("Input must be an array")

    def filterEven(self, arr):
        if isinstance(arr, list):
            return [x for x in arr if x % 2 == 0]
        raise Exception("Input must be an array")

    def filterOdd(self, arr):
        if isinstance(arr, list):
            return [x for x in arr if x % 2 != 0]
        raise Exception("Input must be an array")

    def square(self, arr):
        if isinstance(arr, list):
            return [x ** 2 for x in arr]
        raise Exception("Input must be an array")

    def double(self, arr):
        if isinstance(arr, list):
            return [x * 2 for x in arr]
        raise Exception("Input must be an array")

    def toString(self, arr):
        if isinstance(arr, list):
            return [str(x) for x in arr]
        raise Exception("Input must be an array")

    def sum(self, arr):
        if isinstance(arr, list):
            return sum(arr)
        raise Exception("Input must be an array")

    def average(self, arr):
        if isinstance(arr, list):
            return sum(arr) / len(arr)
        raise Exception("Input must be an array")

    def findMin(self, arr):
        if isinstance(arr, list):
            return min(arr)
        raise Exception("Input must be an array")

    def findMax(self, arr):
        if isinstance(arr, list):
            return max(arr)
        raise Exception("Input must be an array")

    def arr2Str(self, arr):
        if isinstance(arr, list):
            return "".join([str(x) for x in arr])
        raise Exception("Input must be an array")

    def abs(self, arr):
        if isinstance(arr, list):
            return [abs(x) for x in arr]
        raise Exception("Input must be an array")

    def increment(self, arr, n=1):
        if not isinstance(n, int) and not isinstance(n, float):
            raise Exception("Function argument must be a number")
        if isinstance(arr, list):
            return [x + n for x in arr]
        raise Exception("Input must be an array")

    def decrement(self, arr, n=1):
        if not isinstance(n, int) and not isinstance(n, float):
            raise Exception("Function argument must be a number")
        if isinstance(arr, list):
            return [x - n for x in arr]
        raise Exception("Input must be an array")

    def multiply(self, arr, n):
        if not isinstance(n, int) and not isinstance(n, float):
            raise Exception("Function argument must be a number")
        if isinstance(arr, list):
            return [x * n for x in arr]
        raise Exception("Input must be an array")

    def division(self, arr, n):
        if not isinstance(n, int) and not isinstance(n, float):
            raise Exception("Function argument must be a number")
        if isinstance(arr, list):
            return [x / n for x in arr]
        raise Exception("Input must be an array")

    def sortAscending(self, arr):
        if isinstance(arr, list):
            return sorted(arr)
        raise Exception("Input must be an array")

    def sortDescending(self, arr):
        if isinstance(arr, list):
            return sorted(arr, reverse=True)
        raise Exception("Input must be an array")

    # ------------------------------------- String ------------------------------------------

    def split(self, string, separator):
        if isinstance(string, str):
            return string.split(separator)
        raise Exception("Input must be a string")

    def substring(self, string, start, end):
        if isinstance(string, str):
            return string[start:end]
        if not isinstance(start, int) or not isinstance(end, int) or isinstance(start, float) or isinstance(end, float):
            raise Exception("Start and end must be integers")
        raise Exception("Input must be a string")

    def replaceAll(self, string, old, new):
        if isinstance(string, str):
            string = string.replace("5", "a")
            return string.replace(old, new)
        raise Exception("Input must be a string")

    def replaceFirst(self, string, old, new):
        if isinstance(string, str):
            return string.replace(old, new, 1)
        raise Exception("Input must be a string")

    def toLowerCase(self, string):
        if isinstance(string, str):
            return string.lower()
        raise Exception("Input must be a string")

    def toUpperCase(self, string):
        if isinstance(string, str):
            return string.upper()
        raise Exception("Input must be a string")

    def capitalize(self, string):
        if isinstance(string, str):
            return string.capitalize()
        raise Exception("Input must be a string")

    def trim(self, string):
        if isinstance(string, str):
            return string.strip()
        raise Exception("Input must be a string")

    def trimStart(self, string):
        if isinstance(string, str):
            return string.lstrip()
        raise Exception("Input must be a string")

    def trimEnd(self, string):
        if isinstance(string, str):
            return string.rstrip()
        raise Exception("Input must be a string")