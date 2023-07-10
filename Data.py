
data = { 
    "id": "1", "name": "first",
    "metadata": {
        "system": { "size": 10.7  },
        "user": { "batch": 10 }
    }
}

class Data:
    id, name = "", ""

    def get_all_keys(self, d):
        for key, value in d.items():
            yield key
            if isinstance(value, dict):
                yield from self.get_all_keys(self, value)

    @classmethod
    def from_dict( cls, data):
        
        for x in cls.get_all_keys(cls, data):
            print(x)
            
        new_dict = cls()  # equivalent to `dict()`: creates a new dictionary instance
        for key in data:
            print(str(key))
        
        return new_dict

    def to_dict(self):
        ...
  

# load from dict
my_inst_1 = Data.from_dict(data)
print(str(my_inst_1))

# load from inputs
my_inst_2 = Data(name="my")

# reflect inner value
print(my_inst_1.size)  # should print 10

# default values
print(my_inst_1.height)  # should set a default value of 100 in metadata.system.height
print(my_inst_1.to_dict()['metadata']['system']['height'])  # should print the default value

# autocomplete - should complete to metadata
data.me