import discord 
import os
from discord.ext import commands
from keep_alive import keep_alive
#Define class basic stats dict
cls = {
    #Soul Dancer's basic stats
    'sd': 
        {   'INS': {'HP': 240, 'MATK/PATK': 2, 'AP': 2, 'CDR': 6},
            'INT': {'HP': 120, 'MATK/PATK': 5, 'MS': 2},
            'DEX': {'HP': 240, 'MATK/PATK': 2,'CRIT': 4, ' MS': 4},
            'STR': {'HP':120, 'AP': 2},
            'CON': {'HP':400, 'PDEF': 2,'MDEF': 2, 'CRITRes': 2}
        },
    #Assasin's basic stats
    'an':
        {
            'INS': {'HP': 240, 'MATK/PATK': 2, 'AP':4,'CDR':4},
            'INT': {'HP': 120, 'MATK/PATK':5, 'MS':2},
            'DEX': {'HP': 240, 'MATK/PATK': 2, 'CRIT':4, 'MS':4},
            'STR': {'HP': 120, 'AP': 2},
            'CON': {'HP': 400, 'PDEF': 2,'MDEF': 2,'CRITRes': 2}
        },
    #Puppeteer's basic stats  
    'pp':
        {
            'INS': {'HP': 240, 'MATK/PATK': 2,'AP': 2, 'CDR': 6},
            'INT': {'HP': 120, 'MATK/PATK': 5, 'MS': 2},
            'DEX': {'HP': 240, 'MATK/PATK': 2,'CRIT': 4, 'MS': 4},
            'STR': {'HP': 120, 'AP':2},
            'CON': {'HP': 400, 'PDEF': 2, 'MDEF': 2, 'CRITRes': 2}
        },
    #Reaper's basic stats
    'rp': 
        {
            'INS': {'HP': 240, 'MATK/PATK': 2, 'AP':4,'CDR':4},
            'INT': {'HP': 120, 'MATK/PATK':5, 'MS':2},
            'DEX': {'HP': 240, 'MATK/PATK': 2, 'CRIT':4, 'MS':4},
            'STR': {'HP': 120, 'AP': 2},
            'CON': {'HP': 400, 'PDEF': 2,'MDEF': 2,'CRITRes': 2}
        },
    #Gunslinger's basic stats
    'gs':{
            'INS': {'HP': 240, 'MATK/PATK': 2, 'AP':4, 'CDR': 4},
            'INT': {'HP': 120, 'MS': 2},
            'DEX': {'HP': 240, 'MATK/PATK': 2, 'CRIT': 6, ' MS': 2},
            'STR': {'HP': 120, 'MATK/PATK': 5, 'AP': 2},
            'CON': {'HP': 400, 'PDEF': 2, 'MDEF': 2, 'CRITRes': 2}
    },
    #Fighter's basic stats
    'ft':
    {
        'INS': {'HP': 240, 'MATK/PATK': 2, 'AP':4, 'CDR': 4},
        'INT': {'HP': 120, 'MS': 2},
        'DEX': {'HP': 240, 'MATK/PATK': 2, 'CRIT': 4, ' MS': 4},
        'STR': {'HP': 120, 'MATK/PATK': 5, 'AP': 2},
        'CON': {'HP': 400, 'PDEF': 2, 'MDEF': 2, 'CRITRes': 2}
    },
    #Blade Master's basic stats
    'bm':
    {
        'INS': {'HP': 240, 'MATK/PATK': 2, 'AP':4, 'CDR': 4},
        'INT': {'HP': 120, 'MS': 2},
        'DEX': {'HP': 240, 'MATK/PATK': 2, 'CRIT': 4, ' MS': 4},
        'STR': {'HP': 120, 'MATK/PATK': 5, 'AP': 2},
        'CON': {'HP': 400, 'PDEF': 2, 'MDEF': 2, 'CRITRes': 2}
    },
    #Thank you for basic stats info from https://www.mrguider.org/ written by Yatin

    #Phantom sound's basic stats
    'ps':
    {
        'INS': {'HP': 240, 'MATK/PATK': 2, 'AP':4,'CDR':4},
        'INT': {'HP': 120, 'MATK/PATK':5, 'MS':2},
        'DEX': {'HP': 240, 'MATK/PATK': 2, 'CRIT':2, 'MS':6},
        'STR': {'HP': 120, 'AP': 2},
        'CON': {'HP': 400, 'PDEF': 2,'MDEF': 2,'CRITRes': 2}
    }
}

