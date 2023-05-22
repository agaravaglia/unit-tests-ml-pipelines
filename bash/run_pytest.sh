!#bin/bash

path="$1"

# Run pytests
if [ "$path" != "" ]
then
    python -m pytest "$path" --disable-pytest-warnings
else
    python -m pytest --disable-pytest-warnings
fi

# Remove folder at root
rm -r .pytest_cache || exit