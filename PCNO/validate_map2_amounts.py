import pandas as pd


MAP2_SATELLITES = '../../../rcc-uchicago/PCNO/CSV/chicago/Maps/map2_satellites.csv'
MAP2_HQ = '../../../rcc-uchicago/PCNO/CSV/chicago/Maps/map2_hq.csv'


if __name__ == '__main__':

    hq = pd.read_csv(MAP2_HQ)
    hq_total = hq.Dollars_Per_Location.sum()

    sat = pd.read_csv(MAP2_SATELLITES)
    sat_total = sat.Dollars_Per_Location.sum()

    map2_total = hq_total + sat_total

    print(map2_total)
    # $3810692646.12