gem = {
    1:{'value':1,'gem5':'0','essense':'0','dm_gem5':'0','dm_essense':'0','gold': '0','dm_total': '0'},
    2:{'value':2,'gem5':'0','essense':'0','dm_gem5':'0','dm_essense':'0','gold': '1,000','dm_total': '0'},
    3:{'value':4,'gem5':'0','essense':'0','dm_gem5':'0','dm_essense':'0','gold': '3,000','dm_total': '0'},
    4:{'value':8,'gem5':'0','essense':'0','dm_gem5':'0','dm_essense':'0','gold': '7,000','dm_total': '0'},
    5:{'value':12,'gem5':'1','essense':'0','dm_gem5':'48','dm_essense':'0','gold': '15,000','dm_total': '48'},
    6:{'value':20,'gem5':'2','essense':'0','dm_gem5':'96','dm_essense':'0','gold': '31,000','dm_total': '96'},
    7:{'value':32,'gem5':'4','essense':'0','dm_gem5':'192','dm_essense':'0','gold': '63,000','dm_total': '192'},
    8:{'value':50,'gem5':'8','essense':'0','dm_gem5':'384','dm_essense':'0','gold': '128,000','dm_total': '384'},
    9:{'value':70,'gem5':'16','essense':'0','dm_gem5':'768','dm_essense':'0','gold': '258,000','dm_total': '768'},
    10:{'value':92,'gem5':'32','essense':'1','dm_gem5':'1,536','dm_essense':'247','gold': '518,000','dm_total': '1,783'},
    11:{'value':120,'gem5':'64','essense':'3','dm_gem5':'3,072','dm_essense':'741','gold': '1,038,000','dm_total': '3,813'},
    12:{'value':150,'gem5':'128','essense':'7','dm_gem5':'6,144','dm_essense':'1,729','gold': '2,078,000','dm_total': '7,873'},
    13:{'value':210,'gem5':'256','essense':'15','dm_gem5':'12,288','dm_essense':'3,705','gold': '4,158,000','dm_total': '15,993'},
    14:{'value':290,'gem5':'512','essense':'31','dm_gem5':'24,576','dm_essense':'7,657','gold': '8,318,000','dm_total': '32,233'},
    15:{'value':410,'gem5':'1,024','essense':'63','dm_gem5':'49,152','dm_essense':'15,561','gold': '16,638,000','dm_total': '64,713'},
    16:{'value':620,'gem5':'2,048','essense':'127','dm_gem5':'98,304','dm_essense':'31,369','gold': '33,278,000','dm_total': '129,673'},
    17:{'value':930,'gem5':'4,096','essense':'255','dm_gem5':'196,608','dm_essense':'62,985','gold': '66,558,000','dm_total': '259,593'},
    18:{'value':1250,'gem5':'8,192','essense':'511','dm_gem5':'393,216','dm_essense':'126,217','gold': '133,118,000','dm_total': '519,433'},
    19:{'value':1720,'gem5':'16,384','essense':'1,023','dm_gem5':'786,432','dm_essense':'252,681','gold': '266,238,000','dm_total': '1,039,113'}

    #Thank you for info gem lvl 1-15 from https://dragonrajamobile.fandom.com/wiki/Core
}

#define stats for each gem type based on Puppeteer
gemStat = {}
gemStat["fire"] = cls['pp']["INT"]
gemStat["wind"] = cls['pp']["DEX"]
gemStat["water"] = cls['pp']["INS"]
gemStat["earth"] = cls['pp']["CON"]

bs = ["HP","MATK\PATK","CDR","AP","CRIT","MS","PDEF","MDEF","CRITRes"]

bot = commands.Bot(command_prefix='>') #กำหนด Prefix
bot.remove_command("help")

bot.event
async def on_ready() : #เมื่อระบบพร้อมใช้งาน
    print("Bot Started!") #แสดงผลใน CMD

@bot.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title = "Help", color=discord.Color.green(), description = "Hello! This is muti-calculator for Dragon Raja (Main server as SEA)")
    em.add_field(name="Short name of Each class", value="Basic of using this bot is using short name of each clase following by these:\n:droplet:  `sd`  = Souldancer \n:skull_crossbones: `rp`  = Reaper\n:cloud_tornado:  `an`  = Assasin\n:polar_bear:  `pp`  = Puppeteer\n:microphone:   `ps`  = Phantom Sound\n:gun:  `gs`  = Gunslinger\n:robot:  `ft`  = Fighter\n:crossed_swords:  `bm`  = Blade Master", inline=True)
    em.add_field(name="Calculator commands:", value = ":round_pushpin:  `cb`\nBasic stat calculator for specific class\n:round_pushpin: `cbp`\nCompare between 2 basic stats\n:round_pushpin:  `cg`\nGem calculator\n:round_pushpin:  `cgp`\nCompare between 2 gems\n:round_pushpin:  `cp`\nCore plan calculator\n:round_pushpin:  `cpp`\nCompare between 2 core plans",inline=True)
    em.add_field(name=":loudspeaker: Notice :loudspeaker: ",value="1. This bot command prefix is `>`\n2. The first `c` in command is mean `Calculate` and the last `p` is mean `Compare`\n3. Use `>help` `<Command>` for check How to use it",inline=False)
    await ctx.send(embed=em)

