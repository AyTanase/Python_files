from numpy import cos, pi, array, zeros, nan, arange
from scipy.stats import linregress
from pandas import read_csv
import matplotlib.pyplot as plt
from IPython.display import display
from traceback import print_exc


print("#################### Part A ####################")

# (1)
def remove_tree(df):
    return df.ix[df["Plant"] == "shrub"]\
             .reset_index(drop=True)

# (2)
def change_gps_data(df):
    df["GPS_lon"] *= 40075160 * cos(df["GPS_lat"] * pi / 180) / 360
    df["GPS_lat"] *= 40008000 / 360
    return df.rename(index=str, columns={"GPS_lat": "lat_m", "GPS_lon": "lon_m"})

# (3)
def remove_below(df, height=0.5):
    return df.ix[df["height_m"] >= height]\
             .reset_index(drop=True)

"""
try:
                 # (3)
    plants2017 = remove_below(\
                     # (2)
                     change_gps_data(\
                         # (1)
                         remove_tree(\
                             read_csv("environmental_survey/plants2017.csv"))))
    display(plants2017)
except:
    print_exc()
finally:
    input("Press Enter to Continue...")
"""


print("#################### Part B ####################")

# (3-1)
def scale(df):
    if "lon_m" not in df.keys():
        df = change_gps_data(df)

    x_min = df["lon_m"].min() + 222 # 222 = (3445 - 3000) // 2
    x_max = x_min + 3000

    y_min = df["lat_m"].min() + 475 # 475 = (3950 - 3000) // 2
    y_max = y_min + 3000

    df = df.ix[df["lon_m"] >= x_min]\
           .ix[df["lon_m"] <  x_max]\
           .ix[df["lat_m"] >= y_min]\
           .ix[df["lat_m"] <  y_max]\
           .reset_index(drop=True)

    df["x"] = (df["lon_m"] - x_min) // 200
    df["y"] = (df["lat_m"] - y_min) // 200

    return df

"""
try:
         # (3-1)
    pH = scale(\
             # (2)
             change_gps_data(\
                 # (1)
                 read_csv("environmental_survey/pH2017.csv")))

    # (3-2)
    mean = zeros((15, 15))
    count = zeros((15, 15), dtype=int)

    for i, row in pH.iterrows():
        x = int(row["x"])
        y = int(row["y"])
        mean[x, y] += row["pH"]
        count[x, y] += 1

    for x in range(15):
        for y in range(15):
            c = count[x, y]
            if c:
                mean[x, y] /= c
            else:
                mean[x, y] = nan

    # (4)
    plt.matshow(mean.T, origin="lower", cmap="plasma")
    plt.colorbar(cmap="plasma")
    plt.savefig("img/pH2017.png")
    plt.show()
except:
    print_exc()
finally:
    input("Press Enter to Continue...")
"""


print("#################### Part C ####################")

# (1)
def set_spieces(df):
    keys = (("Winter_heath", 1.2, 3.5,  2.0, 2.3),
            ("Bell_heather", 1.8, 1.5,  1.2, 2.3),
            (  "Brush_bush", 0.7, 2.1, 10.2, 1.5),
            ( "Darly_heath", 0.7, 2.2,  3.1, 1.7))
    spieces = list(df.index)
    for i, row in df.iterrows():
        min = ["Winter_heath", 0]
        for j in range(4):
            dat = keys[j]
            v = (row["height_m"]          - dat[1]) ** 2 \
              + (row["leaf_length_cm"]    - dat[2]) ** 2 \
              + (row["leaf_aspect_ratio"] - dat[3]) ** 2 \
              + (row["bud_length_cm"]     - dat[4]) ** 2
            if not j:
                min[1] = v
            elif min[1] > v:
                min[0] = dat[0]
                min[1] = v
        spieces[i] = min[0]
    df["Spieces"] = spieces
    return df

# (3)
# year: str
def create_data_set(year):
    year += ".csv"

    plants = set_spieces(\
                 scale(\
                     remove_below(\
                         remove_tree(\
                             read_csv("environmental_survey/plants" + year)))))

    pH = scale(\
             read_csv("environmental_survey/pH" + year))

    data_set = zeros((15, 15, 5))
    for i, row in pH.iterrows():
        x = int(row["x"])
        y = int(row["y"])
        data_set[x, y, 0] += row["pH"]
        data_set[x, y, 1] += 1

    for x in range(15):
        for y in range(15):
            c = data_set[x, y, 1]
            if c:
                data_set[x, y, 0] /= c
                data_set[x, y, 1] = 0
            else:
                data_set[x, y, 0] = nan

    sp = { "Winter_heath": 1,
           "Bell_heather": 2,
             "Brush_bush": 3,
            "Darly_heath": 4 }
    for i, row in plants.iterrows():
        data_set[int(row["x"]), int(row["y"]), sp[row["Spieces"]]] += 1

    return data_set

"""
try:
    # (3)
    print(create_data_set("2017"))
except:
    print_exc()
finally:
    input("Press Enter to Continue...")
"""

print("#################### Part D ####################")
try:
    # (1)
    years = arange(1997, 2018)
    annual_data = array([create_data_set(str(year)) for year in years])

    points = (("Sketchy_inc",   2,  0),
              ("Philamore_co", 14,  9),
              ("Control",       0, 14))
    titles = ("pH", "Winter_heath", "Bell_heather", "Brush_bush", "Darly_heath")

    # (2)
    for i in range(3):
        point = points[i]
        name = point[0]
        x = point[1]
        y = point[2]
        for j in range(5):
            m, c, r_value, p_value, std_err = linregress(years, annual_data[:, x, y, j])
            y_fit = float(m) * years + c

            plt.plot(years, annual_data[:, x, y, j], 'o')
            plt.plot(years, y_fit, label=f"grad={round(m, 3)}(/year)")

            plt.xlabel("Year")
            plt.title(name + " " + titles[j])
            plt.legend(loc="best")
            plt.savefig("img/Part_D_" + name + "/" + titles[j] + ".png")
            plt.clf()
except:
    print_exc()
finally:
    input("Press Enter to Continue...")
