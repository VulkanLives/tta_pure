import tkinter as tk
from tkinter import *
from tkinter import messagebox

import customtkinter as ctk
import numpy as np
from PIL import Image
from customtkinter import *
from customtkinter import CTkImage

import result_string_single as res_sing
import roll_dice as rd

root = ctk.CTk ()

ctk.set_appearance_mode ("system")
ctk.set_default_color_theme ("dark-blue")
root.title ("TTA: Hits & Wounds Roller")
root.geometry ("750x400+0+0")

roll_count = 0
# grid_display is a var for diplay purposes in roll fucntion
grid_display = 0

# modes
first_activation = True
sim_mode = False
d_three_active = False
test_mode = False
plot_mode = False
single_line_display = False
view_all_mode = False
hnw_mode = True
horozontal_score = True

# list arraay to record the results
record = list
current_session_log = []
session_npy_log = []
sim_log = []
total_dice_rolled = 0
hits_arr = []
wounds_arr = []
string_roll = []
img_string_roll = []
string_hit_roll = []
string_wound_roll = []
string_wound_result = []
wound_roll_arr = []
initial_roll_images = []
# list to immatate intance of complete roll including hits and wounds until i get a to it
fake_instance_log = []

successlbl_border = ""

# fonts
header_font = ctk.CTkFont (
    family='Helvetica',
    size=18, weight='bold'
)
checkbox_font = ctk.CTkFont (
    family='Helvetica',
    size=12, weight='bold'
)
di_font_setup = ctk.CTkFont (
    family='Helvetica',
    size=20, weight='bold'
)
hint_font = ctk.CTkFont (
    family='Helvetica', slant="roman", underline= True,
    size=18, weight='bold'
)
di_font = ctk.CTkFont (
    family='Helvetica',
    size=32, weight='bold'
)

di_font_two = ctk.CTkFont (
    family='Helvetica',
    size=20, weight='bold'
)

roll_option = "normal"

command_frame = ctk.CTkFrame (master= root, fg_color="black", border_color="black", height=350, width=700)
command_frame.pack (side="top", fill="both", expand=True)


# output for dice score
main_roll_frame = ctk.CTkFrame (
    master=command_frame, fg_color="dark olive green", border_color="red",
    border_width=2, height=350, width=350
)
main_roll_frame.pack (side="left", fill="both")

# user_input_frame = ctk.CTkFrame(master=main_roll_frame, fg_color="dark olive green", border_width=5, border_color="black")
user_input_frame = ctk.CTkFrame (
    master=main_roll_frame, fg_color="dark olive green", height=240,
    width=350
)
user_input_frame.pack (side="top", fill="both", ipady=20)
#
# quick_res_frame = ctk.CTkFrame (master=main_roll_frame, width=300)
#
# quick_res_frame.pack (side='left', fill="x")  # frame to show all checkboxes

quick_roll_res_frm = ctk.CTkFrame (master=main_roll_frame, fg_color="red", border_color="yellow", width=300, height=100)
quick_roll_res_frm.pack (side="top", fill="x")

roll_frame_y = ctk.CTkFrame (
    master=main_roll_frame, fg_color="dark olive green", border_color="blue",
    border_width=2, height=100, width=150
)
roll_frame_x = ctk.CTkFrame (
    master=quick_roll_res_frm, fg_color="red", border_color="yellow", border_width=2, height=120, width=345
)
roll_frame_x.pack (side="top", fill="both")

# hnw = hits and wounds, the results that show occurances of eaach di e.g. fours 6s, no 1s and three 5s
hnw_img_frm = ctk.CTkFrame (
    master=roll_frame_x, fg_color="dark olive green", border_color="yellow", border_width=2, width=325
)
hnw_res_frm = ctk.CTkFrame (
    master=roll_frame_x, fg_color="dark olive green", border_color="brown", border_width=2, width=325
)
hnw_img_frm.pack (side='top', fill='both')
hnw_res_frm.pack (side='top', fill='both')
wnd_img_frm = ctk.CTkFrame (
    master=roll_frame_x, fg_color="dark olive green", border_color="yellow", border_width=2, width=325
    )
wnd_res_frm = ctk.CTkFrame (
    master=roll_frame_x, fg_color="dark olive green", border_color="brown", border_width=2, width=325
    )
