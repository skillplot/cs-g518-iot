---
title: Blockchain Private Network
description: Blockchain Private Network
---


# Blockchain Private Network


We are going to create three nodes on Private Ethereum Blockchain that is Go ethereum which based on Go language.
* [geth.ethereum - private-network](https://geth.ethereum.org/docs/interface/private-network)


## A. Installation

1. Installing Go Ethereum
    ```bash
    sudo add-apt-repository -y ppa:ethereum/ethereum
    sudo apt-get update
    sudo apt-get install ethereum
    ```
2. To check whether geth is installed
    ```bash
    geth -h
    ```

## B. Creating Genesis Block file which is a starting point

1. Create different directory called "data" or any name
  ```bash
  mkdir data
  cd data
  touch genesis.json
  ```
2. Add this code into `genesis.json` file. Remember chain id or network id for future reference :1234
    ```json
    {
      "config": {
        "chainId": 1234,
        "homesteadBlock": 0,
        "eip150Block": 0,
        "eip155Block": 0,
        "eip158Block": 0,
        "byzantiumBlock": 0,
        "constantinopleBlock": 0,
        "petersburgBlock": 0,
        "ethash": {}
      },
      "difficulty": "4",
      "gasLimit": "8000000",
      "alloc": {}
    }
    ```
4. Initializing nodes for miners: 3 nodes become miners
    ```bash 
    geth init --datadir node1 genesis.json
    geth init --datadir node2 genesis.json
    geth init --datadir node3 genesis.json
    ```
5. Add account to all nodes (Optional). Do remember the password and other details which we have entered; Refer .gitignore file
    ```bash
    geth --datadir node1 account new //
    geth --datadir node2 account new //
    geth --datadir node3 account new //
    ```


## Stating Nodes

1. Start Nodes
    ```bash
    # (i)
    geth --datadir node1 --networkid 1234 --http --allow-insecure-unlock --nodiscover --port 30303

    # - Open new terminal
    geth attach node1/geth.ipc

    # and in javascript console type below command:
    admin.nodeInfo

    # (ii)
    geth --datadir node2 --networkid 1234 --port 30304 --authrpc.port 8552

    # - Open new terminal
    geth attach node2/geth.ipc

    # and in javascript console type below command:
    admin.nodeInfo

    # (iii)
    geth --datadir node3 --networkid 1234 --port 30305 --authrpc.port 8553 

    # -- Open new terminal
    geth attach node3/geth.ipc

    # -- and in javascript console type below command:
    admin.nodeInfo

    # -- and copy the enode of second node into first node console
    admin.addPeer("enode://fa74ba03b68b149f9ccd89ad2193b10293dbdb0500f5765d0ef2e86742a9f9a73131b50ece9620e80b7e2c768ba773edfd8eadbc12c65fefc063bca6144512d1@127.0.0.1:30304")
    admin.peers

    # -- and copy the enode of third node into second node console
    admin.addPeer("enode://f147f0869a33c854fc4839b4d8256762bc7f4cbee346ab2eb11dd49fa8c30e886cb6bbef342870441d10349aa47cbcdb277f53bb185e3125a845503cb320418a@127.0.0.1:30305")
    # -- and check the peers
    admin.peers
    ```

## Mining

1. Start Mining
    ```bash
    # - Write this in first node javascript console
    personal.newAccount()

    # - Enter Passphrase: 1234

    # - Address has been generated
    "0x56320c97eef22206716a8c8f316430e43b3e4c1f"

    # - start mining
    miner.start() 
    miner.stop()  

    # - To check blocknumber
    eth.blockNumber

    # - To see balance
    eth.getBalance("0x56320c97eef22206716a8c8f316430e43b3e4c1f")

    # - To see the peerCount
    net.peerCount

    # - To see the accounts
    eth.accounts
    
    # -To unlock account
    personal.unlockAccount(eth.accounts[0])

    # -To send some Wei
    eth.sendTransaction({to: "", from: eth.accounts[0],value: 25000})
    eth.sendTransaction({to: "0x8e0ee9a4fc2302b15a61aca22f7f95c829be1583", from: eth.accounts[0],value: 26000000000000000000})
    # -To kill the blockchain
     kill -INT "43872"


    ```

## Rough notes

* https://stackoverflow.com/a/47274698

So AArch64 and ARM64 refer to the same thing.

aarch64 is 64bit
armv7 is 32 bit




