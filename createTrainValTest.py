import os

path_to_data = "data/shape_net_core_uniform_samples_2048"

split_train = .70
split_val   = .20
split_test  = .10

path_to_train = "data/shape_net_core_uniform_samples_2048/train.txt"
path_to_val   = "data/shape_net_core_uniform_samples_2048/val.txt"
path_to_test  = "data/shape_net_core_uniform_samples_2048/test.txt"

train_files = []
val_files   = []
test_files  = []

for subdir in os.listdir(path_to_data):

    num_shapes  = len(subdir)
    count_train = int(num_shapes*split_train)
    count_val   = int(num_shapes*split_val)
    count_test  = int(num_shapes*split_test)
    train = []
    val = []
    test = []
    
    if subdir[-3:] == 'txt':
        continue
    
    for file in os.listdir(os.path.join(path_to_data, subdir)):
        file = os.path.join(path_to_data, subdir, file) + '\n'
        if len(train) < count_train:
            train.append(file)
        elif len(val) < count_val:
            val.append(file)
        else:
            test.append(file)
            
    train_files.extend(train)
    val_files.extend(val)
    test_files.extend(test)
                      
with open(path_to_train, 'w') as train_file:
    train_file.writelines(train_files)
    
with open(path_to_val, 'w') as val_file:
    val_file.writelines(val_files)
    
with open(path_to_test, 'w') as test_file:
    test_file.writelines(test_files)