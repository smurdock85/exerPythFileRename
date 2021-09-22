import os
#changing directory
os.chdir('/Users/shelby/Desktop/Biomedical Informatics/Fall 2021/NURS 6806/exerPythFileRename/Files/')
#iterating through each of the listed files in the directory ^
for f in os.listdir(): 
    #split based on the period 
    f_name, f_ext = os.path.splitext(f)
    #split text based on the dash
    f_title, f_course, f_num = f_name.split('-')

#removing spaces
    f_title = f_title.strip()
    f_course = f_course.strip()
    #make sure number is at least 2 characters long
    f_num = f_num.strip()[1:].zfill(2)
#format the name of the files 
    new_name = '{}-{}{}'.format(f_num, f_title, f_ext)
    #actually renaming the file 
    os.rename(f, new_name)
