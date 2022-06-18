#!/usr/bin/python3
from ic.identity import Identity
from ic.client import Client
from ic.agent import Agent
from Packages.Environment import CANISTER_ID, CLIENT_NET, PEM_FILE

with open(PEM_FILE, 'rb') as f:
    pem = f.read()

nft_canister = CANISTER_ID
identity = Identity.from_pem(pem)
client = Client(url = CLIENT_NET)
agent = Agent(identity, client)
