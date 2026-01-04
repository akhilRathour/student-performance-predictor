This is my first end to end ml project

The steps im taking:
1.create conda env: "conda create -p venv python=3.8 -y"
2.activate venve: "conda activate venv/"
3.initialize git : git init
4. setup.py and req.txt
5.project structure: components-our modules=>data_ingestion.py,data_transformation.py,model_trainer.py,
pipeline folder: train_pipeline, predict_pipeline .py
in src :exception.py, logger.py utils.py:code thats helpffull for whole project
6. logging and exception
7.EDA in EDA.ipynb
8.train model in ipynb
9.map everything done in notebook to src 
10.data ingestion, where we read our dataset from a source, performed a train-test split, and saved the data inside an artifact folder.
11.data transformation, which involves feature engineering and data cleaning, such as converting categorical features into numerical features.
12.