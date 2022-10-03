# 1. Даны два списка из чисел. Найдите все числа, которые входят как в первый, так и во второй список, и выведите их в порядке возрастания.
 
# def random_list(n):
#     from random import randint
#     some_list=[]
#     for i in range(n):
#         some_list.append(randint(0,10))
#     return some_list

# lst1=random_list(7)
# lst2=random_list(7)
# print(f'Первый список: {lst1}')
# print(f'Второй список: {lst2}')
# result=set(lst1).intersection(set(lst2))
# print(sorted(list(result)))
#-----------------------------------------------------

# 2. Во входной строке записана последовательность чисел через пробел. Для каждого числа выведите слово YES (в отдельной строке), 
# если это число встречалось ранее в последовательности, и NO, если не встречалось.

# lst=[1,2,3,2,3,4]
# result_set = set()
# for num in lst:
#     if num in result_set:
#         print('YES')
#     else:
#         print('NO')
#         result_set.add(num)
#-----------------------------------------------------

# 3. Дан текст. В первой строке записано количество строк, далее идут сами строки. Определите, сколько различных слов содержится в этом в тексте. 
# Словом считается последовательность непробельных символов, идущих подряд. Слова разделены одним или большим числом пробелов или символами конца строки.

str1 = "She sells sea shells on the sea shore;"
str2 = "The sells that she sells are sea shells I'm sure."
str3 = "So if she sells sea shells on the sea shore,"
str4 = "I'm sure that the shells are sea shore shells."
text=str1+str2+str3+str4

def get_words(sentences):
    sentences = sentences.replace(",", " ").replace(".", " ").replace(";", " ")
    sentences = sentences.lower()
    words = sentences.split()
    words.sort()
    return words

def get_words_dict(words):
    words_dict = dict()
    for word in words:
        if word in words_dict:
            words_dict[word] = words_dict[word] + 1
        else:
            words_dict[word] = 1
    return words_dict

words = get_words(text)
words_dict = get_words_dict(words)
print(f"Кол-во слов: {len(words)}")
print(f"Кол-во уникальных слов: {len(words_dict)}")