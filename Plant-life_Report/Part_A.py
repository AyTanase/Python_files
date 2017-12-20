from numpy import cos

# (1)
def remove_tree(df):
    df = df.ix[df["Plant"] == "shrub"].reset_index(drop=True)

# (2)
def change_gps_data(df):
    if "GPS_lon" in df.keys():
        df["GPS_lon"] = 40075160 * df["GPS_lon"] * cos(df["GPS_lat"]) / 360
        df["GPS_lat"] = 40008000 * df["GPS_lat"] / 360
        df = df.rename(index=str, columns={"GPS_lat": "lat", "GPS_lon": "lon"})

if __name__ == "__main__":
    from pandas import read_csv
    from IPython.display import display
    from traceback import print_exc

    try:
        plants2017 = read_csv(r"environmental_survey\plants2017")
        remove_tree(plants2017)
        change_gps_data(plants2017)
        display(plants2017)
    except:
        print_exc()
    finally:
        input("Press any key to continue...")
