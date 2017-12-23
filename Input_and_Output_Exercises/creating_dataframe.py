from numpy import random
from pandas import DataFrame
from IPython.display import display
display(DataFrame(random.randint(0, 127, size=(5, 5))))
input("Press Any Key to Continue...")
