from abc import ABC, abstractmethod

# Step 1: Base Pizza class
class Pizza(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass
    
# Simple basic pizza
class BasicPizza(Pizza):
    def __init__(self):
        self.description = 'Basic Pizza'
        self.price = 5.0 # Base price for a plain pizza
        
    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price
    
# Step 2: Base Decorator class
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza
        
    def get_description(self):
        return self._pizza.get_description
    
    def get_price(self):
        return self._pizza.get_price
    
# Step 3: Concrete decorators for various features

# Size decorators
class SmallSize(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self._size_description = 'Small Size'
        self._size_price = -1.0 # Small size reduces prive
        
    def get_description(self):
        return f'{self._pizza.get_description()} + {self._size_description}'
    
    def get_price(self):
        return self._pizza.get_price() + self._size_price
    
class MediumSize(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza
        self._size_description = 'Medium Size'
        self._size_price = 0.0 # No price change for medium size
        
    def get_description(self):
        return f'{self._pizza.get_description()} + {self._size_description}'
    
    def get_price(self):
        return self._pizza.get_price() + self._size_price
    
class LargeSize(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza
        self._size_description = 'Large Size'
        self._size_price = 2.0 # Large size adds price
        
    def get_description(self):
        return f'{self._pizza.get_description()} + {self._size_description}'
    
    def get_price(self):
        return self._pizza.get_price() + self._size_price
    
# Topping decorators
class Pepperoni(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self._topping_description = 'Pepperoni'
        self._topping_price = 1.5
        
    def get_description(self):
        return f'{self._pizza.get_description()} + {self._topping_description}'
    
    def get_price(self):
        return self._pizza.get_price() + self._topping_price
    
class Mushroom(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self._topping_description = 'Mushrooms'
        self._topping_price = 1.2
        
    def get_description(self):
        return f'{self._pizza.get_description()} + {self._topping_description}'
    
    def get_price(self):
        return self._pizza.get_price() + self._topping_price
    
class Cheese(PizzaDecorator):
    def __init__(self, pizza: Pizza):
        super().__init__(pizza)
        self._topping_description = 'Extra Cheese'
        self._topping_price = 1.8
        
    def get_description(self):
        return f'{self._pizza.get_description()} + {self._topping_description}'
    
    def get_price(self):
        return self._pizza.get_price() + self._topping_price
    
# Step 4: Test and build pizzas
def create_custom_pizza():
    pizza = BasicPizza()  # Start with basic pizza
    
    # Decorating pizza with different sizes and toppings
    pizza = LargeSize(pizza)
    pizza = Pepperoni(pizza)
    pizza = Mushroom(pizza)
    
    print(f'Pizza description: {pizza.get_description()}')
    print(f'Price: ${pizza.get_price():.2f}')
    
if __name__ == '__main__':
    create_custom_pizza()