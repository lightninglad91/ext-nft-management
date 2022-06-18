#!/usr/bin/python3
import sys
from Packages.Canister.Methods import updateAsset

if sys.argv[1] == 'ic':
    from Packages.Agent.Mainnet import agent
if sys.argv[1] == 'local':
    from Packages.Agent.Local import agent

canister_id = sys.argv[2]
token_index = int(sys.argv[3])
asset_file = sys.argv[4]
with open(asset_file, 'rb') as f:
    asset = list(f.read())
    asset = [asset]

vals = {
    'assetID' : token_index,
    'payload' : {'ctype' : 'image/jpeg', 'data' : asset}
}

def main():
    results  = updateAsset(agent, canister_id, vals)
    print(results)

if __name__ == "__main__":
    main()
