
import pickle

from xgboost import XGBClassifier


def save_model(fname, model):
    pickle.dump(model, open(fname, "wb"))


def load_model(fname):
    return pickle.load(open(fname, "rb"))


def xgb_train(x_train, y_train):
    model = XGBClassifier()
    model.fit(x_train, y_train)
    return model


def xgb_predict(model, x_pred):
    return model.predict(x_pred)

