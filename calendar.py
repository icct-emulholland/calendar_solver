import numpy as np
from random import shuffle
import copy
import sys
from collections import deque
from random import random
import pandas as pd
import os.path


calandar = np.array([[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,1,1,1]])

date_calandar = np.array([["jan","feb","mar","apr","may","jun","na"],["jul","aug","sept","oct","nov","dec","na"],[1,2,3,4,5,6,7],[8,9,10,11,12,13,14],[15,16,17,18,19,20,21],[22,23,24,25,26,27,28],[29,30,31,"na","na","na","na"]])

todays_month = "apr"
todays_day = '12'

results_df = pd.DataFrame(columns = ['month','day','answer'])
for df_month in ["jan","feb","mar","apr","may","jun","jul","aug","sept","oct","nov","dec"]:
    for df_day in range(1,32):
        results_df = results_df.append({'month':df_month,'day':df_day}, ignore_index = True)

save_to_file_loc = #where to save the results file

#if the file has run already, and some stored solutions are there, this loads those solutions.
if os.path.isfile(save_to_file_loc):
    results_df = pd.read_csv(save_to_file_loc, usecols = ['month','day','answer'])

# =============================================================================
# p1: ###
#     ##   
# =============================================================================

p1_1 = [[1,1,1],[1,1,0]]
p1_2 = [[1,0],[1,1],[1,1]]
p1_3 = [[0,1,1],[1,1,1]]
p1_4 = [[1,1],[1,1],[0,1]]
p1_5 = [[0,1],[1,1],[1,1]]
p1_6 = [[1,1,1],[0,1,1]]
p1_7 = [[1,1],[1,1],[1,0]]
p1_8 = [[1,1,0],[1,1,1]]

# =============================================================================
# p2:   ##
#     ###   
# =============================================================================

p2_1 = [[0,0,1,1],[1,1,1,0]]
p2_2 = [[1,0],[1,1],[0,1],[0,1]]
p2_3 = [[0,1,1,1],[1,1,0,0]]
p2_4 = [[1,0],[1,0],[1,1],[0,1]]
p2_5 = [[1,1,0,0],[0,1,1,1]]
p2_6 = [[0,1],[0,1],[1,1],[1,0]]
p2_7 = [[1,1,1,0],[0,0,1,1]]
p2_8 = [[0,1],[1,1],[1,0],[1,0]]

# =============================================================================
# p3: ###
#     ###
# =============================================================================

p3_1 = [[1,1,1],[1,1,1]]
p3_2 = [[1,1],[1,1],[1,1]]

# =============================================================================
# p4: #
      #
      ###
# =============================================================================

p4_1 = [[1,0,0],[1,0,0],[1,1,1]]
p4_2 = [[0,0,1],[0,0,1],[1,1,1]]
p4_3 = [[1,1,1],[0,0,1],[0,0,1]]
p4_4 = [[1,1,1],[1,0,0],[1,0,0]]

# =============================================================================
# P5: # #
      ###
# =============================================================================

p5_1 = [[1,0,1],[1,1,1]]
p5_2 = [[1,1],[1,0],[1,1]]
p5_3 = [[1,1,1],[1,0,1]]
p5_4 = [[1,1],[0,1],[1,1]]

# =============================================================================
# p6: ##
       #
       ##
# =============================================================================

p6_1 = [[1,1,0],[0,1,0],[0,1,1]]
p6_2 = [[0,1,1],[0,1,0],[1,1,0]]
p6_3 = [[1,0,0],[1,1,1],[0,0,1]]
p6_4 = [[0,0,1],[1,1,1],[1,0,0]]

# =============================================================================
# p7:  # 
      ####    
# =============================================================================

p7_1 = [[0,1,0,0],[1,1,1,1]]
p7_2 = [[1,1,1,1],[0,0,1,0]]
p7_3 = [[0,0,1,0],[1,1,1,1]]
p7_4 = [[1,1,1,1],[0,1,0,0]]
p7_5 = [[0,1],[1,1],[0,1],[0,1]]
p7_6 = [[1,0],[1,0],[1,1],[1,0]]
p7_7 = [[0,1],[0,1],[1,1],[0,1]]
p7_8 = [[1,0],[1,1],[1,0],[1,0]]

# =============================================================================
# p8: ####
      #
# =============================================================================

p8_1 = [[1,1,1,1],[1,0,0,0]]
p8_2 = [[0,0,0,1],[1,1,1,1]]
p8_3 = [[1,0,0,0],[1,1,1,1]]
p8_4 = [[1,1,1,1],[0,0,0,1]]
p8_5 = [[0,1],[0,1],[0,1],[1,1]]
p8_6 = [[1,1],[1,0],[1,0],[1,0]]
p8_7 = [[1,1],[0,1],[0,1],[0,1]]
p8_8 = [[1,0],[1,0],[1,0],[1,1]]


# =============================================================================
# defining all iterations into lists
# =============================================================================

