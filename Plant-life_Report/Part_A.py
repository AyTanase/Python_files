from traceback import print_exc

# 1.
from pandas import read_csv
from IPython.display import display

try:
    plants2017 = read_csv(r"environmental_survey\plants2017.csv")
    plants2017 = plants2017.ix[plants2017["Plant"] == "shrub"].reset_index(drop=True)
    display(plants2017)
except:
    print_exc()
finally:
    input("Press any key to continue...")
