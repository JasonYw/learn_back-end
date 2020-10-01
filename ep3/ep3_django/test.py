from getpass import getuser
from utils import sqlhelper


target = teacher_list =sqlhelper.get_list('''
            SELECT  l.id,t.id teacher_id,t.name,c.id class_id,c.title FROM teacher t
            LEFT JOIN link_t_C l ON t.id =l.teacher_id
            LEFT JOIN class c ON l.class_id =c.id;''',[]
        )
print(target)
dict_ ={}
for key in target:
    if dict_.get(key[1]) ==None:
        dict_[key[1]] ={
            'name':key[2],
            'titles':[key[4],],
            'teacher_id':key[1]
        }
    else:
        dict_[key[1]]['titles'].append(key[4])
print(dict_)
