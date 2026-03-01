def check_balanced_par(s):
    mappings = {
        ')' : '(',
        ']' : '[',
        '}' : '{'
    }
    stack = []
    for c in s:
        if c in mappings.values():
            stack.append(c)
        elif c in mappings.keys() and len(stack) >0 :
            if mappings[c] == stack[-1]:
                stack.pop()
            else: 
                return False
    return len(stack) == 0


    