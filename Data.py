import math

data = { 
    "id": "1", "name": "first",
    "metadata": {
        "system": { "size": 10.7  },
        "user": { "batch": 10 }
    }
}

class Data:
    def __new__(cls, *args, **kwargs):
        # print("1. Create a new instance of Data.")
        return super().__new__(cls)
 
    def __init__(self):
        pass
        # print("2. Initialize the new instance of Data.")

    def __init__(self, name):
        # print("2. Initialize the new instance of Data.")
        self.name = name


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
        for x in cls.get_all_keys(cls, data):
            pass

        for k, v in cls.inLineDict.items():
            setattr(cls, k, v)
   
        # locals().update(cls.inLineDict)
        # print(str(cls.size))
        # print(str(cls.inLineDict))
        # for x in cls.get_all_keys(cls, data):
        #     print(x)
            
        # new_dict = cls()  # equivalent to `dict()`: creates a new dictionary instance
        # for key in data:
        #     print(str(key))
        
        return cls

    def to_dict(self):
        ...
  

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