class FuzzyBool(float):
    def __new__(cls, value: float=0.0):
        return super().__new__(cls, value if 0.0 <= value <= 1.0 else 0.0)
    
    def __invert__(self): # NOT
        return FuzzyBool(1.0 - float(self))
    
    def __and__(self, other):
        return FuzzyBool(min(self, other))
    
    def __iand__(self, other):
        return FuzzyBool(min(self, other))
    
    def __or__(self, other):
        return FuzzyBool(max(self, other)) 
    
    def __ior__(self, other):
        return FuzzyBool(max(self, other))
    
    
    def __repr__(self):
        return f"{self.__class__.__name__}({super().__repr__()})"
    
    def __bool__(self):
        return self > 0.5
    
    def __int__(self):
        return round(self)
    
    def __float__(self):
        return self
    
    
    def __format__(self, format_spec):
        return format(self.__value, format_spec)
    

    @staticmethod
    def conjunction(*fuzzies):
        return FuzzyBool(min([float(x) for x in fuzzies]))
    
    @staticmethod
    def disjunction(*fuzzies):
        return FuzzyBool(max([float(x) for x in fuzzies]))
    

    

