def most_common(list_x):

    list_counter ={}
    for x in list_x:
        if x in list_counter:
            list_counter[x] += 1
        else:
            list_counter[x] = 1
    popular = sorted(list_counter, key = list_counter.get, reverse=True)
    return popular


word_list = ['Jellicle', 'Cats', 'are', 'black', 'and', 'white,', 'Jellicle', 'Cats', 'are', 'rather', 'small;', 'Jellicle', 'Cats', 'are', 'merry', 'and', 'bright,', 'And', 'pleasant', 'to', 'hear', 'when', 'they', 'caterwaul.', 'Jellicle', 'Cats', 'have', 'cheerful', 'faces,', 'Jellicle', 'Cats', 'have', 'bright', 'black', 'eyes;', 'They', 'like', 'to', 'practise', 'their', 'airs', 'and', 'graces', 'And', 'wait', 'for', 'the', 'Jellicle', 'Moon', 'to', 'rise.', '']
# word_counter = {}
# for word in word_list:
#     if word in word_counter:
#         word_counter[word] += 1
#     else:
#         word_counter[word] = 1

# popular_words = sorted(word_counter, key = word_counter.get, reverse = True)

ranked_list = most_common(word_list)

top = ranked_list[0]

#top = popular_words[0]
print(top)
