# Unit tests for Machine Learning Pipelines

Data Scientists usually write code in notebooks, that are an excellent interactive environment for the experimental work that is creating a machine learning model but are not usually deployed to production. In fact, code is typically converted to structured, well-tested and robust modules, and any change to the code-base requires some development time before being integrated into the production pipeline.
In this setting, testing your code is fundamental to minimize disruptions and deploy new features in a more stable manner. The first level of tests of any software are usually unit-tests, that are tests designed to check that a single piece of code is working correctly and produces the desired results. These tests are usually automatically executed and are well known by software developers, but not by Data Scientists.

In this repo, it is implemented a toy end-to-end example of a machine learning pipeline, toghether with the correspongin unit-tests. The example pipeline will does the classical steps of an ML project (preprocessing, feature engineering, training, predicting) for a binary classifier that can predict whether a pokemon is legendary or not.

The repo contains the development notebook where the pipeline was originally desgined, and the corresponding structured module to execute the pipeline programmatically. In the tests folder all the unit tests for the four steps of the pipeline are implemented.

This repo is meant to be an example for data scientists who might not be expert in testing and want to see concrete examples of how implement simple unit-tests for ther projects.

# Table of contents
- [Setup](#setup)
- [Sources](#sources)
- [Scope](#scope)
- [Development notebook](#development-notebook)
- [Productionized pipeline](#productionized-pipeline)
- [Unit tests](#unit-tests)
- [Makefile](#makefile)
- [Spark](#spark)

## Setup
It is recommend to execute the current repo in a virtual environment. We recommend Python 38. For example with conda
```
conda create -n new-env python=3.8
```
To install the needed requirements, you can either use pip
```
pip install -r requirements.txt
```
Otherwise you can launch the setup.py of the custom package of the repo, always via pip
```
pip install -e .
```

## Sources
The dataset used is taken from Kaggle: https://www.kaggle.com/datasets/rounakbanik/pokemon. You can download it by authenticating in Kaggle and launch the jupyter notebook in notebook/create_datasets_from_kaggle.ipynb.

For the notebook to run, you need a valid account in Kaggle and a valid authentication token. You need to store a json file called 'kaggle.json' in the data/credentials directory (the file will be ignored by git).

The kaggle.json file should look like this:

```
{
    "username": "your_username",
    "key": "your_authentication_token"
}
```

The data will be automatically stored into the folder datasets/raw. 


## Scope
In this repo, we implement a classification model in sklearn that predicts whether a pokemon is LEGENDARY or not. For the lable, we use the column "is_legendary" from the dataset.

## Development notebook
For standard data sciene work, you probably work in jupyter notebook or jupyter lab. The prototype of our pipeline is developed in 'notebooks/develop_notebook.ipynb'.

## Productionized pipeline
The prototype of the pipeline is converted into a python module. The setup.py should help you in setting up the dependencies and allow you to run the pipeline.

### Entrypoints
The pipeline is then structured in four block, representing the standard ML workload:

- Preprocess: we take raw data and clean it 
- Feature_engineering: we define features to feed out ML model
- Train: we do hyperparameter tuning and then train a LogisticRegression model from Sklearn
- Predict: we load the model and do prediction on a new batch of data

### Module structure
Every entrypoint has a main method, which uses functions defined in helpers. As you can see, I am not a fan of classes (functions are easier to test).

## Unit tests
Unit tests are located into the tests folder. Tests structure mirror the src structure. For every file like 'src/preprocess/helpers.py' you will see a file called 'tests/preprocess/test_helpers.py', with the unit-tests of that particular file.


## Makefile
In the makefile, there are commands to execute automatically all the commands of the pipeline and the test:

```
    make pipeline step=preprocess
```
will execute the preprocess. As step variable you can provide one of the entrypoints (preprocess, feature_engineering, train, predict). If you do not specify any step
```
    make pipeline
```
will execute all the pipeline.

A similar command works for pytest:
```
    make pytest path=tests/preprocess
```
will execute the tests in the preprocess folder. If you do not specify any path, all tests will be executed.

## Spark
There is an additional test present in the repo as an example of a spark fixture. The test is under tests/extra. By default the test is not executed. If you want to run it, you need to:
- Uncomment the __pyspark==3.2.0__ dependency in the setup.py file
- Change the name from __tests/extra/_test_spark.py__ to __tests/extra/test_spark.py__