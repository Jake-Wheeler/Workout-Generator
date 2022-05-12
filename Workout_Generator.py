
# stored_data can lock in the starting point to the workout_gen


# hr_zone can affect the change of the below values
        # hr needs to prioritize changing smaller variables like reps and sets only when
            # intensity falls or rises slightly, whereas, larger variables likes the changing
                # of exercises or tempo should come when intensity is far from the goal

# todays_target and program_lvl can be the piece that alters the exercise choices
        # program_lvl can create subdivisions for every possible workout layout
# goal can affect the set_tempo start but only change after according to the variables set in intensity
        # goal also affects the starting reps but only changes after from intensity shifting
# intensity can be set to intensity = [goal, hr_zone, program_lvl, set_tempo, amount_reps, amount_sets]
        # a loop can be created so that everytime hr falls lower or higher than expected after a set,
            # the intensity is corrected and depending on the distance from target_intensity it can
                # .remove(intensity[]) the right index accordingly and change the preset value and finally
                    # .append(intensity[]) it back into the circle again and update the workout accordingly

import random
import secrets
from itertools import count

experience_lvl = 1
goal = "endurance"
layout_style = 1
todays_target = "push"
# single ask
# goal = input("Is your goal to increase endurance, muscle size, or muscle strength?: ")
# print("How experienced would you say you are in the gym?")
# experience_lvl = input("Beginner(1), Intermediate(2), Experienced(3), Master(4): ")
# target_intensity = input("What is the intensity lvl%?: ")
# age = input("Age: ")
# if goal == "endurance":
#     print("What kind of layout do you like for training " + goal + "? (Type 1, 2, OR 3)")
#     print("Compound movements first then individual muscles?(1)")
#     print("3-5 exercise circuits?(2)")
#     print("Surprise Me!(3)")
#     layout_style = input("I prefer number: ")
# if goal == "hypertrophy":
#     print("What kind of layout do you like for training " + goal + "? (Type 1, 2, OR 3)")
#     print("Compound movements first then individual muscles?(1): ")
#     print("Super-setting antagonist muscles?(2):")
#     print("Surprise Me!(3): ")
#     layout_style = input("I prefer number: ")
# if goal == "strength":
#     print("What kind of layout do you like for training " + goal + "? (Type 1, 2, OR 3)")
#     print("Compound movements first then individual muscles?(1): ")
#     print("Big lifts, ending with burnouts?(2): ")
#     print("Surprise Me!(3): ")
#     layout_style = input("I prefer number: ")
# todays_target = input("today we're working on: ")






tempo_list = ["1-1-1", "1-2-1", "2-2-1", "4-2-1"]
amount_sets_list = [1, 2, 3, 4]
rep_range_list = [[1, 2, 4, 6], [8, 10, 12], [14, 16, 18, 20], [10, 20, 30, 40, 50, 60]]
muscle_groups = {'legs': ["quads", "hamstrings", "glutes", "hip flexor", "adductors", "abductors", "calves"],
                 'core': ["upper abs", "lower abs", "obliques"], 'chest': ['upper chest', 'middle chest', 'lower chest'],
                 'back': ['upper back', 'middle back', 'lower back', 'lats'],
                 'biceps': ["bicep long head", "bicep short head", "bicep lateral head"],
                 'triceps': ['tricep long head', 'tricep medial head', 'tricep lateral head']}
