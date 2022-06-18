#!/usr/bin/python
import hashlib
from random import randint
from typing import Tuple
from Packages.Canister.Methods import mintNFT
from Packages.Environment import RARE, COMMON, MAX_TEAM_MINT, CANISTER_ID, TEAM_ADDRESS

class Airdrop:
    def __init__(self, Agent, EventHandler, Accounts, Assets, Canister=CANISTER_ID, Team=TEAM_ADDRESS) -> None:
        self._agent = Agent
        self._event_handler = EventHandler
        self._canister = Canister
        self._assets = Assets
        
        if Team:
            self._team_address = Team
            self._team_minted = 0
            self._team_distro = True
        else:
            self._team_distro = False

        if type(Accounts) == list:
            self._controlled = False
            self._all_accounts = Accounts
        elif type(Accounts) == dict:
            try:
                self._controlled = True
                self._active_accounts = Accounts['active']
                self._inactive_accounts = Accounts['inactive']
                self._all_accounts = [*self._inactive_accounts, *self._active_accounts]
            except KeyError:
                self._event_handler.log(2, 'Expected key values [ active || inactive ] missing')
        else:
            self._event_handler.log(2, 'Incorrect type; i_accounts should be [ list || dict ]')
        
    def _controlled_drop(self, assetID) -> Tuple[bool, str, int]:
        try:
            if self._assets[assetID][0] == RARE:
                rare = True
                rand_index = randint(0, len(self._active_accounts)-1)
            elif self._assets[assetID][0] == COMMON:
                rare = False
                rand_index = randint(0, len(self._all_accounts)-1)
            else:
                self._event_handler.log(2, 'Controlled Distribution: self._assets must be a dict with list entries where list[0]\
                     is str == [ "'+RARE+'" || "'+COMMON+'" ]')
        except: self._event_handler.log(2, 'Controlled Distribution: self._assets must be a dict with list entries where list[0]\
            is str ==  "'+RARE+'" || "'+COMMON+'" ]')

        if rare: accountID = self._active_accounts[rand_index]
        else: accountID = self._all_accounts[rand_index]

        results = mintNFT(self._agent, self._canister, accountID, assetID)

        return rare, accountID, rand_index


    def _uncontrolled_drop(self, assetID) -> Tuple[str, int]:
        if len(self._all_accounts) == 1:
            rand_index = 0
            accountID = self._all_accounts[rand_index]
        elif len(self._all_accounts) == 0:
            rand_index = 0
            accountID = TEAM_ADDRESS
        else: 
            rand_index = randint(0, len(self._all_accounts)-1)
            accountID = self._all_accounts[rand_index]

        mintNFT(self._agent, self._canister, accountID, assetID)
        with open('accounts_minted.txt', 'a') as f:
            f.write(accountID+"\n")
            f.close()
        return accountID, rand_index

    def drop(self) -> None:
        mint_range = len(self._assets)
        for assetID in range(0, mint_range):
            verified_mint = False
            attempts = 1
            team = False
            if self._controlled:
                rare, accountID, rand_index, team = self._controlled_drop(assetID)
                if self._team_distro and accountID == self._team_address:
                    self._team_minted += 1
                    if self._team_minted == MAX_TEAM_MINT:
                        self._event_handler.log(0, 'TEAM_ADDRESS REMOVED: Minted = '+str(self._team_minted))
                        self._all_accounts.remove(accountID)
                        if rare: self._active_accounts.remove(accountID)
                    else:
                        self._all_accounts.remove(accountID)
                        if rare:
                            self._active_accounts.remove(accountID)
                else: attempts += 1
            else:
                accountID, rand_index = self._uncontrolled_drop(assetID)
                if self._verify_mint(accountID, assetID, attempts):
                    verified_mint = True
                    if self._team_distro and accountID == self._team_address:
                        self._team_minted += 1
                        if self._team_minted == MAX_TEAM_MINT:
                            self._all_accounts.remove(accountID)
                    else:
                        self._all_accounts.remove(accountID)
                else:
                    attempts += 1

            h_object = hashlib.sha1(''.join(self._all_accounts).encode())
            updatedHash = h_object.hexdigest()
            if accountID == self._team_address:
                self._team_minted += 1
                team = True
            self._event_handler.add_drop(str(assetID), str(rand_index), accountID, str(team), updatedHash)

