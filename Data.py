import math

data = { 
    "id": "1", "name": "first",
    "metadata": {
        "system": { "size": 10.7  },
        "user": { "batch": 10 }
    }
}
import functools
class Data:
    def __new__(cls, *args, **kwargs): 
        return super().__new__(cls)
    def __init__(self):
        pass 
    def __init__(self, name): 
        self.name = name

    @classmethod
    @property
    def height(self): 
        self.main_data['metadata']['system']['height']=100
        return self.main_data['metadata']['system']['height']

    main_data = None
    inLineDict = {}

    def get_all_keys(self, d):
        for key, value in d.items():
            yield key
            if isinstance(value, dict):
                yield from self.get_all_keys(self, value)
            else:
                self.inLineDict[key] = math.floor(value) if isinstance(value, float) else value

    @classmethod
    def from_dict( cls, data):
        cls.main_data = data
        for x in cls.get_all_keys(cls, data):
            pass
        
        for k, v in cls.inLineDict.items():
            setattr(cls, k, v)

        return cls

    @classmethod
    def to_dict(cls):
        return cls.main_data
  

# load from dict
my_inst_1 = Data.from_dict(data)

# load from inputs
my_inst_2 = Data(name="my")

# reflect inner value
print(my_inst_1.size)  # should print 10

# default values
print(my_inst_1.height)  # should set a default value of 100 in metadata.system.height
print(my_inst_1.to_dict()['metadata']['system']['height'])  # should print the default value

# autocomplete - should complete to metadata
data.me