# RelationExtraction-CNN

Data Source : https://aclanthology.org/2024.findings-naacl.230/
Model Frame Source: https://github.com/YoumiMa/TablERT-CNN/


## Environment Setup

Python: 3.7.0

> python -m venv venv

> source venv/bin/activate

> pip install -r requirements.txt


# Training

> python run.py train --config ./configs/train.conf

# Evaluation

> python run.py eval --config ./configs/eval.conf

# Testing

> python run.py --config ./configs/test.conf
