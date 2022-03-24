def print_table(data, column_headers = None,):

    collection_column_widths = []
    collection_lengths = []

    # if dict, change it to list
    if isinstance(data,dict):
        keys = []
        for key in data.keys():
            keys.append(key)
        
        values = []
        for collection in data.values():
            values.append(collection)

        if not column_headers:
            column_headers = keys
        data = values
    
    
    
    if column_headers:
        if(len(column_headers)!= len(data)):
            raise ValueError("The number of columns and number of column headers do not match.")
        for i in range(len(data)):
            # In case its a numpy array, covert it to list.
            data[i] = list(data[i])
            data[i].insert(0,column_headers[i])
                

    for collection in data:
        collection_longest_entry = max(collection , key = lambda x: len(str(x)))
        collection_column_widths.append(len(str(collection_longest_entry)))
        collection_lengths.append(len(collection))

    collection_length = collection_lengths[0]

    ## Check if all columns have the same number of rows
    if not all(element == collection_length for element in collection_lengths):
        raise(ValueError("Number of rows do not match."))
        
    for row in range(collection_length):
        # i = row number
        if(row == 0):
            if column_headers:
                print("#" * (sum([item + 5 for item in collection_column_widths]) + 1 ))
        
        for col in range(len(data)):
            print("#" + str(data[col][row]).center(collection_column_widths[col] + 4) , end="")
            
        print("#")
        
        if(row == 0):
            if column_headers:
                print("#" * (sum([item + 5 for item in collection_column_widths]) + 1 ))
    

