import re
import json
import requests
from core.colors import bad, good, info
from concurrent.futures import ThreadPoolExecutor 

print('''
               __        
   _______  __/ /_  _  __
  / ___/ / / / __ \| |/_/
 (__  ) /_/ / /_/ />  <  
/____/\__,_/_.___/_/|_|  @whamisec
                         ''')
with open('args.json') as arguments:
    args = json.load(arguments)

domain = args['domain']
concurrency = args['concurrency']
wordlist = args['wordlist']

with open(wordlist) as Wordlist:
    read = Wordlist.read().splitlines()

if domain == "":
    print(bad + 'No domain in args.json!')
else:
    pass

if wordlist == "":
    print(bad + 'No wordlist in args.json!')

print('\n'+info+ ':: Domain       : ' +domain)
print(info +     ':: Concurrency  : ' +(str(concurrency)))
print(info+      ':: Wordlist     : '+wordlist+'\n')

def subx(domain, subdomain):
    if re.search('http://', domain):
        domain = domain.replace('http://', '')
    elif re.search('https://', domain):
        domain = domain.replace('https://', '')
    else:
        domain = domain

    build_url = (f'{subdomain}.{domain}')
    switch = ('http://')
    req = requests.get(switch+build_url)
    resp = req.status_code
    resp_url = req.url

    if resp == 200:
        if re.search('http://', resp_url):
            print(good+  f'http://{build_url}')
        elif re.search('https://', resp_url):
            print(good+ f'https://{build_url}')    
    else:
        pass

if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        for subdomain in read:
            executor.submit(subx, domain, subdomain)