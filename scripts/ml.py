
import pickle

from sklearn import preprocessing
from xgboost import XGBClassifier


def save_model(fname, model):
    pickle.dump(model, open(fname, "wb"))


def load_model(fname):
    return pickle.load(open(fname, "rb"))


def xgb_train(x_train, y_train):
    model = XGBClassifier()
    model.fit(x_train, y_train)
    return model


def xgb_predict(model,
                logs_df,
                tracks=["GR", "DTC", "RESD", "RESM", "RHOB", "PEF", "NPHI"]):
    
    data = logs_df[tracks[0]].values.reshape((-1,1))

    for c in tracks[1:]:
        data = np.hstack((data, logs_df[c].values.reshape((-1,1))))

    x_test = preprocessing.scale(data)

    return model.predict(x_test)

