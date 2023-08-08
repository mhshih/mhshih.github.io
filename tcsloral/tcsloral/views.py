from django.http import HttpResponse
from django.shortcuts import render,redirect

def index(request):
    return render(request,'index.htm',{})

def group_question(request,group_num,question_num):
    if group_num==1:
        if question_num==1:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'我們先洗澡再刷牙。',
                                                           'pinyin1':'Wǒmen xiān xǐzǎo zài shuāyá。',
                                                           'chinese2':'我們 一 洗澡 就 刷牙。',
                                                           'pinyin2':'Wǒmen yì xǐzǎo jiù shuāyá',
                                                           'picture_filename':str(group_num)+str(question_num)+'.png'
                                                           })
        elif question_num==2:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'便利商店	前面	站	著	兩	個人	。',
                                                           'pinyin1':'Biànlì shāngdiàn qiánmiàn zhàn zhe liǎng gè rén',
                                                           'chinese2':'便利商店	前面	站	在	兩	個人	。',
                                                           'pinyin2':'Biànlì shāngdiàn qiánmiàn zhàn zài liǎng gè rén',
                                                           'picture_filename':str(group_num)+str(question_num)+'.png'
                                                           })
        elif question_num==3:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'有 一個 小女孩 坐在 地上 玩 玩具 。',
                                                           'pinyin1':'Yǒu yí ge xiǎo nǚhái zuò zài dìshang wán wánjù',
                                                           'chinese2':'有 一個 小女孩 坐 著 地上 玩 玩具 。',
                                                           'pinyin2':'Yǒu yī gè xiǎo nǚ hái zuò zhe dì shang wán wán jù',
                                                           'picture_filename':str(group_num)+str(question_num)+'.png'
                                                           })
        elif question_num==4:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'明天 放假 ， 今天 可以 晚 一點 睡 。',
                                                           'pinyin1':'Míngtiān fàngjià , jīntiān kěyǐ wǎn yìdiǎn shuì',
                                                           'chinese2':'明天 放假 ， 今天 可以 睡 晚 一點 。',
                                                           'pinyin2':'Míngtiān fàngjià , jīntiān kěyǐ shuì wǎn yìdiǎn',
                                                           'picture_filename':str(group_num)+str(question_num)+'.png'
                                                           })
        elif question_num==5:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'快 一點 走 ， 再不 走 就 看不到 他 了 。',
                                                           'pinyin1':'Kuài yìdiǎn zǒu zài bù zǒu jiù kàn bù dào tā le',
                                                           'chinese2':'走 快 一點 ， 再不 走 就 看不到 他 了 。',
                                                           'pinyin2':'Zǒu kuài yìdiǎn zài bù zǒu jiù kàn bú dào tā le',
                                                           'picture_filename':str(group_num)+str(question_num)+'.png'
                                                           })
        else:return redirect('/')
    elif group_num==2:        
        if question_num==1:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'以前結婚的人很多，現在結婚的人卻很少。',
                                                           'pinyin1':'Yǐqián jiéhūn de rén hěn duō, xiànzài jiéhūn de rén què hěn shǎo.',
                                                           'chinese2':'以前結婚的人很多，卻現在結婚的人很少。',
                                                           'pinyin2':'Yǐqián jiéhūn de rén hěn duō, què xiànzài jiéhūn de rén hěn shǎo.',
                                                           'picture_filename':str(group_num)+str(question_num)+'.png'
                                                           })
        elif question_num==4:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'我到了美國以後，會常常給你打電話。',
                                                           'pinyin1':'Wǒ dàole měiguó yǐhòu, huì chángcháng gěi nǐ dǎ diànhuà.',
                                                           'chinese2':'我到了美國以後，會往往給你打電話。',
                                                           'pinyin2':'Wǒ dàole měiguó yǐhòu, huì wǎngwǎng gěi nǐ dǎ diǎnhuà.',
                                                           })
        elif question_num==2:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'不論來得及來不及，你都要來。',
                                                           'pinyin1':'Búlùn láidejí láibùjí, nǐ dōu yào lái.',
                                                           'chinese2':'不論來得及來不及，你也要來',
                                                           'pinyin2':'Búlùn láidejí huò láibùjí, nǐ yě yào lái.',
                                                           })
        elif question_num==3:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'既然在學校上課，就應該利用學校的資源好好地學習。',
                                                           'pinyin1':'Jìrán zài xuéxiào shàngkè, jiù yīnggāi lìyòng xuéxiào de zīyuán hǎohǎo de xuéxí. ',
                                                           'chinese2':'即使在學校上課，也應該利用學校的資源好好地學習。',
                                                           'pinyin2':'Jíshǐ zài xuéxiào shàngkè, yě yīnggāi lìyòng xuéxiào de ziyuán hǎohǎo de xuéxí.',
                                                           })

        elif question_num==5:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'chinese1':'這次的報告我寫得不好，但總算寫完了',
                                                           'pinyin1':'Zhè cì de bàogào wǒ xiě de bùhǎo, dàn zǒngsuàn xiěwán le.',
                                                           'chinese2':'這次的報告我寫得不好，但終於寫完了。',
                                                           'pinyin2':'Zhè cì de bàogào wǒ xiě de bùhǎo, dàn zhōngyú xiěwán le.',
                                                           })
        else:return redirect('/')
    else:        
        if question_num==1:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'reading_question':['哥哥：小美真可愛，不知道有沒有機會認識她？','弟弟：癩蝦蟆想吃天鵝肉，簡直想得美。','請問弟弟說的話是什麼意思？'],
                                                           'chinese2':'（B）弟弟覺得哥哥條件不好，但可以認識小美。',
                                                           'chinese1':'（A）弟弟覺得哥哥不可能認識小美。',
                                                           'picture_filename':str(group_num)+str(question_num)+'.png',
                                                       })
        elif question_num==3:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'reading_question':['季偉：今天的考試你考得怎麼樣？',
                                                                               '怡芬：我沒複習，應該考得很差。',
                                                                               '季偉：哪怕是臨時抱佛腳，也要準備一下啊！至少不會不及格。',
                                                                               '怡芬：最近太忙了，連臨時抱佛腳的時間都沒有。',
                                                                               '請問「臨時抱佛腳」是什麼意思？',
                                                               ],
                                                           'chinese1':'A）準備得隨隨便便',
                                                           'chinese2':'B）準備得很充分'})
        elif question_num==4:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'reading_question':['小李：這次幸虧有林經理的幫忙，才能談下這筆生意。',
                                                                               '老闆：薑是老的辣，交給林經理負責，我很放心。',
                                                                               '請問老闆說的話是什麼意思？'],
                                                           'chinese1':'A) 林經理經驗豐富',
                                                           'chinese2':'B)林經理做事很嚴肅',
                                                        })
        elif question_num==5:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'reading_question':['弟弟：我只不過考不好就被媽媽罵了一頓，媽媽是不是不愛我。',
                                                                               '爸爸：媽媽是刀子嘴豆腐心。',
                                                                               '請問爸爸說的話是什麼意思？',],
                                                           'chinese1':'A）媽媽講的話很難聽，卻是為了弟弟好。',
                                                           'chinese2':'B）媽媽講的話很難聽，因為她不愛弟弟。'})
        elif question_num==6:
            return render(request,'question_template.htm',{'group_num':group_num,
                                                           'question_num':question_num,
                                                           'reading_question':['李小姐：我昨天在百貨公司看見怡君跟她男朋友在一起有說有笑的。',
                                                                               '張先生：真的嗎？我聽說他們最近吵架了？好像是因為她男朋友發現她跟別的男生在網路上聊天。',
                                                                               '李小姐：難不成她男朋友被戴綠帽了？',
                                                                               '請問李小姐最後說的話是什麼意思？',],
                                                           'chinese1':'A）怡君背叛了她的男朋友。',
                                                           'chinese2':'B）怡君和她的男朋友和好了。'})
        else:return redirect('/')
        


