import json, os, tempfile


temp = tempfile.TemporaryFile('w+t')


def to_json(func):
    def wrapper():
        json.dump(func(), temp)
    return wrapper


@to_json
def get_data():
    return {'data1': (42, 34), 'data2': (44, 22)}


get_data()
temp.seek(0)
print(json.load(temp))
temp.close()