wnd_img_frm.pack (side='top', fill='both')
wnd_res_frm.pack (side='top', fill='both')


dice_frame = ctk.CTkFrame (
    command_frame, fg_color="dark olive green", border_color="orange", border_width=2,
    # label_text="Roll Log",
    width=350, height=300
)
dice_frame.pack (side='right', fill='both', expand=True)
check_box_frame = ctk.CTkFrame (master=command_frame, fg_color="dark olive green", border_color="black", width=200)
# check_box_frame = ctk.CTkFrame(master=command_frame, fg_color="dark olive green", border_color="black", width=200)
# check_box_frame.pack (side="left", fill="both")

# variable for check box options to determined and then actioned
display_session = IntVar ()
b_chart = IntVar ()
dropdownbox = IntVar ()
test_mode_var = IntVar ()
var5 = IntVar ()
var6 = IntVar ()
sim_var = IntVar ()
d_three_var = BooleanVar ()
chk_frame_var = IntVar ()
hits_wound_var = IntVar ()
score_view = IntVar ()

# USER input boxes

preset_img = CTkImage (Image.open (r"./app_images/black_dice/2.jpg"), size=(45, 45))
wnd_img = CTkImage (Image.open (r"./app_images/black_dice/3.jpg"), size=(45, 45))
hit_img = CTkImage (Image.open (r"./app_images/black_dice/4.jpg"), size=(45, 45))

lbl = ctk.CTkLabel (
    user_input_frame, fg_color="dark olive green", text="Singles", bg_color="dark olive green",
    width=35, height=5, font=hint_font, text_color = "white"
).grid (row=1, column=1, padx=10, pady=10, sticky="N")
lbl = ctk.CTkLabel (
    user_input_frame, fg_color="dark olive green", text="Handfuls", bg_color="dark olive green",
    width=35, height=5, font=hint_font, text_color = "white"
).grid (row=1, column=2, padx=5, pady=10, sticky="N")
custom_entry = ctk.CTkEntry (user_input_frame, width=50, font=di_font_setup)
custom_entry.configure (state="normal", fg_color="white")
custom_entry.grid (row=2, column=1, padx=10, sticky="N")

presets = ["-", "1", "5", "10", "15", "20"]
preset_option_box = ctk.CTkComboBox (
    user_input_frame, values=presets, state="readonly", width=80,
    font=di_font_setup
)
preset_option_box.grid (row=2, column=2, sticky="N")
preset_option_box.set ("10")

lbl = ctk.CTkLabel (
    user_input_frame, fg_color="dark olive green", text="To Hit", bg_color="dark olive green",
    width=35, height=5, font=hint_font, text_color = "white"
).grid (row=4, column=1, padx=5, pady=5, sticky="N")
lbl = ctk.CTkLabel (
    user_input_frame, fg_color="dark olive green", text="To Wound", bg_color="dark olive green",
    width=35, height=5, font=hint_font, text_color = "white"
).grid (row=4, column=2, pady=5, sticky="N")

hit_presets = ["-", "2+", "3+", "4+", "5+", "6"]

hit_option_box = ctk.CTkComboBox (
    user_input_frame, values=hit_presets, state="readonly", border_color='grey', border_width=1, width=50,
    font=di_font_setup
)
hit_option_box.grid (row=5, column=1, padx=5, pady=5)
hit_option_box.set ("3+")

wound_presets = ["-", "2+", "3+", "4+", "5+", "6"]
wound_option_box = ctk.CTkComboBox (
    user_input_frame, values=wound_presets, state="readonly", width=80,
    font=di_font_setup
)
wound_option_box.grid (row=5, column=2, pady=5)
wound_option_box.set ("3+")

test_img: ctk.CTkImage = CTkImage (Image.open (r"./app_images/blue_di/1.png"), size=(35, 35))

# hit_wound_frame = ctk.CTkFrame (
#     master=main_roll_frame, fg_color="dark olive green", border_color="red", border_width=2, height=300, width=300
#     )
# hit_wound_frame.pack (side="left")

# user_input_frame.pack(side="left", fill="both")

# roll_frame_x.pack(side="left",fill="both")
# hit_wound_topframe = ctk.CTkFrame (
#    master=command_frame, fg_color="dark olive green", border_color="orange",
#    border_width=2, width=200
#    )
# hit_wound_topframe.pack (side="right", fill="both")




