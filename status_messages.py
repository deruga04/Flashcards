from termcolor import colored, cprint

#print_success = lambda x: cprint('[+] ' + x, 'green')
print_success = lambda x: print(colored('[+] ', 'green') + x)
print_fail = lambda x: print(colored('[-] ', 'red') + x)
print_warn = lambda x: print(colored('[!] ', 'yellow') + x)
print_input = lambda x: print(colored('[>] ', 'white') + x)