legs = muscle_groups['legs']
core = muscle_groups['core']
chest = muscle_groups['chest']
back = muscle_groups['back']
biceps = muscle_groups['biceps']
triceps = muscle_groups['triceps']
leg_exer_lst = {
    'BB Squat': ['legs', 'quads', '', 'together', 'compound', 'bb'],
    'BB Deadlift': ['legs', 'quads', 'lower back', 'together', 'compound', 'bb'],
    'BB Front Squat': ['legs', 'quads', 'core', 'together', 'compound', 'bb'],
    'BB RDL': ['legs', 'hamstrings', 'lower back', 'together', 'compound', 'bb'],
    'BB Single Leg Lunges': ['legs', 'quads', '', 'single', 'compound', 'bb'],
    'BB Alt. Lunges': ['legs', 'quads', '', 'single', 'compound', 'bb'],
    'DB Goblet Squat': ['legs', 'quads', '', 'together', 'compound', 'db'],
    'DB Goblet Squat, elevated heel': ['legs', 'hamstrings', '', 'together', 'compound', 'db'],
    'DB RDL': ['legs', 'hamstrings', 'lower back', 'together', 'compound', 'db'],
    'DB Bulgarian Split Squat': ['legs', 'quads', '', 'single', 'compound', 'db'],
    'DB Single Leg Lunges': ['legs', 'quads', '', 'single', 'compound', 'db'],
    'DB Alt. Lunges': ['legs', 'quads', '', 'single', 'compound', 'db'],
    'Smith Machine Squats': ['legs', 'quads', '', 'together', 'compound', 'machine'],
    'Smith Machine Squats, elevated heel': ['legs', 'hamstrings', '', 'together', 'compound', 'machine'],
    'Leg Press Machine': ['legs', 'quads', '', 'together', 'compound', 'machine'],
    'Smith Machine Single Leg Lunges': ['legs', 'quads', '', 'single', 'compound', 'machine'],
    'Smith Machine Alt. Lunges': ['legs', 'quads', '', 'single', 'compound', 'machine'],
    'Single Leg Press Machine': ['legs', 'quads', '', 'single', 'compound', 'machine'],
    'Leg Ext Machine': ['legs', 'quads', '', 'together', 'isolated', 'machine'],
    'Leg Curl Machine': ['legs', 'hamstrings', '', 'together', 'isolated', 'machine'],
    'Calf Raise Machine': ['legs', 'calves', '', 'together', 'isolated', 'machine'],
    'Prisoner Squat': ['legs', 'quads', '', 'together', 'compound', 'calisthenic'],
    'Bulgarian Split Squat': ['legs', 'quads', '', 'single', 'compound', 'calisthenic'],
    'Single Leg Lunges': ['legs', 'quads', '', 'single', 'compound', 'calisthenic'],
    'Alt. Lunges': ['legs', 'quads', '', 'single', 'compound', 'calisthenic'],
    'Single Leg Reverse Lunge': ['legs', 'quads', '', 'single', 'compound', 'calisthenic'],
    'Alt. Reverse Lunge': ['legs', 'quads', '', 'single', 'compound', 'calisthenic']
    'Standing Abductor Raises': ['legs', 'abductors', '', 'single', 'compound', 'calisthenic'],
    'Calf Raises': ['legs', 'calves', '', 'together', 'compound', 'calisthenic']
}
chest_exer_lst = {
    'BB Bench Press': ['chest', 'middle', 'triceps', 'together', 'compound', 'bb'],
    'BB Bench Incline Press': ['chest', 'upper', 'triceps', 'together', 'compound', 'bb'],
    'DB Chest Press': ['chest', 'middle', 'triceps', 'together', 'compound', 'db'],
    'DB Alt. Chest Press': ['chest', 'middle', 'triceps', 'single', 'compound', 'db'],
    'DB Chest Fly': ['chest', 'middle', '', 'together', 'isolated', 'db'],
    'Cable Chest Press': ['chest', 'middle', 'triceps', 'together', 'compound', 'cable'],
    'Cable Chest Fly': ['chest', 'middle', '', 'together', 'isolated', 'cable'],
    'Chest Press Machine': ['chest', 'middle', 'triceps', 'together', 'compound', 'machine'],
    'Incline Chest Press Machine': ['chest', 'upper', 'triceps', 'together', 'compound', 'machine'],
    'Chest Fly Machine': ['chest', 'middle', '', 'together', 'isolated', 'machine'],
    'Wall Push Up': ['chest', 'lower', 'triceps', 'together', 'compound', 'calisthenic'],
    'Bench Dips, Chest Oriented': ['chest', 'lower', 'triceps', 'together', 'compound', 'calisthenic'],
    'Knee Push Ups': ['chest', 'middle', 'triceps', 'together', 'compound', 'calisthenic'],
    'Push Up': ['chest', 'middle', 'triceps', 'together', 'compound', 'calisthenic'],
    'Pike Push Up': ['chest', 'upper', 'triceps', 'together', 'compound', 'calisthenic'],
    'Reactive Push Ups': ['chest', 'middle', 'triceps', 'together', 'compound', 'calisthenic'],
    'Side to Side Push Ups': ['chest', 'middle', 'triceps', 'single', 'comp', 'calisthenic'],
    'Floating Dips': ['chest', 'lower', 'triceps', 'together', 'comp', 'calisthenic']
}
back_exer_lst = {
    'BB Bent Over Row': ['back', 'lats', 'middle', 'together', 'comp', 'bb'],
    'BB Push Jerk': ['back', 'upper', 'triceps', 'together', 'comp', 'bb'],
    'DB Single Arm Row': ['back', 'lats', 'middle', 'single', 'comp', 'db'],
    'DB Reverse Fly': ['back', 'middle', '', 'together', 'isolated', 'db'],
    'DB Bent Over Row': ['back', 'lats', 'middle', 'together', 'comp', 'db'],
    'DB Y Raises': ['back', 'middle', '', 'together', 'isolated', 'db'],
    'Cable Low Row': ['back', 'lats', 'upper', 'together', 'comp', 'cable'],
    'High Row Machine': ['back', 'lats', 'lower', 'together', 'comp', 'machine'],
    'Seated Row Machine': ['back', 'lats', 'middle', 'together', 'comp', 'machine'],
    'Low Row Machine': ['back', 'lats', 'upper', 'together', 'comp', 'machine'],
    'Assisted Pull Up Machine': ['back', 'lats', 'lower', 'together', 'comp', 'machine'],
    'Lat Pull Machine': ['back', 'lats', 'lower', 'together', 'comp', 'machine'],
    'Chin Up': ['back', 'lats', 'biceps', 'together', 'comp', 'calisthenic'],
    'Pull Up': ['back', 'lats', 'middle', 'together', 'comp', 'calisthenic'],
    'Side to Side Pull Up': ['back', 'lats', 'middle', 'single', 'comp', 'calisthenic']
}
biceps_exer_lst = {
    'BB Curl': ['biceps', 'short head', '', 'together', 'isolated', 'bb'],
    'BB Drag Curl': ['biceps', 'long head', 'short head', 'together', 'iso', 'bb'],
    'BB 1/2 curl': ['biceps', 'short head', '', 'together', 'iso', 'bb'],
    'DB Curl': ['biceps', 'short head', '', 'together', 'iso', 'db'],
    'DB Alt. Curl': ['biceps', 'short head', '', 'single', 'iso', 'db'],
    'DB Hammer Curl': ['biceps', 'lateral head', '', 'together', 'db', 'db'],
    'DB Alt. Hammer Curl': ['biceps', 'lateral head', '', 'single', 'iso', 'db'],
    'DB Seated incline Curl': ['biceps', 'long head', 'short head', 'together', 'iso', 'db'],
    'DB Seated Incline Hammer Curl': ['biceps', 'long head', 'lateral head', 'together', 'iso', 'db'],
    'DB Zottman Curl': ['biceps', 'lateral head', 'short head', 'together', 'iso', 'db'],
    'DB Lateral Curl': ['biceps', 'lateral head', '', 'together', 'iso', 'db'],
    'Cable Hammer Curl': ['biceps', 'lateral head', '', 'together', 'iso', 'cable'],
    'Cable Supinated Curl': ['biceps', 'short head', '', 'together', 'iso', 'cable'],
    'Cable Pulled Back Curl': ['biceps', 'long head', 'short head', 'together', 'iso', 'cable'],
    'Cable Alt. Pulled Back Curl': ['biceps', 'long head', 'short head', 'single', 'iso', 'cable'],
    'Cable Alt. Supinated Curl': ['biceps', 'short head', '', 'single', 'iso', 'cable'],
    'Cable Alt. Hammer Curl': ['biceps', 'lateral head', '', 'single', 'iso', 'cable']
}
triceps_exer_lst = {
    'BB Skullcrusher': ['triceps', 'long head', 'medial head', 'together', 'iso', 'bb'],
    'DB Lateral Ext.': ['triceps', 'lateral head', 'long head', 'single', 'iso', 'db'],
    'DB Standing Tricep Kickback': ['triceps', 'long head', 'short head', 'single', 'iso', 'db'],
    'DB Horizontal Tricep Kickback': ['triceps', 'long head', 'medial head', 'single', 'iso', 'db'],
    'Cable Tricep Pushdown': ['triceps', 'short head', 'long head', 'together', 'iso', 'cable'],
    'Cable Overhead Ext.': ['triceps', 'long head', 'short head', 'together', 'iso', 'cable'],
    'Cable Single Arm Tricep Lateral Ext.': ['triceps', 'lateral head', 'long head', 'single', 'iso', 'cable'],
    'Seated Dip Machine': ['triceps', 'long head', 'short head', 'together', 'iso', 'machine'],
    'Bench Dips, Tricep Oriented': ['triceps', 'long head', 'medial head', 'together', 'compound', 'calisthenic'],
    'Knee Diamond Push Ups': ['triceps', 'lateral head', 'long head', 'together', 'comp', 'calisthenic'],
    'Diamond Push Ups': ['triceps', 'lateral head', 'long head', 'together', 'comp', 'calisthenic']
}
core_exer_lst = {
    'Crunches': ['core', 'upper', '', 'one side', 'isolated', 'calisthenic'],
    'Plank, Arms Straight': ['core', 'upper', 'back', 'hold', 'isolated', 'calisthenic'],
    'Butterfly Kicks': ['core', 'lower', '', 'two sides', 'isolated', 'calisthenic'],
    'Single Leg Raise': ['core', 'lower', '', 'single', 'isolated', 'calisthenic'],
    'Leg Raises': ['core', 'lower', '', 'together', 'isolated', 'calisthenic'],
    'Seated Knee Tucks': ['core', 'lower', 'upper', 'together', 'compound', 'calisthenic'],
    'Plank, Arms Bent': ['core', 'upper', 'lower', 'hold', 'compound', 'calisthenic'],
    'Mountain Climbers': ['core', 'obliques', 'upper', 'two sides', 'compound', 'calisthenic'],
    'Seated Knee Tuck, Inside/Outside': ['core', 'lower', 'obliques', 'single', 'compound', 'calisthenic'],
    'Sit-Ups': ['core', 'upper', '', 'together', 'compound', 'calisthenic'],
    'V-Ups': ['core', 'lower', 'upper', 'together', 'compound', 'calisthenic'],
    'Side-to-Side Crunches': ['core', 'obliques', 'upper', 'single', 'isolated', 'calisthenic'],
    'Hanging Leg Raise': ['core', 'lower', '', 'together', 'isolated', 'calisthenic'],
    'Hanging Knee Tuck': ['core', 'lower', 'upper', 'together', 'compound', 'calisthenic'],
    'Hanging Straight Crunch': ['core', 'upper', '', 'together', 'isolated', 'calisthenic'],
    'Hanging Side Crunch': ['core', 'obliques', '', 'single', 'isolated', 'calisthenic'],
    'Reverse Lowering Plank': ['core', 'lower', 'upper', 'together', 'compound', 'calisthenic']
}

