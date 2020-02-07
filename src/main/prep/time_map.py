from src.main.prep.node import Node
import heapq

def set(k, t, v, map):

    eval = map.get(k)
    print(eval)
    if eval is None:
        head = Node(t)
        arr = []
        heapq.heappush(arr, v)
        head.set_heap_ref(arr)
        map[k] = head
    else:
        node = eval
        inserted = False
        prev = None
        while node:
            if node.value == t:
                arr = node.heapref
                heapq.heappush(arr, v)
                inserted = True
                break
            elif node.prev and  node.prev.value < t and node.next and node.next.value > t:
                tmp = Node(t)
                arr = []
                heapq.heappush(arr, v)
                tmp.set_heap_ref(arr)
                prev = node.prev
                next = node.next
                prev.next = tmp
                tmp.prev = prev
                tmp.next = next
                next.prev = tmp
                inserted = True
                break
            else:
                prev = node
                node = node.next

        if not inserted:
            if t > prev.value:
                print('inserting at ',t)
                tmp = Node(t)
                arr = []
                heapq.heappush(arr, v)
                tmp.set_heap_ref(arr)
                prev.next= tmp
                tmp.prev = prev
            else:
                print('inserting1 at ', t , prev)
                tmp = Node(t)
                arr = []
                heapq.heappush(arr, v)
                tmp.set_heap_ref(arr)

                prev.prev.next = tmp
                tmp.prev = prev.prev
                tmp.next = prev
                prev.prev = tmp
                prev.next = None



map = {}

set('k1', 2, 4, map)
print(map)
set('k1', 5, 3, map)
print(map)
set('k1', 3, 2, map)
print(map)

eval = map['k1']
print(eval.value, eval.next.value, eval.next.next.value)