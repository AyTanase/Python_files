import numpy as np

# Part A

# (1)
def remove_tree(df):
    return df.ix[df["Plant"] == "shrub"]\
        .reset_index(drop=True)

# (2)
def change_gps_data(df):
    if "GPS_lon" in df.keys():
        df["GPS_lon"] *= 40075.160 * np.cos(df["GPS_lat"] * np.pi / 180) / 360
        df["GPS_lat"] *= 40008.000 / 360

        # You can change df's members, but you cannot change df itself.
        # df may be the copy of the pointer to the DataFrame.
        return df.rename(index=str, columns={"GPS_lat": "lat_km", "GPS_lon": "lon_km"})
    else:
        return df

# (3)
def remove_below(df, height=0.5):
    return df.ix[df["height_m"] >= height]\
        .reset_index(drop=True)

# Part B

# (3)
def scale(df):
    x_min = np.min(df["lon_km"])
    x_max = np.max(df["lon_km"])

    y_min = np.min(df["lat_km"])
    y_max = np.max(df["lat_km"])

    orig = {"x": x_min + 222 #(3445 - 3000) // 2,
            "y": y_min + 475 #(3950 - 3000) // 2}

if __name__ == "__main__":
    from pandas import read_csv
    from IPython.display import display
    from traceback import print_exc
    path = "environmental_survey\\"

    try:
        # Part A

        # (1)
        plants2017 = read_csv(path + "plants2017.csv")
        #print("Original Data:")
        #display(plants2017)
        plants2017 = remove_tree(plants2017)
        #print("\nRemove Tree")
        #display(plants2017)

        # (2)
        plants2017 = change_gps_data(plants2017)
        #print("\nChange GPS Data to meter")
        #display(plants2017)

        # (3)
        plants2017 = remove_below(plants2017)
        #print("\nRemove below 0.5m height")
        #display(plants2017)

        # Part B

        # (1)
        pH = read_csv(path + "pH2017.csv")

        # (2)
        pH = change_gps_data(pH)

        display(pH)
    except:
        print_exc()
    finally:
        input("\nPress any key to continue...")
