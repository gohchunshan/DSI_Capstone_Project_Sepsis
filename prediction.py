import joblib
import pickle

def predict(data):
    model = joblib.load('model.sav')
    #model = pickle.load(open(filename, 'rb'))
    #model = pickle.load('my_best_model.pkl')
    return model.predict(data)