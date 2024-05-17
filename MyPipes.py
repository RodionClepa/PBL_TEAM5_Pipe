class myPipe():
    def __init__(self, varName, var, typeVar):
        self.debugWork = False
        self.varName = varName
        self.var = var
        self.type = typeVar
        self.pipeFunctions = []
        self.function_map = {
            "someFunctionName1": self.someFunctionName1,
            "someFunctionName2": self.someFunctionName2,
            "removeAllZero": self.removeAllZero,
            "filterPositive": self.filterPositive,
            "filterNegative": self.filterNegative,
            "filterEven": self.filterEven,
            "filterOdd": self.filterOdd,
            "mapSquare": self.mapSquare,
            "mapDouble": self.mapDouble,
            "mapToString": self.mapToString,
            "sum": self.sum,
            "average": self.average,
            "findMin": self.findMin,
            "findMax": self.findMax,
            "arr2Str": self.arr2Str,
            "allAbs": self.allAbs,
            "increment": self.increment,
            "decrement": self.decrement,
            "multiply": self.multiply,
            "division": self.division,
            # ------------------------------------- String ------------------------------------------
            "sortAscending": self.sortAscending,
            "sortDescending": self.sortDescending,
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
    
    def addPipeFunctions(self, functionName, params):
        self.pipeFunctions.append({
            "functionName": functionName,
            "params": params
        })

    # Define functions to be executed
    def someFunctionName1(self):
        if self.debugWork == True:
            print(self.var)

    def someFunctionName2(self):
        if self.debugWork == True:
            print(self.var)
    
    # ---------------------------------------------- Array -------------------------------
    def removeAllZero(self):
        if not isinstance(self.var, list):
            raise Exception("removeAllZero work only with arrays")
        filtered_array = [i for i in self.var if i != 0]
        self.var = filtered_array.copy()
        if self.debugWork == True:
            print(self.var)

    def filterPositive(self):
        if not isinstance(self.var, list):
            raise Exception("filterPositive works only with arrays")
        filtered_array = [i for i in self.var if i > 0]
        self.var = filtered_array.copy()
        if self.debugWork == True:
            print(self.var)

    def filterNegative(self):
        if not isinstance(self.var, list):
            raise Exception("filterNegative works only with arrays")
        filtered_array = [i for i in self.var if i < 0]
        self.var = filtered_array.copy()
        if self.debugWork == True:
            print(self.var)

    def filterEven(self):
        if not isinstance(self.var, list):
            raise Exception("filterEven works only with arrays")
        filtered_array = [i for i in self.var if i % 2 == 0]
        self.var = filtered_array.copy()
        if self.debugWork == True:
            print(self.var)

    def filterOdd(self):
        if not isinstance(self.var, list):
            raise Exception("filterOdd works only with arrays")
        filtered_array = [i for i in self.var if i % 2 != 0]
        self.var = filtered_array.copy()
        if self.debugWork == True:
            print(self.var)
    
    def mapSquare(self):
        if not isinstance(self.var, list):
            raise Exception("mapSquare works only with arrays")
        self.var = [num ** 2 for num in self.var]
        if self.debugWork == True:
            print(self.var)

    def mapDouble(self):
        if not isinstance(self.var, list):
            raise Exception("mapDouble works only with arrays")
        self.var = [num * 2 for num in self.var]
        if self.debugWork == True:
            print(self.var)

    def mapToString(self):
        if not isinstance(self.var, list):
            raise Exception("mapToString works only with arrays")
        self.var = [str(num) for num in self.var]
        if self.debugWork == True:
            print(self.var)

    def sum(self):
        if not isinstance(self.var, list):
            raise Exception("sum works only with arrays")
        self.var = sum(self.var)
        self.type = "float"
        if self.debugWork == True:
            print(self.var)

    def average(self):
        if not isinstance(self.var, list):
            raise Exception("average works only with arrays")
        self.var = sum(self.var) / len(self.var)
        self.type = "float"
        if self.debugWork == True:
            print(self.var)

    def findMin(self):
        if not isinstance(self.var, list):
            raise Exception("findMin works only with arrays")
        self.var = min(self.var)
        self.type = "float"
        if self.debugWork == True:
            print(self.var)

    def findMax(self):
        if not isinstance(self.var, list):
            raise Exception("findMax works only with arrays")
        self.var = max(self.var)
        self.type = "float"
        if self.debugWork == True:
            print(self.var)

    def arr2Str(self):
        if not isinstance(self.var, list):
            raise Exception("removeAllZero work only with arrays")
        string = ''.join(str(i) for i in self.var)
        self.var = string
        if self.debugWork == True:
            print(self.var)

    def allAbs(self):
        if not isinstance(self.var, list):
            raise Exception("removeAllZero work only with arrays")
        new_arr = [abs(i) for i in self.var]
        self.var = new_arr.copy()
        if self.debugWork == True:
            print(self.var)

    def increment(self, value):
        if not isinstance(self.var, list):
            raise Exception("removeAllZero work only with arrays")
        new_arr = [i + value for i in self.var]
        self.var = new_arr.copy()
        if self.debugWork == True:
            print(self.var)

    def decrement(self, value):
        if not isinstance(self.var, list):
            raise Exception("removeAllZero work only with arrays")
        new_arr = [i - value for i in self.var]
        self.var = new_arr.copy()
        if self.debugWork == True:
            print(self.var)
    
    def multiply(self, value):
        if not isinstance(self.var, list):
            raise Exception("removeAllZero work only with arrays")
        new_arr = [i * value for i in self.var]
        self.var = new_arr.copy()
        if self.debugWork == True:
            print(self.var)
    
    def division(self, value):
        if not isinstance(self.var, list):
            raise Exception("removeAllZero work only with arrays")
        new_arr = [i / value for i in self.var]
        self.var = new_arr.copy()
        if self.debugWork == True:
            print(self.var)
# ------------------------------------- String ------------------------------------------------------
    def sortAscending(self):
        if not isinstance(self.var, list):
            raise Exception("sortAscending works only with arrays")
        self.var.sort()
        if self.debugWork == True:
            print(self.var)

    def sortDescending(self):
        if not isinstance(self.var, list):
            raise Exception("sortDescending works only with arrays")
        self.var.sort(reverse=True)
        if self.debugWork == True:
            print(self.var)

    def split(self):
        if not isinstance(self.var, str):
            raise Exception("split works only with strings")
        arr = [i for i in self.var]
        self.var = arr.copy()
        if self.debugWork == True:
            print(self.var)
    
    def substring(self, start, end):
        if not isinstance(self.var, str):
            raise Exception("substring works only with strings")
        self.var = self.var[start:end]
        if self.debugWork == True:
            print(self.var)

    def toLowerCase(self):
        if not isinstance(self.var, str):
            raise Exception("toLowerCase works only with strings")
        self.var = self.var.lower()
        if self.debugWork == True:
            print(self.var)

    def toUpperCase(self):
        if not isinstance(self.var, str):
            raise Exception("toUpperCase works only with strings")
        self.var = self.var.upper()
        if self.debugWork == True:
            print(self.var)

    def capitalize(self):
        if not isinstance(self.var, str):
            raise Exception("capitalize works only with strings")
        self.var = self.var.capitalize()
        if self.debugWork == True:
            print(self.var)

    def trim(self):
        if not isinstance(self.var, str):
            raise Exception("trim works only with strings")
        self.var = self.var.strip()
        if self.debugWork == True:
            print(self.var)

    def trimStart(self):
        if not isinstance(self.var, str):
            raise Exception("trimStart works only with strings")
        self.var = self.var.lstrip()
        if self.debugWork == True:
            print(self.var)

    def trimEnd(self):
        if not isinstance(self.var, str):
            raise Exception("trimEnd works only with strings")
        self.var = self.var.rstrip()
        if self.debugWork == True:
            print(self.var)

    def replaceAll(self, target, scope):
        if not isinstance(self.var, str):
            raise Exception("replaceAll works only with strings")
        self.var = self.var.replace(target, scope)
        if self.debugWork == True:
            print(self.var)

    def replaceFirst(self, target, scope):
        if not isinstance(self.var, str):
            raise Exception("replaceFirst works only with strings")
        self.var = self.var.replace(target, scope, 1)
        if self.debugWork == True:
            print(self.var)

    def executePipes(self):
        for pipe in self.pipeFunctions:
            funName = pipe["functionName"]
            params = pipe["params"]

            # Check if the function exists in the function map
            if funName not in self.function_map:
                raise Exception("No such function: " + funName)

            # Retrieve the function from the function map
            function = self.function_map[funName]

            # Check if the number of parameters matches the expected number
            expected_params = function.__code__.co_argcount - 1  # Subtract 1 for self
            if len(params) != expected_params:
                raise Exception(f"Function {funName} requires {expected_params} parameters")

            # Call the function with parameters
            if params:
                function(*params)
            else:
                function()

        print(self.var)