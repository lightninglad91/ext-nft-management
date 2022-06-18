#!/usr/bin/python3
import sys, hashlib
from Packages.Utils import bulk_update, process_accounts, bulk_upload
from Packages.Classes.EventHandler import EventHandler
from Packages.Classes.Airdrop import Airdrop
from Packages.Environment import TEAM_ADDRESS

if len(sys.argv) > 1 and sys.argv[1] == 'ic':
    from Packages.Agent.Mainnet import agent, nft_canister
else:
    from Packages.Agent.Local import agent, nft_canister

def main() -> None:
    accounts = process_accounts()
    #assets = bulk_upload(agent, nft_canister)
    assets = bulk_update(agent, nft_canister)
    #init_hash = hashlib.sha1(''.join(accounts).encode()).hexdigest()
    #event_handler = EventHandler(init_hash)
    #airdrop = Airdrop(agent, event_handler, accounts, assets)
    #airdrop.drop()
    #event_handler.write_report()

if __name__ == '__main__':
    main()