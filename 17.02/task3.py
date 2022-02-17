text = "The reasonable man adapts himself to the world the unreasonable one persists in trying to adapt the world to himself"
text_list = text.split()
index_first, index_second = text_list.index('reasonable'), text_list.index('unreasonable')
text_list[index_first], text_list[index_second] = text_list[index_second], text_list[index_first]
print(*text_list)
