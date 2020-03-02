# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import gmplot

import matplotlib.pyplot as plt

import folium
from IPython.display import display

import sklearn
import sklearn.preprocessing as preprocessing
import sklearn.model_selection as mdl
import sklearn.cluster as cluster

#import sklearn.model_selection as mdl
import sklearn.metrics as mat
import sklearn.svm as svm


import random

class Model():
    classifier = ''
    def startModel(self):
        accident2 = pd.read_csv('../RawData/KSI(2008-2018).csv')
        accident = accident2[['DATE','LATITUDE', 'LONGITUDE', 'STREET1', 'STREET2', 'ROAD_CLASS', 'District',
                      'LOCCOORD', 'ACCLOC', 'INJURY', 'INITDIR', 'VEHTYPE', 'MANOEUVER', 'DRIVACT',
                      'SPEEDING', 'AG_DRIV', 'REDLIGHT', 'ALCOHOL']]

        accident["DATE"] = pd.to_datetime(accident["DATE"])
        accident.index = accident["DATE"]

        accident = accident.replace(' ', np.NAN, regex=False)


        accident["District"][accident["District"].isnull()]
#        print(len(accident["District"][accident["District"].isnull()]))
        accident["District"][accident["District"].isnull()] = "Scarborough"
#        print(len(accident["District"][accident["District"].isnull()]))

        accident["ROAD_CLASS"][accident["ROAD_CLASS"].isnull()]
#        print(len(accident["ROAD_CLASS"][accident["ROAD_CLASS"].isnull()]))
        accident["ROAD_CLASS"][accident["ROAD_CLASS"].isnull()] = "Major Arterial"
#        print(len(accident["ROAD_CLASS"][accident["ROAD_CLASS"].isnull()]))


        accident["STREET2"][accident["STREET2"].isnull()]
#        print(len(accident["STREET2"][accident["STREET2"].isnull()]))
        accident["STREET2"][accident["STREET2"].isnull()] = "Major Arterial"
#        print(len(accident["STREET2"][accident["STREET2"].isnull()]))


        accident["LOCCOORD"][accident["LOCCOORD"].isnull()]
#        print(len(accident["LOCCOORD"][accident["LOCCOORD"].isnull()]))
        accident["LOCCOORD"][accident["LOCCOORD"].isnull()] = "Intersection"
#        print(len(accident["LOCCOORD"][accident["LOCCOORD"].isnull()]))

        accident["ACCLOC"][accident["ACCLOC"].isnull()]
        #print(len(accident["ACCLOC"][accident["ACCLOC"].isnull()]))
        accident["ACCLOC"][accident["ACCLOC"].isnull()] = "Non Intersection"
        #print(len(accident["ACCLOC"][accident["ACCLOC"].isnull()]))

        accident["INJURY"][accident["INJURY"].isnull()]
#        print(len(accident["INJURY"][accident["INJURY"].isnull()]))
        accident["INJURY"][accident["INJURY"].isnull()] = "Fatal"
#        print(len(accident["INJURY"][accident["INJURY"].isnull()]))

        accident["INITDIR"][accident["INITDIR"].isnull()]
#        print(len(accident["INITDIR"][accident["INITDIR"].isnull()]))
        accident["INITDIR"][accident["INITDIR"].isnull()] = "North"
#        print(len(accident["INITDIR"][accident["INITDIR"].isnull()]))

        accident["VEHTYPE"][accident["VEHTYPE"].isnull()]
#        print(len(accident["VEHTYPE"][accident["VEHTYPE"].isnull()]))
        accident["VEHTYPE"][accident["VEHTYPE"].isnull()] = "Other"
#        print(len(accident["VEHTYPE"][accident["VEHTYPE"].isnull()]))

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["District"])
        new_cat_features = enc.transform(accident["District"])
#        print(new_cat_features) # [1 2 0]
        accident["District"] = new_cat_features

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["ROAD_CLASS"])
        new_cat_features = enc.transform(accident["ROAD_CLASS"])
#        print(new_cat_features) # [1 2 0]
        accident["ROAD_CLASS"] = new_cat_features

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["LOCCOORD"])
        new_cat_features = enc.transform(accident["LOCCOORD"])
#        print(new_cat_features) # [1 2 0]
        accident["LOCCOORD"] = new_cat_features

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["ACCLOC"])
        new_cat_features = enc.transform(accident["ACCLOC"])
#        print(new_cat_features) # [1 2 0]
        accident["ACCLOC"] = new_cat_features

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["INJURY"])
        new_cat_features = enc.transform(accident["INJURY"])
#        print(new_cat_features) # [1 2 0]
        accident["INJURY"] = new_cat_features

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["INITDIR"])
        new_cat_features = enc.transform(accident["INITDIR"])
#        print(new_cat_features) # [1 2 0]
        accident["INITDIR"] = new_cat_features

        enc = preprocessing.LabelEncoder()
        enc.fit(accident["VEHTYPE"])
        new_cat_features = enc.transform(accident["VEHTYPE"])
#        print(new_cat_features) # [1 2 0]
        accident["VEHTYPE"] = new_cat_features

        accidentValue = accident.iloc[:, 5:12]
        accidentValue = accidentValue.reset_index()
        accidentValue = accidentValue.drop(['DATE'], axis=1)

        accidentValue = accidentValue.values

        kmeans = cluster.KMeans(n_clusters=3, init="k-means++", max_iter=300, n_init=10, random_state=0)
        yMeans = kmeans.fit_predict(accidentValue)

        self.classifier = svm.SVC(kernel='linear', random_state=0)
        self.classifier.fit(accidentValue, yMeans)

    def Predict(self, par):
        return self.classifier.predict(par)

def Main():
    pass