# hit_wound_frame.pack(side="left", fill="both", padx=10)
# hit_wound_frame.forget()

# check_box_frame.forget()

def load_screen (rec, hit_num, wnd_num, wnds_made, wnd_whole):
    global header_font, di_font_setup, di_font
    disp_rolls = np.array (rec)
    disp_wounds = np.array (wnds_made)
    hits = str (hit_num)
    wounds = str (wnd_num)

    print ("first activation = " + str (first_activation))

    d_one_img = CTkImage (Image.open (r"./app_images/black_dice/1.jpg"), size=(35, 35))
    d_two_img = CTkImage (Image.open (r"./app_images/black_dice/2.jpg"), size=(35, 35))
    d_three_img = CTkImage (Image.open (r"./app_images/black_dice/3.jpg"), size=(35, 35))
    d_four_img = CTkImage (Image.open (r"./app_images/black_dice/4.jpg"), size=(35, 35))
    d_five_img = CTkImage (Image.open (r"./app_images/black_dice/5.jpg"), size=(35, 35))
    d_six_img = CTkImage (Image.open (r"./app_images/black_dice/6.jpg"), size=(35, 35))
    hits_icon = CTkImage (Image.open (r"./app_images/icons/crosshair1.png"), size=(35, 35))
    wounds_icon = CTkImage (Image.open (r"./app_images/icons/knife.png"), size=(35, 35))
    # blue_d_one = CTkImage (Image.open ('./blue_di/1.png'), size=(35, 35))
    #    # lbl = ctk.CTkLabel(res_frame, image=img).pack()

    # array for horizontal_wound_view should do the same and horizontal_view()
    # with less code
    d_img_arr = [d_one_img, d_two_img, d_three_img, d_four_img, d_five_img, d_six_img]

    ones = str (np.count_nonzero (disp_rolls == 1))
    twos = str (np.count_nonzero (disp_rolls == 2))
    threes = str (np.count_nonzero (disp_rolls == 3))
    fours = str (np.count_nonzero (disp_rolls == 4))
    fives = str (np.count_nonzero (disp_rolls == 5))
    sixes = str (np.count_nonzero (disp_rolls == 6))

    w_ones = str (np.count_nonzero (disp_wounds == 1))
    w_twos = str (np.count_nonzero (disp_wounds == 2))
    w_threes = str (np.count_nonzero (disp_wounds == 3))
    w_fours = str (np.count_nonzero (disp_wounds == 4))
    w_fives = str (np.count_nonzero (disp_wounds == 5))
    w_sixes = str (np.count_nonzero (disp_wounds == 6))

    woundres_arr = [w_ones, w_twos, w_threes, w_fours, w_fives, w_sixes]

    di_font = ctk.CTkFont (
        family='Helvetica',
        size=34, weight='bold'
    )


    ctk.CTkLabel (
        master=hnw_img_frm, fg_color="dark olive green", text="", image=d_one_img, bg_color="dark olive green",
        width=25
    ).grid (row=1, column=1, sticky="W", pady=2, padx=2)
    ctk.CTkLabel (master=hnw_res_frm, text=ones, bg_color="white", font=di_font_setup, width=35, height=35).grid (
        row=2,
        column=1,
        sticky="W",
        pady=2, padx=2
    )

    ctk.CTkLabel (
        master=hnw_img_frm, fg_color="dark olive green", text="", image=d_two_img, bg_color="dark olive green",
        width=35, height=35
    ).grid (row=1, column=2, pady=2, padx=2)
    ctk.CTkLabel (master=hnw_res_frm, text=twos, bg_color="white", font=di_font_setup, width=35, height=35).grid (
        row=2,
        column=2,
        pady=2, padx=2,
        sticky="W"
    )

    ctk.CTkLabel (
        master=hnw_img_frm, fg_color="dark olive green", text="", image=d_three_img,
        bg_color="dark olive green", width=35, height=35
    ).grid (row=1, column=3, pady=2, padx=2)
    ctk.CTkLabel (master=hnw_res_frm, text=threes, bg_color="white", font=di_font_setup, width=35, height=35).grid (
        row=2,
        column=3,
        pady=2, padx=2,
        sticky="W"
    )

    ctk.CTkLabel (
        master=hnw_img_frm, fg_color="dark olive green", text="", image=d_four_img, bg_color="dark olive green",
        width=35, height=35
    ).grid (row=1, column=4, pady=2, padx=2, sticky="W")
    ctk.CTkLabel (master=hnw_res_frm, text=fours, bg_color="white", font=di_font_setup, width=35, height=35).grid (
        row=2,
        column=4,
        sticky="W",
        pady=2, padx=2
    )

    ctk.CTkLabel (
        master=hnw_img_frm, fg_color="dark olive green", text="", image=d_five_img, bg_color="dark olive green",
        width=35, height=35
    ).grid (row=1, column=5, pady=2, padx=2, )
    ctk.CTkLabel (master=hnw_res_frm, text=fives, bg_color="white", font=di_font_setup, width=35, height=35).grid (
        row=2,
        column=5,
        sticky="W",
        pady=2, padx=2
    )

    ctk.CTkLabel (
        master=hnw_img_frm, fg_color="dark olive green", text="", image=d_six_img, bg_color="dark olive green",
        width=35
    ).grid (row=1, column=6, pady=2, padx=2, )
    ctk.CTkLabel (master=hnw_res_frm, text=sixes, bg_color="white", font=di_font_setup, width=35, height=35).grid (
        row=2,
        column=6,
        pady=2, padx=2, sticky="W"
    )
    ctk.CTkLabel (
        master=hnw_img_frm, fg_color="dark olive green", text="", image=hits_icon, bg_color="dark olive green",
        width=35
    ).grid (row=1, column=7, pady=2, padx=20, )
    ctk.CTkLabel (master=hnw_res_frm, text=hits, bg_color="white", font=di_font_setup, width=35, height=35).grid (
        row=2,
        column=7,
        pady=2, padx=20
    )