@help.command()
async def cb(ctx):
    em = discord.Embed(title = ":grey_question: How to use : Basic stat calculator `>cb`", color=discord.Color.green(), description = "Basic stat calculator use for calculate basic stats are INT, INS, CON, DEX, STR")
    em.add_field(name=":arrow_down_small: Syntax :arrow_down_small: ", value="**Stat type**\n`INT`  `INS`  `CON`\n`DEX`  `STR`\nNeed  __**3**__  values\n`>cb` `<Class>` `<Stat>` `<Value>`", inline=True)
    em.add_field(name=":arrow_down_small:  Example :arrow_down_small: ", value = "`>cb` `sd` `int` `100`",inline=True)
    await ctx.send(embed=em)

@help.command()
async def cbp(ctx):
    em = discord.Embed(title = ":grey_question: How to use : Compare between 2 basic stats `>cbp`", color=discord.Color.green(), description = "Compare between 2 basic stats use for comparing between 2 basic stats of the class")
    em.add_field(name=":arrow_down_small:  Syntax :arrow_down_small: ", value="**Stat type**\n`INT`  `INS`  `CON`\n`DEX`  `STR`\nNeed  __**5**__  values\n`>cbp` `<Class>` `<Stat1>` `<Value1>` `<Stat2>` `<Value2>`", inline=True)
    em.add_field(name=":arrow_down_small:  Example :arrow_down_small: ", value = "`>cbp` `sd` `int` `100` `con` `50`",inline=True)
    await ctx.send(embed=em)

@help.command()
async def cp(ctx):
    em = discord.Embed(title = ":grey_question: How to use : Core plan calculator `>cp`", color=discord.Color.green(), description = "Making a Core plan for calculate the value of each gem and total of each stat")
    em.add_field(name=":arrow_down_small:  Syntax :arrow_down_small: ", value="Need  __**5**__  values\n`>cp` `<Fire>` `<Water>` `<Wind>` `<Earth>` `<Lv. of gem>`", inline=False)
    em.add_field(name=":arrow_down_small:  Example :arrow_down_small: ", value = "``>cp` `5` `1` `9` `0` `10`\nIt's mean Fire 5 Water 1 Wind 9 Earth 0 and  Gem's level 10",inline=False)
    em.add_field(name=":loudspeaker: Notice :loudspeaker: ",value="1. This Calculator doesn't support spirit gem\n2. This Calculator only support gem lvl 1-19\n3. The Max value must equal or less than 9\n4. If the value is 9 rest must less than 5",inline=False)
    await ctx.send(embed=em)

@help.command()
async def cpp(ctx):
    em = discord.Embed(title = ":grey_question: How to use : Compare between 2 core plans `>cpp`", color=discord.Color.green(), description = "Compare between 2 Core plans for calculate the value of each gem and total of each stat and compare them")
    em.add_field(name=":arrow_down_small:  Syntax :arrow_down_small: ", value="Need  __**9**__  values\n`>cpp` `<Plan1:Fire>` `<Plan1:Water1>` `<Plan1:Wind1>` `<Plan1:Earth1>` `<Plan2:Fire2>` `<Plan2:Water2>` `<Plan2:Wind2>` `<Plan2:Earth2>` `<Lv. of gem>`", inline=False)
    em.add_field(name=":arrow_down_small:  Example :arrow_down_small: ", value = "`>cpp` `5` `2` `0` `9` `5` `1` `1` `9` `10`\nIt's mean Plan1 : Fire 5 Water 2 Wind 0 Earth 9\nPlan2 : Fire 5 Water 1 Wind 1 Earth 9\nGem's level 10",inline=False)
    em.add_field(name=":loudspeaker: Notice :loudspeaker: ",value="1. This Calculator doesn't support spirit gem\n2. This Calculator only support gem lvl 1-19\n3. The Max value must equal or less than 9\n4. If the value is 9 rest must less than 5")
    await ctx.send(embed=em)

@help.command()
async def cg(ctx):
    em = discord.Embed(title = ":grey_question: How to use : Gem Calculator `>cg`", color=discord.Color.green(), description = "Gem Calculator use for calculate stats in each gem")
    em.add_field(name=":arrow_down_small: Syntax :arrow_down_small: ", value="**Gem type**\n❤ Fire  `f`    💙 Water  `wt`\n💚 Wind `wd`    💛 Earth  `e`\nNeed  __**2**__  values\n`>cg` `<Gem type>` `<Gem's lvl>`", inline=True)
    em.add_field(name=":loudspeaker: Notice :loudspeaker: ",value="1. This Calculator doesn't support spirit gem\n2.This Calculator only support gem lvl 1-19\n3. the diamonds cost are using lowest prize of gem lv 5 (💎 48) and essense (💎 247)",inline=True)
    em.add_field(name=":arrow_down_small:  Example :arrow_down_small: ", value = "`>cg` `wt` `10`",inline=False)
    await ctx.send(embed=em)

