minutos = int(input("Qual é os minutos da sua maquina atual?"))

senha = "LIBERDADE"

def descobrir(min, p):
    
    nums = []
    count = 0
    
    while True:
        if min != count:
            count = count + 1
            nums.append(count)

        if min == count:
            nums.reverse()
            del nums[0]
            for number in nums:
                novo, min = number, min * number
                print(novo, min)

            return p + str(min)



print(descobrir(minutos, senha))