from numpy import cos, pi

# (1)
def remove_tree(df):
    return df.ix[df["Plant"] == "shrub"]\
             .reset_index(drop=True)

# (2)
def change_gps_data(df):
    df["GPS_lon"] *= 40075160 * cos(df["GPS_lat"] * pi / 180) / 360
    df["GPS_lat"] *= 40008000 / 360

    # You can change df's members, but you cannot change df itself.
    # df may be the copy of the pointer to the DataFrame.
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
        # (1)
        plants2017 = read_csv("environmental_survey/plants2017.csv")
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
        display(plants2017)

    except:
        print_exc()
    finally:
        input("\nPress Enter to continue...")
