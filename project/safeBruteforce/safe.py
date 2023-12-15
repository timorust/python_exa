import time

#####################################################
#                                                   #
#                                        ___        #
#      /\  _  _ |__  |_  _ | _ _  _| _ _  | _ |     #
#     /--\|||(_)|_/_ | )(_)|(-| )(_|(-|   |(_||     #
#     v1.0                              (c)2023     #
#####################################################


safeDB = {1: ['Lex Luthor', '$75 billion', '8685'], 
          2: ['Pablo Escobar', '$64 billion', '9180'], 
          3: ['Kingpin', '$20 billion', '8897'], 
          4: ['Al Capone', '$18.6 billion', '0171'], 
          5: ['Gordon Gekko', '$16.5 billion', '9092'], 
          6: ['Joaquin “El Chapo” Guzmán', '$14 billion', '8029'],
          7: ['Norman Osborn', '$10 billion', '7066'],
          8: ['Montgomery Burns', '$8 billion', '0969'],
          9: ['Ozymandias', '$7 billion', '5656'], 
          10: ['Meyer Lansky', '$6.8 billion', '7026'],
          11: ['Auric Goldfinger', '$6.5 billion', '3634'],
          12: ['Terry Benedict', '$3.3 billion', '7815'],
          13: ['Tywin Lannister', '$1.8 billion', '8514'], 
          14: ['Tony Montana', '$900 million', '6374'], 
          15: ['Hans Gruber', '$640 million', '5987'],
          16: ['Commodus', '$600 million', '7404'],
          17: ['George Jung', '$593 million', '6849'],
          18: ['Magneto', '$500 million', '7655'],
          19: ['Tony Soprano', '$76 million', '2356'],
          20: ['Calvin Candie', '$71 million', '4493']}

def safe_owners_list(): 
    print("$$$$$$ Safe Owners - Top Secret List $$$$$$\n")
    for i in safeDB.items():
        print(f"{i[1][0]}, in safe number {i[0]}") # i[1][0]: first slice to pull the list in index 1, second slice to pull the name (in index 0) from the list
    print("$$$$$$ Top Secret $$$$$$\n")
        
def connect_to_safe(user_pin_code, safe_number):
    sn = int(safe_number)
    s_owner, s_content, s_pincode = list(safeDB.items())[sn-1][1]
    time.sleep(0.001)  # slow down time for display 
    if user_pin_code == s_pincode:
        screen(s_owner, s_content)
        return convertor(s_content) #withdraw money to your wallet
    else:
        return False

def convertor(dollars_in_letters): 
    if "million" in dollars_in_letters:
        return int(float(dollars_in_letters.lstrip("$").rstrip(" bmilon"))*(10**6))
    elif "billion" in dollars_in_letters:
        return int(float(dollars_in_letters.lstrip("$").rstrip(" bmilon"))*(10**9))
    
def screen(s_owner, s_content):
    print(f"""
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $                                                              $
        $            welcome back Mr. {s_owner}                        $
        $        there is Total of {s_content} in your safe            $
        $                                                              $
        $            _ _ _       _         _                 _         $
        $           (_) | |     (_)       | |               | |        $
        $     __   ___| | | __ _ _ _ __   | |__   __ _ _ __ | | __     $
        $     \ \ / / | | |/ _` | | '_ \  | '_ \ / _` | '_ \| |/ /     $
        $      \ V /| | | | (_| | | | | | | |_) | (_| | | | |   <      $
        $       \_/ |_|_|_|\__,_|_|_| |_| |_.__/ \__,_|_| |_|_|\_\     $
        $                                                              $
        $                                                              $
        $                                                              $
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
    """)
    
    
# print(convertor('$75 billion')) 
# safe_owners_list()
# choose_safe()
# connect_to_safe("0000", 1)
 