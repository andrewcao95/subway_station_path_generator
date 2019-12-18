line1=u'''苹果园 古城路 八角游乐园 八宝山 玉泉路 五棵松 万寿路 公主坟 军事博物馆 木樨地
南礼士路 复兴门 西单 天安门西 天安门东 王府井 东单 建国门 永安里 国贸 大望路 四惠 四惠东'''
line2=u'''西直门 车公庄 阜成门 复兴门 长椿街 宣武门 和平门 前门 崇文门 北京站 建国门
朝阳门 东四十条 东直门 雍和宫 安定门 鼓楼大街 积水潭'''
line5=u'''宋家庄 刘家窑 蒲黄榆 天坛东门 磁器口 崇文门 东单 灯市口 东四 张自忠路
北新桥 雍和宫 和平里北街 和平西桥 惠新西街南口 惠新西街北口 大屯桥东 北苑路北 立水桥南 立水桥 天通苑南 天通苑 天通苑北'''
line4=u'''天宫院 生物医药基地 义和庄 黄村火车站 黄村西大街 清源路 枣园 高米店南
高米店北 西红门 新宫 公益西桥 角门西 马家堡 北京南站 陶然亭 菜市口 宣武门 西单 灵境胡同 西四
平安里 新街口 西直门 动物园 国家图书馆 魏公村 人民大学 海淀黄庄 中关村 北京大学东门 圆明园 西苑 北宫门 安河桥北'''
line6=u'''海淀五路居 慈寿寺 白石桥南 车公庄西 车公庄 平安里 北海北 南锣鼓巷 东四 朝阳门 东大桥
呼家楼 金台路 十里堡 青年路 褡裢坡 黄渠 常营 草房 物资学院路 通州北关 通运门 北运河西 北运河东 郝家府 东夏园 潞城'''
line8=u'''朱辛庄 育知路 平西府 回龙观东大街 霍营 育新 西小口 永泰庄 林萃桥 森林公园南门
奥林匹克公园 奥体中心 北土城 安华桥 鼓楼大街 什刹海 南锣鼓巷'''
line9=u'''国家图书馆 白石桥南 白堆子 军事博物馆 北京西站 六里桥东 六里桥 七里庄
丰台东大街 丰台南路 科怡路 丰台科技园 郭公庄'''
line10=u'''劲松 双井 国贸 金台夕照 呼家楼 团结湖 农业展览馆 亮马桥 三元桥 太阳宫 芍药居
惠新西街南口 安贞门 北土城 健德门 牡丹园 西土城 知春路 知春里 海淀黄庄 苏州街 巴沟 火器营
长春桥 车道沟 慈寿寺 西钓鱼台 公主坟 莲花桥 六里桥 西局 泥洼 丰台站 首经贸 纪家庙 草桥
角门西 角门东 大红门 石榴庄 宋家庄 成寿寺 分钟寺 十里河 潘家园'''
line13=u'''西直门 大钟寺 知春路 五道口 上地 西二旗 龙泽 回龙观 霍营 立水桥 北苑 望京西
                        芍药居 光熙门 柳芳 东直门'''
line14=u'''张郭庄 园博园 大瓦窑 郭庄子 打井 七里庄 西局'''
line15=u'''俸伯 顺义 石门 南法信 后沙峪 花梨坎 国展 孙河 马泉营 崔各庄望京 望京西'''
YiZhuangLine=u'''宋家庄 肖村 小红门 旧宫 亦庄桥 亦庄文化园 万源街 荣京东街 荣昌东街
                       同济南路 经海路 次渠南 次渠'''
FangShanLine=u'''郭公庄 大葆台 稻田 长阳 篱笆房 广阳城 良乡大学城北 良乡大学城 良乡大学城西 良乡南关 苏庄'''
ChangPingLine=u'西二旗 生命科学园 朱辛庄 巩华城 沙河 沙河高教园 南邵'
BaTongLine=u'''四惠 四惠东 高碑店 中国传媒大学 双桥 管庄 八里桥 通州北苑 果园 九棵树 梨园 临河里 土桥'''


