# RelationExtraction-CNN

#### Data Source : https://aclanthology.org/2024.findings-naacl.230/

#### Model Frame Source: https://github.com/YoumiMa/TablERT-CNN/

Execute the preprocessing script to get the processed data files or download them along with the trained model from the link given under the folder's README.md

## Processing FIRE Data
```
python ./processing/process.py $DATA_DIR $PROCESSED_DATA_DIR
```

## Environment Setup

Python: 3.7.0

```
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


## Model Training

```
python run.py train --config ./configs/train.conf
```

## Model Evaluation

```
python run.py eval --config ./configs/eval.conf
```

## Test the model with a custom example
```
python test.py --config ./configs/test.conf
```

## Colab Execution

1. Setup the folder structure in Google Drive
2. Execute the Train.ipynb / Test.ipynb respectively
