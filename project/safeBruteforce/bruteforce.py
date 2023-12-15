import safe

def bruteForcing():
        global wallet # the keyword 'gloabl' allows using a global variable in a local enviroment
        safe.safe_owners_list() # get safe owners list
        safe.connect_to_safe() # send a pin code to the safe.(p1 = pin number p2 = safe number)
        
# wallet = 0
# wallet += safe.connect_to_safe("8685",1)
# print(wallet)

# bruteForcing()

# print(safe.safe_owners_list())