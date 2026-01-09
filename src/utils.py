#for modules that are helpfull throghout project
import os
import pandas as pd
from src.exception import CustomException
import dill
import sys

def save_object(file_path,obj):
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,"wb") as file_obj:
            dill.dump(obj,file_obj)

    except CustomException as e:
        raise CustomException(e,sys)