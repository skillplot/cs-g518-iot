#!/bin/bash


function docs-build() {
  local LSCRIPTS=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
  local mkdocs_yml=$1
  local jsdoc_json=$2
  [[ ! -z ${mkdocs_yml} ]] || mkdocs_yml="${LSCRIPTS}/mkdocs.yml"
  [[ ! -z ${jsdoc_json} ]] || jsdoc_json="${LSCRIPTS}/jsdoc.json"

  echo "Using Mkdocs YAML: ${mkdocs_yml}"
  echo "Using Jsdoc Json: ${jsdoc_json}"

  source ${LSCRIPTS}/mkdocs.sh ${mkdocs_yml}
  source ${LSCRIPTS}/jsdoc.sh ${jsdoc_json}
}

docs-build "$@"
