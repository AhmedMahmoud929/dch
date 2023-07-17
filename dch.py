import sys
import argparse
import requests
from urllib.parse import urlparse
from colorama import init, Fore

init(autoreset=True)

STATUS_CODES = {
    200: "OK",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    500: "Internal Server Error"
}



def check_domains():
    # read the input as a file
    input_file = open(input_path, 'r')
    domains = input_file.read().splitlines()

    for domain in domains:
        # make the domain a valid : google.com -> http://google.com 
        if not urlparse(domain).scheme:
            domain = "http://" + domain

        # TRY
        try:
            # send http GET request and store the status code
            session = requests.Session()
            request = session.prepare_request(requests.Request("GET", domain, headers=headers))
            if verbose:
                print_request(request)

            # response
            response = session.send(request, timeout=timeout)
            status_code = response.status_code
            status_text = STATUS_CODES.get(status_code, "Unknown")
  
            # main condition block
            if status_code == 200:
                print_result(f"{Fore.GREEN}\U0001F7E9 {domain} -> {status_code} ({status_text})")
            # print another codes if --onlylive not set
            elif status_code!=200 and not only_live:
            	print_result(f"{Fore.YELLOW}\U0001F7E7 {domain} -> {status_code} ({status_text})")

        # Exceptions
        except requests.RequestException:
            if not only_live:
            	print_result(f"{Fore.RED}\U0001F7E5 {domain} -> Failed to connect") 
        except requests.Timeout:
            if not only_live:
                print_result(f"{Fore.RED}\U0001F7E5 {domain} -> Timeout")  
        except KeyboardInterrupt: 
            sys.exit(0)


def print_result(result):

    # add seperator if verbose is set
    if verbose:
        result += "\n\n" +  Fore.RESET + "="*50 + "\n"

    # output in the terminal
    if not output_path:
        print(result)
    # output into a file
    else:
        with open(output_path,"a") as output_file:
            output_file.write(result+"\n")

def print_info():
    
    # get domains number
    input_file = open(input_path, 'r')
    domains = input_file.read().splitlines()
    num_domains = len(domains)
    
    # ==================== #
    print(Fore.BLUE + '='*50)

    # if only_live is set
    if only_live:
        print(f"{Fore.YELLOW}[+] Scanning for only live in : {num_domains} domain(s)")
    # defualt print
    else:
        print(f"{Fore.YELLOW}[+] Scanning for : {num_domains} domain(s)")

    # if output_path is set
    if output_path:
        print(f"{Fore.YELLOW}[+] Results will be in {output_path}")

    # if timeout is set
    if timeout!=5.0:
        print(f"{Fore.YELLOW}[+] Timeout for each request will be {timeout}s")

    # ==================== #
    print(Fore.BLUE + '='*50 + "\n")

def print_request(request):
    print(f"Request: {request.method} {request.url}")
    print("Headers:")
    for name, value in request.headers.items():
        print(f"  {name}: {value}")
    print()

def print_banner():
    banner = rf"""
//////////////////////////////////////////////////
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
/////////////{Fore.YELLOW}  ____     ____ _   _   {Fore.BLUE}/////////////
\\\\\\\\\\\\\{Fore.YELLOW} |  _ \   / ___| | | |  {Fore.BLUE}\\\\\\\\\\\\\
/////////////{Fore.YELLOW} | | | |=| |   | |_| |  {Fore.BLUE}/////////////
\\\\\\\\\\\\\{Fore.YELLOW} | |_| |=| |___|  _  |  {Fore.BLUE}\\\\\\\\\\\\\
/////////////{Fore.YELLOW} |____/   \____|_| |_|  {Fore.BLUE}/////////////
\\\\\\\\\\\\\{Fore.BLUE}                        \\\{Fore.YELLOW}version{Fore.BLUE}\\\
/////////////////////////////////////////{Fore.YELLOW}0.0.1{Fore.BLUE}////
\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    """
    print(Fore.BLUE + banner)
    
    

# Create the argument parser
parser = argparse.ArgumentParser(description='Domain Checker')
parser.add_argument('-i', '--input', help='File path containing the list of domains', required=True)
parser.add_argument('-t', '--timeout', type=float, help='Timeout for each request in seconds', default=5.0)
parser.add_argument('-l', '--live',action='store_true', help='Only live domains (200 OK)')
parser.add_argument('-o', '--output', help='Output file path')
parser.add_argument('-ua', '--user-agent', help='Custom User-Agent header value')
parser.add_argument('-ch', '--custom-header', help='Custom header in the format "Name: Value"')
parser.add_argument('-v','--verbose', action='store_true', help='Enable verbose output, providing more detailed information about each request')




# Parse the command-line arguments
args = parser.parse_args()

# Retrieve the input file path and timeout from the parsed arguments
input_path = args.input
output_path = args.output
timeout = args.timeout
only_live = args.live
user_agent = args.user_agent
custom_header = args.custom_header
verbose = args.verbose

# Set the headers of the request
headers = {}
if user_agent:
    headers['User-Agent'] = user_agent
if custom_header:
    parts = custom_header.split(':')
    if len(parts) == 2:
        name = parts[0].strip()
        value = parts[1].strip()
        headers[name] = value


# Print functions
print_banner()
print_info()

# Check the domains
try:
    check_domains()
except KeyboardInterrupt:
    print("\nProgram interrupted by user. Exiting...")
    sys.exit(0)
