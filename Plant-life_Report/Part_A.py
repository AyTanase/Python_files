from numpy import cos
from numpy import pi

# (1)
def remove_tree(df):
    return df.ix[df["Plant"] == "shrub"]\
        .reset_index(drop=True)

# (2)
def change_gps_data(df):
    if "GPS_lon" in df.keys():
        df["GPS_lon"] *= 40075160 * cos(df["GPS_lat"] * pi / 180) / 360
        df["GPS_lat"] *= 40008000 / 360
        return df.rename(index=str, columns={"GPS_lat": "lat_m", "GPS_lon": "lon_m"})

# (3)
def remove_below(df, height=0.5):
    return df.ix[df["height_m"] >= height]\
        .reset_index(drop=True)

if __name__ == "__main__":
    from pandas import read_csv
    from IPython.display import display
    from traceback import print_exc

    try:
        plants2017 = read_csv(r"environmental_survey\plants2017.csv")
        display(plants2017)
        plants2017 = remove_tree(plants2017)
        display(plants2017)
        plants2017 = change_gps_data(plants2017)
        display(plants2017)
        plants2017 = remove_below(plants2017)
        display(plants2017)
    except:
        print_exc()
    finally:
        input("Press any key to continue...")
