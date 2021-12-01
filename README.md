<img src="https://github.com/whoamisec75/subx/blob/main/static/IMG_20211201_184428.jpg"/>

<p align="center"><b><i>Fast subdomain scanner, Takes arguments from a Json file ("args.json") and outputs the subdomains.</b></i></p>

## File Structure

* core/
  * colors.py
* db/
  * wordlist.txt
* README.md
* LICENCE
* subx.py
* args.json

## Installation

```
▶ git clone https://github.com/whoamisec75/subx.git
▶ cd subx
▶ python3 subx.py
```

## Usage 

First add  `domain`, `concurrency`, `wordlist` in `args.json`: 

```json
{
    "domain": "google.com", 
    "concurrency": 40, 
    "wordlist": "db/wordlist.txt" 
}
```
Now run the tool:

```
▶ python3 subx.py
               __         
   _______  __/ /_  _  __
  / ___/ / / / __ \| |/_/
 (__  ) /_/ / /_/ />  <  
/____/\__,_/_.___/_/|_|  @whamisec
                         

[INF] :: Domain       : google.com
[INF] :: Concurrency  : 40
[INF] :: Wordlist     : db/wordlist.txt

[RES] http://www.google.com
[RES] http://images.google.com
[RES] http://video.google.com
[RES] http://image.google.com
[RES] https://services.google.com
[RES] https://search.google.com
[RES] https://music.google.com
[RES] https://home.google.com
[RES] https://ads.google.com
[RES] https://blog.google.com
[RES] https://chat.google.com
...
```

Similarly if you want to find subdomains of another domain then just edit the `args.json`:

Finding subdomains of `microsoft.com`

```json
{
    "domain": "microsoft.com", 
    "concurrency": 40, 
    "wordlist": "db/wordlist.txt" 
}
```

run the tool:

```
               __        
   _______  __/ /_  _  __
  / ___/ / / / __ \| |/_/
 (__  ) /_/ / /_/ />  <  
/____/\__,_/_.___/_/|_|  @whamisec
                         

[INF] :: Domain       : microsoft.com
[INF] :: Concurrency  : 40
[INF] :: Wordlist     : db/wordlist.txt

[RES] https://admin.microsoft.com
[RES] https://www.microsoft.com
[RES] https://support.microsoft.com
[RES] https://img.microsoft.com
[RES] https://download.microsoft.com
[RES] https://ads.microsoft.com
[RES] https://test.microsoft.com
[RES] https://shop.microsoft.com
[RES] https://dev.microsoft.com
[RES] https://music.microsoft.com
[RES] https://lists.microsoft.com
[RES] https://business.microsoft.com
[RES] https://s.microsoft.com
[RES] https://i.microsoft.com
[RES] https://apps.microsoft.com
[RES] https://dns.microsoft.com
[RES] https://connect.microsoft.com
...
```
