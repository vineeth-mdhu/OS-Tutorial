from queue import Queue

def pageFaults(pages, n, capacity):
    s = set() 
    indexes = Queue()  
    page_faults = 0
    print("ref-bit\t\thit/miss\tpage frames")
    for i in range(n):
        
        print(pages[i],end="\t\t")

        if (len(s) < capacity):
            if (pages[i] not in s):
                s.add(pages[i])
                page_faults += 1
                indexes.put(pages[i])
                print("Miss",end="\t\t")
            else:
                print("Hit",end="\t\t")
        else:
            if (pages[i] not in s):
                val = indexes.get()
                s.remove(val) 
                s.add(pages[i]) 
                indexes.put(pages[i]) 
                page_faults += 1
                print("Miss (del:"+str(val)+")",end="\t")
            else:
                print("Hit",end="\t\t")

        print(s)
  
    return page_faults


if _name=="main_":
    
    input_string = input("Enter reference string : ")
    pages = input_string.split()
    n = len(pages)

    capacity = int(input("Enter no. of Frames : "))
    
    faults=pageFaults(pages,n,capacity)

    print("\nNo. of Page Faults : ",faults)
    print("\nHit Ratio : ",(n-faults)/n)
    print("\nMiss Ratio : ",(faults)/n)