@help.command()
async def cgp(ctx):
    em = discord.Embed(title = ":grey_question: How to use : Compare between 2 gems `>cgp`", color=discord.Color.green(), description = "Compare between 2 gems  use for calculate stats in each gem and compare")
    em.add_field(name=":arrow_down_small: Syntax :arrow_down_small: ", value="**Gem type**\n❤ Fire  `f`    💙 Water  `wt`\n💚 Wind `wd`    💛 Earth  `e`\nNeed  __**4**__  values\n`>cg` `<Gem type1>` `<Gem's lvl1>` `<Gem type2>` `<Gem's lvl2>`", inline=True)
    em.add_field(name=":loudspeaker: Notice :loudspeaker: ",value="1. This Calculator doesn't support spirit gem\n2.This Calculator only support gem lvl 1-19\n3. the diamonds cost are using lowest prize of gem lv 5 (💎 48) and essense (💎 247)",inline=True)
    em.add_field(name=":arrow_down_small:  Example :arrow_down_small: ", value = "`>cg` `wt` `10` `fire` `10`",inline=False)
    await ctx.send(embed=em)



@bot.event
async def on_message(message) :
    await bot.process_commands(message) #bot.process_commands = wait for commands 


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.CommandNotFound):
        em = discord.Embed(title = ":no_entry_sign: Command doesn't exit!", color=discord.Color.red(), description = "You can check all commands by using >help")
        await ctx.send(embed=em)
    if isinstance(error, discord.ext.commands.errors.UserInputError):
        em = discord.Embed(title = ":no_entry_sign: Command syntax error!", color=discord.Color.red(), description = "You can check command's syntax by using >help <command>")
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title = ":no_entry_sign: Sorry something error!", color=discord.Color.red())
        await ctx.send(embed=em)

def corePlan(fire:int,water:int,wind:int,earth:int,lvl:int):
    #define values from para of each gem
    gl = {"fire":fire,"water":water,"wind":wind,"earth":earth}
    copy_gl = dict(gl)
    ls = []
    check = sum(gl.values())
    if lvl >0 and lvl <= 19:
        if check > 0 and check <= 16:   #check total of gem it's must be 1-19
            for k,v in gl.items():       #check each value in dict
                max_value = max(gl.values())
                if v > 9:               #if some gem > 9 = not ok
                    return "{} {} is not ok".format(v,str.upper(k))
                else:
                    if v <= 9:
                        copy_gl.pop(k)
                        max_copy = max(copy_gl.values())
                        if v ==9 and max_copy>5:
                            return "{} {} is not ok".format(max_copy,str.upper(k))
                        else:
                            for k,v in gl.items():    #loop for find value of each gem from number of gem * lvl's value                         
                                for kk,vv in gemStat[k].items(): #kk = key2 vv = value2
                                    cal = v*gemStat[k][kk]*gem[lvl]['value']
                                    temp = [kk,cal]
                                    ls.append(temp)
                        #make new list 
                        newlist = [[':heart: FIRE',ls[0:3]],[':blue_heart: WATER',ls[3:7]],[':green_heart: WIND',ls[7:11]],[':yellow_heart: EARTH',ls[11:15]]] # make new list for split stat to each core start from fire, water, wind,earth
                        return newlist
        else:
            return "Total of gem must have value between 1-16"
    else:
        return "Sorry! Now, the bot only support gem lvl 1-19!"

def sumCore(l:list):
    valuesOfStat = [] #sort by HP>ATK>CDR>AP>CRIT>MS>PDEF>MDEF>CRITRes
    sum_hp=0
    sum_atk=0
    sum_cdr=0
    sum_ap=0
    sum_crit=0
    sum_ms=0
    sum_pdef=0
    sum_mdef=0
    sum_cres=0
    for i in l:
        for j in i[1]:
            if 'HP' in j:
                sum_hp += j[1]
            elif 'MATK/PATK' in j:
                sum_atk += j[1]
            elif 'CDR' in j:
                sum_cdr += j[1]
            elif 'AP' in j:
                sum_ap += j[1]
            elif 'CRIT' in j:
                sum_crit += j[1]
            elif 'MS' in j:
                sum_ms += j[1]
            elif 'PDEF' in j:
                sum_pdef += j[1]
            elif 'MDEF' in j:
                sum_mdef += j[1]
            else:
                sum_cres += j[1]
    valuesOfStat=[sum_hp,sum_atk,sum_cdr,sum_ap,sum_crit,sum_ms,sum_pdef,sum_mdef,sum_cres]
    return valuesOfStat

