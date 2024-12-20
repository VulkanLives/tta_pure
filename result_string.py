from customtkinter import CTkImage
from PIL import Image

test = [6, 5, 1, 4, 5, 5, 2, 6, 3, 3, 6]
hit_test = [6, 5, 1, 5, 4, 3, 4, 6]
wound_test = [6, 5, 6, 3, 3, 6]
landed_wounds = [5,6,8]
# This class builds a string of the rolled dice just for showing the dice result on the
# top of window

initial_throw_list = []
initial_throw_img = []
score_list = []

hit_list = []
hit_img = []
wound_throw = []
wound_throw_img = []
wound_succes = []
wound_succes_img = []





class ResultString:
    # def reset(self):

    def __init__ (self, arr, hit, wnd_throw, wnd_landed):
        self.score_temp = None
        self.score_temp = None
        self.score_temp = None
        self.score_temp = None
        self.score_temp = None
        self.score_temp = None
        self.result_list = initial_throw_list
        self.img_result_list = initial_throw_img
        self.hit_list = hit_list
        self.wound_success = wound_succes
        self.wound_succes_img = wound_succes
        self.wound_throw = wound_throw
        self.wound_throw_img = wound_throw_img
        self.hit_img = hit_img
        initial_throw_list.clear ()
        initial_throw_img.clear ()


        hit_list.clear()
        hit_img.clear()
        wound_succes.clear()
        wound_succes_img.clear()
        wound_throw.clear()
        wound_throw_img.clear()
        

        d1_img_path = '.app_images/blue_di/blue_di/1.png'
        d2_img_path = '.app_images/blue_di/blue_di/2.png'
        d3_img_path = '.app_images/blue_di/blue_di/3.png'
        d4_img_path = '.app_images/blue_di/blue_di/4.png'
        d5_img_path = '.app_images/blue_di/blue_di/5.png'
        d6_img_path = '.app_images/blue_di/blue_di/6.png'

        dice_tex_img_str = ['\u2680', '\u2681', "\u2682", "\u2683", "\u2684", "\u2685"]
      #  dice_img_str = [blue_d_one, blue_d_two, blue_d_three, blue_d_four, blue_d_five, blue_d_six]
        d_img_path = [d1_img_path, d2_img_path, d3_img_path, d4_img_path, d5_img_path, d6_img_path]
        image_dice_str = []
        r = int (wnd_landed.__len__ ())
        x = int (arr.__len__ ())
        y = int (hit.__len__ ())
        z = int (wnd_throw.__len__ ())
        print (str (x))
        print (str (y))
        print (str (z))

        for die in range (x):

            if (arr[die]) == 6:
                self.result_list.append (dice_tex_img_str[5])
                self.img_result_list.append (d_img_path[5])
                self.score_temp[5] += 1

            elif (arr[die]) == 5:
                self.result_list.append (dice_tex_img_str[4])
                self.img_result_list.append (d_img_path[4])
                self.score_temp[4] += 1
            elif (arr[die]) == 4:
                self.result_list.append (dice_tex_img_str[3])
                self.img_result_list.append (d_img_path[3])
                self.score_temp[3] += 1

            elif (arr[die]) == 3:
                self.result_list.append (dice_tex_img_str[2])
                self.img_result_list.append (d_img_path[2])
                self.score_temp[2] += 1

            elif (arr[die]) == 2:
                self.result_list.append (dice_tex_img_str[1])
                self.img_result_list.append (d_img_path[1])
                self.score_temp[1] += 1

            else:
                self.result_list.append (dice_tex_img_str[0])
                self.img_result_list.append (d_img_path[0])
                self.score_temp[0] += 1

        for hit_die in range (y):

            if (hit[hit_die]) == 6:
                self.hit_list.append (dice_tex_img_str[5])
                self.hit_img.append (d_img_path[5])
            elif (hit[hit_die]) == 5:
                self.hit_list.append (dice_tex_img_str[4])
                self.hit_img.append (d_img_path[4])
            elif (hit[hit_die]) == 4:
                self.result_list.append (dice_tex_img_str[3])
                self.hit_list.append (dice_tex_img_str[3])
                self.hit_img.append (d_img_path[3])
            elif (hit[hit_die]) == 3:
                self.hit_list.append (dice_tex_img_str[2])
                self.hit_img.append (d_img_path[2])
            elif (hit[hit_die]) == 2:
                self.hit_list.append (dice_tex_img_str[1])
                self.hit_img.append (d_img_path[1])
            else:
                self.hit_list.append (dice_tex_img_str[0])
                self.hit_img.append (d_img_path[0])

        for wound_di in range (z):

            if (wnd_throw[wound_di]) == 6:
                self.wound_success.append (dice_tex_img_str[5])
                self.wound_throw_img.append (d_img_path[5])
            elif (wnd_throw[wound_di]) == 5:
                self.wound_success.append (dice_tex_img_str[4])
                self.wound_throw_img.append (d_img_path[4])
            elif (wnd_throw[wound_di]) == 4:
                self.result_list.append (dice_tex_img_str[3])
                self.wound_success.append (dice_tex_img_str[3])
                self.wound_throw_img.append (d_img_path[3])
            elif (wnd_throw[wound_di]) == 3:
                self.wound_success.append (dice_tex_img_str[2])
                self.wound_throw_img.append (d_img_path[2])
            elif (wnd_throw[wound_di]) == 2:
                self.wound_success.append (dice_tex_img_str[1])
                self.wound_throw_img.append (d_img_path[1])
            else:
                self.wound_success.append (dice_tex_img_str[0])
                self.wound_throw_img.append (d_img_path[0])


ResultString (test, hit_test, wound_test,landed_wounds)
# #
# print ("initial_throw_list= " + str(initial_throw_list))
# print ("score_list= " + str(score_list))
# print ("initial_throw_img= " + str(initial_throw_img))
# print ("hit_list = " + str(hit_list))
# print ("hit_img= " + str(hit_img))
# print ("wound_list=" + str(wound_list))
# print ("wound_img=" + str(wound_img))
