import os
from sys import exit
from Packages.Environment import REPORT_FILE, LOG_FILE, CANISTER_ID, COLLECTION, PRINCIPAL
from Packages.Formats import COLL_FMT, DROP_FMT, SUMM_FMT

class EventHandler:

    def __init__(self, Snapshot, ProjectName=COLLECTION, CanisterID=CANISTER_ID, OwnerID=PRINCIPAL, MinterID=PRINCIPAL) -> None:
        header = COLL_FMT(ProjectName, CanisterID, OwnerID, MinterID, Snapshot)
        self.log_file = LOG_FILE
        self.report_file = REPORT_FILE
        self._report = {
            'header' : header,
            'drop' : [],
            'summary' : ''
        }

    def print_screen(self, display_str=str) -> None:
        os.system('clear')
        print(display_str)

    def log(self, severity, context) -> None:
        with open(self.log_file, 'a') as f:
            if severity == 0:
                f.write(context)
                f.close
            elif severity == 1:
                f.write('WARNING:: '+context+'\n')
                f.close()
            else:
                f.write('FATAL:: '+context+'\n')
                input('FAULT:: The system has encountered a FATAL fault.\n\
                    Press [ENTER] to exit...')
                f.close()
                exit()
    
    def add_drop(self, TokenID, RandIndex, AccountID, Team, UpdatedHash) -> None:
        entry = DROP_FMT(TokenID, RandIndex, AccountID, Team, UpdatedHash)
        self.log(0, entry)
        self._report['drop'].append(entry)
        self.print_screen(entry)

    def add_summary(self, TotalMint, TeamAlloc, CommAlloc) -> None:
        summary = SUMM_FMT(TotalMint, TeamAlloc, CommAlloc)
        self._report['summary'] = summary
    
    def write_report(self) -> None:
        with open(self.report_file, 'w') as f:
            f.write(self._report['header'])
            f.writelines(self._report['drop'])
            f.write(self._report['summary'])
            f.close()