#Calculate a stat by specific class
def calStat(cname:str, stype:str, num:int): #cname = class name || stype = stat type||num = number of stat
    ls = []
    cname = str.lower(cname)
    stype = str.upper(stype)
    if cname in cls.keys():      #use str.lower() and str.upper() for ignore incencitive case
        if stype in cls[cname].keys():
            for k, v in cls[cname][stype].items():    #loop all key and values in cls>(class name)>stat type
                cal = cls[cname][stype][k]*num
                withSign = addSign(k)
                temp = [withSign,cal]
                ls.append(temp)
            return ls
        else:
            return ":no_entry_sign: Sorry, {} is not base stat!".format(stype)
    else: 
        return ":no_entry_sign: Sorry, {} doesn't exit!".format(cname)

def addSign(msg:str):
    if 'HP' in msg:
        msg = ":drop_of_blood: {}".format(msg)  
    elif 'MATK/PATK' in msg:
        msg = ":crossed_swords: {}".format(msg)
    elif 'CDR' in msg:
        msg = ":stopwatch: {}".format(msg)
    elif 'AP' in msg:
        msg = ":syringe: {}".format(msg)
    elif 'CRIT' in msg:
        msg = ":boom: {}".format(msg)
    elif 'MS' in msg:
        msg = ":magic_wand: {}".format(msg)
    elif 'PDEF' in msg:
        msg = ":beginner: {}".format(msg)
    elif 'MDEF' in msg:
        msg = ":shield: {}".format(msg)
    else:
        msg = ":man_running: {}".format(msg)
    return msg

def compare(data1:int,data2:int):
    subt = 0
    if data1 > data2:
        subt = data1 - data2
        return "d1   :thumbsup:    **{}**".format(subt)   #define text d1 > d2
    elif data2 > data1:
        subt = data2 - data1
        return "d2   :thumbsup:    **{}**".format(subt)   #define text d2 > d1
    else:
        return "equal"

def calGem(ele:str,lvl:int):
    ele = str.lower(ele)
    ls = []
    if lvl > 0 and lvl <= 19:
        lvl = gem[lvl]['value']
        if ele == 'fire' or ele == 'f':
            ls.append('fire')
            for k,v in gemStat['fire'].items():
                cal = v*lvl
                withSign = addSign(k)
                temp = withSign,cal
                ls.append(temp)
            return ls
        elif ele == 'water' or ele == 'wt':
            ls.append('water')
            for k,v in gemStat['water'].items():
                cal = v*lvl
                withSign = addSign(k)
                temp = withSign,cal
                ls.append(temp)
            return ls
        elif ele == 'wind' or ele == 'wd':
            ls.append('wind')
            for k,v in gemStat['wind'].items():
                cal = v*lvl
                withSign = addSign(k)
                temp = withSign,cal
                ls.append(temp)
            return ls
        elif ele == 'earth' or ele == 'e':
            ls.append('earth')
            for k,v in gemStat['earth'].items():
                cal = v*lvl
                withSign = addSign(k)
                temp = withSign,cal
                ls.append(temp)
            return ls
        else:
            return "Sorry, {} doesn't exit!".format(ele)
    else:
        return "Sorry! Now, the bot only support gem lvl 1-19!"

@bot.command()
async def cb(ctx, cname:str, stype:str, num:int) : #specific num must be int 
    ls = calStat(cname, stype, num)
    msg = ""
    if type(ls) is list:
        for i in ls:
            msg+="{} : {}\n".format(i[0],i[1])
        em = discord.Embed(title = ":writing_hand: Result {} {} of  {} \n".format(num,str.upper(stype),str.upper(cname)), description=msg, color=discord.Color.blue())
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "{}".format(ls))
        await ctx.send(embed=em)

@bot.command()
async def cbp(ctx,cname1:str, stype1:str, num1:int,stype2:str, num2:int) : #specific num must be int 
    msg1 = ""
    msg2 = ""
    cname2 = cname1
    c1 = calStat(cname1, stype1, num1)
    c2 = calStat(cname2, stype2, num2)
    if type(c1) is list and type(c2) is list:
        for i in c1:
            msg1 +="{} : {}\n".format(i[0],i[1])
        for i in c2:
            msg2 +="{} : {}\n".format(i[0],i[1])
        em = discord.Embed(title = ":straight_ruler:  Comparision between {} {} and {} {} of  {} ".format(num1,str.upper(stype1),num2,str.upper(stype2),str.upper(cname1)), color=discord.Color.blue())
        em.add_field(name = ":writing_hand: Result {} {} of  {}  \n".format(num1,str.upper(stype1),str.upper(cname1)),value=msg1)
        em.add_field(name = ":writing_hand: Result {} {} of  {}  \n".format(num2,str.upper(stype2),str.upper(cname2)),value=msg2)
        await ctx.send(embed=em)
    elif type(c1) != list and type(c2) != list:
        em = discord.Embed(title = "Error! Both plans are not correct", color=discord.Color.red(), description = "You can check how to use this by using >help <Command's name>")
        em.add_field(name="Error Plan 1!",value="{}".format(c1))
        em.add_field(name="Error Plan 2!",value="{}".format(c2))
        await ctx.send(embed=em)
    elif type(c1) is str:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "{}".format(c1))
        await ctx.send(embed=em)
    elif type(c2) is str:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "{}".format(c2))
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "Sorry, Something is not correct!")
        await ctx.send(embed=em)