def build_subway(**lines):
    """
    Input is build_subway(linename='station1 station2...'...)
    Ouput is a dictionary like {station:{neighbor1:line number,neighbor2:line number,...},station2:{...},...}
    """
    for key in lines.keys():
        value = lines[key]
        lines[key] = value.split()
    stations = set()
    for key in lines.keys():
        stations.update(set(lines[key]))
    system = {}
    for station in stations:
        next_station = {}
        for key in lines:
            if station in lines[key]:
                line = lines[key]
                idx = line.index(station)
                if idx == 0:
                    next_station[line[1]] = key
                elif idx == len(line)-1:
                    next_station[line[idx-1]]=key
                else:
                    next_station[line[idx-1]] = key
                    next_station[line[idx+1]] = key
        system[station] = next_station
    return system

def update_subway(BeiJingSubway):
    """
    due to line2 and line10 are circle lines.
    the BeiJingSubway need to update
    """
    BeiJingSubway[u'西直门'][u'积水潭'] = 'line_2'
    BeiJingSubway[u'积水潭'][u'西直门'] = 'line_2'
    BeiJingSubway[u'劲松'][u'潘家园'] = 'line_10'
    BeiJingSubway[u'潘家园'][u'劲松'] = 'line_10'
    return BeiJingSubway


bj_subway = build_subway(
    line_1=u'''苹果园 古城 八角游乐园 八宝山 玉泉路 五棵松 万寿路 公主坟 军事博物馆 木樨地 南礼士路 复兴门 西单 天安门西 天安门东 王府井 东单 建国门 永安里 国贸 大望路 四惠 四惠东''',
    line_2=u'''西直门 车公庄 阜成门 复兴门 长椿街 宣武门 和平门 前门 崇文门 北京站 建国门 朝阳门 东四十条 东直门 雍和宫 安定门 鼓楼大街 积水潭''',
    line_4_daxing=u'''天宫院 生物医药基地 义和庄 黄村火车站 黄村西大街 清源路 枣园 高米店南 高米店北 西红门 新宫 公益西桥 角门西 马家堡 北京南站 陶然亭 菜市口 宣武门 西单 灵境胡同 西四 平安里 新街口 西直门 动物园 国家图书馆 魏公村 人民大学 海淀黄庄 中关村 北京大学东门 圆明园 西苑 北宫门 安河桥北''',
    line_5=u'''宋家庄 刘家窑 蒲黄榆 天坛东门 磁器口 崇文门 东单 灯市口 东四 张自忠路 北新桥 雍和宫 和平里北街 和平西桥 惠新西街南口 惠新西街北口 大屯桥东 北苑路北 立水桥南 立水桥 天通苑南 天通苑 天通苑北''',
    line_6=u'''金安桥 苹果园 杨庄 西黄村 廖公庄 田村 海淀五路居 慈寿寺 花园桥 白石桥南 车公庄西 车公庄 平安里 北海北 南锣鼓巷 东四 朝阳门 东大桥 呼家楼 金台路 十里堡 青年路 褡裢坡 黄渠 常营 草房 物资学院路 通州北关 通运门 北运河西 北运河东 郝家府 东夏园 潞城''',
    line_7=u'''北京西站 湾子 达官营 广安门内 菜市口 虎坊桥 珠市口 桥湾 磁器口 广渠门内 广渠门外 九龙山 大郊亭 百子湾 化工 南楼梓庄 欢乐谷景区 垡头 双合 焦化厂''',
    line_8_north=u'''朱辛庄 育知路 平西府 回龙观东大街 霍营 育新 西小口 永泰庄 林萃桥 森林公园南门 奥林匹克公园 奥体中心 北土城 安华桥 安德里北街 鼓楼大街 什刹海 南锣鼓巷 中国美术馆''',
    line_8_south=u'''瀛海 德茂 五福堂 火箭万源 东高地 和义 大红门南 大红门 海户屯 木樨园 永定门外 天桥 珠市口''',
    line_9=u'''国家图书馆 白石桥南 白堆子 军事博物馆 北京西站 六里桥东 六里桥 七里庄 丰台东大街 丰台南路 科怡路 丰台科技园 郭公庄''',
    line_10=u'''劲松 双井 国贸 金台夕照 呼家楼 团结湖 农业展览馆 亮马桥 三元桥 太阳宫 芍药居 惠新西街南口 安贞门 北土城 健德门 牡丹园 西土城 知春路 知春里 海淀黄庄 苏州街 巴沟 火器营 长春桥 车道沟 慈寿寺 西钓鱼台 公主坟 莲花桥 六里桥 西局 泥洼 丰台站 首经贸 纪家庙 草桥 角门西 角门东 大红门 石榴庄 宋家庄 成寿寺 分钟寺 十里河 潘家园''',
    line_13=u'''西直门 大钟寺 知春路 五道口 上地 西二旗 龙泽 回龙观 霍营 立水桥 北苑 望京西 芍药居 光熙门 柳芳 东直门''',
    line_14_west=u'''张郭庄 园博园 大瓦窑 郭庄子 大井 七里庄 西局''',
    line_14_east=u'''北京南站 永定门外 景泰 蒲黄榆 方庄 十里河 北工大西门 平乐园 九龙山 大望路 金台路 朝阳公园 枣营 东风北桥 将台 高家园 望京南 阜通 望京 东湖渠 来广营 善各庄''',
    line_15=u'''俸伯 顺义 石门 南法信 后沙峪 花梨坎 国展 孙河 马泉营 崔各庄 望京东 望京 望京西 关庄 大屯路东 安立路 奥利匹克公园 北沙滩 六道口 清华东路西口''',
    line_16=u'''西苑 农大南路 马连洼 西北旺 永丰南 永丰 屯佃 稻香湖路 温阳路 北安河''',
    line_yizhuang=u'''宋家庄 肖村 小红门 旧宫 亦庄桥 亦庄文化园 万源街 荣京东街 荣昌东街 同济南路 经海路 次渠南 次渠 亦庄火车站''',
    line_fangshan=u'''郭公庄 大葆台 稻田 长阳 篱笆房 广阳城 良乡大学城北 良乡大学城 良乡大学城西 良乡南关 苏庄 阎村东''',
    line_changping=u'''西二旗 生命科学园 朱辛庄 巩华城 沙河 沙河高教园 南邵 北邵洼 昌平东关 昌平 十三陵景区 昌平西山口''',
    line_batong=u'''四惠 四惠东 高碑店 传媒大学 双桥 管庄 八里桥 通州北苑 果园 九棵树 梨园 临河里 土桥''',
    line_yanfangxian=u'''阎村东 紫草坞 阎村 星城 大石河东 马各庄 饶乐府 房山城关 燕山''',
    line_s1=u'''金安桥 四道桥 桥户营 上岸 栗园庄 小园 石厂''',
    line_shoudu_airport=u'''东直门 三元桥 3号航站楼 2号航站楼''',
    line_daxing_airport=u'''草桥 大兴新城 大兴机场''',
    line_xijiao=u'''巴沟 颐和园西门 茶棚 万安 植物园 香山''',
)

