# finding a key in a box full of boxes


# approach 1
# make a pile of boxes -> while pile is not empty -> grab a box
# if find a box, add to pile of boxes, go back to pile OR
# if find key, done

def look_for_key(main_box):
    pile = main_box.make_a_pile_to_look_through()
    while(pile is not empty):
        box = pile.grab_a_box()
        for(item in box):
            if item.is_a_box():
                pile.append(item)
            elif item.is_a_key():
                print "found the key!"


# approach 2 (recursion)
# go through every item in box
# if find a box, repeat
# if find key, done

def look_for_key_2(main_box):
    for item in box:
        if item.is_a_box:
            # RECURSION!
            look_for_key(item)
        elif item.is_a_key:
            print "found the key!"


# BASE CASE AND RECURSIVE CASE
def countdown(i):
    print i
    # BASE CASE
    if i <= 1:
        return
    # RECURSIVE CASE
    else:
        countdown(i-1)

# THE CALL STACK
def greet(name):
    print "hello, " + name + "!"
    greet2(name)
    print "getting ready to say bye..."
    bye()

def greet2(name):
    print "how are you, " + name + "?"

def bye():
    print "okay bye!"

# THE FLOW
# STACK : greet(name)
# STACK: greet2(name)-> greet(name)
# STACK: greet(name)
# STACK: bye() -> greet(name)
# STACK: greet(name)
# STACK: empty


# factorial recursion function
def fact(x):
    if x == 1:
        return 1
    else
        return x + fact(x-1)

# THE FLOW:
# STACK: fact(3)
# STACK: fact(2) -> fact(3)
# STACK: fact(1) -> fact(2) -> fact(3)
# STACK: fact(2) returns 2 + 1 -> fact(3)
# STACK: fact(3) returns 3 + 3
# STACK: empty 