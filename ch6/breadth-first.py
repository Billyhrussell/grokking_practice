# graphs, breadth-first, queues,

graph = {}

graph["you"] = ["alice", "bob", "claire"]
graph["bob"] = ["anuj", "peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["thom", "johnny"]
graph["anuj"] = []
graph["peggy"] = []
graph["thom"] = []
graph["johnny"] = []

# BFS FIRST EXAMPLE
# deque = double-ended queue function

from collections import deque

search_queue = deque() #creates a new queue
search_queue += graph["you"] #adds all of your neighbors to the search queue

# ALL of my direct neighbors are in the list ["alice, bob, claire"] in "order",
# since alice is checked first and no mangos, add the rest of her neighbors
# list is now ["bob", "claire", "peggy"]
# now checking BOB
# not a mango seller either, add his friends to list
# list is now ["claire", "peggy", "anuj"]
# and so on
while search_queue: #while queue isnt empty
    person = search_queue.popleft() #grabs first person off queue
    if person_is_seller(person): #checks if person is mango seller
        print person + " is a mango seller"
        return True
    else:
        search_queue += graph[person] #not a mango seller. add all of this persons friends to search queue

return false # if reach this far, nobody is a mango seller

# if persons name ends in m, they sell mangos
def person_is_seller(name):
    return name[-1] == "m"

# BFS SECOND EXAMPLE(better), making sure to keep track of where you've been! (or else infinite loop)
def search(name):
    search_queue = deque() #creates a new queue
    search_queue += graph[name] #adds all of your neighbors to the search queue
    searched = []

    while search_queue:
        person = search_queue.popleft() #grabs first person off queue

        if not person in searched:      #only search this person if you haven't already
            if person_is_seller(person): #checks if person is mango seller
                print person + " is a mango seller"
                return True
            else:
                search_queue += graph[person] #not a mango seller. add all of this persons friends to search queue
                searched.append(person)

    return false
