def remove_duplicate(name1_list, name2_list):

    # find the matching letters in both names
    duplicates = set(name1_list) & set(name2_list)

    # create a list for the matching letters
    duplicates = list(duplicates)

    # concatenate both names 
    # set * as a border mark
    name_list = name1_list + ["*"] + name2_list

    uniques = []

    if not duplicates:
        # if no matching letters are found
        # return the concatenated list with False flag 
        return [name_list, False]
    else:
        for item in name_list:
            if item not in duplicates:
                uniques.append(item)

        # return the concatenated list with True flag 
        return [uniques, True]