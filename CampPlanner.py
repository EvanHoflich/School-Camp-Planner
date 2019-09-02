#School Camp Menu Planning Program Version four
#Written By Evan Hoflich
#Todays date
#Fourth version adds different meals for days and new vegetarian option and feedback options and actual calories per food instead of per 100g
#Calorie information provided by www.nutritionix.com (Used large size for meals as program doesn't account for snacks or drinks)

#-------------------------Import Libraries------------------------#
from tkinter import *
from tkinter import ttk
#----------------------------Constants----------------------------#
STARTING_TOTAL = 0

PANCAKES_CAL = 1173
SAUSAGE_CAL = 676
EGGS_CAL = 397
BACON_CAL = 1139
WEETBIX_CAL = 302
HAM_CAL = 714
OATMEAL_CAL = 204

BLT_CAL = 933
WRAP_CAL = 467
C_SANDWICH_CAL = 875
BAGEL_CAL = 422
KEBAB_CAL = 720
GREEK_SALAD = 440
PORK_SLIDER_CAL = 690
SCONE_CAL = 424

BURGER_CAL = 984
CAESAR_SALAD_CAL = 544
MINCE_PIE_CAL = 746
MACNCHEESE_CAL = 639
FISH_CAL = 192
LASAGNE_CAL = 921
TURKEY_CAL = 722
CHILLI_CAL = 637
PORK_CAL = 562
FRITTER_CAL = 714

#----------------------------List items---------------------------#
breakfast_list = ["Pancakes (v)","Sausage (m)", "Eggs (v)","Bacon (m)", "Weet-Bix (v)", "Ham (m)", "Oatmeal (v)"]
breakfast_cal_list = [PANCAKES_CAL, SAUSAGE_CAL, EGGS_CAL, BACON_CAL, WEETBIX_CAL, HAM_CAL, OATMEAL_CAL]
lunch_list = ["BLT Sandwitch (m)", "Wrap (v)", "Chicken Sandwich (m)", "Sesame Bagel (v)", "Chicken Kebab (m)", "Greek Salad (v)","Pork Slider (m)","Scone (v)"]
lunch_cal_list = [BLT_CAL, WRAP_CAL, C_SANDWICH_CAL, BAGEL_CAL, KEBAB_CAL, GREEK_SALAD, PORK_SLIDER_CAL, SCONE_CAL]
dinner_list = ["Burger (m)", "Caesar Salad (v)", "Mince Pie (m)", "Mac N' Cheese (v)", "Fish Fillet (m)", "Lasagne (v)", "Turkey (m)", "Chilli beans (v)", "Roast Pork (m)", "Apple Fritters (v)"]
dinner_cal_list = [BURGER_CAL, CAESAR_SALAD_CAL, MINCE_PIE_CAL, MACNCHEESE_CAL, FISH_CAL, LASAGNE_CAL, TURKEY_CAL, CHILLI_CAL, PORK_CAL, FRITTER_CAL]
#-------------------------Class Definition------------------------#
class Order:
    def __init__(self, item, calories):
        self.item = item
        self.calories = calories
        
def vegetarian():
    breakfast_list = ["Pancakes (v)","Sausage (m)", "Eggs (v)","Bacon (m)", "Weet-Bix (v)", "Ham (m)", "Oatmeal (v)"]
    lunch_list = ["BLT Sandwitch (m)", "Wrap (v)", "Chicken Sandwich (m)", "Sesame Bagel (v)", "Chicken Kebab (m)", "Greek Salad (v)","Pork Slider (m)","Scone (v)"]
    dinner_list = ["Burger (m)", "Caesar Salad (v)", "Mince Pie (m)", "Mac N' Cheese (v)", "Fish Fillet (m)", "Lasagne (v)", "Turkey (m)", "Chilli beans (v)", "Roast Pork (m)", "Apple Fritters (v)"]
    for str in breakfast_list:
        if "(m)" in str:
            breakfast_list.remove(str)
    for str in lunch_list:
        if "(m)" in str:
            lunch_list.remove(str)
    for str in dinner_list:
        if "(m)" in str:
            dinner_list.remove(str)
    breakfast_one_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_one, state="readonly").grid(row=2, column=1, pady=5, padx=5)
    breakfast_two_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_two, state="readonly").grid(row=2, column=2, pady=5, padx=5)
    breakfast_three_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_three, state="readonly").grid(row=2, column=3, pady=5, padx=5)    
    lunch_one_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_one, state="readonly").grid(row=3, column=1, pady=5, padx=5)
    lunch_two_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_two, state="readonly").grid(row=3, column=2, pady=5, padx=5)
    lunch_three_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_three, state="readonly").grid(row=3, column=3, pady=5, padx=5)    
    dinner_one_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_one, state="readonly").grid(row=4, column=1, padx=5, pady=5)
    dinner_two_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_two, state="readonly").grid(row=4, column=2, padx=5, pady=5) 
    dinner_three_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_three, state="readonly").grid(row=4, column=3, padx=5, pady=5)    
            
