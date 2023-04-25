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


