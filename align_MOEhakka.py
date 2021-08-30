import sys
MOEmin_filename = sys.argv[1]#《臺灣客家語常用詞辭典》內容資料\(1090728\)ods檔.xlsx\ -\ records.tsv_每條詞意一行_僅中文平行例句_加斷詞詞類.tsv 2
substitution_cost = int(sys.argv[2])

from align_and_POStransfer import align_and_tag

headers ="系統編號,詞目,詞性,詞目索引分類,釋義,近義詞,反義詞,對應國語,大埔腔相關字詞,饒平腔相關字詞,詔安腔相關字詞,南四縣相關字詞".split(",")
print("@".join(headers + ["tagged_words_count", "tagged_nan_words_count", "diff_words", "zh_chr_count", "hakka_chr_count", "diff_chr", "hakka_tagged"]))

for line in open(MOEmin_filename):
    系統編號,詞目,詞性,詞目索引分類,四縣腔音讀,海陸腔音讀,大埔腔音讀,饒平腔音讀,詔安腔音讀,南四縣腔音讀,sense,raw,chinese,tagged_words,釋義,近義詞,反義詞,對應國語,大埔腔相關字詞,大埔腔相關字詞音讀,饒平腔相關字詞,饒平腔相關字詞音讀,詔安腔相關字詞,詔安腔相關字詞音讀,南四縣相關字詞,南四縣相關字詞音讀 = line.split('\t')#[11:14]
    tagged_words = tagged_words.split("　")
    tagged_words_count = len(tagged_words)

    tagged_words = [(tagged_word.split("(")[0], tagged_word.split("(")[1]) for tagged_word in tagged_words]

    X, Y = align_and_tag(min=raw, tagged_words=tagged_words, substitution_cost=substitution_cost)
    tagged_nan_string = "".join([w for w in X[1:]])
    tagged_nan_words = tagged_nan_string.replace('＊',"").split(")")
    tagged_nan_words_count = len(tagged_nan_words) - 1

    diff_words = tagged_words_count - tagged_nan_words_count

    num_chinese_characters = len(chinese)
    num_hakka_characters = len(raw)
    diff_characters = num_chinese_characters - num_hakka_characters

#   print(系統編號,詞目,詞性,詞目索引分類,sense,raw,chinese,釋義,近義詞,反義詞,對應國語,大埔腔相關字詞,饒平腔相關字詞,詔安腔相關字詞,南四縣相關字詞, tagged_words_count, tagged_nan_words_count, diff_words, num_chinese_characters, num_hakka_characters, diff_characters, "\t".join([word + "(" + tag for word, tag in tagged_words]), sep="@")
#   print(系統編號,詞目,詞性,詞目索引分類,sense,raw,chinese,釋義,近義詞,反義詞,對應國語,大埔腔相關字詞,饒平腔相關字詞,詔安腔相關字詞,南四縣相關字詞, tagged_words_count, tagged_nan_words_count, diff_words, num_chinese_characters, num_hakka_characters, diff_characters, ")\t".join(tagged_nan_words), sep="@")
    print("\n".join(tagged_nan_words))