arms = biceps + triceps
upper_body = biceps + triceps + back + chest
lower_body = legs + core
push = chest + triceps
pull = back + biceps
exer_pick = []


def assign_sets_reps_tempo():
    if goal == "endurance":
        sets = 2
        reps = 15
        speed = "2-2-1"
        return sets, reps, speed
    elif goal == "hypertrophy":
        sets = 2
        reps = 10
        speed = "2-2-1"
        return sets, reps, speed
    elif goal == "strength":
        sets = 2
        reps = 6
        speed = "1-2-1"
        return sets, reps, speed


def assign_program_lvl():
    if experience_lvl == 1:
        lvl = program_lvl1
        return lvl
    if experience_lvl == 2:
        lvl = program_lvl2
        return lvl
    if experience_lvl == 3:
        lvl = program_lvl3
        return lvl
    if experience_lvl == 4:
        lvl = program_lvl4
        return lvl


def target_muscle():
    if todays_target == "legs":
        tmg = legs
        return tmg
    elif todays_target == "arms":
        tmg = arms
        return tmg
    elif todays_target == "chest":
        tmg = chest
        return tmg
    elif todays_target == "back":
        tmg = back
        return tmg
    elif todays_target == "core":
        tmg = core
        return tmg
    elif todays_target == "upper body":
        tmg = upper_body
        return tmg
    elif todays_target == "lower body":
        tmg = lower_body
        return tmg
    elif todays_target == "push":
        tmg = push
        return tmg
    elif todays_target == "pull":
        tmg = pull
        return tmg
    else:
        print("No Valid Workouts")


