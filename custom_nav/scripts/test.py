# def wall(d1,d2,d3):
#     grid_paths = {
#         (0, 0): {
#             (1, 0): 1,(0, 1): 1
#         },
#         (0, 1): {
#             (0, 0): 1,(1, 1): 0,(0, 2): 1
#         },
#         (0, 2): {
#             (0, 1): 1,(1, 2): 1 ,(0, 3): 1
#         },
#         (0, 3): {
#             (0, 2): 1,(1, 3): 1 ,(0, 4): 1
#         },
#         (0, 4): {
#             (0, 3): 1,(1, 4): 1 ,(0, 5): 1
#         },
#         (0, 5): {
#             (0, 4): 1,(1, 5): 1
#         },
#         (1, 0): {
#             (0, 0): 1,(1, 1): 1,(2, 0): 0
#         },
#         (1, 1): {
#             (1, 0): 1,(1, 2): 0,(0, 1): 0,(2, 1): 1
#         },
#         (1, 2): {
#             (1, 1): 0,(1, 3): 0,(0, 2): 1,(2, 2): 1
#         },
#         (1, 3): {
#             (1, 2): 0,(1, 4): 1,(0, 3): 1,(2, 3): 1
#         },
#         (1, 4): {
#             (1, 3): 1,(1, 5): 0,(0, 4): 1,(2, 4): 0
#         },
#         (1, 5): {
#             (1, 4): 0,(0, 5): 1,(2, 5): 1
#         },
#         (2, 0): {
#             (2, 1): 1,(1, 0): 0,(3, 0): 1
#         },
#         (2, 1): {
#             (2, 0): 1,(2, 2): 1,(1, 1): 1,(3, 1): 0
#         },
#         (2, 2): {
#             (2, 1): 1,(2, 3): 1,(1, 2): 1,(3, 2): 0
#         },
#         (2, 3): {
#             (2, 2): 1,(2, 4): 1,(1, 3): 1,(3, 3): 1
#         },
#         (2, 4): {
#             (2, 3): 1,(2, 5): 1,(1, 4): 0,(3, 4): 1
#         },
#         (2, 5): {
#             (2, 4): 1,(1, 5): 1,(3, 5): 1
#         },
#         (3, 0): {
#             (3, 1): 1,(2, 0): 1,(4, 0): 1
#         },
#         (3, 1): {
#             (3, 0): 1,(3, 2): 1,(2, 1): 0,(4, 1): 1
#         },
#         (3, 2): {
#             (3, 1): 1,(3, 3): 1,(2, 2): 0,(4, 2): 1
#         },
#         (3, 3): {
#             (3, 2): 1,(3, 4): 0,(2, 3): 1,(4, 3): 0
#         },
#         (3, 4): {
#             (3, 3): 0,(3, 5): 1,(2, 4): 1,(4, 4): 0
#         },
#         (3, 5): {
#             (3, 4): 1,(2, 5): 1,(4, 5): 1
#         },
#         (4, 0): {
#             (4, 1): 0,(3, 0): 1,(5, 0): 1
#         },
#         (4, 1): {
#             (4, 0): 0,(4, 2): 1,(3, 1): 1,(5, 1): 0
#         },
#         (4, 2): {
#             (4, 1): 1,(4, 3): 1,(3, 2): 1,(5, 2): 0
#         },
#         (4, 3): {
#             (4, 2): 1,(4, 4): 1,(3, 3): 0,(5, 3): 1
#         },
#         (4, 4): {
#             (4, 3): 1,(4, 5): 0,(3, 4): 0,(5, 4): 1
#         },
#         (4, 5): {
#             (4, 4): 0,(3, 5): 1,(5, 5): 1
#         },
#         (5, 0): {
#             (4, 0): 1,(5, 1): 1
#         },
#         (5, 1): {
#             (5, 0): 1,(4, 1): 0,(5, 2): 1
#         },
#         (5, 2): {
#             (5, 1): 1,(4, 2): 0 ,(5, 3): 1
#         },
#         (5, 3): {
#             (5, 2): 1,(4, 3): 1 ,(5, 4): 0
#         },
#         (5, 4): {
#             (5, 3): 0,(4, 4): 1 ,(5, 5): 1
#         },
#         (5, 5): {
#             (5, 4): 1,(4, 5): 1
#         }
#     }
#     return grid_paths
# w = wall(1,1,1)
# def possible_path(start,end,wall):
#     allpath = []
#     unfinishpath = [[[start[0],start[1]]]]
#     z = 1
#     leastpathn = 100000
#     while 1:
#         # print('unfinishpath',unfinishpath)
#         for path in unfinishpath:
#             # print('path',path)
#             if len(path)> leastpathn:
#                 unfinishpath.remove(path)
#             else:
#                 pathend = path[len(path)-1] #[0,0]
#                 # print('pathend',pathend)
#                 if pathend != end:
#                     availablepath = []
#                     if pathend[0]>=1:
#                         availablepath.append([pathend[0]-1,pathend[1]])
#                     if pathend[0] <=4:
#                         availablepath.append([pathend[0]+1,pathend[1]])
#                     if pathend[1]>=1:
#                         availablepath.append([pathend[0],pathend[1]-1])
#                     if pathend[1] <=4:
#                         availablepath.append([pathend[0],pathend[1]+1])
#                     # print(path,'ava',availablepath)
#                     check = 0
#                     check2 = len(availablepath)
#                     for i in availablepath:
#                         # print('i',i)
#                         if (i not in path) and wall[(pathend[0],pathend[1])][(i[0],i[1])]:
#                             temp = path.copy()
#                             # print('temp',temp)
#                             temp.append(i)
#                             unfinishpath.append(temp)
#                             if path in unfinishpath:
#                                 # print('path tho remove',path)
#                                 check = 1
#                                 # print('remove',unfinishpath)
#                         else:
#                             check2 -= 1
#                     if(check2 == 0):
#                         unfinishpath.remove(path)
#                     if check:
#                         # print('unfinishpath',unfinishpath)
#                         unfinishpath.remove(path)
#                         # print('unfinishpath after remove',unfinishpath)
#                 else:
#                     leastpathn = len(path)
#                     allpath.append(path)
#                     unfinishpath.remove(path)       
#                 # print('unfinishpath',unfinishpath)
#                 # print("*"*100)
#         if len(unfinishpath) == 0:
#             break
#         # print(allpath)
#         # print("___________")
#         # print(unfinishpath)
#         # print("****************")
#     return allpath
# # path = possible_path([0,0],[5,5],w)
# # for item in path:
# #     print(len(item))
# # print(path)
from random import sample, randint
# random_numbers = sample(range(4), 2)
# while 1:
#     finish = 0
#     for x in random_numbers:
#         count = 0
#         for y in random_numbers:
#             if x == y:
#                 count+=1
#         if count >1:
#             finish+=1
#             x = randint(0,3)
#     print(random_numbers)
#     print(finish)
#     if finish == 0:
#         break
# print(random_numbers)
# repeat = 2
# door = []
# check = 0
# if not check:
#     for i in range(repeat):
#         while True:
#             rand = randint(0,3)
#             if rand not in door:
#                 door.append(rand)
#                 break

# print(door)
escapedoorindex = [[0,0],[3,0],[5,3],[2,5]]
# a = [0,0,1,0]
# import math
# print('ASDASD'+str(a))
# print(int(0.3))
# try:
#     asdfasdf
# except:
#     print('error')
# ed = [0,0,1,1]
# indices = [i for i, x in enumerate(ed) if x == 1]
# print(indices)
# for item in indices:
#     if item in escapedoorindex:
#         print (item)

escapedoorindex = [[0,0],[3,0],[5,3],[2,5]]
indices = [i for i, x in enumerate([0,1,0,1]) if x == 1]
ed = []
for i in indices:
    ed.append(escapedoorindex[i])
print(ed)
# print(enumerate([0,1,0,1]))