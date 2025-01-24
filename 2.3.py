def f(s, c, repl):
    if len(s) == 0:
        return ""
    if s[0] == c:
        return repl + f(s[1: ], c, repl)
    else:
         return s[0] + f(s[1: ], c, repl)

string = "abcacd"
result = f(string, "c", "xy")
print(result)



