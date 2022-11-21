#!/bin/bash

# * https://stackoverflow.com/a/47274698
## AArch64 and ARM64 refer to the same thing.
## aarch64 is 64bit
## armv7 is 32 bit

## ARM64/AArch64 - RPI
# https://gethstore.blob.core.windows.net/builds/geth-linux-arm64-1.10.26-e5eb32ac.tar.gz
# https://archlinuxarm.org/packages/aarch64/go-ethereum
# https://geth.ethereum.org/downloads/

## AMD64 - Ubuntu
# https://gethstore.blob.core.windows.net/builds/geth-linux-amd64-1.10.26-e5eb32ac.tar.gz

PROG=geth-linux-arm64-1.10.26-e5eb32ac
FILE=${PROG}.tar.gz
URL=https://gethstore.blob.core.windows.net/builds/${FILE}

echo "PROG: ${PROG}"
echo "FILE: ${FILE}"
echo "URL: ${URL}"

wget ${URL}
tar -xvf ${FILE}
cd ${PROG}
sudo mv geth /usr/local/bin/