def num_exer_needed():
    num_exer = 0
    if goal == "endurance":
        if layout_style == 1:
            if experience_lvl == 1:
                num_exer += 10
                return num_exer
            elif experience_lvl == 2:
                num_exer += 10
                return num_exer
            elif experience_lvl == 3:
                num_exer += 15
                return num_exer
            elif experience_lvl == 4:
                num_exer += 20
                return num_exer
        elif layout_style == 2:
            if experience_lvl == 1:
                num_exer += 4
                return num_exer
            elif experience_lvl == 2:
                num_exer += 6
                return num_exer
            elif experience_lvl == 3:
                num_exer += 8
                return num_exer
            elif experience_lvl == 4:
                num_exer += 10
                return num_exer
        elif layout_style == 3:
            if experience_lvl == 1:
                num_exer += 5
                return num_exer
            elif experience_lvl == 2:
                num_exer += 10
                return num_exer
            elif experience_lvl == 3:
                num_exer += 15
                return num_exer
            elif experience_lvl == 4:
                num_exer += 20
                return num_exer
    elif goal == "hypertrophy":
        if layout_style == 1:
            if experience_lvl == 1:
                num_exer += 6
                return num_exer
            elif experience_lvl == 2:
                num_exer += 9
                return num_exer
            elif experience_lvl == 3:
                num_exer += 12
                return num_exer
            elif experience_lvl == 4:
                num_exer += 15
                return num_exer
        elif layout_style == 2:
            if experience_lvl == 1:
                num_exer += 8
                return num_exer
            elif experience_lvl == 2:
                num_exer += 12
                return num_exer
            elif experience_lvl == 3:
                num_exer += 16
                return num_exer
            elif experience_lvl == 4:
                num_exer += 20
                return num_exer
        elif layout_style == 3:
            if experience_lvl == 1:
                num_exer += 8
                return num_exer
            elif experience_lvl == 2:
                num_exer += 12
                return num_exer
            elif experience_lvl == 3:
                num_exer += 16
                return num_exer
            elif experience_lvl == 4:
                num_exer += 20
                return num_exer
    elif goal == "strength":
        if layout_style == 1:
            if experience_lvl == 1:
                num_exer += 6
                return num_exer
            elif experience_lvl == 2:
                num_exer += 8
                return num_exer
            elif experience_lvl == 3:
                num_exer += 10
                return num_exer
            elif experience_lvl == 4:
                num_exer += 12
                return num_exer
        elif layout_style == 2:
            if experience_lvl == 1:
                num_exer += 6
                return num_exer
            elif experience_lvl == 2:
                num_exer += 8
                return num_exer
            elif experience_lvl == 3:
                num_exer += 10
                return num_exer
            elif experience_lvl == 4:
                num_exer += 12
                return num_exer
        elif layout_style == 3:
            if experience_lvl == 1:
                num_exer += 6
                return num_exer
            elif experience_lvl == 2:
                num_exer += 8
                return num_exer
            elif experience_lvl == 3:
                num_exer += 10
                return num_exer
            elif experience_lvl == 4:
                num_exer += 12
                return num_exer