def meat():
    breakfast_list = ["Pancakes (v)","Sausage (m)", "Eggs (v)","Bacon (m)", "Weet-Bix (v)", "Ham (m)", "Oatmeal (v)"]
    lunch_list = ["BLT Sandwitch (m)", "Wrap (v)", "Chicken Sandwich (m)", "Sesame Bagel (v)", "Chicken Kebab (m)", "Greek Salad (v)","Pork Slider (m)","Scone (v)"]
    dinner_list = ["Burger (m)", "Caesar Salad (v)", "Mince Pie (m)", "Mac N' Cheese (v)", "Fish Fillet (m)", "Lasagne (v)", "Turkey (m)", "Chilli beans (v)", "Roast Pork (m)", "Apple Fritters (v)"]
    for str in breakfast_list:
        if "(v)" in str:
            breakfast_list.remove(str)
    for str in lunch_list:
        if "(v)" in str:
            lunch_list.remove(str)
    for str in dinner_list:
        if "(v)" in str:
            dinner_list.remove(str)
    breakfast_one_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_one, state="readonly").grid(row=2, column=1, pady=5, padx=5)
    breakfast_two_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_two, state="readonly").grid(row=2, column=2, pady=5, padx=5)
    breakfast_three_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_three, state="readonly").grid(row=2, column=3, pady=5, padx=5)    
    lunch_one_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_one, state="readonly").grid(row=3, column=1, pady=5, padx=5)
    lunch_two_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_two, state="readonly").grid(row=3, column=2, pady=5, padx=5)
    lunch_three_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_three, state="readonly").grid(row=3, column=3, pady=5, padx=5)    
    dinner_one_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_one, state="readonly").grid(row=4, column=1, padx=5, pady=5)
    dinner_two_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_two, state="readonly").grid(row=4, column=2, padx=5, pady=5) 
    dinner_three_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_three, state="readonly").grid(row=4, column=3, padx=5, pady=5)
    
def all():
    breakfast_one_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_one, state="readonly").grid(row=2, column=1, pady=5, padx=5)
    breakfast_two_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_two, state="readonly").grid(row=2, column=2, pady=5, padx=5)
    breakfast_three_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_three, state="readonly").grid(row=2, column=3, pady=5, padx=5)    
    lunch_one_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_one, state="readonly").grid(row=3, column=1, pady=5, padx=5)
    lunch_two_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_two, state="readonly").grid(row=3, column=2, pady=5, padx=5)
    lunch_three_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_three, state="readonly").grid(row=3, column=3, pady=5, padx=5)    
    dinner_one_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_one, state="readonly").grid(row=4, column=1, padx=5, pady=5)
    dinner_two_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_two, state="readonly").grid(row=4, column=2, padx=5, pady=5) 
    dinner_three_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_three, state="readonly").grid(row=4, column=3, padx=5, pady=5)

def collect_info():
    total = STARTING_TOTAL
    #-----------------------------------------------Breakfast-----------------------------------------------------#
    total += Order(breakfast_day_one.get(), breakfast_cal_list[breakfast_list.index(breakfast_day_one.get())]).calories
    total += Order(breakfast_day_two.get(), breakfast_cal_list[breakfast_list.index(breakfast_day_two.get())]).calories
    total += Order(breakfast_day_three.get(), breakfast_cal_list[breakfast_list.index(breakfast_day_three.get())]).calories
    #------------------------------------------------Lunch-----------------------------------------------------#
    total += Order(lunch_day_one.get(), lunch_cal_list[lunch_list.index(lunch_day_one.get())]).calories
    total += Order(lunch_day_two.get(), lunch_cal_list[lunch_list.index(lunch_day_two.get())]).calories
    total += Order(lunch_day_three.get(), lunch_cal_list[lunch_list.index(lunch_day_three.get())]).calories
    #-----------------------------------------------Dinner------------------------------------------------------#
    total += Order(dinner_day_one.get(), dinner_cal_list[dinner_list.index(dinner_day_one.get())]).calories
    total += Order(dinner_day_two.get(), dinner_cal_list[dinner_list.index(dinner_day_two.get())]).calories
    total += Order(dinner_day_three.get(), dinner_cal_list[dinner_list.index(dinner_day_three.get())]).calories    
    total_calorie_amount.set("{} total calories / ~{:.0f} Calories per day".format(total, total/3))
    global total_calories
    total_calories=total/3

def bmr_calculator():
    bmr= STARTING_TOTAL
    bmr = 10 * weight_number.get() + 6.25 * height_number.get() - 5 * age_number.get()  #The Harris-Benedict equation to calculate BMR (Metabolic rate is used to find how many calories you should be intaking
    bmr_amount.set("{:} cal/day".format(bmr))
    global bmr_for_feedback
    bmr_for_feedback = bmr

