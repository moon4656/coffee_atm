
from itemlist import ItemList

def add_menu(itemlist:ItemList):
    
    cnt = 1
    print("========== Add menu ==========")
    for menu in itemlist.menu:
        print(f'{cnt} {menu}')
        cnt += 1
    
    print(f'{cnt} 동작취소')
    item = int(input('선택:'))
    item_name = list(itemlist.menu)
    itemlist.add_menu.append(item_name[item-1])
    print('f{item_name} 추가')
    