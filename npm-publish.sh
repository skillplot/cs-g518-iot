#!/bin/bash

npm publish --tag $(basename ${PWD})-$(cat package.json | jq '.version' | tr -d '"')
