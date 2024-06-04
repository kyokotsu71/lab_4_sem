import itertools

#функция для генерации всех комбинаций как можно разложить обЪекты по ящикам
def generate_combinations(objects, boxes):
    combinations = list(itertools.combinations(objects.keys(), boxes))
    return combinations

#заполнение ящиков
def box_filling(objects, boxes, max_weight_in_box):
    result = -1

    for _ in generate_combinations(objects, boxes):
        # распределение объектов по ящикам равномерно
        boxes_contents = [[] for _ in range(boxes)]
        for i, obj in enumerate(objects):
            boxes_contents[i % boxes].append(obj)

        # проверка превышения веса
        if all([sum([objects[obj] for obj in box]) <= max_weight_in_box for box in boxes_contents]):
            result = boxes_contents
            break
    return result


result = -1
boxes = 2
max_weight_in_box = 0.9

objects = {'item1': 0.5, 'item2': 0.3, 'item3': 0.4, 'item4': 0.6}

while box_filling(objects, boxes, max_weight_in_box) == -1 and boxes <= len(objects):
    boxes += 1
    if box_filling(objects, boxes, max_weight_in_box) != -1:
        break
result = box_filling(objects, boxes, max_weight_in_box)

print(result)