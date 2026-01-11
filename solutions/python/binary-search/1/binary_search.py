def find(search_list, value):
    low = 0
    high = len(search_list) - 1

    while (low <= high):
        mid = low + (high - low) // 2

        if search_list[mid] == value:
            pass

        elif search_list[mid] < value:
            low = mid + 1
        
        else:
            high = mid - 1
            
    raise ValueError("value not in array")