#output_frame = ctk.CTkFrame (
#    master=root, fg_color="dark olive green", border_color="black", border_width=2, height=350,
#    width=700
#)
#output_frame.pack (side="bottom", fill="both", expand=True)
#    # ctk.CTkLabel (
    #     master=user_input_frame, fg_color="dark olive green", text="", image=hits_icon, bg_color="dark olive green",
    #     width=35
    # ).grid(row=9, column=1, columnspan=1, pady=10)
    # ctk.CTkLabel (master=user_input_frame, text=hits, bg_color="white", font=di_font_setup, width=35, height=35).grid(
    #     row=10, column=1, columnspan=1, pady=10)
    # ctk.CTkLabel (
    #     master=user_input_frame, fg_color="dark olive green", text="", image=wounds_icon, bg_color="dark olive green",
    #     width=35
    # ).grid (row=9, column=3, pady=2, padx=1)
    # ctk.CTkLabel (master=user_input_frame, text=wnd_num, bg_color="white", font=di_font_setup, width=35, height=35).grid (
    #     row=10,
    #     column=3,
    #     pady=2, padx=1, sticky='W'
    # )

    def horizontal_wound_view ():
        for i in range (6):
            ctk.CTkLabel (
                master=wnd_img_frm, fg_color="dark olive green", text="", image=d_img_arr[i],
                bg_color="dark olive green",
                width=25
            ).grid (row=1, column=int (i + 1), sticky="W", pady=2, padx=2)
            ctk.CTkLabel (
                master=wnd_res_frm, text=woundres_arr[i], bg_color="white", font=di_font_setup, width=35, height=35
            ).grid (
                row=2,
                column=int (i + 1),
                sticky="W",
                pady=2, padx=2
            )
            wnd_string_index = +1
        ctk.CTkLabel (
            master=wnd_img_frm, fg_color="dark olive green", text="", image=wounds_icon, bg_color="dark olive green",
            width=35
        ).grid (row=1, column=8, pady=2, padx=20)
        ctk.CTkLabel (
            master=wnd_res_frm, text=wnd_num, bg_color="white", font=di_font_setup, width=35, height=35
            ).grid (
            row=2,
            column=8,
            pady=2, padx=20, sticky='W'
        )

    horizontal_wound_view ()


