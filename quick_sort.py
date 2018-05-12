#Quick sort
import random
import time

def randomNumber(st, ed, N):
    """
        Return length == N random numbers list
    """
    reList = []
    for i in range(N):
        reList.append(random.randint(st, ed))
    
    return reList

### 
 
def partition(List, left_index, right_index, selected_index): 
    """
        [5, 6, 4, 2, 7, 8, 1]  
        left_index
               |           right_index
               |            
               selected           
        
    """
    #1
    #print("1:My List\t",List)
    select_value = List[selected_index] #4
    
    List[right_index], List[selected_index] =   List[selected_index], List[right_index]
    #print("2:SWAP(Prov,R)\t",List,"Prove:",List[right_index])
    #[5, 6, 1, 2, 7, 8, 4] 
    # ^ SI
    SI = left_index 
    #print("3:SI",SI)
    for i in range(left_index, right_index, 1):
    #    print("i=",i,"SI",SI, List)
        if List[i] <= select_value: #需要放到左邊的情況
            List[i], List[SI] = List[SI], List[i] 
            #List[i] == 1 (i == 2
            SI += 1
            #[1, 6, 5, 2, 7, 8, 4]
            #    ^ SI 
            #--------
            #List[i] == 2 (i == 3
            #[1, 2, 5, 6, 7, 8, 4]
            #       ^ SI
    #[1, 2, 5, 6, 7, 8, 4]
    #       ^ SI
    List[SI], List[right_index] = List[right_index], List[SI]
    #[1, 2, 4, 6, 7, 8, 5]
    #       ^ SI
    #print("End","SI",SI, List)
    return SI #NEW index of selected_value
    
def quick_sort(AList, left_index, right_index):
    if left_index < right_index: #else: end of sort
        New_SI = partition(AList, left_index, right_index, right_index-1)
        #left sort
        quick_sort(AList, left_index, New_SI-1)
        #right sort
        quick_sort(AList, New_SI+1, right_index)
    return 
     
if __name__ == "__main__":
    aList = randomNumber(0,50000, 40000)#[5, 6, 4, 2, 7, 8, 1,23,442,3,2,2,11,2,3,5]
    #print(aList)
    tStart = time.time()
    #quick_sort(aList, 0, len(aList)-1)
    aList.sort()
    tEnd = time.time()
    #print(aList)
    print("It cost %f sec" % (tEnd - tStart))