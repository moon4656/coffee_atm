
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
    
    ccnt = len(itemlist.add_menu)
    if ( ccnt < 10 ):
        itemlist.add_menu.append(item_name[item-1])
        print('f{item_name} 추가')
    else :
        print("주문 최대 수량은 10잔 입니다.")
        

    