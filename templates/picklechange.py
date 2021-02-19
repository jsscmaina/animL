import csv
# from six.moves import cPickle as pickle
import _pickle
import joblib
# from sklearn.externals import pickle
import numpy as np


def main(path_pickle, path_csv):
    x = []
    with open(path_pickle, 'rb') as f:
        x = joblib.load(f)

    with open(path_csv, 'w') as f:
        writer = csv.writer(f)
        for line in x:
            writer.writerow(line)


if __name__ == '__main__':
    picklef = "RFModelforMPG.sav"
    csvf = "RFModelforMPG.csv"
    main(picklef, csvf)
