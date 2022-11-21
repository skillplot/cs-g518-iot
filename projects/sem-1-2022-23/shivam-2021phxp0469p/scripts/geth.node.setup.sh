
#!/bin/bash

function log.echo() {
  (>&2 echo -e "${bred}$*${nocolor}")
}


## step-1
function create_node() {
  type uuid &>/dev/null || sudo apt install uuid
  local node_name=$(uuid)
  log.echo "created node_name: ${node_name}"
  # geth init --datadir ${node_name} genesis.json
  echo ${node_name}
}


## step-2
function add_account() {
  local node_name=$1
  echo "add account for node: ${node_name}"
  # geth --datadir ${node_name} account new
}


## step-3
function start_node() {
  local node_name
  # geth --datadir node1 --networkid 1234 --http --allow-insecure-unlock --nodiscover --port 30303
  geth --datadir node1 --networkid 1234 --http --allow-insecure-unlock --nodiscover --port 30303
}

## step-4; in new terminal
function get_node_info() {
  # Open new terminal
  geth attach node1/geth.ipc

  # and in javascript console type below command:
  admin.nodeInfo
}

## step-5; type of node configuration: peer-to-peer;
## TODO: work in progress
function peer_to_peer() {
  echo "peer-to-peer"
  # # and copy the enode of second node into first node console
  # admin.addPeer("enode://fa74ba03b68b149f9ccd89ad2193b10293dbdb0500f5765d0ef2e86742a9f9a73131b50ece9620e80b7e2c768ba773edfd8eadbc12c65fefc063bca6144512d1@127.0.0.1:30304")
  # admin.peers

  # # and copy the enode of third node into second node console
  # admin.addPeer("enode://f147f0869a33c854fc4839b4d8256762bc7f4cbee346ab2eb11dd49fa8c30e886cb6bbef342870441d10349aa47cbcdb277f53bb185e3125a845503cb320418a@127.0.0.1:30305")
  # # and check the peers
  # admin.peers
}


function main() {
  echo "main"
  local node_name=$(create_node "$@")
  add_account ${node_name}
}


main "$@"
