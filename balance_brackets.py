''' Balance of opening and closing brackets '''

def find_balance(data, left='[{(', right=']})'):
    res = []
    for i in data:
        if i in left:
            res.append(i)
        elif i in right:
            if len(res) == 0:
                return False
            elif right.index(i) == left.index(res[-1]):
                res = res[:-1]
            else:
                return False
    return len(res) == 0


## -----------------testing----------------------


def find_name(x, g=globals()):
    return ([n for n in g if id(g[n]) == id(x)])


test_string_1 = '[{()}]'
test_string_2 = '[[]{()[]}(){}]'
test_string_3 = '[w[23]f,.g0{()[qwer,ty]12}()<{}0]'
test_string_4 = ']({[]})[])}'
test_string_5 = '[adsf{3g(fe(3cfa)rt )4 }45'


test_list = [test_string_1, test_string_2, test_string_3, test_string_4, test_string_5]


for test in test_list:
    print('{name}: {func}.'.format(name=find_name(test)[0], func=find_balance(test)))



# Will be displayed

# Test_String_1: True.
# Test_String_2: True.
# Test_String_3: True.
# Test_String_4: False.
# Test_String_5: False.
