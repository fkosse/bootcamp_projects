import random 
import pandas as pd
import numpy as np
from faker import Faker

mx=pd.read_csv('mx.csv')
mx=mx.set_index('before')

SIMULATE_MINUTES = 15

class Customer:
    """
    a single customer that moves through the supermarket in a MCMC simulation.
    new line
    """
    
    def __init__(self, id, name):
        self.id=id
        self.name = name
        self.location='entrance'
        self.transition_probs=mx
        
    def __repr__(self):
        return f"{self.name}, customer {self.id}, is in {self.location}"
    
    def next_state(self):
        ''' Propagates the customer to the next state. Returns nothing.   '''
        self.location = np.random.choice(self.transition_probs.columns.values, p=self.transition_probs.loc[self.location])
    
    def is_active(self):
        """ Returns True if the customer has not reached the checkout yet. """
        if self.location=='checkout':
            return False
        else:
            return True

class Supermarket:
    """manages multiple Customer instances that are currently in the market.    
    new comments"""
    
    def __init__(self):
        # a list of Customer objects
        self.customers = []
        self.minutes = 0
        self.last_id = 0
        self.list = pd.DataFrame(columns=['timestamp', 'id', 'name', 'location'])
    def get_time(self):
        hour = 7 + self.minutes // 60
        min = self.minutes % 60
        self.timestamp = pd.Timestamp(year=2021, month=7, day=1, hour= hour, minute = min)
        return None
    
    def print_customers(self):
        """print all customers with the current time and id in CSV format.
        """
        for customer in self.customers:
            self.get_time()
            timestamp = self.timestamp
            customer_name = customer.name
            customer_id = customer.id
            location = customer.location
            self.list = self.list.append({'timestamp' : timestamp, 'id' : customer_id, 'name' : customer_name, 'location' : location}, ignore_index = True)
    
    def add_new_customers(self): #create a customer
        """randomly creates new customers."""
        f = Faker()
        name = f.name()
        id = self.last_id
        self.customers.append(Customer(id, name)) #this function in my supermarket object literally creates other objects
        self.last_id += 1
        
    def next_minute(self): #control our customers
        """propagates all customers to the next state."""
        self.minutes += 1
        for shopper in self.customers:
            shopper.next_state()
    
    def remove_exited_customers(self):
        """removes every customer that is not active any more.
        """
        self.customers = [i for i in self.customers if i.is_active()]

#    def __repr__(self): # needs to be defined what happens when the class is called
#       return f"{self.time}, {self.name}, {self.n_customers}"


if __name__ == "__main__":
    s = Supermarket()
    for i in range(SIMULATE_MINUTES):
        'Hello from Daria from home!'
        'Hello from Felix, here'
        s.next_minute()
        s.add_new_customers()
        s.remove_exited_customers()
        s.print_customers()
    s.list.to_csv('monday.csv')


