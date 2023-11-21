import json


class Person:
    def __init__(self, name, age, address, phone):
        self.name = name
        if age is not None:
            self.age = age
        if address is not None:
            self.address = address
        self.phone = phone


def convert_to_json(obj):
    # 将对象转换为字典形式
    obj_dict = obj.__dict__ if hasattr(obj, '__dict__') else obj

    # 将字典转换为JSON字符串，忽略空值(null)
    json_string = json.dumps(obj_dict, skipkeys=True)

    return json_string


# 示例对象
person = Person("John", None, None, "1234567890")

# 转换为JSON字符串，忽略空值(null)
json_string = convert_to_json(person)

print(json_string)
