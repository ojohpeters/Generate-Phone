#!/usr/bin/python
try:
    from alive_progress import alive_bar
    import argparse
    import json
    import re
    import requests
    import time
    from numgen import numgen

    st = time.time()

    banner = r'''
   ___  _     _ _____  __  __   ____ ____  __________ ____
 / _ \| |__ / |___  | \ \/ /  / ___|  _ \|___ /___ /|  _ \
| | | | '_ \| |  / /   \  /  | |  _| |_) | |_ \ |_ \| |_) |
| |_| | |_) | | / /    /  \  | |_| |  _ < ___) |__) |  __/
 \___/|_.__/|_|/_/    /_/\_\  \____|_| \_\____/____/|_| 
  
    '''
    doc = '''
    [1]. provide a path to the numbers you want to validate.
        \nexample: python app.py /home/smok3scr33n/Documents/numbers.txt
    \n[2]. if you want to use our built in Numbers generator, do not provide any path just run the script
    \n[3]. If the default api credit is exuasted, you will have to visit https://abstractapi.com and signup for an api key \nAfter getting it, replace it with the default key in config.json \nFeel free to contact me for help
    Enjoy!  

    '''
    print(banner)
    parser = argparse.ArgumentParser("app.py",description=doc)
    p = parser.add_argument("file", nargs='?', help="Path to phone number list file.", default=None, type=str)  
    args = parser.parse_args()
    if args.file is not None:
        ini = args.file
        if "/" in args.file:
            ini2 = re.split("/", args.file)
            infile = ini2[-1]
        else: 
            infile = ini
            
    else:
        print('File argument is missing! Using Our inbuilt number generator instead.')
        file = numgen()
        if "/" in file:
            
            ini2 = re.split("/", args.file)
            infile = ini2[-1]
        else: 
            ini = file
            infile = ini        

    if infile == '':
        print('Select a file and not directory!')
        exit()

    c = json.load(open("config.json"))
    API_KEY = c["api_key"]
    nc = c["422"]["d"]

    '''
    Reserved for version 2 lol

    ok = c["200"]["d"]
    ek = c["401"]["d"]
    se = c["500"]["d"]
    se2 = c["503"]["d"]
    '''

    op = open(ini,"r")
    number = op.readlines()
    lines = len([0 for _ in number])
    print(f'{lines} number(s) loaded!')
    time.sleep(2)

    outfile = "Full Numbers.txt"
    outfile2 = "genNumbers.txt"
    o,o2 = open(outfile, "w"),open(outfile2, "w")
    o.write("Phone Number,Status,Country,Location,Carrier\n")
    # o2.write("")

    def checker(API_KEY, number, lines):
        try:
            
            for numb in number:
                stripped = numb.strip('\n')
                response = requests.get(f"https://phonevalidation.abstractapi.com/v1/?api_key={API_KEY}&phone={stripped}")
                if response.status_code == 422:
                    print(nc)
                    exit()
                rep = response.json()
                time.sleep(1)
                if rep['valid'] == True:
                    cstripped = stripped
                    o2.write(cstripped+"\n")
                    print(f"REsponse is {rep['valid']} added {cstripped} to genNumbers.txt")
                o.write(f"{stripped}, {rep['valid']}, {rep['country']['name']}, {rep['location']}, {rep['carrier']}\n")
                yield
        except requests.exceptions.ConnectionError:
            print("Check your internet connection...")
        except Exception as e:
            print(f"Encountered an error Hint:{e}")            

    with alive_bar() as bar:
        for i in checker(API_KEY, number, lines):
            bar()
        
    et  = time.time()
    tt = round(et - st, 2)
    op2 = open("genNumbers.txt",'r')
    tnums = op2.readlines()
    lines2 = len([0 for _ in number])-1
    print(f'Successfully loaded {lines} number(s) and {lines2} were valid\nScript completed this in {tt}secs')
except Exception as e:
    print(f'We encountered an error please contact an me to resolve...\nomoh oti sun mi\nah!!!!\nHint: {e}')    
