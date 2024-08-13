from itemlist import ItemList

def order(item_list:ItemList):

    print(f'주문 품목 총액 {item_list.total_price}입니다. 품목은 다음과 같습니다.')
    print(*item_list.add_menu, sep=', ', end='')
    print('주문하시겠습니까?')
    print('1: yes')
    print('2: no')

    user_intput = input('선택: ')
    if not user_intput.isdecimal():
        return False
    user_intput_number = int(user_intput)
    if user_intput_number != 1:
        return False
    
    return True