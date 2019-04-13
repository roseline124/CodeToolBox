def is_opposite(face, n):
    op = False 
    
    if face == n : 
        op = 'same'
    else : 
        if face == 1 : 
            op = True if n == 6 else False
        elif face == 2 : 
            op = True if n == 5 else False
        elif face == 3 : 
            op = True if n == 4 else False
        elif face == 4 : 
            op = True if n == 3 else False
        elif face == 5 : 
            op = True if n == 2 else False
        elif face == 6 : 
            op = True if n == 1 else False

    return op