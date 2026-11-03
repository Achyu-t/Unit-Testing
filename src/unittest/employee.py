class Employee :

    raise_amt = 1.1

    def __init__(self , first , last , salary):

        self.first = first
        self.last = last
        self.salary = salary


    @property
    def email(self):
        return '{}.{}@pymail.com'.format(self.first , self.last)

    @property
    def name(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.salary =  int(self.salary * self.raise_amt)

    


   