def bmr_feedback():
    net_calories = total_calories - bmr_for_feedback
    net_calories = abs(net_calories)
    if total_calories < bmr_for_feedback:
        bmr_suggestion.set("Your calorie count is {:.0f} and your recommended count is {:.0f}. This means you are eating \n {:.0f} calories less than recommended and means you have chosen a healty meal choice \n for your body type".format(total_calories, bmr_for_feedback, net_calories))
    if total_calories > bmr_for_feedback:
        bmr_suggestion.set("Your calorie count is {:.0f} and your recommended count is {:.0f}. This means you are eating \n{:.0f} calories more than recommended and means you are not eating a healthy meal choice \n for your body type".format(total_calories, bmr_for_feedback, net_calories))
    if total_calories == bmr_for_feedback:
        bmr_suggestion.set("Your calorie count is {:.0f} and your recommended count is {:.0f}. This means you are eating \n the perfect balance of calories inside your meal for your body type".format(total_calories, bmr_for_feedback))
        
def reset_choices():
    breakfast_one_option.set("")
    breakfast_two_option.set("")
    breakfast_three_option.set("")
    lunch_one_option.set("")
    lunch_two_option.set("")
    lunch_three_option.set("")
    dinner_one_option.set("")
    dinner_two_option.set("")
    dinner_three_option.set("")
    weight_entry.delete(first=0,last=22)
    height_entry.delete(first=0,last=22)
    age_entry.delete(first=0,last=22)
    total_calorie_amount.set("")
    bmr_amount.set("")
    bmr_suggestion.set("")
    
    
        
#-------------------------Start the window------------------------#

root = Tk()
root.title("School camp menu planning")

#------------------------Declaring Frames-------------------------#

heading_frame = ttk.LabelFrame(root)
heading_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")
main_frame =  ttk.LabelFrame(root)
main_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")
footer_frame = ttk.LabelFrame(root)
footer_frame.grid(row=2, column=0, padx=10, pady=10, sticky="NSEW")
feedback_frame = ttk.LabelFrame(root)
feedback_frame.grid(row=3, column=0, padx=10, pady=10, sticky="NSEW")

#------------------------Value Declaration------------------------#

opening_message = StringVar()
opening_message.set("Welcome to the school camp menu planning program")
key_message = StringVar()
key_message.set("Key - (m) means the meal contains meat, (v) means the meal is vegetarian")
feedback_title = StringVar()
feedback_title.set("Calculate BMR based on age, weight and height")

breakfast_day_one = StringVar()
breakfast_day_two = StringVar()
breakfast_day_three = StringVar()
lunch_day_one = StringVar()
lunch_day_two = StringVar()
lunch_day_three = StringVar()
dinner_day_one = StringVar()
dinner_day_two = StringVar()
dinner_day_three = StringVar()
feedback_total = StringVar()
total_calorie_amount = StringVar()
bmr_amount = StringVar()
weight_number = IntVar()
age_number = IntVar()
height_number = IntVar()
bmr_suggestion = StringVar()
net_calories = IntVar()
daily_calorie_amount = IntVar()

#-----------------------------Styles------------------------------#
labelstyle = ttk.Style()
labelstyle.configure("labelstyle.TButton", font=("Open Sans", 8, "bold"))
textstyle = ttk.Style()
textstyle.configure("textstyle.TLabel", font=("Open Sans", 9))

#--------------------------Widget Boxes---------------------------#

opening_label = ttk.Label(heading_frame, textvariable=opening_message, style="textstyle.TLabel")
opening_label.grid(row=0, column=0, padx=70, pady=5)
key_label = ttk.Label(heading_frame, textvariable=key_message, style="textstyle.TLabel")
key_label.grid(row=1, column=0, padx=70, pady=5)
day_one_label = ttk.Label(main_frame, text="Day One", style="textstyle.TLabel")
day_one_label.grid(row=1, column=1, pady=5, padx=20)
day_two_label = ttk.Label(main_frame, text="Day Two", style="textstyle.TLabel")
day_two_label.grid(row=1, column=2, pady=5, padx=20)
day_three_label = ttk.Label(main_frame, text="Day Three", style="textstyle.TLabel")
day_three_label.grid(row=1, column=3, pady=5, padx=20)

dinner_label = ttk.Label(main_frame, text="Breakfast", style="textstyle.TLabel")
dinner_label.grid(row=2, column=0, padx=5, pady=5)
dinner_label = ttk.Label(main_frame, text="Lunch", style="textstyle.TLabel")
dinner_label.grid(row=3, column=0, padx=5, pady=5)
dinner_label = ttk.Label(main_frame, text="Dinner", style="textstyle.TLabel")
dinner_label.grid(row=4, column=0, padx=5, pady=5)

