#!/bin/bash

## install twine if not installed
# pip publish twine
## to publish using twine
# twine upload ./dist/* --config-file ${HOME}/.pypirc
## if `.pypirc` file is on the root of the project
twine upload ./dist/* --config-file ./.pypirc
