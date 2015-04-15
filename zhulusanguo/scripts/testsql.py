import sqlite3
import json
import time

print "ok start at:",time.clock()
db = sqlite3.connect("sanguo.db")
cu = db.cursor()

#create city table
cu.execute('create table city(id integer primary key, ename text, cname text, xpos integer, ypos integer, flag integer, capital integer,level integer, hall integer, barrack integer, archer integer, cavalry integer, wizard integer, blacksmith integer, tavern integer, market integer, lumbermill integer, steelmill integer, magictower integer, tower1 integer, tower2 integer, tower3 integer, tower4 integer, warriorCount integer, archerCount integer, cavalryCount integer, wizardCount integer, ballistaCount integer)')
db.commit()

#create index
cu.execute('create index city_ename_index on city(ename)')
cu.execute('create index city_cname_index on city(cname)')
cu.execute('create index city_owner_index on city(flag)')
db.commit()

#now insert record
f = open('cityinfo-test.json')
citydata = json.loads(f.read())
f.close()
for city in citydata:
	sql = "insert into city values("+str(city["id"])+",'"+city["ename"]+"','"+city["cname"]+"',"+str(city["xpos"])+","+str(city["ypos"])+","+str(city["flag"])+","+str(city["capital"])+","+str(city["level"]) +","+str(city["hall"])+","+str(city["barrack"])+","+str(city["archer"])+","+str(city["cavalry"])+","+str(city["wizard"])+","+str(city["blacksmith"])+","+str(city["tavern"])+","+str(city["market"])+","+str(city["lumbermill"])+","+str(city["steelmill"])+","+str(city["magictower"])+","+str(city["tower1"])+","+str(city["tower2"])+","+str(city["tower3"])+","+str(city["tower4"])+","+str(city["warriorCount"])+","+str(city["archerCount"])+","+str(city["cavalryCount"])+","+str(city["wizardCount"])+","+str(city["ballistaCount"]) +")"
	cu.execute(sql)
db.commit()

#now create hero table
cu.execute('create table hero(id integer primary key, cname text, ename text, owner integer, headImage integer, skill1 integer, skill2 integer, skill3 integer, attackImage integer, defendImage integer, city integer, strength integer, intelligence integer, level integer, move integer, article1 integer, article2 integer, attackRange integer, experience integer, alive integer, troopAttack integer, troopMental integer, troopType integer, troopCount integer)')
db.commit()

#create index on hero
cu.execute('create index hero_ename_index on hero(ename)')
cu.execute('create index hero_cname_index on hero(cname)')
cu.execute('create index hero_owner_index on hero(owner)')
cu.execute('create index hero_alive_index on hero(alive)')
db.commit()


#now insert record
f = open('heroes.json')
herodata = json.loads(f.read())
f.close()
for hero in herodata:
	sql = "insert into hero values("+str(hero["id"])+",'"+hero["cname"]+"','"+hero["ename"]+"',"+str(hero["owner"])+","+str(hero["headImage"])+","+str(hero["skill1"])+","+str(hero["skill2"])+","+str(hero["skill3"])+","+str(hero["armyAttackImage"])+","+str(hero["armyDefendImage"])+","+str(hero["city"])+","+str(hero["strength"])+","+str(hero["intelligence"])+","+str(hero["level"])+","+str(hero["move"])+","+str(hero["article1"])+","+str(hero["article2"])+","+str(hero["attackRange"])+","+str(hero["experience"])+","+str(hero["alive"])+","+str(hero["troopAttack"])+","+str(hero["troopMental"])+","+str(hero["troopType"])+","+str(hero["troopCount"]) +")"
	cu.execute(sql)
db.commit()

#cu.execute('create table cityBuild(id integer primary key, hall integer, barrack integer, archer integer, cavalry integer, wizard integer, blacksmith integer, tavern integer, market integer, lumbermill integer, steelmill integer, magictower integer, tower1 integer, tower2 integer, tower3 integer, tower4 integer, warriorCount integer, archerCount integer, cavalryCount integer, wizardCount integer, ballistaCount integer)')
#db.commit()
#need to calculate the hero army , and add together...............
#calculate the hero troop and update the city table

