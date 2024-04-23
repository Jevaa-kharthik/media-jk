#! /Library/Frameworks/Python.framework/Versions/3.11/bin/python3
import sys
from lib.Argument import Argument
import os
import json

def print_help():
    print("Usage: "+sys.argv[0]+" [track --type=<query>] --file=<filename> ")
    exit(-1)

a = Argument(sys.argv)

if a.hasOptions(['-h', '--help']):
    print_help()

if(a.hasOptionValue('--file')):
    data = json.loads(os.popen('mediainfo --Output=JSON '+a.getOptionValue('--file')).read())
    if(a.hasCommand('track') and a.hasOptionValue('--type')):
        print("Checking tracks...")
        err = 0
        for track in data["media"]["track"]:
            if(track['@type'] == a.getOptionValue('--type')):
                d = json.dumps(track, indent=4)
                if(a.hasOptions(['--list-keys', '-l'])):
                    print(track.keys())
                    err=0
                    break
                if(a.hasOptionValue('--key')):
                    print(track[a.getOptionValue('--key')])
                else:
                    print(d)
                err=0
                break   
            else:
                err=1
        if(err):
            print("Unable to fetch track")
    else:
        json.dumps(data, indent=4)
        
else:
    print_help()
