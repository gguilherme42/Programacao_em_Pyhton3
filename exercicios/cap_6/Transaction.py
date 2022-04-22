class Transaction:
    """
    >>> test = Transaction(50, '22/10/2012')
    >>> test.amount
    50.0
    >>> test.date
    '22/10/2012'
    >>> test.currency
    'USD'
    >>> test.usd_conversion_rate
    1
    >>> test.description
    """
    def __init__(self, amount: float, date, currency: str="USD", usd_conversion_rate: int=1, description=None):
        self.__amount = float(amount)
        self.__date = date
        self.__currency = currency
        self.__usd_conversion_rate = usd_conversion_rate
        self.__description = description
    

    @property
    def amount(self):
        return self.__amount
    
    @property
    def date(self):
        return self.__date
    
    @property 
    def currency(self):
        return self.__currency
    
    @property
    def usd_conversion_rate(self):
        return self.__usd_conversion_rate
    
    @property
    def description(self):
        return self.__description
    
    @property
    def usd(self):
        return self.__amount * self.__usd_conversion_rate


if __name__ == "__main__":
    import doctest
    doctest.testmod()


