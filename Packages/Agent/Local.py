#!/usr/bin/python3
from ic.identity import Identity
from ic.client import Client
from ic.agent import Agent
from Packages.Environment import PEM_FILE

with open(PEM_FILE, 'rb') as f:
    pem = f.read()

nft_canister = "rrkah-fqaaa-aaaaa-aaaaq-cai"
identity = Identity.from_pem(pem)
client = Client(url = "http://localhost:8000")
agent = Agent(identity, client)
