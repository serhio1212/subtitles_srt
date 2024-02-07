import os
import colorama



def readData(InFile):
    time_arr = []
    text_arr = []
    count = 0

    f = open(InFile)
    for line in f:
        count = count + 1
        if count > 4:
            count = 1
        if count == 2:
            tmp_time_val = line.strip()
            # print (f'Time tmp {tmp_time_val}')
            time_arr.append(tmp_time_val.split(" "))
        if count == 3:
            tmp_text_val = line.strip()
            # print (f'Text tmp {tmp_text_val}')
            text_arr.append(tmp_text_val)
        # print (f'All array {time_arr}')
        # print (f'All array {text_arr}')
    #print (f'Length array {len(time_arr)}')
    #print (f'Length array {len(text_arr)}')
    f.close
    return time_arr, text_arr

def CorrectData(time_arr, text_arr):
    correct_time_arr = []
    correct_text_arr = []
    tmp_string = ""
    buffer_item = ""
    buffer_count = 0
    first = 0
    for count, item in enumerate(text_arr, start=0):
        # print (f'Length array {count}, {item}')
        buffer_item = buffer_item+ " " + item
        if len(buffer_item) > 100:
            correct_text_arr.append(buffer_item)
            if first !=0:
                correct_time_arr.append([time_arr[count-buffer_count][2], "-->", time_arr[count][2]])
            else:
                correct_time_arr.append([time_arr[count-buffer_count][0], "-->", time_arr[count][2]])
                first+=1
            buffer_count =0
            buffer_item = ""
        buffer_count = buffer_count + 1
    correct_text_arr.append(buffer_item)
    correct_time_arr.append([time_arr[count-buffer_count+1][2], "-->", time_arr[count][2]])
    # print (f'Correct array {correct_time_arr}')
    # print (f'Correct array {correct_text_arr}')
    return correct_time_arr, correct_text_arr

def OutFile(correct_time_arr, correct_text_arr, InFile):
    name_file = os.path.basename(InFile)
    dir_path = os.path.dirname(InFile)
    name_file_no_ext = name_file[slice(0,-3)]
    # print (f'Name of file {name_file}')
    # print (f'Name of file {name_file[slice(0,-3)]}')
    one_string_path = f'{dir_path}/{name_file_no_ext}convert.srt'
    print (one_string_path)
    f_rezult = open (one_string_path, "w")

    buffer_count_2  = 0
    number_count = 1

    for count_rez, item_rez in enumerate(correct_text_arr, start=0):
        # print (f'Correct array {count_rez}, {item_rez}')
        f_rezult.write (str(number_count)+"\n")
        f_rezult.write (correct_time_arr[count_rez][0] + " "+  correct_time_arr[count_rez][1] + " " + correct_time_arr[count_rez][2] +"\n" )
        f_rezult.write (correct_text_arr[count_rez]+"\n")
        f_rezult.write ("\n")
        if buffer_count_2 >= 3:
            buffer_count_2 = 0
        buffer_count_2 = buffer_count_2 + 1
        number_count+=1
    f_rezult.close

def main():
    path = os.getcwd()
    print(path)
    path = os.path.dirname(__file__)
    InFileInput = input ("Path to file or name file in directory with script: ")
    if os.path.isfile(f'{path}/{InFileInput}'):
        InFile = f'{path}/{InFileInput}'
    else:
        InFile = InFileInput
    print ("main", InFile)
    array_obj = readData(InFile)
    correct_array_obj = CorrectData(array_obj[0], array_obj[1])
    OutFile(correct_array_obj[0], correct_array_obj[1], InFile)

main()
