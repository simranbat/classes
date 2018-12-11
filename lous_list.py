# Simran Batra
# November 30, 2017
# Lou's List is a UVA resource to search through classes


import urllib.request


def instructors(department):
    link = "http://cs1110.cs.virginia.edu/files/louslist/" + str(department)
    stream = urllib.request.urlopen(link)
    list_of_instructors = []
    for line in stream:
        entry = line.decode("UTF-8").strip().split("|")
        if "+" in entry[4]:
            entry[4] = entry[4][0:len(entry[4])-2]
        list_of_instructors.append(entry[4])
    list_of_instructors = set(list_of_instructors)
    list_of_instructors = list(list_of_instructors)
    return sorted(list_of_instructors)


def class_search(dept_name, has_seats_available=True, level=None, not_before=None, not_after=None):
    link = "http://cs1110.cs.virginia.edu/files/louslist/" + str(dept_name)
    stream = urllib.request.urlopen(link)
    available_classes = []
    available_classes2 = []
    available_classes3 = []
    available_classes4 = []
    available_classes5 = []
    intersection = []
    a = 0
    b = 0
    c = 0
    d = 0
    for line in stream:
        entry = line.decode("UTF-8").strip().split("|")
        available_classes.append(entry)
        if has_seats_available:
            a = 1
            if entry[15] < entry[16]:
                available_classes2.append(entry)
        if level != None:
            level = str(level)
            b = 1
            if entry[1][0] == level[0]:
                available_classes3.append(entry)
        if not_before != None:
            not_before = str(not_before)
            c = 1
            if int(not_before) <= int(entry[12]):
                available_classes4.append(entry)
        if not_after != None:
            not_after = str(not_after)
            d = 1
            if int(not_after) >= int(entry[12]):
                available_classes5.append(entry)
    if available_classes2 == [] and a == 0:
        available_classes2 = available_classes
    if available_classes3 == [] and b == 0:
        available_classes3 = available_classes
    if available_classes4 == [] and c == 0:
        available_classes4 = available_classes
    if available_classes5 == [] and d == 0:
        available_classes5 = available_classes
    for line in available_classes:
        if line in available_classes2:
            if line in available_classes3:
                if line in available_classes4:
                    if line in available_classes5:
                        intersection.append(line)
    return intersection
