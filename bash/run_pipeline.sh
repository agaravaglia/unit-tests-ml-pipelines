!#bin/bash

step="$1"

if [ "$step" == "" ]
then
    preprocess
    feature_engineering
    train
    predict
else
    $step
fi
