#! /usr/bin/env python3

from database import dbhandler

def compilate_with_error_support(command):
    print(command)

    #fel uppkom, kolla i db efter matchande fel och returnera nod och snyggt felmdellande
    if(error_message != ""):
        #snygga till felmeddelande
        error_message_pretty = Filter.parse(error_message)
        print("FELMEDDELANDE")
        print(error_message_pretty)

        #fetch all matching error_message from db
        possible_nodes = dbhandler.find(error_message)

        print("Following node(s) may be needed:")
        for node in possible_nodes:
            print(node)


