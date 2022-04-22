import pickle

from Transaction import Transaction


class AccountError(Exception): pass
class SaveError(AccountError): pass
class LoadError(AccountError): pass

class Account:
    """
    >>> import os
    >>> import tempfile
    >>> name = os.path.join(tempfile.gettempdir(), "account01")
    >>> account = Account(name, "Qtrac Ltd.")
    >>> os.path.basename(account.account_number), account.name,
    ('account01', 'Qtrac Ltd.')
    >>> account.balance, account.all_usd, len(account)
    (0.0, True, 0)
    >>> account.apply(Transaction(100, "2008-11-14"))
    >>> account.apply(Transaction(150, "2008-12-09"))
    >>> account.apply(Transaction(-95, "2009-01-22"))
    >>> account.balance, account.all_usd, len(account)
    (155.0, True, 3)
    >>> account.apply(Transaction(50, "2008-12-09", "EUR", 1.53))
    >>> account.balance, account.all_usd, len(account)
    (231.5, False, 4)
    >>> account.save()
    >>> newaccount = Account(name, "Qtrac Ltd.")
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (0.0, True, 0)
    >>> newaccount.load()
    >>> newaccount.balance, newaccount.all_usd, len(newaccount)
    (231.5, False, 4)
    >>> try:
    ...     os.remove(name + ".acc")
    ... except EnvironmentError:
    ...     pass
    """
    def __init__(self, account_number, name):
        self.__account_number = account_number
        self.__name = name
        self.__transactions: list[Transaction] = []
    

    @property
    def account_number(self):
        return self.__account_number
    
    @property
    def name(self):
        return self.__name
    
    @property
    def balance(self):
        result = 0
        for t in self.__transactions:
            result += t.usd 
        return float(result)
    
    @property
    def all_usd(self):
        for transaction in self.__transactions:
            if transaction.currency != "USD":
                return False
        return True


    @name.setter
    def name(self, name):
        assert len(name) >= 4, "Name should have at least 4 characters"
        self.__name = name
    
    def __len__(self):
        return len(self.__transactions)
    

    def apply(self, transaction: Transaction):
        assert isinstance(transaction, Transaction), "can't add non-Transaction type"
        self.__transactions.append(transaction)
    

    def save(self): 
        """Saves the account's data in file number.acc"""
        fh = None
        try:
            data = [self.__account_number, self.__name, self.__transactions]
            fh = open(f"{self.__account_number}.acc", 'wb')
            pickle.dump(data, fh, pickle.HIGHEST_PROTOCOL)

        except (EnvironmentError, pickle.PicklingError) as err:
            raise SaveError(str(err))
        finally:
            if fh is not None:
                fh.close()

    def load(self): 
        """Loads the account's data in file number.acc
        
        All previous data is lost
        """
        fh = None
        try: 
            fh = open(f"{self.__account_number}.acc", "rb")
            data = pickle.load(fh)
            assert self.__account_number == data[0], "account number doesn't match"
            self.__name, self.__transactions = data[1:]
            
        except (EnvironmentError, pickle.UnpicklingError) as err:
            raise LoadError(str(err))
        finally:
            if fh is not None:
                fh.close()


if __name__ == "__main__":
    import doctest
    doctest.testmod()


