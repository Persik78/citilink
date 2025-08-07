def filter_unique_words(answer_list: str) -> str:
    answer_list2 = answer_list.split()
    new_list = []
    for i in answer_list2:
        if i not in new_list:
            new_list.append(i)
    if new_list == []:
        return -1
    else:
        return new_list


answer_list = input()

unique_words = filter_unique_words(answer_list)

print(unique_words)