T = int(input())
group_count = int(0)


for i in range(T):
    this_group = True
    used = [],[]
    word = str(input())
    word = word+'Z'
    for p in range(len(word)-1):
        used[1].append(0)                   
    for p in range(len(word)-1):
        word_info = word[p]
        used[0].append(word_info)
        if(word_info in used[0] and used[1][used[0].index(word_info)] == 1):
            this_group = False
            break
            
        elif(word[p] != word[p+1] and used[1][used[0].index(word_info)] == 0):
            used[1][used[0].index(word_info)] = 1

            
            
    if(this_group == True or len(word)==2):
        group_count+=1
print(group_count)
        