def set_workout_pace():
    tmg = target_muscle()
    sets, reps, speed = assign_sets_reps_tempo()
    lvl = assign_program_lvl()
    num_exer = num_exer_needed()
    return tmg, sets, reps, speed, lvl, num_exer





target_muscle_group, amount_sets, amount_reps, tempo, program_lvl, amount_exer = set_workout_pace()
intensity = [layout_style, exer_pick, program_lvl, amount_reps, "weight", amount_sets, "tempo"]


def find_comp_lst():
    x = []
    for a in comp_move_exer_list:
        if a in program_lvl:
            if a in target_muscle_group:
                x.extend([a])
    return x


def find_iso_lst():
    x = []
    for a in iso_move_exer_list:
        if a in program_lvl:
            if a in target_muscle_group:
                x.extend([a])
    return x


def find_bb_comp_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in bb_exer_list:
                if x in comp_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_db_comp_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in db_exer_list:
                if x in comp_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_cable_comp_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in cable_exer_list:
                if x in comp_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_mach_comp_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in mach_exer_list:
                if x in comp_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_cali_comp_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in calisthenic_exer_list:
                if x in comp_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_bb_iso_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in bb_exer_list:
                if x in iso_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_db_iso_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in db_exer_list:
                if x in iso_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_cable_iso_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in cable_exer_list:
                if x in iso_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_mach_iso_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in mach_exer_list:
                if x in iso_move_exer_list:
                    if x not in exer_pick:
                        return x