@bot.command()
async def cp(ctx,fire:int,water:int,wind:int,earth:int,lvl:int) : #specific num must be int 
    ls = corePlan(fire, water, wind, earth, lvl)
    msg = ""
    smsg = ""
    if type(ls) is list:
        sCore = sumCore(ls)
        em = discord.Embed(title = ":writing_hand: Result Core plan Lv. {}".format(lvl), color=discord.Color.blue()) #"**Thesea are basic stats values based on Souldancer\nBut you can use ><Class Short Name> for checks stat's value"
        for i in ls:
            msg+="\n**{}**\n".format(i[0])
            for j in i[1]:
                msg+="{} : {}\n".format(j[0],j[1])
        for i in range(9):
            smsg += "{} : {}\n".format(bs[i],sCore[i])
        em.add_field(name=":abacus: Sum of each stats", value=smsg, inline=True)
        em.add_field(name="**Fire** {} **Water** {} **Wind** {} **Earth** {}".format(fire,water,wind,earth),value=msg, inline=True)
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "{}".format(ls))
        await ctx.send(embed=em)

@bot.command()
async def cpp(ctx,fire1:int,water1:int,wind1:int,earth1:int,fire2:int,water2:int,wind2:int,earth2:int,lvl:int) : #specific num must be int 
    msg1 = ""       #for each gem values of plan 1
    msg2 = ""       #for each gem values  of plan 2
    cp = ""         #for check condition compare()
    cp1 = ""        #for sum plan 1
    cp2 = ""        #for sum plan 2
    #lvl2 = lvl
    ls1 = corePlan(fire1, water1, wind1, earth1, lvl)
    ls2 = corePlan(fire2, water2, wind2, earth2, lvl)
    if type(ls1) is list and type(ls2) is list:
        sCore1 = sumCore(ls1)
        sCore2 = sumCore(ls2)
        for i in ls1:
            msg1 +="\n**{}**\n".format(i[0])
            for j in i[1]:
                msg1 +="{} : {}\n".format(j[0],j[1])
        for i in ls2:
            msg2 +="\n**{}**\n".format(i[0])
            for j in i[1]:
                msg2 +="{} : {}\n".format(j[0],j[1])
        for i in range(9):
            cp = compare(sCore1[i],sCore2[i])
            if 'd1' in cp:
                cp = cp.replace("d1", "")   #remove definetext "d1"
                cp1 += "{} : {}{}\n".format(bs[i],sCore1[i],cp)
                cp2 += "{} : {}\n".format(bs[i],sCore2[i])
            elif 'd2' in cp:
                cp = cp.replace("d2", "")   #remove definetext "d2"
                cp2 += "{} : {}{}\n".format(bs[i],sCore2[i],cp)
                cp1 += "{} : {}\n".format(bs[i],sCore1[i])
            else:
                cp1 += "{} : {}\n".format(bs[i],sCore1[i])
                cp2 += "{} : {}\n".format(bs[i],sCore2[i])
        em = discord.Embed(title = ":straight_ruler:  Comparision between\nFire {} Water {} Wind {} Earth {} & Fire {} Water {} Wind {} Earth {} Lv {}\n".format(fire1,water1,wind1,earth1,fire2,water2,wind2,earth2,lvl), color=discord.Color.blue())
        em.add_field(name=":abacus: Sum of each stats of Plan 1", value=cp1, inline=True)
        em.add_field(name=":abacus: Sum of each stats of Plan 2", value=cp2, inline=True) 
        em.add_field(name =":loudspeaker: Notice :loudspeaker: ", value = "**Thesea are basic stats values based on Souldancer\nBut you can use ><Class Short Name> for checks stat's value",inline=False)
        em.add_field(name="Fire {} Water {} Wind {} Earth {}".format(fire1,water1,wind1,earth2),value=msg1, inline=True)
        em.add_field(name="Fire {} Water {} Wind {} Earth {}".format(fire2,water2,wind2,earth2),value=msg2, inline=True)       
        await ctx.send(embed=em)
    elif type(ls1) is str and type(ls2) is str:
        em = discord.Embed(title = "Error! Both plan are not correct", color=discord.Color.red(), description = "You can check how to use this by using >help <Command's name>")
        em.add_field(name="Error Plan 1!",value="{}".format(ls1))
        em.add_field(name="Error Plan 2!",value="{}".format(ls2))
        await ctx.send(embed=em)
    elif type(ls1) is str:
        em = discord.Embed(title = "Error! Plan 1", color=discord.Color.red(), description = ls1)
        await ctx.send(embed=em)
    elif type(ls2) is str:
        em = discord.Embed(title = "Error! Plan 2", color=discord.Color.red(), description = ls2)
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "Sorry, Something is not correct!")
        await ctx.send(embed=em)    
    