meal_option_label = ttk.Label(main_frame, text="Meal Options")
meal_option_label.grid(row=0, column=0, padx=5, pady=5)
all_button = ttk.Radiobutton(main_frame, text="All meals", value=1, command=all, cursor="hand2")
all_button.grid(row=0, column=1, padx=5, pady=5)
vegetarian_button = ttk.Radiobutton(main_frame, text="Vegetarian", value=2, command=vegetarian, cursor="hand2")
vegetarian_button.grid(row=0, column=2, padx=5, pady=5)
meat_button = ttk.Radiobutton(main_frame, text="Meat Only", value=3, command=meat, cursor="hand2")
meat_button.grid(row=0, column=3, padx=5, pady=5)



breakfast_one_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_one, state="readonly")
breakfast_one_option.grid(row=2, column=1, pady=5, padx=5)
breakfast_two_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_two, state="readonly")
breakfast_two_option.grid(row=2, column=2, pady=5, padx=5)
breakfast_three_option = ttk.Combobox(main_frame, values=breakfast_list, textvariable=breakfast_day_three, state="readonly")
breakfast_three_option.grid(row=2, column=3, pady=5, padx=5)


lunch_one_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_one, state="readonly")
lunch_one_option.grid(row=3, column=1, pady=5, padx=5)
lunch_two_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_two, state="readonly")
lunch_two_option.grid(row=3, column=2, pady=5, padx=5)
lunch_three_option = ttk.Combobox(main_frame, values=lunch_list, textvariable=lunch_day_three, state="readonly")
lunch_three_option.grid(row=3, column=3, pady=5, padx=5)


dinner_one_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_one, state="readonly")
dinner_one_option.grid(row=4, column=1, padx=5, pady=5)
dinner_two_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_two, state="readonly")
dinner_two_option.grid(row=4, column=2, padx=5, pady=5)
dinner_three_option = ttk.Combobox(main_frame, values=dinner_list, textvariable=dinner_day_three, state="readonly")
dinner_three_option.grid(row=4, column=3, padx=5, pady=5)
total_button = ttk.Button(main_frame, text="Calculate Total Calories", command=collect_info, cursor="hand2", style="labelstyle.TButton")
total_button.grid(row=5, column=0, padx=5, pady=5)
total_label = ttk.Label(main_frame, textvariable=total_calorie_amount)
total_label.grid(row=5, column=1, padx=5, pady=5, columnspan=2)

bmr_name_label = ttk.Label(footer_frame, text="Calculate your BMR to find out how many calories \n you're recomened to eat", style="textstyle.TLabel")
bmr_name_label.grid(row=0, column=2, padx=5, pady=5)


weight_label = ttk.Label(footer_frame, text="Enter Weight (kg)", style="textstyle.TLabel")
weight_label.grid(row=0, column=0, padx=5, pady=5)
height_label = ttk.Label(footer_frame, text="Enter Height (cm)", style="textstyle.TLabel")
height_label.grid(row=1, column=0, padx=5, pady=5)
age_label = ttk.Label(footer_frame, text="Enter Age", style="textstyle.TLabel")
age_label.grid(row=2, column=0, padx=5, pady=5)
                         
                         
weight_entry = ttk.Entry(footer_frame, textvariable=weight_number)
weight_entry.grid(row=0, column=1, padx=5, pady=5)
height_entry = ttk.Entry(footer_frame, textvariable=height_number)
height_entry.grid(row=1, column=1, padx=5, pady=5)
age_entry = ttk.Entry(footer_frame, textvariable=age_number)
age_entry.grid(row=2, column=1, padx=5, pady=5)

bmr_button = ttk.Button(footer_frame, text="Recommended Calories/day", command=bmr_calculator, cursor="hand2", style="labelstyle.TButton")
bmr_button.grid(row=3, column=0, padx=5, pady=5)
bmr_label = ttk.Label(footer_frame, textvariable=bmr_amount)
bmr_label.grid(row=3, column=1, padx=5, pady=5)


bmr_button = ttk.Button(feedback_frame, text="Feedback for food choices", command=bmr_feedback, cursor="hand2", style="labelstyle.TButton")
bmr_button.grid(row=0, column=0, padx=5, pady=5)
bmr_suggestion_label = ttk.Label(feedback_frame, textvariable=bmr_suggestion)
bmr_suggestion_label.grid(row=0, column=1, padx=5, pady=5)

reset_button = ttk.Button(feedback_frame, text="           Reset Choices           ", command=reset_choices, cursor="hand2", style="labelstyle.TButton")
reset_button.grid(row=1, column=0, padx=5, pady=5)
#----------------------Running the Program------------------------#

root.mainloop()