def answer(request,group_num,question_num):
    ans=request.GET['radio']
    if ans=='A':
        return render(request,'correct_template.htm',{'group_num':group_num,
                                                      'next_question_num':question_num+1,
                                                      'radio_value':ans})
    if group_num==1:
        if question_num==1:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi':'''「先A再B」與「一A就B」皆表示時間順序。「先A再B」表示前後順序，例如「我們先找位置再點菜。」；「一A就B」表示連續發生的兩件事，A事件結束馬上發生B事件，例如「他們一見面就聊天。」。
                                                                    xiān A zài B yǔ yī A jiù B jiē biǎo shì shí jiān shùn xù。
                                                                    xiān A zài B biǎo shì qián hòu shùn xù ， lì rú wǒ men xiān zhǎo wèi zhi zài diǎn cài 。
                                                                    yī A jiù B biǎo shì lián xù fā shēng de liǎng jiàn shì ， A shì jiàn jié shù mǎ shàng fā shēng B shì jiàn ， lì rú tā men yí jiàn miàn jiù liáo tiān 。
                                                                    '''
                                                        })
        elif question_num==2:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi':'「 地點 + V + 著 + N 」 是 存 現 句 ， 表示 N 出現 在 一個 地方 ， 例如 ： 「 餐桌 上 放 著 許多 水果 」 ；「 在 」 後面 表示 地點 ， 例如 ： 「 水果 放在 餐桌 上 」。「 dìdiǎn + V + zhe + N 」 shì cún xiàn jù , biǎoshì N chūxiàn zài yí ge dìfāng , lìrú : 「 Cānzhuō shàng fàng zhe xǔduō shuǐguǒ 」 ; 「 zài 」 hòumiàn biǎoshì dìdiǎn , lìrú : 「 Shuǐguǒ fàng zài cānzhuō shàng 」 。'})
        elif question_num==3:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi2':['「 地上 」 為 地點 ， 用 「 在 」 不用 「 著 」 「 在 / 著 」 可 表示 動作 進行 ；「 在 + 地點 」 ， 只能 說 「 坐在 地上 」 ， 不能 說 「 坐 著 地上 」 。','dì shang wèi dì diǎn ， yòng zài bú yòng zhe zài zhe kě biǎo shì dòng zuò jìn xíng ; zài dì diǎn , zhǐ néng shuō zuò zài dì shang , bù néng shuō zuò zhe dì shang.']})
        elif question_num==4:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi2':['如果 平常 晚上 九 點 睡覺 ， 「 今天 晚 一點 睡 」 是 今天 晚上 十 點 睡覺 。','Rúguǒ píngcháng wǎnshang jiǔ diǎn shuìjiào , jīntiān wǎn yìdiǎn shuì shì jīntiān wǎnshang shí diǎn shuìjiào .','如果 平常 睡 到 早上 八 點 ， 「 今天 睡 晚 一點 」 是 今天 睡 到 早上 九 點 。','Rúguǒ píngcháng shuì dào zǎoshang bā diǎn , jīntiān shuì wǎn yìdiǎn shì jīntiān shuì dào zǎoshang jiǔ diǎn']})
        elif question_num==5:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi2':['「 快 一點 走 」 是 叫 別人 趕快 離開 ， 「 走 快 一點 」 是 別人 正在 走路 ， 但是 他 走 得 太 慢 了 ， 你 希望 他 快 一點 。','kuài yìdiǎn zǒu shì jiào biéren gǎnkuài líkāi , zǒu kuài yìdiǎn shì biéren zhèng zài zǒulù , dànshì tā zǒu dé tài màn le , nǐ xīwàng tā kuài yìdiǎn']})
    elif group_num==2:
        if question_num==1:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi2':['「現在結婚的人很少」，「少」是動詞(verb)，',
                                                                  '"Xiànzài jiéhūn de rén hěn shǎo", "shǎo" shì dòngcí (verb),',
                                                                  '放在「卻」的後面。',
                                                                  'fàng zài "què" de hòumiàn.']
                                                    })
        elif question_num==4:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi2':['「常常」與「往往」都表示「經常發生」。','"Chángcháng" yǔ "wǎngwǎng" dōu biǎoshì "jīngcháng fāshēng".','「常常」是描述次數多，','"Chángcháng" shì miáoshù cìshù duō,','可以用於過去、現在或未來發生的事件；','kěyǐ yòng yú guòqù、xiànzài huò wèilái fāshēng de shìjiàn;','「往往」是根據過去經驗。','"wǎngwǎng" shì gēnjù guòqù jīngyàn.','這個題目的事件發生在未來，','Zhè ge tímù de shìjiàn fāshēng zài wèilái,','用「常常」較合適。','yòng "chángcháng" jiào héshì.']})
        elif question_num==2:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi2':['「不論/不管...都...」：表示不論哪一個條件或事情發生，最後結果都一樣。','"Bùlùn/ Bùguǎn...dōu...": Biǎoshì búlùn nǎ yí ge tiáojiàn huò shìqíng fāshēng, zuìhòu jiéguǒ dōu yíyàng.','這句話也可以說成「就算你來不及，你也要來」，','Zhè jù huà yé kěyǐ shuō chéng "Jiùsuàn nǐ lái bùjí, nǐ yěyào lái."','表示「如果你沒辦法準時到，也要來。」','biǎoshì  "Rúguǒ nǐ méi bànfǎ zhǔnshí dào, yěyào lái."']})
        elif question_num==3:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi2':['「既然...就」表示已經發生的事實；','"Jìrán...jiù" biǎoshì yǐjīng fāshēng de shìshí;','「即使...也」表示假設的事件。','"jíshǐ...yě" biǎoshì jiǎshè de shìjiàn.','在這一題，','Zài zhè yì tí,','「在學校上課」是已經發生的事實，','"zài xuéxiào shàngkè" shì yǐjīng fāshēng de shìshí,','所以只能用「既然...就」來表達。','suǒyǐ zhǐnéng yòng "jìrán...jiù" lái biǎodá.']})
        elif question_num==5:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                        'next_question_num':question_num+1,
                                                        'jiexi2':['「總算」與「終於」都可以用來表示「經過長時間後得到的結果」。','“Zǒngsuàn” yǔ “zhōngyú” dōu kěyǐ yòng lái biǎoshì“jīngguò cháng shíjiān hòu dé dào de jiéguǒ”.','但是「總算」還可以用來表示「可以說是」、「可以算是」，','Dànshì “zǒngsuàn” hái kěyǐ yòng lái biǎoshì “kěyǐ shuō shì”, "kěyǐ suàn shì" ,','題目的意思是「我寫完報告之後覺得寫得不好，但可以說是寫完了」，','tímù de yìsi shì "Wǒ xiě wán bàogào zhīhòu juéde xiě de bùhǎo, dàn kěyǐ shuō shì xiě wán le"','這時候只能用「總算」來表達。','zhè shíhòu zhǐ néng yòng "zǒngsuàn" lái biǎodá.']})
    else:
        if question_num==2:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                            'next_question_num':question_num+1,
                                                        'jiexi':'解析：「癩蝦蟆想吃天鵝肉」表示幻想不能實現的事實，不能正確地衡量自己的力量。',
                                                        })
        elif question_num==5:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                            'next_question_num':question_num+1,
                                                            'jiexi':'「臨時抱佛腳」表示平常沒有準備，來不及了才開始想辦法補救。'})
        elif question_num==1:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                            'next_question_num':question_num+1,
                                                            'jiexi':'「薑是老的辣」比喻年紀大的人經驗豐富，看過的事情多，考慮廣，做事熟練。'})
        elif question_num==3:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                            'next_question_num':question_num+1,
                                                            'jiexi':'「戴綠帽」是嘲笑他人的伴侶有其他感情對象。'})
        elif question_num==4:
            return render(request,'wrong_template.htm',{'group_num':group_num,
                                                            'next_question_num':question_num+1,
                                                            'jiexi':'「刀子嘴豆腐心」表示人說話不好聽，嘴像刀子一樣利，但是心像豆腐一樣軟，內心容易受感動。'})


def about(request):
    return render(request,'about.htm',{})
