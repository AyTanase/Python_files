from Part_C import create_data_set
from numpy import array
import matplotlib.pyplot as plt
from scipy.stats import linregress
from traceback import print_exc

try:
    annual_data = []
    years = range(1997, 2018)
    for year in years:
        annual_data.append(create_data_set(str(year)))

    annual_data = array(annual_data)
    years = array(years)

    points = [["Sketchy_inc",   2,  0],
              ["Philamore_co", 14,  9],
              ["Control",       0, 14]]
    titles = ["pH", "Winter_heath", "Bell_heather", "Brush_bush", "Darly_heath"]

    for i in range(3):
        for j in range(5):
            m, c, r_value, p_value, std_err = linregress(years, \
                annual_data[:, points[i][1], points[i][2], j])
            y_fit = float(m) * years + c

            plt.plot(years, \
                annual_data[:, points[i][1], points[i][2], j], 'o')
            plt.plot(years, y_fit, label=f"grad={round(m, 3)}(/year)")

            plt.xlabel("Year")
            plt.title(points[i][0] + " " + titles[j])
            plt.legend(loc="best")
            plt.savefig("img/Part_D_" + points[i][0] + "/" + titles[j] + ".png")
            plt.clf()
except:
    print_exc()
finally:
    input("Press Enter to Continue...")
