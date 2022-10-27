#!/bin/bash

function jsdoc-build() {
  local LSCRIPTS=$( cd "$( dirname "${BASH_SOURCE[0]}")" && pwd )
  local jsdoc_json=$1
  [[ ! -z ${jsdoc_json} ]] || jsdoc_json="${LSCRIPTS}/jsdoc.json"

  echo "Using Jsdoc Json: ${jsdoc_json}"
  npm run jsdoc -- --configure ${jsdoc_json} --verbose
}

jsdoc-build "$@"
