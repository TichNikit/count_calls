calls = 0
def count_calls():
    global calls
    calls+=1

def string_info(word):
    count_calls()
    return (len(word), word.upper(), word.lower())

def is_contains(word, lis):
    count_calls()
    for i in lis:
        if word.lower() == i.lower():
            return True
    return False




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
