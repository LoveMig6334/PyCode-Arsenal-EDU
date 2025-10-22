def text_prefix(text: str):
    my_list = []
    for i in range(len(text) + 1):
        my_list.append(text[0:i])
    return my_list


print(text_prefix("hello world"))
