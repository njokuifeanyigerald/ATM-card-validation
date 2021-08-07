def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    # print(sum(even_digits*2))
    # print(sum(odd_digits))
    checksum = 0
    checksum += sum(odd_digits)
    # print(checksum)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
        print(checksum)
    print(checksum)
    # print(checksum % 10)
    return checksum % 10
    
    

print('valid') if luhnpp_checksum('4225841114046491')==0 else print('invalid')

