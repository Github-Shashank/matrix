import copy
import random

class matrix:
    def __init__(self,m):
        val = matrix._check(m)
        if val == True:
            pass
        else:
            raise ValueError(f"Invalid Format! len({val}) is not matched with first one.")
        self.m = m

    @staticmethod
    def _check(m):
        n = len(m[0])
        for i in m:
            if len(i) != n :
                return i
        else:
            return True
    
    def __repr__(self):
        return '{}'.format(self.m)
    
    def __str__(self):
        return "{}".format(self.m)
    
    def __eq__(self, other):
        if not self.isEqualOrder(other):
            return False

        r,l = self.order
        for i in range(r):
            for j in range(l):
                if not self[i,j] == other[i,j]:
                    return False
        else:
            return True

    def __add__(self, other):
        if not self.isEqualOrder(other):
            raise ValueError(f"Not Equal Order! {self.order} not equal to {other.order}")
        ord = self.order
        m = [[self[i,j]+other[i,j] for j in range(ord[1])] for i in range(ord[0]) ]
        return matrix(m)

    def __sub__(self, other):
        if not self.isEqualOrder(other):
            raise ValueError(f"Not Equal Order! {self.order} not equal to {other.order}")
        ord = self.order
        m = [[self[i,j]-other[i,j] for j in range(ord[1])] for i in range(ord[0]) ]
        return matrix(m)

        def __mul__(self, other):
            if isinstance(other, (int, float)):
                return matrix([[val * other for val in row] for row in self.m])
            elif isinstance(other, matrix):
                r, n = self.order
                c = other.order[1]
                m = [[sum(self[i,k]*other[k,j] for k in range(n)) for j in range(c)] for i in range(r)]
                return matrix(m)
            else:
                raise TypeError("Unsupported operand type for *")

        def __rmul__(self, other):
            return self.__mul__(other)

    def __pow__(self, raisedTo):
        if isinstance(raisedTo, int) and raisedTo > 0:
            I = self.identity
            for i in range(raisedTo):
                I = I*self
            return I

    def __getitem__(self, index):
        if self.isValidIndex(index):
            row, col = index
            return self.m[row][col]

    def __setitem__(self, key, value):
        r,c = key
        self.m[r][c] = value

    def __iter__(self):
        for row in self.m:
            yield row

    @property
    def traverse(self):
        l = [x for lists in self.m for x in lists]
        return l

    def insertRow(self, rowMat):
        lr = self.order[1]
        if len(rowMat)==lr:
            self.m.append(rowMat)
        else:
            raise ValueError(f"Length Error! length of rowMat is not suitable for this matrix.")

    def insertCol(self, colMat):
        lc = self.order[0]
        if len(colMat)==lc:
            for i in range(lc):
                self.m[i].append(colMat[i])
        else:
            raise ValueError(f"Length Error! length of colMat is not suitable for this matrix.")

    def delRow(self, rowIndex, inplace=False):
        r = self.order[0]
        l = copy.deepcopy(self.m)
        if 0<=rowIndex<r:
            l.pop(rowIndex)
            if inplace:
                self.m = l
            else:
                return matrix(l)
        else:
            raise ValueError(f"Index Error! index out of range {rowIndex} for 0 to {r}")

    def delCol(self, colIndex, inplace=False):
        r,c = self.order
        l = copy.deepcopy(self.m)
        if 0<=colIndex<c:
            for row in range(r):
                l[row].pop(colIndex)
            if inplace:
                self.m = l
            else:
                return matrix(l)
        else:
            print(colIndex,c)
            raise ValueError(f"Index Error! index out of range {colIndex} for 0 to {c}")

    def getRow(self, rowIndex):
        r = self.order[0]
        if 0<=rowIndex<r:
            return self.m[rowIndex]
        else:
            raise ValueError()

    def getCol(self, colIndex):
        r,c = self.order
        if 0<=colIndex<c:
            return [self.m[i][colIndex] for i in range(r)]
        else:
            raise ValueError()

    @property
    def isSqrMatrix(self):
        r,c = self.order
        return r==c

    @property
    def isDiagMatrix(self):
        if not self.isSqrMatrix:
            return False
        r,c = self.order
        s =  {self.m[i][j] for i in range(r) for j in range(c) if i!=j }
        return s == {0}

    @property
    def order(self):
        return (len(self.m),len(self.m[0])) 

    @property
    def isColMatrix(self):
        c = self.order[1]
        return c==1

    @property
    def isRowMatrix(self):
        r = self.order[0]
        return r==1

    @property
    def isSclrMatrix(self):
        if not self.isDiagMatrix:
            return False
        r,c = self.order
        s =  {self.m[i][j] for i in range(r) for j in range(c) if i==j }
        return len(s)==1

    @property
    def isIdntMatrix(self):
        if not self.isDiagMatrix:
            return False
        r,c = self.order
        s =  {self.m[i][j] for i in range(r) for j in range(c) if i==j }
        return s=={1}

    @property
    def isZeroMatrix(self):
        r,c = self.order
        s =  {self.m[i][j] for i in range(r) for j in range(c) }
        return s=={0}
    
    @property
    def transpose(self):
        r,c = self.order
        m = [ [ self.m[j][i] for j in range(r)] for i in range(c)]
        return matrix(m)

    @property
    def isSymtMatrix(self): 
        return self == self.transpose

    @property
    def isSkewSymtMatrix(self):
        return -1*self == self.transpose

    @property
    def identity(self):
        r,c = self.order
        if r!=c:
            raise ValueError()
        return matrix([[ (0 if i != j else 1) for i in range(r)] for j in range(c)])

    @property
    def isInvertible(self):
        return self.isSqrMatrix and self.determinant != 0

    def isEqualOrder(self, other):
        return self.order == other.order

    def isValidIndex(self, index):
        if not len(index) == 2:
            return False
        
        r, c = index
        rows, cols = self.order
        return 0 <= r < rows and 0 <= c < cols

    def isMultiplicable(self, other):
        if self.order[1] == other.order[0]:
            return True
        else:
            return False

    def minor(self,rowIndex, colIndex):
        return self.delRow(rowIndex).delCol(colIndex)

    def coffactor(self,rowIndex, colIndex):
        return ((-1)**(rowIndex+colIndex))*self.minor(rowIndex,colIndex).determinant

    @property
    def matrixOfMinors(self):
        r,c = self.order
        l = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                l[i][j] = self.minor(i,j)
        return matrix(l)

    @property
    def matrixOfCoffactors(self):
        r,c = self.order
        l = [[0 for _ in range(c)] for _ in range(r)]
        for i in range(r):
            for j in range(c):
                l[i][j] = self.coffactor(i,j)
        return matrix(l)

    @property
    def determinant(self):
        r,c = self.order
        if r != c:
            raise ValueError()
        if r == 2:
            l = self.m
            return l[0][0]*l[1][1]-l[0][1]*l[1][0]
        return sum( self.m[0][i]*self.coffactor(0,i) for i in range(c))

    @property
    def trace(self):
        r,c = self.order
        if not r == c:
            raise ValueError()
        return sum(self.m[i][i] for i in range(r))
    
    @property
    def adjoint(self):
        return self.matrixOfCoffactors.transpose
    
    @property
    def inverse(self):
        if not self.isInvertible:
            raise ValueError()
        return self.adjoint * (1/self.determinant)
    
    @property
    def isSingularMatrix(self):
        return self.determinant == 0
    
    @property
    def isNonSingularMatrix(self):
        return self.determinant != 0
    
    @classmethod
    def one(cls, rows, cols=None):
        if cols is None:
            cols = rows
        return cls([[1 for _ in range(cols)] for _ in range(rows)])
    
    @classmethod
    def zero(cls, rows, cols=None):
        if cols is None:
            cols = rows
        return cls([[0 for _ in range(cols)] for _ in range(rows)])
    
    @classmethod
    def identity(cls,n):
        return cls([[1 if i == j else 0 for j in range(n)] for i in range(n)])

    @classmethod
    def constant(cls, rows, cols=None, value=0):
        if cols is None:
            cols = rows
        return cls([[value for _ in range(cols)] for _ in range(rows)])
    
    @classmethod
    def diagonal(cls, diag_list):
        n = len(diag_list)
        return cls([[diag_list[i] if i == j else 0 for j in range(n)] for i in range(n)])
    
    @classmethod
    def random(cls, rows, cols=None, low=0, high=10):
        if cols is None:
            cols = rows
        return cls([[random.randint(low, high) for _ in range(cols)] for _ in range(rows)])
    
    @classmethod
    def elementwise(cls, rows, cols=None, func=lambda i, j: 0):
        if cols is None:
            cols = rows
        return cls([[func(i,j) for j in range(cols)] for i in range(rows)])

    @classmethod
    def from_string(cls, my_string, dtype=float,row_sep='\n'):
        s = my_string.strip()
        char_list = [char for char in s if char.isdigit() or char in ' .+-j'+row_sep]
        clean_string = "".join(char_list)
        l = [
            [dtype(val) for val in row.split() if val] 
             for row in clean_string.split(row_sep) if row.strip()
             ]
        return cls(l)
