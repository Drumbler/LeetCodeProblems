def convertToBase7(num):
    sign = ""
    converted_num = ""
    match num:
        case 0:
            return "0"
        case 1:
            return "1"
        case 2:
            return "2"
        case 3:
            return "3"
        case 4:
            return "4"
        case 5:
            return "5"
        case 6:
            return "6"
        case _ if num < 0:
            sign = "-"
            num = num * -1
    while num:
        remainder = num % 7
        num = num // 7
        converted_num = str(remainder) + converted_num
    converted_num = sign + converted_num
    return converted_num


print(convertToBase7(1))
