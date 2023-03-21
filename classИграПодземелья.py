import time
import random

class Character:
    def __init__(self,name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        
        
class Player:
    def __init__(self, name,hp,damage):
        self.name=name
        self.hp=hp
        self.damage=damage
        self.level=1
        self.expiriens=0
    def create_person(class_type,race_type):
        hp=0
        damage=0
        if class_type==class_list[0]:
            hp+=100
            damage+=200
            #return Player(name,hp,damage)
        elif class_type==class_list[1]:
            hp+=12
            damage+=3
            #return Player(name,hp,damage)
        elif class_type==class_list[2]:
            hp+=3
            damage+=3
            #return Player(name,hp,damage)
        elif class_type==class_list[3]:
            hp+=1
            damage+=3
            #return Player(name,hp,damage)
        else:
            print("Что-то пошло не так, класс не найден")
        if race_type==race_list[0]:
            hp+=300
            damage+=200
            #return Player(name,hp,damage)
        elif race_type==race_list[1]:
            hp+=8
            damage+=5
            #return Player(name,hp,damage)
        elif race_type==race_list[2]:
            hp+=2
            damage+=1
            #return Player(name,hp,damage)
        elif race_type==race_list[3]:
            hp+=5
            damage-=2
            #return Player(name,hp,damage)
        elif race_type==race_list[4]:
            hp+=2
            damage+=3

            
        else:
            print("Что-то пошло не так, расса не найдена")
        return Player(name,hp,damage)
    
    def lvlup():
        player.expiriens=0
        player.hp+=5*player.level
        player.damage+= 5.5*player.level        
        player.level+=1       
        print("Ваш уровень повысился! Теперь у Вас:%s"%player.level)
        return player.level        
            
    def create_armor():
        rnd_armor_type=armor_type_list[random.randint(0,len(armor_type_list)-1)]
        rnd_armor_rare=random.choice(list(armor_rare_dict.keys()))
        if rnd_armor_type==armor_type_list[0]:
            player.hp+=4*rnd_armor_rare
        elif rnd_armor_type==armor_type_list[1]:
            player.hp+=5*rnd_armor_rare
        elif rnd_armor_type==armor_type_list[2]:
            player.hp+=6*rnd_armor_rare
        return rnd_armor_type,armor_rare_dict[rnd_armor_rare]
    
    def create_wearpon():
        rnd_wpn_type=wearpon_type_list[random.randint(0,len(wearpon_type_list)-1)]
        rnd_wpn_rare=random.choice(list(wearpon_rare_dict.keys()))
        if rnd_wpn_type==wearpon_type_list[0]:
            player.damage+=4*rnd_wpn_rare
        elif rnd_wpn_type==wearpon_type_list[1]:
            player.damage+=5*rnd_wpn_rare
        elif rnd_wpn_type==wearpon_type_list[2]:
            player.damage+=6*rnd_wpn_rare
        return rnd_wpn_type,wearpon_rare_dict[rnd_wpn_rare]    
     
    def create_heal():
        rnd_heal_size=random.choice(list(heal_size_choice.keys()))
        player.hp+=rnd_heal_size
        return heal_size_choice[rnd_heal_size]
    def attack(self,victim):
        batle=random.randint(0,2)
        if batle==0:
            print("Крит удар! Вы нанесли врагу: ", self.damage*2,"урона.")
            time.sleep(0.5)
            victim.hp-=self.damage*2
        elif batle==1:
            print("Ой-ёй... Вы промахнулись")
            time.sleep(0.5)
        else:
            print(self.name,"Нанёс удар:%s"%self.damage)
            time.sleep(0.5)
            victim.hp-=self.damage

        if victim.hp<=0:
            print(victim.name,"Повержен. +10 опыта")
            time.sleep(0.5)
            self.expiriens+=10
            print('Ваш опыт', self.expiriens)
            expiriens=1+ self.level*50
            if self.expiriens>=expiriens:
                Player.lvlup()            
            
            heal_wearpon_choice=random.choice(choice_list)
            if heal_wearpon_choice=="wearpon":
                wearpon=Player.create_wearpon()
                print("Вам выпало новое оружие! %s %s."%(wearpon[0], wearpon[1]))
                time.sleep(0.5)
            elif heal_wearpon_choice=="armor":
                armor=Player.create_armor()
                print("Вам выпала новая броня! %s %s."%(armor[0], armor[1]))
                time.sleep(0.5)
            elif heal_wearpon_choice=="heal":
                heal=Player.create_heal()
                print("Вам выпала %s" %heal)
                time.sleep(0.5)
            else:
                time.sleep(1)
                print("Награды нет... Повезет в следующий раз.")
            
            '''if self.expiriens==100:
                self.expiriens=0
                self.level+=1
                print("Поздравляем,Ваш уровень повысился. Уровень:",self.level)
                self.hp+=5
                self.damage+=2'''                
            return False
        else:            
            print(victim.name,"Теперь имеет",victim.hp,"Очков здоровья")
            time.sleep(0.5)
            return True 
    
   
class Enemy(Character):
    def __init__(self,name,hp,damage):
        Character.__init__(self,name,hp,damage)
 
    def create_monstr():
        rnd_name=random.choice(monstr_name)
        rnd_hp=random.choice(monstr_hp)+player.level*6
        #rnd_hp=random.choice(monstr_hp)
        rnd_damage=random.choice(monstr_damage)*player.level*0.5
        #rnd_damage=random.choice(monstr_damage)
        return Enemy(rnd_name, rnd_hp, rnd_damage)
    def attack(self,victim):
        victim.hp-=self.damage
        if victim.hp<=0:
            time.sleep(1)
            print(victim.name,"Повержен. Конец игры.")
            quit()            
        else:
            print(self.name,"Нанёс удар:%s"%self.damage)
            time.sleep(0.5)
            print(victim.name,"Теперь имеет",victim.hp,"Очков здоровья")
            time.sleep(0.5)
            
    def boss():
        boss_hp = monstr.hp*2
        boss_damage = monstr.damage*2
        boos_name = "BOSS"
        return Enemy(boos_name,boss_hp,boss_damage)
    
    def boss_attack(self, victim):
        victim.hp-=self.damage
        if victim.hp<=0:
            time.sleep(1)
            print(victim.name,"Повержен. Конец игры.")
            quit()            
        else:
            #print(self.name,"Нанёс удар:%s"%self.damage)
            time.sleep(0.5)
            print(victim.name,"Теперь имеет",victim.hp,"Очков здоровья")
            time.sleep(0.5)
def fight_choice():
    answer=int(input("Атаковать (нажми на 1) или бежать(нажми на 2)?\n"))
    if answer==1:
        win_loose=player.attack(monstr)
        if win_loose==True:
            time.sleep(0.5)
            monstr.attack(player)
            fight_choice()
    elif answer==2:
        plan=random.choice(nymer)
        if plan==0:
            print("Побег не удался. Вы подвергаетесь нападению монстра")
            monstr.attack(player)
            fight_choice()
        elif plan==1:
            print("Вы сбежали от монстра")
    else:
        print("Будь внимательнее, ибо у меня нет такого варианта действий")  
        fight_choice()

def battle_with_boss():
    answer=int(input("Атаковать (нажми на 1) или бежать(нажми на 2)?\n"))
    if answer==1:
        win_loose=player.attack(monstr)
        if win_loose==True:
            time.sleep(0.5)
            monstr.attack(player)
            battle_with_boss()
    elif answer==2:
        plan=random.randint(0,5)
        if plan==0:
            print("Вы сбежали от монстра")            
        else:
            print("Побег не удался. Вы подвергаетесь нападению монстра")
            monstr.attack(player)
            battle_with_boss()
    else:
        print("Будь внимательнее, ибо у меня нет такого варианта действий")  
        battle_with_boss()
    
class_list=["лучник", "воин", "жрец", "маг"]
race_list=["человек", "огр", "гном", "эльф", "панда"]
monstr_name=["скелет", "вампир", "зомби", "цербер"]
monstr_hp=[10, 15, 20, 25, 30]
monstr_damage=[1, 2, 3, 4, 5, 6, 7]
wearpon_type_list=["Меч","Лук","Топор"]
wearpon_rare_dict={1:"Обычный", 2:"Редкий", 3:"Эпический"}
armor_type_list=["Шлем","Нагрудник","Латы"]
armor_rare_dict={1:"Обычный", 2:"Редкий", 3:"Эпический"}
choice_list=("wearpon", "heal", "armor", 0)
heal_size_choice={5:"Малая фляга", 10:"Средняя фляга", 15:"Большая фляга"}
#person=[]
#person.append(input("Как Вас зовут?\n"))
#name=person
name=input("Как Вас зовут?\n")
print("На данный момент доступны классы:")
for i in class_list:
    print(i)
class_type=input("Выберите класс\n").lower()
print("На данный момент доступны рассы:")
for i in race_list:
    print(i)
race_type=input("Выберите рассу\n").lower()
class_type=class_type.lower()
#person.append(race_type)
#person.append(class_type)
player=Player.create_person(class_type,race_type)

#print("Ваше здоровье:",player.hp,"Ваш урон:",player.damage)
#print("Главный герой:",player.name,"Количество Вашего здоровья:",player.hp,"Количество Вашего урона:",player.damage,"Ваш уровень:",player.level)
#print(monstr.name, monstr.hp, monstr.damage)
nymer=[0,1]
while True:
    monstr=Enemy.create_monstr()
    ivent=random.randint(0,2)
    if ivent==0:
        print("Тебе никто не встретился")
        time.sleep(0.5)
    elif ivent==1:
        print("Тебе встретился  монстр")
        time.sleep(0.5)
        print(f"{monstr.name},Здоровья:{monstr.hp},Урон:{monstr.damage}")
        time.sleep(0.5)
        print("Главный герой:",player.name,"Количество Вашего здоровья:",player.hp,"Количество Вашего урона:",player.damage,"Ваш уровень:",player.level, "Очки опыта",player.expiriens)
        time.sleep(0.5)
        fight_choice()
        time.sleep(0.5)
    elif ivent ==2:
        monstr=Enemy.boss()
        print("Тебе встретился  BOSS")
        time.sleep(0.5)
        print(f"Здоровья:{monstr.hp},Урон:{monstr.damage}")
        time.sleep(0.5)
        print("Главный герой:",player.name,"Количество Вашего здоровья:",player.hp,"Количество Вашего урона:",player.damage,"Ваш уровень:",player.level, "Очки опыта",player.expiriens)
        time.sleep(0.5)
        battle_with_boss()
        time.sleep(0.5)
time.sleep(0.5)
