import math
import sys
from heapq import heapify, heappush, heappop

m ={0: [0.7798606835438107, 0.6922727646627362],
 1: [0.7647837074641568, 0.3252670836724646],
 2: [0.7155217893995438, 0.20026498027300055],
 3: [0.7076566826610747, 0.3278339270610988],
 4: [0.8325506249953353, 0.02310946309985762],
 5: [0.49016747075266875, 0.5464878695400415],
 6: [0.8820353070895344, 0.6791919587749445],
 7: [0.46247219371675075, 0.6258061621642713],
 8: [0.11622158839385677, 0.11236327488812581],
 9: [0.1285377678230034, 0.3285840695698353]}

m2= [[7, 6, 5],
 [4, 3, 2],
 [4, 3, 1],
 [5, 4, 1, 2],
 [1, 2, 3],
 [7, 0, 3],
 [0],
 [0, 5],
 [9],
 [8]]

def estimate_function(from_point,to_point):
    ab = from_point[0]- to_point[0]
    ac = from_point[1]- to_point[1]
    bc = math.sqrt(math.pow(ab,2)+math.pow(ac,2))
    return bc


class Point:
    
    def __init__(self,number,x,y,next,h) :
        self.number=number
        self.X= x
        self.Y=y
        self.H=h
        self.previous_point=None
        self.path_cost= sys.maxsize
        self.next=next
        
    def __lt__(self, other):
        return self.path_cost+self.H < other.path_cost+other.H
        
        
    def __str__(self):
        return 'Number:{} , next: {}, total : {}'.format(self.number,self.next,self.path_cost+self.H)

start=0
goal= 4
estimated= dict()
for p in m:
    h = estimate_function(m[p],m[goal])
    point = Point(p,m[p][0],m[p][1],m2[p],h)
    estimated[p]=point
    
visited=[]
waiting_to_visit = []
heapify(waiting_to_visit)
start_point=estimated[start]
start_point.path_cost=0
heappush(waiting_to_visit,start_point)
while len(waiting_to_visit)>0:
    print("=====================")
    current = heappop(waiting_to_visit)
    for vi in visited:
        print("visited:",vi)
    print("Current :",current)
    if current.number==goal:
        print("ting tang tung")
        break
    for next in current.next:
        if estimated[next] in visited:
            continue
        point_next= estimated[next]
        point_next.path_cost= current.path_cost+ estimate_function([current.X,current.Y],[point_next.X,point_next.Y])
        point_next.previous_point= current
        heappush(waiting_to_visit,point_next)
    visited.append(current)

