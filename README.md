# helper_functions
Helper functions and utilities 

To import helper functions:

import requests
from pathlib import Path

# Download helper functions from this repository
if not Path("helper_functions.py").exists():
    request = requests.get("https://raw.githubusercontent.com/flumi77/helper_functions/helper_functions.py")  
    with open("helper_functions.py", "wb") as f:
        f.write(request.content)