for hero in herodata:
	if hero["troopCount"]>0:
		if hero["troopType"]==1:
			sql = "select warriorCount from city where id="+str(hero["city"])
			cu.execute(sql)
			res = cu.fetchone()
			rc = res[0]
			rc += hero["troopCount"]
			sql = "update city set warriorCount="+str(rc)+" where id="+str(hero["city"])
			cu.execute(sql)
			db.commit()
		elif hero["troopType"]==2:
			sql = "select archerCount from city where id="+str(hero["city"])
			cu.execute(sql)
			res = cu.fetchone()
			rc = res[0]
			rc += hero["troopCount"]
			sql = "update city set archerCount="+str(rc)+" where id="+str(hero["city"])
			cu.execute(sql)
			db.commit()
		elif hero["troopType"]==3:
			sql = "select cavalryCount from city where id="+str(hero["city"])
			cu.execute(sql)
			res = cu.fetchone()
			rc = res[0]
			rc += hero["troopCount"]
			sql = "update city set cavalryCount="+str(rc)+" where id="+str(hero["city"])
			cu.execute(sql)
			db.commit()
		elif hero["troopType"]==4:
			sql = "select wizardCount from city where id="+str(hero["city"])
			cu.execute(sql)
			res = cu.fetchone()
			rc = res[0]
			rc += hero["troopCount"]
			sql = "update city set wizardCount="+str(rc)+" where id="+str(hero["city"])
			cu.execute(sql)
			db.commit()
		elif hero["troopType"]==5:
			sql = "select ballistaCount from city where id="+str(hero["city"])
			cu.execute(sql)
			res = cu.fetchone()
			rc = res[0]
			rc += hero["troopCount"]
			sql = "update city set ballistaCount="+str(rc)+" where id="+str(hero["city"])
			cu.execute(sql)
			db.commit()

cu.execute('select warriorCount,archerCount,cavalryCount,wizardCount,ballistaCount from city')
res = cu.fetchall()
for r in res:
	print r



#create table experience
cu.execute('create table experience(id integer primary key, exp integer)')
cu.execute('create index experience_exp_index on experience(exp)')
db.commit()
exps = [2000, 3200, 4600, 6200, 8000, 10000, 12200, 14700, 17500, 20600, 24320, 28784, 34141, 40569, 48283, 57539, 68647, 81977, 97972, 117166, 140200, 167839, 201007, 240809, 288571, 345885, 414662, 497194, 596233, 715079, 857695, 1028834, 1234201, 1480641, 1776370, 2131244, 2557092, 3068111, 3681333, 4417199, 5300239, 6359887, 7631465, 9157358, 10988429, 13185715, 15822458, 18986549, 22783459]
lv = 2
for ee in exps:
	sql = "insert into experience values("+str(lv)+","+str(ee)+")"
	cu.execute(sql)
	lv += 1
db.commit()




#table playerInfo contain info about player select kingid, year month day
cu.execute('create table playerInfo(kingID integer primary key, year integer, month integer, day integer, savedate text, gold integer, lumber integer, iron integer , inBattle integer, difficulty integer, cityCount integer)')
db.commit()

#table autoIncResource
cu.execute('create table autoIncResource(kingID integer, incGold integer, incWood integer, incIron integer)')
db.commit()

gold = [0,0,0,0,0,0,0,0,0,0,0,0]
wood = [0,0,0,0,0,0,0,0,0,0,0,0]
iron = [0,0,0,0,0,0,0,0,0,0,0,0]
for hero in herodata:
	if hero["owner"]==99:
		continue
	if hero["skill1"]==1:
		#gold
		gold[hero["owner"]] += 1
	elif hero["skill1"]==0:
		iron[hero["owner"]] += 1
	elif hero["skill1"]==2:
		wood[hero["owner"]] += 1

print gold
print wood
print iron

for i in range(12):
	sql = 'insert into autoIncResource values('+ str(i) + ',' + str(gold[i]) + ',' + str(wood[i]) + ',' + str(iron[i]) + ')' 
	cu.execute(sql)
	db.commit()



#table cityWithSpecialHero , security/doctor/water_wheel     41/15/46/
cu.execute('create table cityWithSpecialHero(cityID integer,heroID integer, skillID integer)')
db.commit()

