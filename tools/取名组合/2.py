from pypinyin import pinyin, lazy_pinyin, Style
import os
import subprocess


def read_file_as_str():
    file_path = os.path.join('basedata.txt')
    all_the_text = open(file_path).read()
    return all_the_text
def style3(ming):
    pinyinstr = str(pinyin(ming,style=Style.TONE3)[0][0])
    if "4" in pinyinstr:
        return 4
    elif '3' in pinyinstr:
        return 3
    elif '2' in pinyinstr:
        return 2
    elif '1' in pinyinstr:
        return 1
    else:
        return 0

if __name__ == "__main__":
    '''
    strs = str(read_file_as_str())
    count = 0
    num = len(strs)*len(strs)
    for j in range(0, len(strs)):
        for i in range(0, len(strs)):
            ming1 = strs[j][0]
            ming2 = strs[i][0]
            datastr = ("金"+ming1+ming2+"  "+ str(pinyin("金")[0][0]) +"  "
                  +str(pinyin(ming1)[0][0])+"  " +str(pinyin(ming2)[0][0])
                  + "  1" + str(style3(ming1))+ str(style3(ming2)))

            if "112" in datastr:
                #写入文件
                file = os.path.join('to-data2.txt')
                with open(file, 'a+') as f:
                    f.write(datastr + '\n')
                #显示写入进度
                count += 1
                print(str(round((count/num)*100,2)) +str("%"))
    '''
    strs1 = '千夕之丰东申芝贞伊欢芬芳芯沙枝枫昭思钦熙彰玑孜姗莎葳萱煊璋嬉熹霏'
    strs2 = '十人儿于才凡丸及门习王元云尤牙屯牛毛壬仁什仇从仑匀文节石龙平卢田由禾仪白丛冯玄兰宁穴尼民弘辽皮台矛戎吉执扬芒权臣协存而夺达成夷尧尘团同回则年廷竹乔传伏延伦华行全合旬名刘齐决羊池宅农寻弛阳如红级驰巡形扶坛投芙芜芹严芦劳材极杨匣吾辰还来连呈时吴园围足邮男员吟别财何伯伶佛余含条彤迎言闲灼沦沉怀忱完宏牢良评识词灵层迟局陈纯纹环责玫坪拦择其苹苗直茁茅林枚杭杰奇轮歧卓贤国明昂迪鸣岩罗图迭垂和侠凭侨肴朋肪服鱼庞炎炉河油泽怡学宜实郎房诚祈询详弥弦承函迢玲型持城拾甚革茫荣荧胡南查栏柠勃咸研厘临尝昨虹咱峡贻俗皇泉侯盆胧独急饶峦亭庭闻阁娄前洁洪活浏洋浑浓恒觉神祠屏眉娃姚盈柔绒结耘秦盐袁哲壶莱莲荷莹桔桐桥桃格核酌原逐柴眠圆钱铃乘值徒徐航拿逢留凌席离唐凉旁拳烛涤流容读祥谈陵陶陪娱娥娘能球琉琅描捷排培职聆菱黄萌萝菊菩萍萤营乾梧梅曹堂常晨悬唯啤逻帷崇铜铭银甜梨笼笛符偿得衔盘舶船斜凰毫麻廊族旋阎羚鸿涯渠淮渔淘淳涵梁情寅谋谐屠随隆骑绳维绵巢琴琳琢琼提博彭联葛葡韩朝葵棋植棉榔雄棠晴畴幅赔程筏答牌集循然蛮童翔曾湖渤滑渝游惶愉寒裙禅强搏勤蓝蓬蒲蓉蒙槐榆楼酬雷零雹辑频龄睫愚盟锣锤辞愁筹魁衙鹏腾廉粮慈煤煌源溶福群叠模榴榕碟蝉膊豪旗熔察寥谭熊横醇题蝶蝴黎德颜潜潮潭澜澄擂擎薄橙橘融辙黔篮篷篱儒衡燃藉藏檀霞螺簧爵赢藤镰籍韦毋札邢芍凫汲祁丞牟圻芸芩芪岑岚佟孚狄炀沅沂汾诒妍妤邰纭纶耶苻苓郏昙昀竺迤佶帛泸泠泓穹诘妲骅敖莆莜荻桓砝虔晟晁铎倪栾亳涔宸娴绥逵萁菏萦晗铨偕皑徜翎斛馗孰焓烷淇淙隗婕婵绫骐琵琶琪琦琮颉揆椟覃雯嵘嵬锒犊筵筌颌阑遒湄谟祺遐婷缇瑜瑕颐楠楫楣裘虞嗷暌筠牒貉滢滦溏瑶瑭蔷蕖裴箔銮韶漩谯嫱嫦翟缪璜璇撷墀蕤赜樊槲瞑磐虢滕潼寮勰螯翮醛霖霓圜翱寰璩壕'
    count = 0
    num = len(strs1) * len(strs2)
    for j in range(0, len(strs1)):
        for i in range(0, len(strs2)):
            ming1 = strs1[j][0]
            ming2 = strs2[i][0]
            '''
            datastr = ("金" + ming1 + ming2 + "  " + str(pinyin("金")[0][0]) + "  "
                       + str(pinyin(ming1)[0][0]) + "  " + str(pinyin(ming2)[0][0])
                       + "  1" + str(style3(ming1)) + str(style3(ming2)))
            '''
            datastr = (ming1 + ming2)

                       # 写入文件
            file = os.path.join('to-data2.txt')
            with open(file, 'a+') as f:
                f.write(datastr + '\n')
            # 显示写入进度
            count += 1
            print(str(round((count / num) * 100, 2)) + str("%"))




