import numpy as np
class DataFrame:
    def __init__(self, dictionary): #intializing the class
        self._col_names = dictionary.keys() 
        self._col_values = dictionary.values()
        self._items = dictionary
        
    def __setitem__(self, key, new_value):
        self._items[key] = new_value

    def __getitem__(self, key):
        return np.array(self._items[key])
    
    
    @property
    def col_values(self):
        return list(self._col_values)
    
    @property
    def ncols(self):
        return len(self._items)

    @property
    def sum(self):
        sum_collector = []
        columns = []
        for key in self._items:
            if self._items[key].dtype == "float64" or self._items[key].dtype == "int32":
                columns.append(key)
                sum_collector.append(sum(self._items[key]))
        print(columns)
        return sum_collector
