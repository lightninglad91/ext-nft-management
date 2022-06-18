#!/usr/bin/python3
from ic.candid import encode, Types
from Packages.Canister.Types import t_asset, t_mintingRequest, t_UpdateRequest

def getMinter(agent, canister_id):
    method = 'getMinter'
    params = []
    return agent.query_raw(canister_id, method, encode(params))

def setMinter(agent, canister_id, principal):
    method = 'setMinter'
    params =[{'type' : Types.Principal, 'value' : principal}]
    return agent.update_raw(canister_id, method, encode(params))

def updateAsset(agent, canister_id, vals):
    method = 'updateAsset'
    params = [{'type' : t_UpdateRequest, 'value' : vals}]
    return agent.update_raw(canister_id, method, encode(params))

def addAsset(agent, canister_id, vals): 
    method = 'addAsset'
    params = [{'type' : t_asset, 'value' : vals}]
    return agent.update_raw(canister_id, method, encode(params))

def mintNFT(agent, canister_id, destination, asset_id):
    method = 'mintNFT'
    vals = {
        'to' : destination, 
        'asset' : asset_id
    }
    params = [{'type' : t_mintingRequest, 'value' : vals}]
    return agent.update_raw(canister_id, method, encode(params))

def getBearer(agent, canister_id, tokenID):
    method = 'bearer'
    params = [{'type' : Types.Text, 'value' : tokenID}]
    return agent.query_raw(canister_id, method, encode(params))

def getMetadata(agent, canister_id, tokenID):
    method = 'metadata'
    params = [{'type' : Types.Text, 'value' : tokenID}]
    return agent.query_raw(canister_id, method, encode(params))