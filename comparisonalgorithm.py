def sort_lists(list1, list2):
    #sorting the lists in order to do binary search
    list1.sort()
    list2.sort() 

#we should search each elem
#where allergy is if the user is allergic or not to list 1 

#list1 = of stuff that you could or could NOT be allergic to 
#allergy = boolean 
#List2 = random thing you wanna see if you're allergic to 

#venn diagram OO

def compare_lists(list1, list2, allergy): 
    sort_lists(list1, list2)
    allergic = []
    non_allergic = []
    maybe_allergic = []

    for ingredient in list1: 
        if ingredient in list2 and allergy: 
            allergic.append(ingredient)
            #return ingredient
        elif allergy: 
            allergic.append(ingredient)
        else: 
            non_allergic.append(ingredient)

    for ingredient in list2: 
        if ingredient not in list1: 
            maybe_allergic.append(ingredient)
        

    return allergic, non_allergic, maybe_allergic
    #optimize later


def main(): 
    list1 = ["sugar", "spice", "everything nice"]
    list2 = ["sugar", "mean", "green"]
    allergic, non_allergic, maybe_allergic = compare_lists(list1, list2, True)
    print(allergic)
    print(non_allergic)
    print(maybe_allergic)    

if __name__ == "__main__": 
    main()