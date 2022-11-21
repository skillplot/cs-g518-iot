#!/bin/bash

type geth &>/dev/null || {
  echo "Ethereum will be installed. sudo access required".
  sudo add-apt-repository -y ppa:ethereum/ethereum
  sudo apt-get update
  sudo apt-get install ethereum
} && {
  echo "geth is already installed"
}

geth version
