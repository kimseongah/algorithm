def solution(phone_book):
    phone_book.sort()
    phone_set = set()
    for phone_number in phone_book:
        for i in range(len(phone_number)):
            if phone_number[:i] in phone_set:
                return False
        phone_set.add(phone_number)       
    return True