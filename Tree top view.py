def topView(root):
    d = {}
    def viaje(root,key,level):
        if root:
            if key not in d:
                d[key] = [root,level]
            elif d[key][1] > level:
                d[key] = root,level
            viaje(root.left,key - 1,level + 1)
            viaje(root.right,key +1,level + 1)
    viaje(root,0,0)
    for _ in sorted(d):
        print(d[_][0],end= " ")