def solve(date):
    li = list(date)
    if li[3] == '7':
        li[3] = '8'

    return ''.join(li)

print(solve('2017/01/07') == '2018/01/07')
print(solve('2017/01/31') == '2018/01/31')
