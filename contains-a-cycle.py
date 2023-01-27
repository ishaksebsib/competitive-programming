nodes = set()
def has_cycle(head):
    if head == None:
        return 0
    if head in nodes:
        return 1
    nodes.add(head)
    return has_cycle(head.next)
