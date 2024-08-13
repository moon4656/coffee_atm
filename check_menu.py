from itemlist import ItemList

def check_menu(item_list: ItemList):
    
    total_price = 0
    for menu in item_list.add_menu:
        total_price += item_list.menu[menu]

    print(f'주문 품목 총액 {total_price}입니다.')
    print('=⇒', end='')
    # for menu in item_list.add_menu:
    print(*item_list.add_menu, sep=', ', end='')
    print()