for hero in herodata:
	if hero["skill1"]==41:
		sql = 'insert into cityWithSpecialHero values(' + str(hero["city"]) + ',' + str(hero["id"]) + ',' + str(hero["skill1"]) +')'
		cu.execute(sql)
		db.commit()
	elif hero["skill1"]==46:
		sql = 'insert into cityWithSpecialHero values(' + str(hero["city"]) + ',' + str(hero["id"]) + ',' + str(hero["skill1"]) +')'
		cu.execute(sql)
		db.commit()
	elif hero["skill1"]==15:
		sql = 'insert into cityWithSpecialHero values(' + str(hero["city"]) + ',' + str(hero["id"]) + ',' + str(hero["skill1"]) +')'
		cu.execute(sql)
		db.commit()


#table skillList
cu.execute('create table skillList(skillID integer primary key, cname text, ename text, passive integer, filename text)')
f = open('skills.json')
skilldata = json.loads(f.read())
f.close()
for sk in skilldata:
	sql = "insert into skillList values("+str(sk["id"])+",'"+sk["cname"]+"','"+sk["ename"]+"',"+str(sk["passive"])+",'"+str(sk["skillIcon"]) +"')"
	cu.execute(sql)
db.commit()

#table
#cu.execute('create table battleInfo()')

# turn , a integer in (1,30) , attackOrDefend 1-attack,2-defend, weather 1 sunny,2 rain
cu.execute('create table battleInfo(turn integer, attackOrDefend integer, weather integer, playerLostHP integer, computerLostHP integer)')
db.commit()
# include player side and computer side , heroID = 9999 means camp, heroID = 9000,9001,9002,9003 means tower
# heroState 1 not attack, 2 attacked, 3 retreated 4 defeated
# troopState 1 not attack , 2 attacked , 3 defeated
cu.execute('create table battleHeroInfo(heroID integer primary key, heroState integer, hp integer, mp integer, posx integer, posy integer, troopType integer, troopInitCount integer, troopLost integer, troopPosx integer, troopPosy integer, troopState integer)')
db.commit()

#on select new king,
cu.execute('create table kingInit(kingid integer primary key, gold integer, lumber integer, iron integer, cityCount integer)')
db.commit()

kingCityCount = [0,0,0,0,0,0,0,0,0,0,0,0]
for city in citydata:
	if city["flag"]!=99:
		kid = city["flag"]
		kingCityCount[kid] += 1

cu.execute('insert into kingInit values(0,20000,200,200,'+ str(kingCityCount[0]) +')')
cu.execute('insert into kingInit values(1,10000,100,100,'+ str(kingCityCount[1]) +')')
cu.execute('insert into kingInit values(2,15000,100,100,'+ str(kingCityCount[2]) +')')
cu.execute('insert into kingInit values(3,12000,100,100,'+ str(kingCityCount[3]) +')')
cu.execute('insert into kingInit values(4,10000,100,100,'+ str(kingCityCount[4]) +')')
cu.execute('insert into kingInit values(5,12000,90,90,'+ str(kingCityCount[5]) +')')
cu.execute('insert into kingInit values(6,11000,110,100,'+ str(kingCityCount[6]) +')')
cu.execute('insert into kingInit values(7,9000,130,150,'+ str(kingCityCount[7]) +')')
cu.execute('insert into kingInit values(8,18000,150,150,'+ str(kingCityCount[8]) +')')
cu.execute('insert into kingInit values(9,25000,200,200,'+ str(kingCityCount[9]) +')')
cu.execute('insert into kingInit values(10,8000,80,80,'+ str(kingCityCount[10]) +')')
cu.execute('insert into kingInit values(11,15000,110,110,'+ str(kingCityCount[11]) +')')


#table ai, every turn ai read this table, then increase new resource and troop
cu.execute('create table aiIncrease(difficulty integer primary key, goldInc integer, lumberInc integer, ironInc integer, warriorInc integer, archerInc integer, cavalryInc integer, wizardInc integer, ballistaInc integer)')
cu.execute('insert into aiIncrease values(1,4000,10,10,8,3,2,2,1)')
cu.execute('insert into aiIncrease values(2,4000,10,10,15,8,2,4,1)')
cu.execute('insert into aiIncrease values(3,4000,10,10,30,15,4,8,3)')
cu.execute('insert into aiIncrease values(4,4000,10,10,40,20,6,10,5)')
db.commit()

cu.close()
db.close()
print "finish insert:",time.clock()
