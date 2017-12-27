import Part_A

# (1)
def set_spieces(df):
    keys = [["Winter_heath", 1.2, 3.5,  2.0, 2.3],
            ["Bell_heather", 1.8, 1.5,  1.2, 2.3],
            [  "Brush_bush", 0.7, 2.1, 10.2, 1.5],
            [ "Darly_heath", 0.7, 2.2,  3.1, 1.7]]
    for row in keys:
        df[row[0]] = (df["height_m"]          - row[1]) ** 2 \
                   + (df["leaf_length_cm"]    - row[2]) ** 2 \
                   + (df["leaf_aspect_ratio"] - row[3]) ** 2 \
                   + (df["bud_length_cm"]     - row[4]) ** 2
    spieces = list(df.index)
    for i, row in df.iterrows():
        min_key = keys[0][0]
        for j in range(1, 4):
            if row[min_key] > row[keys[j][0]]:
                min_key = keys[j][0]
        spieces[i] = min_key
    for i in range(4):
        del df[keys[i][0]]
    df["Spieces"] = spieces

if __name__ == "__main__":
    from pandas import read_csv
    from IPython.display import display
    from traceback import print_exc

    try:
        # (1)
        plants2017 = Part_A.remove_tree(      \
                         Part_A.remove_below( \
                             read_csv("environmental_survey/plants2017.csv")))
        set_spieces(plants2017)
        display(plants2017)
    except:
        print_exc()
    finally:
        input("Press Enter to continue...")
