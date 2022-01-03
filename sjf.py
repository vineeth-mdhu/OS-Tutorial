import heapq #importing priority queue module

jobs=[[1,2,0],[0,8,1],[5,6,2],[3,4,3],[10,1,4],[4,1,5],[6,5,6]]  # list of processes to be scheduled of format [[arrival time,burst time, process id]...]
jobs.sort(key=lambda x:x[0])

class job:                                   # class job 
  def __init__(self,at,bt,id):
    self.id=id
    self.at=at
    self.bt=bt

  def __lt__(self,other):                   # redefining behaviour of < operator for job class objects
    return self.bt<other.bt
 
time=jobs[0][0]                             #arrival time of the first job that arrived
heap=[job(jobs[0][0],jobs[0][1],jobs[0][2])]  # pushing the first job to the heap
heapq.heapify(heap)     
i=0
j=1

print("id","at"," bt","  ct"," tat"," wt")

while i<len(jobs):
  curr=heapq.heappop(heap)  #pop the job with minimum burst time
  time+=curr.bt             #increment time by current job's burst time
  
  print(curr.id," ",curr.at," ",curr.bt," ",time," ",time-curr.at," ",time-curr.at-curr.bt)
  
  while(j<len(jobs) and jobs[j][0]<time): #checking for jobs that have arrived to push into the heap
    heapq.heappush(heap,job(jobs[j][0],jobs[j][1],jobs[j][2]))
    j+=1
    
  i+=1
