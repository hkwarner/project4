if value < cur_node.value:
    cur_node.left = self.__rec_remove(value, cur_node.left)
    #cur_node.__height -= 1
elif value > cur_node.value:
    cur_node.right = self.__rec_remove(value, cur_node.right)
    #cur_node.__height -= 1
elif value == cur_node.value:
    if cur_node.left != None and cur_node.right != None:
        prec = cur_node
        replace_with = cur.right
        while replace_with.left != None:
            prec = replace_with
            replace_with = replace_with.left
        current.val = replace_with.val
        prec.left = None
        if prec.right == None:
            prec.height -= 1
    elif cur_node.right == None:
        cur_node = cur_node.left
        if cur_node != None:
            cur_node.height -= 1
    elif cur_node.left == None:
        cur_node = cur_node.right
        if cur_node != None:
            cur_node.height -= 1
#if preceding value has two children, don't update height
#if preceding value has one or zero children, update self.__height if .height == self.__height - 1
return cur_node
