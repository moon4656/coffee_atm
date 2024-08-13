from itemlist import ItemList

def remove_menu(item_list: ItemList):
    print('========== Remove Menu ==========')
    for i, item in enumerate(item_list.add_menu):
        print(f'{i + 1}. {item}')
    
    index  = input('선택: ')

    if not index.isdecimal():
        return
    
    index = int(index)
    if index <= 0 or index > len(item_list.add_menu):
        return
    
    
    menu_name = item_list.add_menu[index - 1]

    print(f'{index + 1}. {menu_name} 주문이 취소되었습니다.')
    item_list.total_price -= item_list.menu[menu_name]
    item_list.add_menu.remove(menu_name)