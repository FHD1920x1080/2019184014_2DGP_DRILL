

objects = [[],[],[]]

def all_objects():
    for layer in objects:
        for o in layer:
            yield o

def add_object(o, depth = 0):
    objects[depth].append(o)

def add_objects(ol, depth = 0):# 객체 여러개(리스트인채로) 추가
    objects[depth] += ol

def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    print('없')