#======================================#
#                                      #
#                                      #
#    Author is not responsible for     #
#       any misuse of the tool.        #
#                                      #
#                                      #
#======================================#

# Type: OSINT
# Author: Semiii
# Contact: r3moved777@protonmail.com 
# Github: github.com/semiiixyz
# Language/s: Python3

# Install all required modules
import json, requests
from termcolor import cprint

# Interface
def interface():
    cprint("\t\t       Merry Christmas!", "white", attrs=['bold'])
    cprint("==============================================================", "yellow", attrs=['bold'])
    cprint("██╗██████╗ ██╗  ██╗██╗   ██╗███╗  ██╗████████╗███████╗██████╗", "red")
    cprint("██║██╔══██╗██║  ██║██║   ██║████╗ ██║╚══██╔══╝██╔════╝██╔══██╗", "red")
    cprint("██║██████╔╝███████║██║   ██║██╔██╗██║   ██║   █████╗  ██████╔╝", "red")
    cprint("██║██╔═══╝ ██╔══██║██║   ██║██║╚████║   ██║   ██╔══╝  ██╔══██╗", "red")
    cprint("██║██║     ██║  ██║╚██████╔╝██║ ╚███║   ██║   ███████╗██║  ██║", "red")
    cprint("╚═╝╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚══╝   ╚═╝   ╚══════╝╚═╝  ╚═╝", "red")
    cprint("==============================================================", "yellow", attrs=['bold'])
    cprint('[    Author is not responsible for any misuse of the tool    ]', 'white',attrs=['bold'])
    print('')
interface()
# IP address to hunt
ip_address = input('Enter IP Address: ')
print('')

# Request for data
request_url = 'https://geolocation-db.com/jsonp/' + ip_address
response = requests.get(request_url)
result = response.content.decode()
result = result.split("(")[1].strip(")")
result = json.loads(result)

# Print results in a clean format
print("Geolocation Results:")
for key, value in result.items():
    print(f"[*] {key.title()}: {value}")