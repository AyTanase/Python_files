import Part_A
import Part_B
from pandas import read_csv

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

# (3)
# year: str
def create_data_set(year):
    path = "environmental_survey/"

    plants = Part_B.scale(        \
             Part_A.remove_below( \
             Part_A.remove_tree(  \
             read_csv(path + "plants" + year + ".csv"))))

    pH = Part_B.scale( \
         read_csv(path + "pH" + year + ".csv"))

    set_spieces(plants)

    data_set = Part_B.zeros((15, 15, 5))
    for i, row in pH.iterrows():
        data_set[int(row["x"]), int(row["y"]), 0] += row["pH"]
        data_set[int(row["x"]), int(row["y"]), 1] += 1

    for i in range(15):
        for j in range(15):
            if data_set[i, j, 1] != 0:
                data_set[i, j, 0] /= data_set[i, j, 1]
                data_set[i, j, 1] = 0
            else:
                data_set[i, j, 0] = Part_B.nan

    sp = { "Winter_heath": 1,
           "Bell_heather": 2,
             "Brush_bush": 3,
            "Darly_heath": 4 }
    for i, row in plants.iterrows():
        data_set[int(row["x"]), int(row["y"]), sp[row["Spieces"]]] += 1

    return data_set


if __name__ == "__main__":
    from IPython.display import display
    from traceback import print_exc

    try:
        # (1)
        plants2017 = Part_A.remove_tree(      \
                         Part_A.remove_below( \
                             read_csv("environmental_survey/plants2017.csv")))
        set_spieces(plants2017)

        # (2)
        plants2017 = Part_B.scale(plants2017)

        display(plants2017)

        print(create_data_set("2017"))
    except:
        print_exc()
    finally:
        input("Press Enter to continue...")