@bot.command()
async def cg(ctx, ele:str, lvl:int) : #specific num must be int 
    ls = calGem(ele,lvl)
    msg = ""
    name = ls[0]
    copy_ls = ls
    if type(ls) is list:
        copy_ls.remove(name) #remove element name in copy list
        for i in copy_ls:
            msg+="{} : {}\n".format(i[0],i[1])
        em = discord.Embed(title = ":writing_hand: Result  of  *{}*  Lv. *{}*\n".format(str.upper(name),lvl), description="🧮  **Basic stats**\n{}\n:loudspeaker: **Notice** :loudspeaker:\nFor fusion cost below, the diamonds cost are using lowest prize of gem lv 5 (💎 48) and essense (💎 247)\n\n💸  **Fusion cost**\n5️⃣  Use gem lvl 5 : {}\n💎  Diamond : {}\n🧪  Use fusion essence : {}\n💎  Diamond : {}\n💎  *Total of diamond : {}  💎*".format(msg,gem[lvl]['gem5'],gem[lvl]['dm_gem5'],gem[lvl]['essense'],gem[lvl]['dm_essense'],gem[lvl]['dm_total']), color=discord.Color.blue())
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "{}".format(ls))
        await ctx.send(embed=em)

@bot.command()
async def cgp(ctx,ele1:str, lvl1:int,ele2:str, lvl2:int):
    ls1 = calGem(ele1,lvl1)
    ls2 = calGem(ele2,lvl2)
    msg1 = ""
    msg2 = ""
    name1 = ls1[0]
    name2 = ls2[0]
    copy_ls1 = ls1
    copy_ls2 = ls2
    if type(ls1) is list and type(ls2) is list:
        copy_ls1.remove(name1)
        copy_ls2.remove(name2)
        for i in ls1:
            msg1 +="{} : {}\n".format(i[0],i[1])
        for i in ls2:
            msg2 +="{} : {}\n".format(i[0],i[1])
        em = discord.Embed(title = ":straight_ruler:  Comparision between **{}**  **{}**  and  **{}**  **{}**".format(str.upper(name1),lvl1,str.upper(name2),lvl2), color=discord.Color.blue())
        em.add_field(name = ":writing_hand: Result  of  **{}**  Lv. **{}**\n".format(str.upper(name1),lvl1),value="🧮  **Basic stats**\n{}\n".format(msg1),inline=True)
        em.add_field(name = ":writing_hand: Result  of  **{}**  Lv. **{}**\n".format(str.upper(name2),lvl2),value="🧮  **Basic stats**\n{}\n".format(msg2),inline=True)
        em.add_field(name=":loudspeaker: Notice :loudspeaker: ",value="For fusion cost below, the diamonds cost are using lowest prize of gem lv 5 (💎 48) and essense (💎 247)",inline=False)
        em.add_field(name = ":writing_hand: Result  of  **{}**  Lv. **{}**\n".format(str.upper(name1),lvl1),value="💸  **Fusion cost**\n5️⃣  Use gem lvl 5 : {}\n💎  Diamond : {}\n🧪  Use fusion essence : {}\n💎  Diamond : {}\n💎  *Total of diamond : {}  💎*".format(gem[lvl1]['gem5'],gem[lvl1]['dm_gem5'],gem[lvl1]['essense'],gem[lvl1]['dm_essense'],gem[lvl1]['dm_total']),inline=True)
        em.add_field(name = ":writing_hand: Result  of  **{}**  Lv. **{}**\n".format(str.upper(name2),lvl2),value="💸  **Fusion cost**\n5️⃣  Use gem lvl 5 : {}\n💎  Diamond : {}\n🧪  Use fusion essence : {}\n💎  Diamond : {}\n💎  *Total of diamond : {}  💎*".format(gem[lvl2]['gem5'],gem[lvl2]['dm_gem5'],gem[lvl2]['essense'],gem[lvl2]['dm_essense'],gem[lvl2]['dm_total']),inline=True)
        await ctx.send(embed=em)
    elif type(ls1) != list and type(ls2) != list:
        em = discord.Embed(title = "Error! Both plans are not correct", color=discord.Color.red(), description = "You can check how to use this by using >help <Command's name>")
        em.add_field(name="Error Plan 1!",value="{}".format(ls1))
        em.add_field(name="Error Plan 2!",value="{}".format(ls2))
        await ctx.send(embed=em)
    elif type(ls1) is str:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "{}".format(ls1))
        await ctx.send(embed=em)
    elif type(ls2) is str:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "{}".format(ls2))
        await ctx.send(embed=em)
    else:
        em = discord.Embed(title = "Error!", color=discord.Color.red(), description = "Sorry, Something is not correct!")
        await ctx.send(embed=em)

