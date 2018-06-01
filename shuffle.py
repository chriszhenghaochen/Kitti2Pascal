# create_train_test_txt.py  
# encoding:utf-8  
import pdb  
import glob  
import os  
import random  
import math  
  
def get_sample_value(txt_name, category_name):  
    label_path = './label_2/'  
    txt_path = label_path + txt_name+'.txt'  
    try:  
        with open(txt_path) as r_tdf:  
            if category_name in r_tdf.read():  
                return ' 1'  
            else:  
                return '-1'  
    except IOError as ioerr:  
        print('File error:'+str(ioerr))  
  
txt_list_path = glob.glob('./label_2/*.txt')  
txt_list = []  
  
for item in txt_list_path:  
    temp1,temp2 = os.path.splitext(os.path.basename(item))  
    txt_list.append(temp1)  
txt_list.sort()  
print(txt_list)  
  
# shuffle to 8:1:1
num_trainval = random.sample(txt_list, int(math.floor(len(txt_list)*9/10.0)))
num_trainval.sort()  
print(num_trainval)  
  
num_train = random.sample(num_trainval, int(math.floor(len(num_trainval)*8/9.0)))
num_train.sort()  
print(num_train)
  
num_val = list(set(num_trainval).difference(set(num_train)))  
num_val.sort()  
print(num_val)  
  
num_test = list(set(txt_list).difference(set(num_trainval)))  
num_test.sort()  
print(num_test)  
  
# pdb.set_trace()  
  
Main_path = './ImageSets/Main/'  
train_test_name = ['trainval','train','val','test']  
category_name = ['Person']  
  
# make trainvl train val test  
for item_train_test_name in train_test_name:  
    list_name = 'num_'  
    list_name += item_train_test_name  
    train_test_txt_name = Main_path + item_train_test_name + '.txt'   
    try:  
        with open(train_test_txt_name, 'w') as w_tdf:  
            for item in eval(list_name):  
                w_tdf.write(item+'\n')  
        for item_category_name in category_name:  
            category_txt_name = Main_path + item_category_name + '_' + item_train_test_name + '.txt'  
            with open(category_txt_name, 'w') as w_tdf:  
                for item in eval(list_name):  
                    w_tdf.write(item+' '+ get_sample_value(item, item_category_name)+'\n')  
    except IOError as ioerr:  
        print('File error:'+str(ioerr))