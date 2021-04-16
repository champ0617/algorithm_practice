# 注意python输入多行的时候 可以通过try except 跳出


while True:
    try:
        i = 0
        num = int(input())
        data = []
        while i < num:
            i += 1
            temp_data = int(input())
            data.append(temp_data)
        data = list(set(data))
        data.sort()
        for item in data:
            print(item)
    except:
        break
