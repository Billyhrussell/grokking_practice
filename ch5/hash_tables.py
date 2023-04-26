# hash tables (implementation. collisions. hash-functions)

#hash map to tell if someone has voted already or not

voted = {}

def check_voter(name):
    if voted.get(name):
        print("kick them out")
    else:
        voted[name] = True
        print("let them vote rn")

