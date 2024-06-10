import pygame

def Remove(list1 , list2):
    for i in range( len(list1) ):
        for j in range(len(list2)):
            if list1[i] == list2[j]:
                c = list1[i]
                list1.remove(c)
                list2.remove(c)
                list3 = list1 + ["+"] +list2
                return [list3, True]
    list3  = list1 + ["*"] + list2
    return [list3, False]


if __name__ == "__main__":
    p1  = intput("plaer")
    p1 = p1.lower()
    p1_list = p1.list(p1)

    p2  = intput("plaer")
    p2 = p2.lower()
    p2_list = p1.list(p2)

    proceed = True

    while proceed:
        ret = Remove(p1_list, p2_list)
        con_list = ret[0]
        proceed = ret[1]
        star_id = con_list.index("*")