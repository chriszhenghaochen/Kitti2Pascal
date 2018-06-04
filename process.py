# coding=UTF-8  
import glob  
import string  
  
txt_list = glob.glob('./label_2/*.txt') # directory
def show_category(txt_list):  
    category_list= []  
    for item in txt_list:  
        try:  
            with open(item) as tdf:  
                for each_line in tdf:  
                    labeldata = each_line.strip().split(' ')
                    category_list.append(labeldata[0])
        except IOError as ioerr:  
            print('File error:'+str(ioerr))  
    print(set(category_list)) # 输出集合  
  
def merge(line):  
    each_line=''  
    for i in range(len(line)):  
        if i!= (len(line)-1):  
            each_line=each_line+line[i]+' '  
        else:  
            each_line=each_line+line[i]
    each_line=each_line+'\n'  
    return (each_line)  
  
print('before modify categories are:\n')  
show_category(txt_list)  
  
for item in txt_list:  
    new_txt=[]  
    try:  
        with open(item, 'r') as r_tdf:  
            for each_line in r_tdf:  
                labeldata = each_line.strip().split(' ')  
                if labeldata[0] in ['Truck','Van','Tram','Car']: #I don't need cat category
                    continue 
                if labeldata[0] in ['Person_sitting', 'Pedestrian', 'Cyclist', 'Person']: # only person is what I need
                    labeldata[0] = labeldata[0].replace(labeldata[0],'person')  
                if labeldata[0] == 'DontCare': # miss don't care 
                    continue  
                if labeldata[0] == 'Misc': #miss Misc
                    continue  
                new_txt.append(merge(labeldata)) 
        with open(item,'w+') as w_tdf:
            for temp in new_txt:  
                w_tdf.write(temp)  
    except IOError as ioerr:  
        print('File error:'+str(ioerr))  
  
print('\nafter modify categories are:\n')  
show_category(txt_list)  
