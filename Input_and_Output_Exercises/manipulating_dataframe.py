from pandas import read_csv
import matplotlib.pyplot as plt
from traceback import print_exc
try:
    headers = ["X", "Y"]
    data = read_csv(r"..\..\ILAS_python\sample_data\noHeader_noIndex_vert.csv", names=headers)
    data.insert(loc=2, column="Z", value=data["X"]*(data["Y"]+50))
    data.plot("X", "Z", kind="scatter")
    plt.show()
except:
    print_exc()
finally:
    input("Press Any Key to Continue...")
