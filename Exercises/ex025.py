nums = []
num1 = int(input('Digite o primeiro número: '))
nums.append(num1)
num2 = int(input('Digite o segundo número: '))
nums.append(num2)
num3 = int(input('Digite o terceiro número: '))
nums.append(num3)
nums.sort()
print('{} é o menor valor e {} é o maior.'.format(nums[0], nums[2]))
