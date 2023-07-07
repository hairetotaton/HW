def find_count_to_turn_out_to_all_zero_or_all_one(string):
    groups = 1
    for i in range(1, len(string)):
        if string[i] != string[i-1]:
            groups += 1
    return groups - 1


input = "011110"
result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)

