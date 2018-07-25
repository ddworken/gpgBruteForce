#!/bin/python
from subprocess import check_output as run
try: 
    from progress.bar import Bar
    progressBar = True
except:
    progressBar = False
import argparse

def getWordlist(wordlistFilename):
    with open(wordlistFilename) as f:
        return f.read().splitlines()

def isCorrectPassword(password, filename):
    try:
        output = run("gpg --pinentry-mode loopback --batch --yes --passphrase " + password + " -d " + filename + " 2>&1", shell=True)   #shell injection potential, do not run on untrusted input
        if "decryption failed:" in output:
            return False
        else:
            return True
    except:
        return False

parser = argparse.ArgumentParser(description='GPG Brute Forcer')
parser.add_argument('-f','--filename', help='Location of the GPG encrypted file', required=True)
parser.add_argument('-w','--wordlistFilename', help='Location of the wordlist', required=True)
args = parser.parse_args()

filename = args.filename
wordlist = getWordlist(args.wordlistFilename)

if progressBar: bar = Bar("Brute Forcing...", max=len(wordlist))
for password in wordlist:
    if isCorrectPassword(password, filename):
        if progressBar: bar.finish()
        print "The password is: " + password
        exit()
    if progressBar: bar.next()
if progressBar: bar.finish()
print "Failed to find the password, expand your wordlist and try again"
