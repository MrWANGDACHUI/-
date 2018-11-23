n_alphabet = 0
n_alphabet = 0
n_number = 0
n_space = 0
n_other = 0
s = input('请输入一行字符')
for c in s:
    if 'A' <= c <= 'Z' or 'a' <= c <= 'z':
        n_alphabet += 1
    elif '0' <= c <= '9':
        n_number += 1
    elif c == ' ':
        n_space += 1
    else:
        n_other += 1
print('有{0}个英文字符，{1}个数字，{2}个空格和{3}个其它字符'.format(n_alphabet, n_number, n_space, n_other))