def show_history ():
    global roll_count, current_session_log, session_npy_log, current_session_log
    # check atleast one roll has happened
    font_setup = ctk.CTkFont (
        family='Helvetica',
        size=20, weight='bold'
    )
    rolled = current_session_log.__len__ ()
    valid_check = roll_count
    if valid_check > 0:
        roll_history_win = ctk.CTkToplevel (root, fg_color="white")
        roll_history_win.title ("Session Results")
        roll_history_win.geometry ("400x200+800+100")
        roll_history_win.resizable (True, True)  # Width, He

        hist_frame = ctk.CTkFrame (
            master=roll_history_win, fg_color="dark olive green", width=400, height=200,
            border_color="black"
        )
        print (grid_display)
        # header_font = ctk.CTkFont(family='Helvetica',
        #                          size=20, weight='normal')

        literal_font_setup = ctk.CTkFont (
            family='Helvetica',
            size=20, weight='bold'
        )
        literal_roll_log = ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green",
            text=str ("Roll") + str (roll_count) + str (string_roll[roll_count - 1]),
            font=literal_font_setup
        )
        literal_roll_log.pack ()
        ctk.CTkLabel (
            master=roll_history_win, fg_color="dark olive green", text="Breakdown of Session"
        ).pack ()
        btm_frame = ctk.CTkScrollableFrame (
            master=roll_history_win, fg_color="dark olive green", border_width=2,
            width=200, height=200,
            border_color="black"
        )
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text=str (rolled) + " rolls : ",
            font=font_setup
        ).grid (row=2, column=1, pady=10)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text='\u2680' + str (current_session_log.count (1)),
            font=font_setup
        ).grid (row=2, column=2, pady=10)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text='  ',
            font=font_setup
        ).grid (row=2, column=3, pady=10)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text='\u2681' + str (current_session_log.count (2)),
            font=font_setup
        ).grid (row=2, column=4, pady=10)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text='  ',
            font=font_setup
        ).grid (row=2, column=5, pady=10)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text="\u2682" + str (current_session_log.count (3)),
            font=font_setup
        ).grid (row=2, column=6)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text='  ',
            font=font_setup
        ).grid (row=2, column=7)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text="\u2683" + str (current_session_log.count (4)),
            font=font_setup
        ).grid (row=2, column=8)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text='  ',
            font=font_setup
        ).grid (row=2, column=9)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text="\u2684" + str (current_session_log.count (5)),
            font=font_setup
        ).grid (row=2, column=10)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text='  ',
            font=font_setup
        ).grid (row=2, column=12)
        ctk.CTkLabel (
            master=hist_frame, fg_color="dark olive green", text="\u2685" + str (current_session_log.count (6)),
            font=font_setup
        ).grid (row=2, column=13)
        score_log_scroll = ctk.CTkScrollableFrame(master=hist_frame, orientation="vertical", fg_color="dark olive green",label_text="Score Log", width=300, height=50)
        score_log_scroll.pack (side='left', fill="both")
        
        mini_w_result_frame = ctk.CTkFrame (master=hist_frame, fg_color="dark olive green", border_color="grey", border_width=3, width=300)
        mini_w_result_frame.pack (side='top', fill="both")
    #hist_frame.pack ()
        #ctk.CTkLabel (
#            master=roll_history_win, fg_color="dark olive green", text="Average"
#        ).pack ()
    for result in range (roll_count):
            # display each roll each on new line
            dice_lbl = ctk.CTkLabel (
                btm_frame, fg_color="dark olive green",
                text="roll " + str (result + 1) + ":" + str (session_npy_log[result - 1])
            )
            dice_lbl.pack (side='top')

            btm_frame.pack (side='left')
    else:
        messagebox.showwarning ("Error", "No rolls have been made")  # first text is title of new window


