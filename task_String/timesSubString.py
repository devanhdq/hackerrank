def count_substring(string, sub_string):
    results = 0
    sub_len = len(sub_string)
    print(sub_len)
    for i in range(len(string)):
        if string[i:i + sub_len] == sub_string:
            results += 1
    return results


# string = input().strip()
# sub_string = input().strip()
string = "ABCDCDC"
sub_string = "CDC"

print(count_substring(string, sub_string))
