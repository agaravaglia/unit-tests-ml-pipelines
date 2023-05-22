!#bin/bash

# Remove all nested folders
find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf