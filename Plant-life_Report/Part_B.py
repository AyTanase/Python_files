from Part_A import change_gps_data
from numpy import zeros, nan

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

# (3-2)
def mean_of_pH(df):
    if "x" not in df.keys():
        df = scale(df)

    means = zeros((15, 15))
    count = zeros((15, 15))

    for i, row in df.iterrows():
        means[int(row["x"]), int(row["y"])] += row["pH"]
        count[int(row["x"]), int(row["y"])] += 1

    for x in range(15):
        for y in range(15):
            if count[x, y] != 0:
                means[x, y] /= count[x, y]
            else:
                means[x, y] = nan
    return means

if __name__ == "__main__":
    from pandas import read_csv
    import matplotlib.pyplot as plt
    from traceback import print_exc

    try:
        # (1)
        pH = read_csv("environmental_survey/pH2017.csv")

        # (2)
        pH = change_gps_data(pH)

        # (3-1)
        pH = scale(pH)

        # (3-2)
        means = mean_of_pH(pH)

        # (4)
        plt.matshow(means.T, origin="lower", cmap="plasma")
        plt.colorbar(cmap="plasma")
        plt.savefig("img/pH2017.png")

    except:
        print_exc()
    finally:
        input("Press any key to continue...")
