import time, random
#import for sorts

if __name__ == "__main__":
    size = 100
    data_unsorted = [random.randint(0, size) for i in range(size)]
    #print(data_unsorted)
    thread_bubble_start = time.time()
    #bubble calls
    thread_bubble_elapsed_time = time.time() - thread_bubble_start
    thread_insertion_start = time.time()
    #insertion calls
    thread_insertion_elapsed_time = time.time() - thread_insertion_start
    thread_quick_start = time.time()
    #quick calls
    thread_quick_elapsed_time = time.time() - thread_quick_start
    thread_merge_start = time.time()
    #merge calls
    thread_merge_elapsed_time = time.time() - thread_merge_start    
    thread_selection_start = time.time()
    #selection calls
    thread_selection_elapsed_time = time.time() - thread_selection_start
    bubble_start = time.time()
    #bubble calls
    bubble_elapsed_time = time.time() - bubble_start
    insertion_start = time.time()
    #insertion calls
    insertion_elapsed_time = time.time() - insertion_start
    quick_start = time.time()
    #quick calls
    quick_elapsed_time = time.time() - quick_start
    merge_start = time.time()
    #merge calls
    merge_elapsed_time = time.time() - merge_start    
    selection_start = time.time()
    #selection calls
    selection_elapsed_time = time.time() - selection_start
    print("Time to for threaded bubble sort: ", thread_bubble_elapsed_time)
    print("Time to for threaded insertion sort: ", thread_insertion_elapsed_time)
    print("Time to for threaded quick sort: ", thread_quick_elapsed_time)
    print("Time to for threaded merge sort: ", thread_merge_elapsed_time)
    print("Time to for threaded selection sort: ", thread_selection_elapsed_time)
    print("Time to for bubble sort: ", bubble_elapsed_time)
    print("Time to for insertion sort: ", insertion_elapsed_time)
    print("Time to for quick sort: ", quick_elapsed_time)
    print("Time to for merge sort: ", merge_elapsed_time)
    print("Time to for selection sort: ", selection_elapsed_time)
