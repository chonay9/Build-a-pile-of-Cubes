def find_nb(m):
    # your code
    n = 1
    result = 0
    while result < m :
        result = result + (n ** 3)
        n = n + 1
        #print(result)
    #print(n)
    if result != m:
        return -1
    return n - 1
    
    
#----------------TDD----------------
test.assert_equals(find_nb(4183059834009), 2022)
test.assert_equals(find_nb(24723578342962), -1)
test.assert_equals(find_nb(135440716410000), 4824)
test.assert_equals(find_nb(40539911473216), 3568)
test.assert_equals(find_nb(26825883955641), 3218)
