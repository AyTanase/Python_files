from pandas import read_csv
import Part_A
from numpy import zeros
from traceback import print_exc

x_min = 0
y_min = 0

def company_site(name, gps_lon, gps_lat):
    global x_min
    global y_min

    gps_lon *= 40075160 * Part_A.cos(gps_lat * Part_A.pi / 180) / 360
    gps_lon -= x_min
    gps_lon //= 200

    gps_lat *= 40008000 / 360
    gps_lat -= y_min
    gps_lat //= 200

    print(name, gps_lon, gps_lat)

try:
    plants2017 = Part_A.change_gps_data(\
                 Part_A.remove_below(   \
                 Part_A.remove_tree(    \
                 read_csv("environmental_survey/plants2017.csv"))))
    x_min = plants2017["lon_m"].min()
    y_min = plants2017["lat_m"].min()

    company_site("Sketchy_inc.", 136.7647, 35.7336)
    company_site("Philamore_co.", 136.8262, 35.7498)

    map = zeros((15, 15))
    for i in range(15):
        for j in range(15):
            map[i][j] += ((i - 2) ** 2 + j ** 2) ** 0.5 + ((i - 17) ** 2 + (j - 9) ** 2) ** 0.5

    d_min = [0, 0, map[0][0]]
    for i in range(15):
        for j in range(15):
            if d_min[2] < map[i][j]:
                d_min[0] = i
                d_min[1] = j
                d_min[2] = map[i][j]
    print(d_min)
except:
    print_exc()
finally:
    input("Press Enter to continue...")
