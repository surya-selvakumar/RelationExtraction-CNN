# RelationExtraction-CNN

Data Source : https://aclanthology.org/2024.findings-naacl.230/
Model Frame Source: https://github.com/YoumiMa/TablERT-CNN/


## Environment Setup

Python: 3.7.0

> python -m venv venv

> source venv/bin/activate

> pip install -r requirements.txt


## Model Training

> python run.py train --config ./configs/train.conf

## Model Evaluation

> python run.py eval --config ./configs/eval.conf

## Model Testing

> python run.py --config ./configs/test.conf
