from datetime import datetime

def chrono_decorator(function):
    def modified(*args,**kwargs):
        start = datetime.now()
        result = function(*args,**kwargs)
        stop = datetime.now()
        print("exec time :" + str(stop-start))
        return result
    return modified
