from setuptools import setup, find_packages


setup(
    name='unit_tests_ml',
    version='0.1.0',
    packages=find_packages(include=['src', 'src.*']),
    install_requires=[
        'pandas==1.5.0',
        'numpy==1.24.3',
        "hyperopt==0.2.7",
        "scikit-learn==1.2.0",
        #pyspark==3.2.0
    ],
    extras_require={
        'interactive': [
            'matplotlib', 
            'jupyter==1.0.0'
        ],
        'tests': [
            "pytest==7.3.1"
        ]
    },
    entry_points={
        "console_scripts": [
            "preprocess=src.preprocess:main",
            "feature_engineering=src.feature_engineering:main",
            "train=src.train:main",
            "predict=src.predict:main",
        ]
    },
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)