def find_cali_iso_exer(muscle):
    for x in program_lvl:
        if x in muscle:
            if x in calisthenic_exer_list:
                if x in iso_move_exer_list:
                    if x not in exer_pick:
                        return x


def search_heavy_lvl_list(muscle, group):
    for x in program_lvl:
        if x in muscle:
            if program_lvl == program_lvl3 or program_lvl4:
                if x in bb_exer_list:
                    if group == 'comp':
                        return find_bb_comp_exer(muscle)
                    if group == 'iso':
                        return find_bb_iso_exer(muscle)
                elif x in db_exer_list:
                    if group == 'comp':
                        return find_db_comp_exer(muscle)
                    if group == 'iso':
                        return find_db_iso_exer(muscle)
            elif program_lvl == program_lvl1 or program_lvl2:
                if x in mach_exer_list:
                    if group == 'comp':
                        return find_mach_comp_exer(muscle)
                    if group == 'iso':
                        return find_mach_iso_exer(muscle)
                elif x in calisthenic_exer_list:
                    if group == 'comp':
                        return find_cali_comp_exer(muscle)
                    if group == 'iso':
                        return find_cali_iso_exer(muscle)


def search_light_lvl_list(muscle, group):
    for x in program_lvl:
        if x in muscle:
            if program_lvl == program_lvl3 or program_lvl4:
                if x in cable_exer_list:
                    if group == 'comp':
                        return find_cable_comp_exer(muscle)
                    if group == 'iso':
                        return find_cable_iso_exer(muscle)
                elif x in calisthenic_exer_list:
                    if group == 'comp':
                        return find_cali_comp_exer(muscle)
                    if group == 'iso':
                        return find_cali_iso_exer(muscle)
            if program_lvl == program_lvl1 or program_lvl2:
                if x in mach_exer_list:
                    if group == 'comp':
                        return find_mach_comp_exer(muscle)
                    if group == 'iso':
                        return find_mach_iso_exer(muscle)
                elif x in calisthenic_exer_list:
                    if group == 'comp':
                        return find_cali_comp_exer(muscle)
                    if group == 'iso':
                        return find_cali_iso_exer(muscle)







# def layout_style1():
#     exercises = []
#     comp_light = round(amount_exer * .25)
#     iso_light = round(amount_exer * .25)
#     comp_heavy = round(amount_exer * .25)
#     iso_heavy = round(amount_exer * .25)


