#!/usr/bin/python3

# Import modules
from os import system as do
from time import sleep

# Set Variables
upCache = " "
upSys = " "
remAuto = " "

# define how to get config
def getConfig(filename):
    import imp
    f = open(filename)
    global data
    data = imp.load_source('data', '', f)
    f.close()

# path to "config" file
getConfig('/home/carson/.pyUpdate/updaterConfig.txt')

if data.autoCache == 0:
    while not upCache == "y" or not upCache == "n":
        upCache = input("Update cache? (Recommended) y/n")
    if upCache == "y":
        do("clear")
        do("sudo apt-get update")
    if upCache == "n":
        print("Not updating cache")
        sleep(3)

if data.autoCache == 1:
    do("clear")
    do("sudo apt-get update --force-yes")

if data.autoUpdate == 0:
    while not upSys == "y" or not upSys == "n":
        upSys = input("Update system? (Recommended) y/n")
    if upSys == "y":
        do("clear")
        do("sudo apt-get upgrade --force-yes")
    if upSys == "n":
        print("Not updating system")
        sleep(3)

if data.autoUpdate == 1:
    do("clear")
    do("sudo apt-get upgrade --force-yes")

if data.autoRemove == 0:
    while not remAuto == "y" or not remAuto == "n":
        remAuto = input("Remove automatically installed packages? (Recommended) y/n")
    if remAuto == "y":
        do("clear")
        do("sudo apt-get autoremove")
    if remAuto == "n":
        print("Not removing automatically installed packages")
        sleep(3)

if data.autoCache == 1:
    do("clear")
    do("sudo apt-get autoremove --force-yes")
