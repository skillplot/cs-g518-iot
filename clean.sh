#!/bin/bash

find ${PWD}/ -iname node_modules -type d | xargs -n 1 bash -c 'rm -rf "$0"'
find ${PWD}/ -iname __pycache__ -type d | xargs -n 1 bash -c 'rm -rf "$0"'
find ${PWD}/ -iname *.egg-info -type d | xargs -n 1 bash -c 'rm -rf "$0"'
find ${PWD}/ -iname _site -type d | xargs -n 1 bash -c 'rm -rf "$0"'