def push_light_to_heavy():
    exercises = []
    for x in program_lvl:
        if x in push:
            exercises.extend([x])
    for z in exercises:
        if z in bb_exer_list:
            a = 1
            break
        elif z in db_exer_list:
            a = 2
            break
        elif z in cable_exer_list:
            a = 3
            break
        elif z in mach_exer_list:
            a = 4
            break
    if a == 1:
        # comp chest/tricep mach, iso chest/tricep cable, comp chest/tricep bb, iso chest/tricep db, xtra exercises go
        # cali
        exer_pick.extend([find_mach_comp_exer(chest)])
        exer_pick.extend([find_mach_iso_exer(triceps)])
        exer_pick.extend([find_cable_iso_exer(chest)])
        exer_pick.extend([find_cable_iso_exer(triceps)])
        exer_pick.extend([find_bb_comp_exer(chest)])
        exer_pick.extend([find_bb_iso_exer(triceps)])
        exer_pick.extend([find_db_iso_exer(chest)])
        exer_pick.extend([find_db_iso_exer(triceps)])

        while len(exer_pick) < num_exer_needed():
            en = num_exer_needed() - len(exer_pick)
            if en >= 4:
                exer_pick.extend([find_db_comp_exer(chest)])
                exer_pick.extend([find_db_iso_exer(triceps)])
            en = num_exer_needed() - len(exer_pick)
            if en >= 3:
                exer_pick.extend([find_cable_comp_exer(chest)])
                exer_pick.extend([find_cable_iso_exer(triceps)])
            en = num_exer_needed() - len(exer_pick)
            if en >= 2:
                exer_pick.extend([find_cali_comp_exer(chest)])
                exer_pick.extend([find_cali_comp_exer(triceps)])
            en = num_exer_needed() - len(exer_pick)
            if en >= 1:
                exer_pick.extend([find_cali_comp_exer(chest)])


def equipment_to_use():
    print('What are we using today?')
    bb = input('Barbells: ')
    db = input('Dumbbells: ')
    cable = input('Cables: ')
    mach = input('Machines: ')
    cali = input('Calisthenics: ')
    band = input('Bands: ')
    return bb, db, cable, mach, cali, band


