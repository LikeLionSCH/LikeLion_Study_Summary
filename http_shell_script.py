# !usr/bin/python
import sys
import os
import json


def print_method(method):

    if method == 'GET':
        print("          _____   ______   _______")
        print("         / ____| |  ____| |__   __|")
        print("        | |  __  | |__       | |   ")
        print("        | | |_ | |  __|      | |   ")
        print("        | |__| | | |____     | |   ")
        print("         \_____| |______|    |_|   ")

    elif method == 'POST':
        print("     _____     ____     _____   _______")
        print("    |  __ \   / __ \   / ____| |__   __|")
        print("    | |__) | | |  | | | (___      | |   ")
        print("    |  ___/  | |  | |  \___ \     | |   ")
        print("    | |      | |__| |  ____) |    | |   ")
        print("    |_|       \____/  |_____/     |_|   ")


def print_success_request():
    print()
    print("############################################")
    print("########### SUCCESS SEND REQUEST ###########")
    print("############################################")


def print_request_message(url):
    print()
    print("############# REQUEST MESSAGE ##############")
    print(url)
    print("############################################")


print("############################################")
print("############ HTTP SHELL SCRIPT #############")
print("############################################")

METHOD = sys.argv[1]

if METHOD == 'GET':
    print_method(METHOD)

    URL = "http GET http://127.0.0.1:8000/post/"

    print_request_message(URL)
    print_success_request()
    result = os.popen(URL).read()

    print()
    print("############### RESPONSE  ##################")
    print(
        json.dumps(
            json.loads(result),
            indent=4,
            sort_keys=True)
    )
    print("############### RESPONSE  ##################")


else:
    start, end = int(sys.argv[2]), int(sys.argv[3]) + 1

    print_method(METHOD)

    for i in range(start, end):
        PREFIX = "http --form POST http://127.0.0.1:8000/post/ "
        DATA = 'title="Post Test Title{}" body="Post Test Body{}"'
        URL = PREFIX + DATA.format(i, i)

        print_request_message(URL)
        print_success_request()
        result = os.popen(URL).read()

        print()
        print("############### RESPONSE  ##################")
        print(
            json.dumps(
                json.loads(result),
                indent=4,
                sort_keys=True)
        )
        print("############### RESPONSE  ##################")


print()
print("############################################")
print("############### END SCRIPT  ################")
print("############################################")
