from numpy import array
import matplotlib.pyplot as plt
from traceback import print_exc

try:
    plt.matshow(array([[0, 1, 2],
                       [3, 4, 5],
                       [6, 7, 8]]).T, cmap="plasma", origin="lower")
    plt.colorbar(cmap="plasma")
    plt.show()
except:
    print_exc()
finally:
    input("Press any key to continue...")
