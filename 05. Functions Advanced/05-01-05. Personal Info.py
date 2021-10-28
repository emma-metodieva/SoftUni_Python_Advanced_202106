# 05-01. Functions Advanced - Lab
# 05. Personal Info

def get_info(**kwargs):
    return f"This is {kwargs.get('name')} from {kwargs.get('town')} and he is {kwargs.get('age')} years old"


print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