def roll_new ():
    global roll_count, current_session_log, session_npy_log, d_three_var, initial_roll_images \
        , plot_mode, hnw_mode, hits_arr, wounds_arr, wound_roll_arr, first_activation, fake_instance_log
    count = int (roll_count)
    latest_arr = current_session_log
    user = custom_entry.get ()
    preset_user_entry = preset_option_box.get ()
    to_hit = int (hit_option_box.get ()[0])
    to_wound = int (wound_option_box.get ()[0])

    if user == "":
        user = "0"
    else:
        user = int (custom_entry.get ())
    if preset_user_entry == "-":
        preset_user_entry = "0"
    else:
        preset_user_entry = int (preset_option_box.get ())

    n: int = int (preset_user_entry) + int (user)

    rd.RollDice (n, to_hit, to_wound)

    roll = rd.first_roll
    hit_success_bdr = rd.hit_highlight
    wound_success_bdr = rd.wound_highlight
    session_npy_log.append (roll)
    current_session_log = latest_arr + roll
    roll_count = count + 1

    hit = rd.hit_roll
    hits = int (rd.hit_roll.__len__ ())
    whole_wound_roll = rd.roll_to_wound
    wound_success = rd.wounded
    wound_count = int (rd.wounded.__len__ ())

    display_array = [("Roll to Hit: ", roll), ("Hit Roll Success = ", hit), ("Roll to Wound = ", whole_wound_roll),
                     ("Wound Roll Success = ", wound_success)]
    fake_instance_log.append (display_array)
    print (str (display_array.__len__ ()) + "display array = " + str (display_array))
    print (str (fake_instance_log.__len__ ()) + "fake_instance_log array = " + str (fake_instance_log))

    first_activation = False
    load_screen (roll, hits, wound_count, wound_success, whole_wound_roll)
    display_intance (roll, hit, whole_wound_roll, wound_success, hit_success_bdr, wound_success_bdr)

def display_intance (hr, hs, wr, ws, sb, wb):
    h_roll = hr
    h_success = hs
    w_roll = wr
    w_success = ws
    hit_win_highlight = sb
    wnd_win_highlight = wb
    print ("h_roll : " + str (h_roll))
    print ("h_success : " + str (h_success))
    print ("w_roll : " + str (w_roll))
    print ("w_success : " + str (w_success))

    di_img = res_sing.img_dice_result

    print ("b = " + str (di_img))

    def show_hit ():
        res_sing.ResultStringSingle (h_roll)
        dice_thrown = h_roll.__len__ ()
        # wound_thrown = wnd_thrown_imgs.__len__ ()
        for widget in dice_frame.winfo_children ():
            widget.destroy ()

        x = 0
        column_grid_plot = 2
        row_grid_plot = 3

        roll_header = ctk.CTkLabel (master=dice_frame, text="Roll to Hit  ", font=hint_font, anchor="center")
        roll_header.grid (row=2, column=1, columnspan=5, pady= 10,sticky="W")

        # load and show dice images to represent roll

        space_lbl = ctk.CTkLabel (master=dice_frame, text="  ", width=25)
        space_lbl.grid (row=(row_grid_plot), column=1)

        for di in range (dice_thrown):
            lbl_limit = dice_thrown / 10
            print (lbl_limit)
            # display each roll each on new line
            print (di)
            # fp stands for filepath
            fp = str (di_img[di])
            border_highlight = str (hit_win_highlight[di])
            print ("fp images" + str (di_img))
            print ("fp border_highlight" + str (border_highlight))

            print ("fp images" + str (fp))
            print ("x" + str (x))
            x += 1
            fp_img = ctk.CTkImage (Image.open (fp))
            print ("fp ima" + str (fp_img))

            # lbl = ctk.CTkLabel (master=dice_frame, image=fp_img, text="", width=25)
            # # lbl.pack(side='left', anchor= 'ne', ipadx = 0 )
            # lbl.grid (row=row_grid_plot, column=int (column_grid_plot))
            # print ("grid plit images" + str (column_grid_plot))
            # column_grid_plot += 1

            hr_lbl = ctk.CTkLabel (master=dice_frame, image=fp_img, text="", bg_color=border_highlight, width=25)
            #   lbl.pack(side='left', anchor= 'ne', ipadx = 0 )
            hr_lbl.grid (row=int (row_grid_plot), column=int (column_grid_plot),padx=3, pady = 5)
            print ("grid plit images" + str (column_grid_plot))
            #     loop to only print up to x amoutn of dice before stating a new line
            if column_grid_plot in range (11):
                column_grid_plot += 1
                print ("grid plit images" + str (column_grid_plot))
            else:
                column_grid_plot = 2
                row_grid_plot += 1

                print ("grid plit images" + str (row_grid_plot))
                # lbl = ctk.CTkLabel (master=dice_frame, text="  ", width=25)
                # lbl.grid (row=int (row_grid_plot), column=1)

        # put if statement to choose wether or not show show wound as well
        show_wound (row_grid_plot)

    def show_wound (row_num):
        w_row_grid_plot = row_num + 2
        w_column_grid_plot = 2
        w_roll_header = ctk.CTkLabel (master=dice_frame, text="Roll to Wound  ", font=hint_font)
        w_roll_header.grid (row=int(w_row_grid_plot - 1), column=1, columnspan=5, padx=20)
        res_sing.ResultStringSingle (w_roll)
        w_dice_thrown = w_roll.__len__ ()

        # load and show dice images to represent roll

        space_lbl = ctk.CTkLabel (master=dice_frame, text="  ", width=25)
        space_lbl.grid (row=int (w_row_grid_plot), column=1)

        for wnd_di in range (w_dice_thrown):
            lbl_limit = w_dice_thrown / 10
            print (lbl_limit)
            # display each roll each on new line

            # fp stands for filepath
            fp = str (di_img[wnd_di])
            w_border_highlight = str (wnd_win_highlight[wnd_di])
            # x += 1
            fp_img = ctk.CTkImage (Image.open (fp))
            print ("fp ima" + str (fp_img))

            # lbl = ctk.CTkLabel (master=dice_frame, image=fp_img, text="", width=25)
            # # lbl.pack(side='left', anchor= 'ne', ipadx = 0 )
            # lbl.grid (row=row_grid_plot, column=int (column_grid_plot))
            # print ("grid plit images" + str (column_grid_plot))
            # column_grid_plot += 1

            wr_lbl = ctk.CTkLabel (master=dice_frame, image=fp_img, text="", bg_color=w_border_highlight, width=25)
            #   lbl.pack(side='left', anchor= 'ne', ipadx = 0 )
            wr_lbl.grid (row=int (w_row_grid_plot), column=int (w_column_grid_plot), padx=3,pady = 5)
            print ("grid plit images" + str (w_column_grid_plot))
            #     loop to only print up to x amoutn of dice before stating a new line
            if w_column_grid_plot in range (11):
                w_column_grid_plot += 1
                print ("grid plit images" + str (w_column_grid_plot))
            else:
                w_column_grid_plot = 2
                w_row_grid_plot += 1

    show_hit ()


    def show_hits_image ():
        print ("hello from hit image")

    dice_frame.pack (side='right')
    # command_frame.update()