@bot.command()
async def sd(ctx):
    msg = ""
    for i in cls['sd']:
        msg+="\n▶  **"+i+"**\n"
        for j,v in  cls['sd'][i].items():       #J is key of cls['sd'][i]
            withSign = addSign(j)
            msg+="{} : {}\n".format(withSign,v)
    em = discord.Embed(title = ":droplet:  Basic stats value of Souldancer".format(), description=msg, color=discord.Color.blue())
    await ctx.send(embed=em)

@bot.command()
async def rp(ctx):
    msg = ""
    for i in cls['rp']:
        msg+="\n▶  **"+i+"**\n"
        for j,v in  cls['rp'][i].items():       #J is key of cls['sd'][i]
            withSign = addSign(j)
            msg+="{} : {}\n".format(withSign,v)
        #print(msg)
    em = discord.Embed(title = ":skull_crossbones:  Basic stats value of Reaper".format(), description=msg, color=discord.Color.blue())
    await ctx.send(embed=em)

@bot.command()
async def an(ctx):
    msg = ""
    for i in cls['an']:
        msg+="\n▶  **"+i+"**\n"
        for j,v in  cls['an'][i].items():       #J is key of cls['sd'][i]
            withSign = addSign(j)
            msg+="{} : {}\n".format(withSign,v)
        #print(msg)
    em = discord.Embed(title = ":cloud_tornado:  Basic stats value of Assasin".format(), description=msg, color=discord.Color.blue())
    await ctx.send(embed=em)

@bot.command()
async def pp(ctx):
    msg = ""
    for i in cls['pp']:
        msg+="\n▶  **"+i+"**\n"
        for j,v in  cls['pp'][i].items():       #J is key of cls['sd'][i]
            withSign = addSign(j)
            msg+="{} : {}\n".format(withSign,v)
        #print(msg)
    em = discord.Embed(title = ":polar_bear:  Basic stats value of Puppeteer".format(), description=msg, color=discord.Color.blue())
    await ctx.send(embed=em)

@bot.command()
async def gs(ctx):
    msg = ""
    for i in cls['gs']:
        msg+="\n▶  **"+i+"**\n"
        for j,v in  cls['gs'][i].items():       #J is key of cls['sd'][i]
            withSign = addSign(j)
            msg+="{} : {}\n".format(withSign,v)
        #print(msg)
    em = discord.Embed(title = ":gun:  Basic stats value of Gunslinger".format(), description=msg, color=discord.Color.blue())
    await ctx.send(embed=em)

@bot.command()
async def ft(ctx):
    msg = ""
    for i in cls['ft']:
        msg+="\n▶  **"+i+"**\n"
        for j,v in  cls['ft'][i].items():       #J is key of cls['sd'][i]
            withSign = addSign(j)
            msg+="{} : {}\n".format(withSign,v)
        #print(msg)
    em = discord.Embed(title = ":robot:  Basic stats value of Fighter".format(), description=msg, color=discord.Color.blue())
    await ctx.send(embed=em)

@bot.command()
async def bm(ctx):
    msg = ""
    for i in cls['bm']:
        msg+="\n▶  **"+i+"**\n"
        for j,v in  cls['bm'][i].items():       #J is key of cls['sd'][i]
            withSign = addSign(j)
            msg+="{} : {}\n".format(withSign,v)
        #print(msg)
    em = discord.Embed(title = ":crossed_swords:  Basic stats value of Blade Master".format(), description=msg, color=discord.Color.blue())
    await ctx.send(embed=em)

@bot.command()
async def ps(ctx):
    msg = ""
    for i in cls['ps']:
        msg+="\n▶  **"+i+"**\n"
        for j,v in  cls['ps'][i].items():       #J is key of cls['sd'][i]
            withSign = addSign(j)
            msg+="{} : {}\n".format(withSign,v)
        #print(msg)
    em = discord.Embed(title = ":microphone:  Basic stats value of Phantom Sound".format(), description=msg, color=discord.Color.blue())
    await ctx.send(embed=em)

keep_alive()
bot.run(os.getenv('TOKEN')) 