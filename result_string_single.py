import numpy as np
from customtkinter import CTkImage
from PIL import Image

test = [6, 5, 1, 4, 5, 5, 2]
hit_test = [6, 5, 1, 5, 4, 3, 4, 6]
wound_test = [6, 5, 6, 3, 3, 6]
whole =[test, hit_test, wound_test]
# This class builds a string of the rolled dice just for showing the dice result on the
# top of window

initial_throw_list = []
initial_throw_img = []
score_list = []

text_dice_result = []
img_dice_result = []
wound_throw = []
wound_throw_img = []
wound_succes = []
wound_succes_img = []
whole_arr = []


class ResultStringSingle:
    def reset(self):
        pass
    def __init__ (self, arr):
        self.text_dice_result = text_dice_result
        self.img_dice_result = img_dice_result
        self.whole_arr = whole_arr

        text_dice_result.clear ()
        img_dice_result.clear ()

        d1_img_path = './app_images/blue_di/1.png'
        d2_img_path = './app_images/blue_di/2.png'
        d3_img_path = './app_images/blue_di/3.png'
        d4_img_path = './app_images/blue_di/4.png'
        d5_img_path = './app_images/blue_di/5.png'
        d6_img_path = './app_images/blue_di/6.png'

        dice_tex_img_str = ['\u2680', '\u2681', "\u2682", "\u2683", "\u2684", "\u2685"]
        #  dice_img_str = [blue_d_one, blue_d_two, blue_d_three, blue_d_four, blue_d_five, blue_d_six]
        d_img_path = [d1_img_path, d2_img_path, d3_img_path, d4_img_path, d5_img_path, d6_img_path]
        image_dice_str = []
        a =int (arr.__len__())
        print("a = " +str(a))

        for hit_die in range (a):

            if (arr[hit_die]) == 6:
                self.text_dice_result.append (dice_tex_img_str[5])
                self.img_dice_result.append (d_img_path[5])
            elif (arr[hit_die]) == 5:
                self.text_dice_result.append (dice_tex_img_str[4])
                self.img_dice_result.append (d_img_path[4])
            elif (arr[hit_die]) == 4:
                self.text_dice_result.append (dice_tex_img_str[3])
                self.img_dice_result.append (d_img_path[3])
            elif (arr[hit_die]) == 3:
                self.text_dice_result.append (dice_tex_img_str[2])
                self.img_dice_result.append (d_img_path[2])
            elif (arr[hit_die]) == 2:
                self.text_dice_result.append (dice_tex_img_str[1])
                self.img_dice_result.append (d_img_path[1])
            else:
                self.text_dice_result.append (dice_tex_img_str[0])
                self.img_dice_result.append (d_img_path[0])
      #      print ("hit_list = " + str(hit_die))

        self.whole_arr.append(self.text_dice_result)
#ResultStringSingle (test)




