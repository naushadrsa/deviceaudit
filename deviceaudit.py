#!/usr/bin/python

import requests
import sys
import getpass
import socket
import argparse

"""
HTTP GET of the logStats from Log Decoder REST interface
"""
def httpGet(user, passwd, host, port, filename):

    # Open CSV for writing
    fpw = open("deviceaudit.csv", "w")
    fpw.write("DEVICE,LOGGING,LAST SEEN\n")

    # get all data from logStats
    url = "http://%s:%s/decoder?msg=logStats&force-content-type=text/plain" % (host, port)
    r = requests.get(url, auth=(user, passwd))
    with open(filename, "r") as devices:
        for device in devices:
            for line in r.content.splitlines():
                # if line has IP or name of host, then split the contents
                if device.strip() in line:
                    tokens = line.split(" ")
                    output = "%s,%s,%s\n" % (device.strip(), "YES", tokens[11].split('"')[1])
                    fpw.write(output)
                    found = True
                    break
                else:
                    found = False

            if found is False:
                output = "%s,%s,\n" % (device.strip(), "NO")
                fpw.write(output)
                
    # Close CSV audit output file
    fpw.close();

"""
"main" logic
"""
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", action="store", required=True, type=str, metavar="#", help="filename")
args = parser.parse_args()

user = raw_input("Username: ")
passwd = getpass.getpass("Password for " + user + ": ")
host = raw_input("Host (Log Decoder): ")
port = "50102"

httpGet(user, passwd, host, port, args.file)