def equipment_checker(equipment):
    z = 0
    if equipment is bb:
        if bb == 'yes':
            for x in program_lvl:
                if x in bb_exer_list:
                    z += 1
            if z == 0:
                print("BB equipment is more advanced than your level!")
                y = input('Do you want to up the level for some exercises to still use this equipment?: ')
                if y == 'yes':
                    binput = 'add'
                    return binput
                elif y == 'no':
                    binput = 'stay'
                    return binput
            else:
                return 'stay'
        elif bb == 'no':
            for x in program_lvl:
                if x in bb_exer_list:
                    z += 1
            if z > 0:
                print("BB equipment is in your level!")
                y = input('Do you still want to avoid this equipment?: ')
                if y == 'yes':
                    binput = 'remove'
                    return binput
                elif y == 'no':
                    binput = 'stay'
                    return binput
            else:
                return 'stay'
    if equipment is db:
        if db == 'yes':
            for x in program_lvl:
                if x in db_exer_list:
                    z += 1
            if z == 0:
                print("DB equipment is more advanced than your level!")
                y = input('Do you want to up the level for some exercises to still use this equipment?: ')
                if y == 'yes':
                    dinput = 'add'
                    return dinput
                elif y == 'no':
                    dinput = 'stay'
                    return dinput
            else:
                return 'stay'
        elif db == 'no':
            for x in program_lvl:
                if x in db_exer_list:
                    z += 1
            if z > 0:
                print("DB equipment is in your level!")
                y = input('Do you still want to avoid this equipment?: ')
                if y == 'yes':
                    dinput = 'remove'
                    return dinput
                elif y == 'no':
                    dinput = 'stay'
                    return dinput
            else:
                return 'stay'
    if equipment is cable:
        if cable == 'yes':
            for x in program_lvl:
                if x in cable_exer_list:
                    z += 1
            if z == 0:
                print("Cable equipment is more advanced than your level!")
                y = input('Do you want to up the level for some exercises to still use this equipment?: ')
                if y == 'yes':
                    cinput = 'add'
                    return cinput
                elif y == 'no':
                    cinput = 'stay'
                    return cinput
            else:
                return 'stay'
        elif cable == 'no':
            for x in program_lvl:
                if x in cable_exer_list:
                    z += 1
            if z > 0:
                print("Cable equipment is in your level!")
                y = input('Do you still want to avoid this equipment?: ')
                if y == 'yes':
                    cinput = 'remove'
                    return cinput
                elif y == 'no':
                    cinput = 'stay'
                    return cinput
            else:
                return 'stay'
    if equipment is mach:
        if mach == 'yes':
            for x in program_lvl:
                if x in mach_exer_list:
                    z += 1
            if z == 0:
                print("Machine equipment is more advanced than your level!")
                y = input('Do you want to up the level for some exercises to still use this equipment?: ')
                if y == 'yes':
                    minput = 'add'
                    return minput
                elif y == 'no':
                    minput = 'stay'
                    return minput
            else:
                return 'stay'
        elif mach == 'no':
            for x in program_lvl:
                if x in mach_exer_list:
                    z += 1
            if z > 0:
                print("Machine equipment is in your level!")
                y = input('Do you still want to avoid this equipment?: ')
                if y == 'yes':
                    minput = 'remove'
                    return minput
                elif y == 'no':
                    minput = 'stay'
                    return minput
            else:
                return 'stay'
    if equipment is cali:
        if cali == 'yes':
            for x in program_lvl:
                if x in calisthenic_exer_list:
                    z += 1
            if z == 0:
                print("Calisthenics is more advanced than your level!")
                y = input('Do you want to up the level for some exercises to still use this equipment?: ')
                if y == 'yes':
                    cainput = 'add'
                    return cainput
                elif y == 'no':
                    cainput = 'stay'
                    return cainput
            else:
                return 'stay'
        elif cali == 'no':
            for x in program_lvl:
                if x in calisthenic_exer_list:
                    z += 1
            if z > 0:
                print("Calisthenics is in your level!")
                y = input('Do you still want to avoid this equipment?: ')
                if y == 'yes':
                    cainput = 'remove'
                    return cainput
                elif y == 'no':
                    cainput = 'stay'
                    return cainput
            else:
                return 'stay'
    if equipment is band:
        if band == 'yes':
            for x in program_lvl:
                if x in band_exer_list:
                    z += 1
            if z == 0:
                print("Band equipment is more advanced than your level!")
                y = input('Do you want to up the level for some exercises to still use this equipment?: ')
                if y == 'yes':
                    bainput = 'add'
                    return bainput
                elif y == 'no':
                    bainput = 'stay'
                    return bainput
            else:
                return 'stay'
        elif band == 'no':
            for x in program_lvl:
                if x in band_exer_list:
                    z += 1
            if z > 0:
                print("Band equipment is in your level!")
                y = input('Do you still want to avoid this equipment?: ')
                if y == 'yes':
                    bainput = 'remove'
                    return bainput
                elif y == 'no':
                    bainput = 'stay'
                    return bainput
            else:
                return 'stay'

print(program_lvl)
bb, db, cable, mach, cali, band = equipment_to_use()

bb_input = equipment_checker(bb)
db_input = equipment_checker(db)
cable_input = equipment_checker(cable)
mach_input = equipment_checker(mach)
cali_input = equipment_checker(cali)
band_input = equipment_checker(band)

def upper_body_workout():









#exer_pick
#   layout_style - set to preferred style
#   program_lvl - based off experience
#   tempo - based off goal
#   amount_reps - based off goal
#   weight - inconsistent base and will change to fix intensity
#   amount_sets - based off goal

#def - how many exercises do we need
#   def - based off amount of comp/iso movements preferred, set number of  comp/iso needed
#       def - BB, DB, Cable, machine, workout order
#           def - layout_style sets the order of which the random.choice will select the movements needed
#def - program_lvl and todays_target examined
#   def - random.choice according to the movement type

# def layout_style1():
