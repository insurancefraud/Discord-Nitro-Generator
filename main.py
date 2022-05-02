try:
    import requests
    import string
    import time
    import random as r
except:
    print('Error: Failed to import one or more libraries.')
    exit_input = input('Enter Any Key to Exit : ')


# Variables
characters = string.ascii_letters + string.digits
var = r.choice
amount_gen = 0


# Functions
def checker():
    
    # Successful
    if requested.status_code == 200:
        valid_codes = [] 
        valid_codes.append(full_url)
        
        print('[-] Valid Nitro Link: ', full_url)
        
        print(', '.join(valid_codes))

        with open ('codes.txt', 'w') as file:
            file.write(''.join(valid_codes))
        
        print(f'\t{amount_gen}/{num}')
    
    # Not successful
    else:
        print('\n' + '[-] Invalid Nitro Link: {}'.format(full_url))
        
        # print('[-] Referral Code: ' + ''.join(url.text))
        
        print(f'\t{amount_gen}/{num}')
    
    
    # Normal invalid error
    # if 'Unknown Gift Code' in requested.text:
        
    #     print('\n' + '[-] Invalid Nitro Link: {}'.format(full_url))
        
    #     # print('[-] Referral Code: ' + ''.join(url.text))
        
    #     print(f'\t{amount_gen}/{num}')
    
    # Rate limited error
    # if requested.status_code == 429:
        
    #     print(f'[-] {full_url} was rate limited. Breaking process')
        
    #     print()
        
    #     # print(url.text)
        
    #     print(f'\t{amount_gen}/{num}')


print(""" _                                             __                     _ 
(_)_ __  ___ _   _ _ __ __ _ _ __   ___ ___   / _|_ __ __ _ _   _  __| |
| | '_ \/ __| | | | '__/ _` | '_ \ / __/ _ \ | |_| '__/ _` | | | |/ _` |
| | | | \__ \ |_| | | | (_| | | | | (_|  __/ |  _| | | (_| | |_| | (_| |
|_|_| |_|___/\__,_|_|  \__,_|_| |_|\___\___| |_| |_|  \__,_|\__,_|\__,_|\n""")


# Check for internet
mystring = 'Checking internet connection.'
print(mystring)

internet = "http://www.kite.com"
timeout = 5

try:
	request = requests.get(internet, timeout=timeout)
	print("Connected to the Internet\n")
except:
    print("No internet connection.")
    exit_input = input('\nEnter Any Key to Exit : ')
    raise ConnectionError('Please connect to the internet, then try again.')




try: # Try to convert the input to an integer
    num = int(input('Enter amount of codes to generate [More Codes may Impact Performance] : '))
except:
    print('Please enter an integer as an input.')
    exit_input = input('\nEnter Any key to Exit : ')
    raise ValueError('Please enter an integer as an input.')

    
print('\nGenerating {} Nitro codes, Please wait.'.format(num))


# Start a timer so we can show how long it took to gen codes.    
start_time = time.time()


for x in range(num):
    
    
    code = ''.join(var(characters) for i in range(16))
    full_url = 'https://discord.gift/{}'.format(code)
    
    

    url = 'https://discordapp.com/api/v9/entitlements/gift-codes/{}?with_application=false&with_subscription_plan=true'.format(code)
    requested = requests.get(url)


    amount_gen += 1


    checker()



print(f'''\n-- {num} codes generated. Took {time.time() - start_time} second(s). Check codes.txt for any valid codes.''')

exit_input = input('\n\nEnter Any Key to Exit : ')



