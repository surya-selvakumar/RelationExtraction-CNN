# RelationExtraction-CNN

### Data Source : https://aclanthology.org/2024.findings-naacl.230/

### Model Frame Source: https://github.com/YoumiMa/TablERT-CNN/

The data files given in this repository containes RAW files without tag elements. Execute the preprocessing script to get the processed files or download them from the link given under the folder

## Processing FIRE Data

> python ./processing/cnn.py 


## Environment Setup

Python: 3.7.0

```
python -m venv venv
```

> source venv/bin/activate

> pip install -r requirements.txt


## Model Training

> python run.py train --config ./configs/train.conf

## Model Evaluation

> python run.py eval --config ./configs/eval.conf

## Test the model with a custom example

> python test.py --config ./configs/test.conf
