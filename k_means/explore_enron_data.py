#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


# Create set of all keys in the system
# masterKeys = set()
# for name, features  in enron_data.items():
#     for k, v in features.items():
#         masterKeys.add(k)
#
# print masterKeys
#

# get max or min features
salaryList = []
for name, features in enron_data.items():
    for k,v in features.items():
        if k == "exercised_stock_options" and v != "NaN":
            salaryList.append(v)

print sorted(salaryList)





