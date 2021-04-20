import csv
import json
import os
from itertools import  tee
from functools import wraps

      
       
class tools:
    
    @staticmethod
    def write_csv(name,header_name):
        def _outer_wrapper(func):
            @wraps(func)
            def _wrapper(*args,**kwargs):
                try:
                    os.mkdir('output_csv')
                except:
                    pass
                s_no=1
                file=open(f'./output_csv/{name}.csv','w')
                csv_w=csv.writer(file, lineterminator='\n')
                csv_w.writerow(list(header_name))
                gen = func(*args,**kwargs)
                for i in gen:
                    csv_w.writerow(i)
                return 
            return _wrapper
        return _outer_wrapper
        
    @staticmethod
    def write_json(name,key):
        def _outer_wrapper(func):
            @wraps(func)
            def _wrapper(*args,**kwargs):
                try:
                    os.mkdir('output_json')
                except:
                    pass
                gen1,gen = tee(func(*args,**kwargs))
                js ={name:[]}
                value =[z for z in gen ]
                for x in value:
                    temp={}
                    for x,y in zip(key,x):
                        temp[str(x)]=y
                    js[name].append(temp)
                js= json.dumps(js)
                with open(f'./output_json/{name}.json','w') as f:
                    f.write(js)
                return gen1
            return _wrapper
        return _outer_wrapper
        

