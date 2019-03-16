import pickle
import json
import numpy as np
import azureml.train.automl
from sklearn.externals import joblib
from azureml.core.model import Model


def init():
    global model
    model_path = Model.get_model_path(model_name = 'AutoML2d8299a8fbest') # this name is model.id of model that we want to deploy
    # deserialize the model file back into a sklearn model
    model = joblib.load(model_path)

def run(timestamp,precip,temp):
    try:
        rawdata = json.dumps({timestamp, precip, temp})
        data = json.loads(rawdata)
        data_arr = numpy.array(data)
        result = model.predict(data_arr)
        # result = json.dumps({'timeStamp':timestamp, 'precip':precip, 'temp':temp})
    except Exception as e:
        result = str(e)
        return json.dumps({"error": result})
    return json.dumps({"result":result.tolist()})
