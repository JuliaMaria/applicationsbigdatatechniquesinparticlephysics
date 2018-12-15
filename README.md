# cloud-bigdata
Repositorio para la asignatura Cloud and Big Data
# Webpage link: 
https://vivianasandagordaguaman.github.io/applicationsbigdatatechniquesinparticlephysics/
# Machine learning model - Boosted Trees with XGBoost (File MachineLearningModel/Higgs.py)
# Parameters:
- Dataset size used: 100000 (Full dataset: 11000000)
- Training set size: 80% of dataset size
- Evaluation set size: 20% of dataset size
- Objective: binary:logitraw
- Eta: 0.01
- Maximal depth: 9
- Evaluation metrics: auc and logloss
- Alpha: 1
- Gamma: 1
- Subsampling: 0.9
- Missing values set as -999.0
- Number of training epochs: 1500 (For better results: 3000)
# Requirements: 
- Python2 installed
- Packages installed: numpy, pandas, xgboost
- Dataset downloaded and saved in the same folder as Python code: https://archive.ics.uci.edu/ml/datasets/HIGGS
# Command to run: 
python Higgs.py
# Results: 
- Trained model saved in the same folder as Python code as higgs.model
