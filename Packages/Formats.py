
def COLL_FMT(ProjectName, CanisterID, OwnerID, MinterID, SnapshotHash) -> str:
    header = '\
    ##### COLLECTION #####\n\n\
    Name:  {0}\n\
    CanisterID:  {1}\n\
    OwnerID:  {2}\n\
    MinterID:  {3}\n\
    Snapshot:  {4}\n\n\
    ##### AIRDROP #####\n'.format(ProjectName, CanisterID, OwnerID, MinterID, SnapshotHash)

    return header

def DROP_FMT(AssetID, RandIndex, AccountID, Team, UpdatedHash) -> str:
    entry = '\
    AssetID:  {0}\n\
    RandIndex:  {1}\n\
    AccountID:  {2}\n\
    Team:  {3}\n\
    Hash:  {4}\n\n'.format(AssetID, RandIndex, AccountID, Team, UpdatedHash)

    return entry

def SUMM_FMT(TotalMint, TeamAlloc, CommAlloc) -> str:
    entry = '\
    Total Minted:  {0}\n\
    Team Allocation:  {1}\n\
    Community Allocation:  {2}\n'.format(TotalMint, TeamAlloc, CommAlloc)

    return entry