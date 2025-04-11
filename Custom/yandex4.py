#Нужно написать функцию normalize, которая принимает на вход юниксовый путь и выдает его нормализованный вариант (схлопываются слеши, обрабатываются все возможные точки).
#Каталоги разделяются слэшами (/). Подряд может идти несколько слэшей ( /// ). Если указан символ точка "." - это означает текущую папку. Если указано два символа точки подряд ".." - это означает ссылку на родительскую папку. Требуется получить нормализованное представление

#Примеры:
#In: /foo/bar//bax/asdf/quux/..
#Out: /foo/bar/bax/asdf

#In: a/../../b
#Out: ../b

#In: /a/../../b
#Out: /b

def normalize(path: str) -> str:
    path = path.strip()
    if not path:
        return path

    # is relative flag
    is_relative = path[0] != '/'

    # split str by / and filter ''
    files = filter(lambda file: file != '', path.split('/'))
    
    # use stack to
    stack = []
    for file in files:
        if file == '.':
            if not stack:
                stack.append('.')
        elif file == '..':
            if stack:
                stack.pop()
            elif is_relative:
                stack.append(file)
        else:
            stack.append(file)
    
    path = '' if is_relative else '/'
    return path + "/".join(stack)


assert normalize('/foo/bar//bax/asdf/quux/..') == '/foo/bar/bax/asdf'
assert normalize('a/../../b') == '../b'
assert normalize('/a/../../b') == '/b'
assert normalize('./a/././b') == './a/b'