p1 = [p1_1,p1_2,p1_3,p1_4,p1_5,p1_6,p1_7,p1_8]
p2 = [p2_1,p2_2,p2_3,p2_4,p2_5,p2_6,p2_7,p2_8]
p3 = [p3_1,p3_2]
p4 = [p4_1,p4_2,p4_3,p4_4]
p5 = [p5_1,p5_2,p5_3,p5_4]
p6 = [p6_1,p6_2,p6_3,p6_4]
p7 = [p7_1,p7_2,p7_3,p7_4,p7_5,p7_6,p7_7,p7_8]
p8 = [p8_1,p8_2,p8_3,p8_4,p8_5,p8_6,p8_7,p8_8]
 
number_of_zeros = 48
# mon_day_check = 0
# while mon_day_check==0:
month = ""
day = ""
# while (number_of_zeros >2):
while (number_of_zeros >2)|(month!=todays_month)|(day!=todays_day):

    #while (number_of_zeros >2):
        # =============================================================================
        # randomize the order
        # =============================================================================    
        shuffle(p1)
        shuffle(p2)
        shuffle(p3)
        shuffle(p4)
        shuffle(p5)
        shuffle(p6)
        shuffle(p7)
        shuffle(p8)
        master_pieces = [p1,p2,p3,p4,p5,p6,p7,p8]   
        calandar = np.array([[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,1,1,1]])
        show_calander = np.array([[0,0,0,0,0,0,1],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,1,1,1]])
        trial_pieces = copy.deepcopy(master_pieces)
        shuffle(trial_pieces)
        pieces_laid=0
        pieces_index = []
        mon_day_check = 0
        
        xs_shift = int(6*random())
        ys_shift = int(6*random())
    
        xs = [0,1,2,3,4,5,6]
        ys = [0,1,2,3,4,5,6]
        xs = deque([0,1,2,3,4,5,6])
        xs.rotate(xs_shift)
        xs = list(xs)
        ys = deque([0,1,2,3,4,5,6])
        ys.rotate(ys_shift)
        ys = list(ys)    
        
        
        
        #shuffle(xs)
        #shuffle(ys)
        
        for y in xs:
            for x in ys:
                if pieces_laid<8:
                    i=1
                    n=0
                    all_pieces = copy.deepcopy(trial_pieces)
                    for pl in range(0,pieces_laid):
                        del all_pieces[pieces_index[pl]]
                    while (i == 1):
                        if len(np.unique([e for f in [c for d in [a for b in all_pieces for a in b] for c in d] for e in f], return_counts=True)[0])==0:
                            i=0
                            pieces_count = {x for l in all_pieces for x in l}
                            # all_pieces = copy.deepcopy(trial_pieces)
                            for pl in range(0,pieces_laid):
                                del all_pieces[pieces_index[pl]]
                        trial_set = all_pieces[n]
                        # print(trial_set)
                        trial_piece = trial_set[0]
                        height = len(trial_piece)
                        length = len(trial_piece[0])
                        if (y+length-1 >=7)|(x+height-1 >=7):
                            del trial_set[0]
                            if len(trial_set)==0:
                                n = n+1
                                if n >= len(all_pieces):
                                    i = 0
                        else:
                            check_date_warning = 0
                            check_calander = calandar.copy()
                            check_date_calandar = date_calandar.copy()
                            check_calander[x:(height+x),y:(length+y)] += trial_piece
                            def occ(my_list):
                                return([g for g, z in enumerate(my_list) if z == 1])
                            
                            indices = [occ(my_list) for my_list in trial_piece]
                            for row in range(0,len(indices)):
                                for location in indices[row]:                                
                                    check_date = str(check_date_calandar[row+x,location+y])
                                    if (check_date == todays_month)|(check_date == todays_day):
                                        check_date_warning=1
                            # if (len(np.unique(check_calander, return_counts=True)[0])>2)|(check_date_warning==1):
                            if (len(np.unique(check_calander, return_counts=True)[0])>2):
                                del trial_set[0]
                                if len(trial_set)==0:
                                    n = n+1
                                    if n >= len(all_pieces):
                                        i = 0
                            else:
                                calandar[x:(height+x),y:(length+y)] += trial_piece
                                show_calander[x:(height+x),y:(length+y)] += np.array(trial_piece)*(pieces_laid+1)
                                del all_pieces[0]
                                i=0
                                pieces_laid = pieces_laid+1
                                pieces_index.append(n)
                                number_of_zeros = np.unique(calandar, return_counts=True)[1][0]
                                
            if len(np.unique(calandar[0:2,0:7])) == 2:
                mon_day_check=1
        if number_of_zeros==2:
            
            def date_occ(my_list):
                return([g for g, z in enumerate(my_list) if z == 0])
            positions = [date_occ(my_list) for my_list in show_calander]
            date_row = 0
            new_positions = []
            for date_list in positions:
                if len(date_list) == 1:
                    new_position = [date_row,date_list[0]]
                    new_positions.append(new_position)
                if len(date_list) == 2:
                    new_positions = [[date_row,date_list[0]],[date_row,date_list[1]]]
                
                date_row = date_row +1
                
            month = date_calandar[new_positions[0][0],new_positions[0][1]]
            day = date_calandar[new_positions[1][0],new_positions[1][1]]
            if ((day.isdigit())&(not month.isdigit())):     
                mon_day = list(results_df['month'].astype(str)+results_df['day'].astype(str))
                results_df.iat[mon_day.index(month+day),2] = (show_calander).tolist()
                results_df.to_csv(save_to_file_loc)
                print(month," ",day)
    
        # show_calander

        
    




