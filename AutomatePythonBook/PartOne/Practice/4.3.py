# A function that removes duplicates from the list while preserving the original order

def removeDuplicate(lst):
    seen = []
    for items in lst:
        if items not in seen:
            seen.append(items)

    return seen

print(removeDuplicate([1,2,3,4,3,4,5,6]))