#
# def display_result (roll_arr, hit_num, wound_num, wound_arr, h_arr, initial_roll_images):
#     global current_session_log, roll_count, grid_display, hits_arr, wound_roll_arr
#     global hnw_mode
#     x = roll_arr
#
#     h = hit_num
#     y = h_arr
#     dice_imgs = initial_roll_images
#
#     print ("dice images" + str (dice_imgs))
#     print ("dice images" + str (dice_imgs.__len__ ()))
#
#     #    ima = ctk.CTkImage (Image.open (dice_imgs[1]))
#     # print("dice images" + str(ima))
#     for di in range (dice_imgs.__len__ ()):
#         # display each roll each on new line
#         fp = str (dice_imgs[di - 1])
#         fp_img = ctk.CTkImage (Image.open (str (fp)))
#         lbl_fp = ctk.CTkLabel (master=command_frame, image=fp_img)
#         lbl_fp.pack ()
#
#     def show_hit_wound (h, w):
#         global roll_count
#         hit = h
#         wound = w
#         count = 0
#         first_dice = str (string_roll[roll_count - 1])
#
#         detail_results_lbl = ctk.CTkLabel (
#             master=mini_w_result_frame, fg_color="dark olive green",
#             text="DETAILED RESULTS ", corner_radius=5, underline=7, font=header_font
#         )
#         detail_results_lbl.grid (row=1, column=1)
#         orig_roll_lbl = ctk.CTkLabel (
#             master=mini_w_result_frame, fg_color="dark olive green",
#             text="INITIAL ROLL:  ", font=header_font
#         )
#         orig_roll_lbl.grid (row=3, column=1, sticky='W')
#         # orig_roll_lbl.configure(justify = LEFT)
#         orig_roll_lbl_two = ctk.CTkLabel (
#             master=mini_w_result_frame, fg_color="dark olive green",
#             text=first_dice, font=di_font_setup
#         )
#         orig_roll_lbl_two.grid (row=3, column=2, sticky='W')
#
#         orig_roll_lbl_three = (ctk.CTkLabel (
#             master=mini_w_result_frame, fg_color="dark olive green",
#             text=(str (hit) + "Hit(s) : " + str (string_hit_roll[roll_count - 1])), image=test_img
#         )
#         )
#
#         orig_roll_lbl_three.grid (row=4, column=1, sticky='W')
#         wound_throw_lbl = (ctk.CTkLabel (
#             master=mini_w_result_frame, fg_color="dark olive green",
#             text=str (hit) + " Dice Rolled to Wound: " + str (
#                 string_wound_roll[roll_count - 1]
#             )
#         ))
#         wound_throw_lbl.grid (row=4, column=2)
#         wound_throw_lbl = (ctk.CTkLabel (
#             master=mini_w_result_frame, fg_color="dark olive green",
#             text=str (wound) + " Dice Wounded: " + str (string_wound_result[count])
#         ))
#         wound_throw_lbl.grid (row=5, column=1, sticky='W')
#
#         print ("dimens" + str (mini_w_result_frame.winfo_width ()))
#
#         count += 1
#
#     show_hit_wound (hit_num, wound_num)
#
# # load_screen(x)


