import random

hit_roll = []
wounded = []
roll_to_wound = []
first_roll = []
hit_highlight = []
wound_highlight = []


class RollDice:
    # first_roll = []
    # def reset(self):
    def __init__ (self, dice_num, hit, wnd):
        n = int (dice_num)
        # print (n)
        to_hit = hit
        to_wound = wnd

        self.first_roll = first_roll
        self.hit_roll = hit_roll
        self.hit_highlight = hit_highlight
        self.wound_highlight = wound_highlight
        self.wounded = wounded
        self.roll_to_wound = roll_to_wound
        hit_roll.clear ()
        wounded.clear ()
        first_roll.clear ()
        roll_to_wound.clear ()
        hit_highlight.clear ()
        wound_highlight.clear ()

        arr = [random.randint (1, 6) for _ in range (n)]
        # print (arr)

        hit_count = 0
        wound_count = 0
        for i in arr:
            #   print("i"+ str(i))
            first_roll.append (i)
            #    print("first roll inside def = " + str(first_roll))

            if i >= to_hit:
                hit_count = hit_count + 1
                self.hit_roll.append (i)
                self.hit_highlight.append (str ("green2"))
            else:
                self.hit_highlight.append ("red")
        #        print("from hit count " + str(hit_count))
        #        print("from hit_roll " + str(hit_roll))
        #
        wound_arr = [random.randint (1, 6) for _ in range (hit_count)]

        for x in wound_arr:
            roll_to_wound.append (x)
            if x >= to_wound:
                wound_count = wound_count + 1
                self.wounded.append (x)
                self.wound_highlight.append (str ("red"))
            else:
                self.wound_highlight.append (str ("green2"))

            # print ("to_hit = " + str (to_hit))
            # print ("to_wound = " + str (to_wound))

#
# print ("first roll = " + str (first_roll))
# print ("hits from first roll= " + str (hit_roll))
#
# print (" hit_highlight wound roll" + str (hit_highlight))
#
# print ("wounded= " + str (wounded))
