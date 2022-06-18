#!/usr/bin/python3
from ic.candid import Types

t_asset = Types.Record({
    'name' : Types.Text,
    'thumbnail' : Types.Opt(Types.Record({
        'data' : Types.Vec(Types.Vec(Types.Nat8)),
        'ctype' : Types.Text})),
    'payload' : Types.Record({
        'data' : Types.Vec(Types.Vec(Types.Nat8)),
        'ctype' : Types.Text})
})

t_UpdateRequest = Types.Record({
    'assetID' : Types.Nat,
    'payload' : Types.Record({
        'data' : Types.Vec(Types.Vec(Types.Nat8)),
        'ctype' : Types.Text
    })
})

t_mintingRequest = Types.Record({
    'to' : Types.Text,
    'asset' : Types.Nat32
})

