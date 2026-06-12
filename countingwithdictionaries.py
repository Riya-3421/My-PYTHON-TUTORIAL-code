##counting with dictionaries
def count_char(s):
    count_dict={}
    for char in s:
        count_dict[char]=count_dict.get(char,0),1
    return count_dict
string="hello world"
print(count_char(string))