def clr ():
    # clears display and previous roll data
    global roll_count, first_activation, current_session_log, record, session_npy_log
    first_activation = True
    roll_count = 0
    # print("test rec =  "+ str(current_session_log))
    # print(" rec =  "+ str(record))
    rd.RollDice (0, 0, 0)
    load_screen ()
    current_session_log.clear ()
    session_npy_log.clear ()
    record.pop ()



def mode_update ():
    global hnw_mode
    if hits_wound_var.get () == 1:
        hnw_mode = True
        print (hnw_mode)
    else:
        hnw_mode = False
        print (hnw_mode)


my_menu = tk.Menu (root)
# Create a category item  menu
file_menu = tk.Menu (my_menu, tearoff=0)
my_menu.add_cascade (label="File", menu=file_menu)
file_menu.add_command (label="Exit", command=root.quit)
edit_menu = tk.Menu (my_menu, tearoff=0)
my_menu.add_cascade (label="Edit", menu=edit_menu)
edit_menu.add_checkbutton (
    label="Speed Roll Hits n Wounds", variable=hits_wound_var, onvalue=1, offvalue=0, command=mode_update
    )
# check1 = Checkbutton(root, text="Pepperoni", variable=var1, onvalue=1, offvalue=0, font=("Helvetica", 18))


view_menu = tk.Menu (my_menu, tearoff=0)
my_menu.add_cascade (label="view", menu=view_menu)
view_menu.add_checkbutton (label="Vertical view", variable=score_view, onvalue=1, offvalue=0)
view_menu.add_checkbutton (label="Show rolls", variable=score_view, onvalue=1, offvalue=0)
view_menu.add_checkbutton (label="Highlight Successful Rolls", variable=score_view, onvalue=1, offvalue=0)

report_menu = tk.Menu (my_menu, tearoff=0)
my_menu.add_cascade (label="Reports", menu=report_menu)
report_menu.add_command (label="Result Report", command=show_history)

sub_edit_menu = tk.Menu (my_menu, tearoff=0)
edit_menu.add_cascade (label="Roll  options", menu=sub_edit_menu)
sub_edit_menu.add_checkbutton (label="Roll D3")

root.config (menu=my_menu)
#
roll_btn = ctk.CTkButton (master=user_input_frame, text="Roll", height=90, width=80, command=roll_new)
roll_btn.grid (row=2, rowspan=4, column=3, columnspan = 2, sticky='W',padx=10)
clear_btn = ctk.CTkButton (master=user_input_frame, text="Reset", width=85, command=clr)
clear_btn.grid (row=9, column=1, columnspan=1, pady=10)
# clear_btn.pack (side='bottom')
quit_btn = ctk.CTkButton (master=user_input_frame, text="Quit", width=85, command=root.quit)
# quit_btn.pack(side='bottom')
quit_btn.grid (row=9, column=2, columnspan=1, pady=10)
# if hnw_mode:
#
#
load_screen (record, "0", "0", wounds_arr, wounds_arr)
root.mainloop ()