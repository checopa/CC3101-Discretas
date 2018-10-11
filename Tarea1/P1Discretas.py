# Run the file as "python SAT.py -v"

# Add further needed modules
import unittest

# To implement the functions below, you are allowed
# to define auxiliary functions, if convenient.


def SetLiteral(formula, lit):
    newlit = []
    for i in formula:
        litlit = []
        for j in i:
            if j == lit:
                litlit = []
                break
            if j == -lit:
                continue
            litlit.append(j)
        if len(litlit) != 0:
            newlit.append(litlit)
    return newlit


def IsSatisfiable(formula):
    if len(formula) == 0:
        return True
    if len(formula) > 1:
        c = 0
        for i in formula:
            if len(i) == 1 and c == 0:
                c = i[0]
            if len(i) == 1 and i[0] == -c:
                return False
    lit = formula[0][0]
    for i in formula:
        if len(i) == 1:
            lit = i[0]
            break
    return IsSatisfiable(SetLiteral(formula, lit))


def BuildModel(formula):
    if not IsSatisfiable(formula):
        return (False, {})
    else:
        literales = {}
        while len(formula) >= 1:
            lit=formula[0][0]
            for i in formula:
                if len(i)==1:
                    lit=i[0]
            if IsSatisfiable(SetLiteral(formula, lit)):
                if lit<0:
                    literales[-lit]=False
                else:
                    literales[lit]=True
                formula = SetLiteral(formula, lit)
            else:
                if lit<0:
                    literales[-lit]=False
                else:
                    literales[lit]=True
                formula = SetLiteral(formula, -lit)
        return (True, literales)

class Tests(unittest.TestCase):
    def setUp(self):
        pass

    def test_SetLiteral(self):
        self.assertEqual(SetLiteral([[1, 2, -3], [-1, -2, 4], [3, 4]], 1), [[-2, 4], [3, 4]])
        self.assertEqual(SetLiteral([[1, 2, -3], [-1, -2, 4], [3, 4]], -1), [[2, -3], [3, 4]])

    def test_IsSatisfiable(self):
        self.assertEqual(IsSatisfiable([[1, 2, -3], [-1, -2, 4], [3, 4]]), True)
        self.assertEqual(IsSatisfiable([[1, 2], [1, -2], [], [-1]]), False)
        self.assertEqual(IsSatisfiable([]), True)

    def test_BuildModel(self):
        self.assertEqual(BuildModel([[-2, 4], [1], [-4,-1]]), (True, {1: True, 2: False, 4: False}))
        self.assertEqual(BuildModel([[1,2], [-1,-2], [-1,2], [1,-2]]), (False, {}))

# Perform the tests when runing the file
if __name__ == '__main__':
    unittest.main()
