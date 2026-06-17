##Check if a string is Palindrone
def is_palindrone(s):
    s=s.lower().replace(" "," ")
    return s == s[::-1]
print(is_palindrone("A man a plan a canal panama"))
print(is_palindrone("Hello"))