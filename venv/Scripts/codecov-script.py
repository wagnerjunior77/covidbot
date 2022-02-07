#!C:\Users\Dinopc\PycharmProjects\COVIDBot\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'codecov==2.1.1','console_scripts','codecov'
__requires__ = 'codecov==2.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('codecov==2.1.1', 'console_scripts', 'codecov')()
    )
