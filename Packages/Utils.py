import sys
from os import listdir
from os.path import isfile, join
from Packages.Canister.Methods import addAsset, updateAsset
from Packages.Environment import ACCOUNTS_FILE, ASSET_FOLDER, THUMB_FOLDER, TOTAL_MINT, MINT_CORRECTION,\
    ASSET_UPDATE_FOLDER, ASSET_EXT, THUMB_UPDATE_FOLDER

def process_accounts() -> list:
    final_list = []
    with open(ACCOUNTS_FILE, 'r') as f:
        lines = f.readlines()
    for line in lines:
        final_list.append(line.strip())
    return final_list

def bulk_upload(agent, CANISTER_ID) -> dict:
    final = {}
    assets = [f for f in listdir(ASSET_FOLDER) if isfile(join(ASSET_FOLDER, f))]
    for asset in assets:
        attributes = asset.split('_')
        final[int(attributes[0])-1] = [asset.strip('.jpg'), attributes[1], join(ASSET_FOLDER, asset)]
    if len(final) != int(TOTAL_MINT):
        print("FATAL:: Total processed assets is < or > TotalMint.")
        sys.exit()
    else:
        for i in range(MINT_CORRECTION, TOTAL_MINT):
            name = final[i][0]
            image_file = final[i][2]
            thumb_file = join(THUMB_FOLDER, name+'.jpg')

            with open(image_file, 'rb') as f:
                payload = f.read()
            with open(thumb_file, 'rb') as f:
                thumbnail = f.read()

            vals = {
                'name' : name,
                'thumbnail' : [{'ctype' : 'image/png', 'data' : [thumbnail]}],
                'payload' : {'ctype' : 'image/jpeg', 'data' : [payload]}
                }
            addAsset(agent, CANISTER_ID, vals)
            print(name+' Uploaded Successfully')
    return final

def bulk_update(agent, CANISTER_ID) -> dict:
    final = {}
    assets = [f for f in listdir(ASSET_UPDATE_FOLDER) if isfile(join(ASSET_UPDATE_FOLDER, f))]
    for asset in assets:
        attributes = asset.split('_')
        final[int(attributes[0])-1] = [asset.strip(ASSET_EXT), attributes[1], join(ASSET_UPDATE_FOLDER, asset)]
    if len(final) != int(TOTAL_MINT):
        print("FATAL:: Total processed assets is < or > TotalMint.")
        sys.exit()
    else:
        for i in range(MINT_CORRECTION, TOTAL_MINT):
            name = final[i][0]
            image_file = final[i][2]

            with open(image_file, 'rb') as f:
                payload = f.read()

            vals = {
                'assetID' : i,
                'payload' : {'ctype' : 'image/jpeg', 'data' : [payload]}
            }
            
            updateAsset(agent, CANISTER_ID, vals)
            print(name+' Updated Successfully')
    return final