bj_subway = update_subway(bj_subway)




def shorter_path(start, goal):
    if start == goal:
        return [start]
    explored = set()
    queue = [ [start] ]
    while queue:
        path = queue.pop(0)
        s = path[-1]
        for state, action in bj_subway[s].items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if state == goal:
                    return path2
                else:
                    queue.append(path2)
    return []









def dijsktra(graph, initial, end):
    # shortest paths is a dict of nodes
    # whose value is a tuple of (previous node, weight)
    shortest_paths = {initial: (None, 0)}
    current_node = initial
    visited = set()

    while current_node != end:
        visited.add(current_node)
        destinations = graph.edges[current_node]
        weight_to_current_node = shortest_paths[current_node][1]

        for next_node in destinations:
            weight = graph.weights[(current_node, next_node)] + weight_to_current_node
            if next_node not in shortest_paths:
                shortest_paths[next_node] = (current_node, weight)
            else:
                current_shortest_weight = shortest_paths[next_node][1]
                if current_shortest_weight > weight:
                    shortest_paths[next_node] = (current_node, weight)

        next_destinations = {node: shortest_paths[node] for node in shortest_paths if node not in visited}
        if not next_destinations:
            return "Route Not Possible"
        # next node is the destination with the lowest weight
        current_node = min(next_destinations, key=lambda k: next_destinations[k][1])

    # Work back through destinations in shortest path
    path = []
    while current_node is not None:
        path.append(current_node)
        next_node = shortest_paths[current_node][0]
        current_node = next_node
    # Reverse path
    path = path[::-1]
    return path





len = len(shorter_path("苹果园", "安立路"))

print(shorter_path("苹果园", "安立路"))
print((len - 1) / 2)


queue = [ ["苹果园"] ]
path = queue.pop(0)
s = path[-1]

print(bj_subway[s].items())