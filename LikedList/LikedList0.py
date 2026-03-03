from LikedList1 import *
def main():
    ll = LinkedList()
    ll.append(12)
    ll.append(4)
    ll.append(10)
    ll.append(20)
    print(ll)
    # 
    ll.perpend(22)
    print(ll)
    # 
    ll.insert(200, 1)
    print(ll)
    # 
    ll.pop(3)
    print(ll)
    # 
    print(ll.get(1))
    # 
    ll.delete(22)
    print(ll)    
    # 
    print(5 in ll)
    print(10 in ll)

if __name__ == "__main__":
    main()
