from typing import List


def skip_null(S):
    if '\n' not in S:
        return S
    header_index = S.find('\n')
    res = S[:header_index] + '\n'
    for row in S[S.find('\n')+1:].splitlines():
        if not any((cell for cell in row.split(',') if cell.strip() == 'NULL')):
            res += row + '\n'
    return res.strip('\n')




e1 = 'id,name,age,score\n4,adv, NULL ,645'
print(skip_null(e1))