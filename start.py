#!/usr/bin/python
from network_stat import *

if __name__ == '__main__':
    config = {}
    f = open('config.txt', 'r')
    temp = f.readlines()
    for line in temp:
        key, value = [x.strip() for x in line.split(',')]
        config[key] = value

    if internetOn():
        data = collectData()
        data["key"] = config["key"]
        data["name"] = raw_input("Enter your Name: ")
        data["roll_no"] = raw_input("Enter your Roll No: ")
        data["room_no"] = raw_input("Enter your Room No: ")
        print data
        if uploadData(data, config["google_form_url"], location="google_form"):
           print "Data uploaded succesfully"
    else:
        print "Please turn on Internet and try running this script again."
