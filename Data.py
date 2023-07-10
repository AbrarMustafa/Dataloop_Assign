
data = { 
    "id": "1", "name": "first",
    "metadata": {
        "system": { "size": 10.7  },
        "user": { "batch": 10 }
    }
}

class Data:
    @classmethod
    def from_dict(cls, data):
        # return cls
        new_dict = cls()  # equivalent to `dict()`: creates a new dictionary instance
        for key in data:
            print(str(key))
            # new_dict[key] = 1
        return new_dict

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