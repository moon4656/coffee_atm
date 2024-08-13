from itemlist import ItemList

def check_menu(item_list: ItemList):
    
    print(f'주문 품목 총액 {item_list.total_price}입니다.')
    print('=⇒', end='')
    # for menu in item_list.add_menu:
    print(*item_list.add_menu, sep=', ', end='')
    print()

