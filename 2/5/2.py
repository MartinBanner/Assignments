# -*- coding: UTF-8 -*-



import sys



class StdoutRedirect:
    def __init__(self):
        self.content = ""

    def write(self, s):
        self.content += s

    def flush(self):
        self.content = ""



class Weapon:
    def __init__(self, name=None, damage=0):
        self.name = name
        self.damage = damage


    def __str__(self):
        return self.stdout_strinize(self.get_inf)


    def stdout_strinize(self, method, *attribute):
        s = ""

        __console__ = sys.stdout

        redirect = StdoutRedirect()
        sys.stdout = redirect

        method(*attribute)
        s = redirect.content

        sys.stdout = __console__
        del(redirect)

        return s[:-2]


    def get_inf(self):
        print("武器名称：{}".format(self.name))
        print("武器伤害：{}".format(self.damage))
        print("***************")



class Armour:
    def __init__(self, name=None, defense=0):
        self.name = name
        self.defense = defense


    def __str__(self):
        return self.stdout_strinize(self.get_inf)


    def stdout_strinize(self, method, *attribute):
        s = ""

        __console__ = sys.stdout

        redirect = StdoutRedirect()
        sys.stdout = redirect

        method(*attribute)
        s = redirect.content

        sys.stdout = __console__
        del(redirect)

        return s[:-2]


    def get_inf(self):
        print("护甲名称：{}".format(self.name))
        print("护甲防御：{}".format(self.defense))
        print("***************")



class Skill:
    def __init__(self, status=False):
        self.status = status


    def __str__(self):
        return self.stdout_strinize(self.get_inf)


    def stdout_strinize(self, method, *attribute):
        s = ""

        __console__ = sys.stdout

        redirect = StdoutRedirect()
        sys.stdout = redirect

        method(*attribute)
        s = redirect.content

        sys.stdout = __console__
        del(redirect)

        return s[:-2]


    def get_inf(self):
        print("技能状态：{0}".format(self.status))
        print("****************")



class Flee(Skill):
    def __init__(self, status=False, flee_count=0):
        Skill.__init__(self, status)

        self.name = "逃跑"
        self.flee_status = False

        self.flee_count = flee_count


    def get_inf(self):
        print("技能“{0}”状态：{1}".format(self.name, self.status))
        print("逃跑次数：{0}".format(self.flee_count))
        print("************")



class Restore(Skill):
    def __init__(self, status=False, restore_amount=0):
        Skill.__init__(self, status)

        self.name = "回复"
        self.restore_status = False

        self.restore_amount = restore_amount


    def get_inf(self):
        print("技能“{0}”状态：{1}".format(self.name, self.status))
        print("每次回复血量：{0}".format(self.restore_amount))
        print("*************")



class People:
    def __init__(self, name=None, damage_base=0, damage_total=0, defense_base=0, defense_total=0, hp=0, hp_max=0):
        self.name = name
        self.damage_base = damage_base
        self.damage_total = damage_total
        self.defense_base = defense_base
        self.defense_total = defense_total
        self.hp = hp
        self.hp_max = hp_max

        self.damage_total = self.damage_base
        self.defense_total = self.defense_base

        if self.hp_max < self.hp:
            self.hp_max = self.hp


    def __str__(self):
        return self.stdout_strinize(self.get_inf)


    def stdout_strinize(self, method, *attribute):
        s = ""

        __console__ = sys.stdout

        redirect = StdoutRedirect()
        sys.stdout = redirect

        method(*attribute)
        s = redirect.content

        sys.stdout = __console__
        del(redirect)

        return s[:-2]


    def get_inf(self):
        print("姓名：{0}".format(self.name))
        print("伤害：{0}".format(self.damage_total))
        print("防御：{0}".format(self.defense_total))
        print("血量：{0}/{1}".format(self.hp, self.hp_max))
        print("***********")


    def attack(self, enemy):
        print("“{0}”伤害为：{1}".format(self.name, self.damage_total))
        print("“{0}”目前血量为：{1}".format(enemy.name, enemy.hp))
        print("“{0}”攻击“{1}”".format(self.name, enemy.name))
        print("“{0}”受到 {1} 点伤害".format(enemy.name, self.damage_total))

        enemy.hp -= self.damage_total
        if enemy.hp < 0:
            enemy.hp = 0

        print("“{0}”剩余血量为：{1}".format(enemy.name, enemy.hp))
        print("********************")


    def die(self):
        print("“{0}”死亡".format(self.name))
        print("💀💀💀💀💀💀")


class Soldier(People):
    def __init__(self, name=None, damage_base=0, damage_total=0, defense_base=0, defense_total=0, hp=0, hp_max=0, faction=None, weapon=Weapon(), armour=Armour()):
        People.__init__(self, name, damage_base, damage_total, defense_base, defense_total, hp, hp_max)

        self.faction = faction
        self.weapon = weapon
        self.armour = armour

        self.damage_total = self.damage_base + self.weapon.damage
        self.defense_total = self.defense_base + self.armour.defense


    def get_inf(self):
        print("姓名：{0}".format(self.name))
        print("伤害：{0}".format(self.damage_total))
        print("防御：{0}".format(self.defense_total))
        print("血量：{0}/{1}".format(self.hp, self.hp_max))
        print("阵营：{0}".format(self.faction))
        print("武器：{0}".format(self.weapon.name))
        print("护甲：{0}".format(self.armour.name))
        print("***********")


    def attack(self, enemy):
        damage = 0

        print("“{0}”伤害为：{1}".format(self.name, self.damage_total))
        print("“{0}”防御为：{1}，目前血量为：{2}".format(enemy.name, enemy.defense_total, enemy.hp))
        print("“{0}”攻击“{1}”".format(self.name, enemy.name))

        damage = self.damage_total - enemy.defense_total
        if damage < 0:
            damage = 0

        print("“{0}”受到 {1} 点伤害".format(enemy.name, damage))

        enemy.hp -= damage
        if enemy.hp < 0:
            enemy.hp = 0

        print("“{0}”剩余血量为：{1}".format(enemy.name, enemy.hp))
        print("********************")


    def take_weapon(self, weapon):
        self.weapon = weapon

        print("士兵“{0}”装备了武器“{1}”".format(self.name, self.weapon.name))

        self.damage_total = self.damage_base + self.weapon.damage

        print("“{0}”的伤害变为 {1}".format(self.name, self.damage_total))
        print("********************")


    def take_equipment(self, armour):
        self.armour = armour

        print("士兵“{0}”装备了护甲“{1}”".format(self.name, self.armour.name))

        self.defense_total = self.defense_base + self.armour.defense

        print("“{0}”的防御变为 {1}".format(self.name, self.defense_total))
        print("********************")


    def drop_weapon(self):
        pass


    def drop_equipment(self):
        pass



class Hero(Soldier):
    def __init__(self, name=None, damage_base=0, damage_total=0, defense_base=0, defense_total=0, hp=0, hp_max=0, faction=None, weapon=Weapon(), armour=Armour(), skill_flee=Flee(), skill_restore=Restore()):
        Soldier.__init__(self, name, damage_base, damage_total, defense_base, defense_total, hp, hp_max, faction, weapon, armour)

        self.skill_flee = skill_flee
        self.skill_restore = skill_restore


    def get_inf(self):
        print("姓名：{0}".format(self.name))
        print("伤害：{0}".format(self.damage_total))
        print("防御：{0}".format(self.defense_total))
        print("血量：{0}/{1}".format(self.hp, self.hp_max))
        print("阵营：{0}".format(self.faction))
        print("武器：{0}".format(self.weapon.name))
        print("护甲：{0}".format(self.armour.name))
        print("技能“{0}”：{1}".format(self.skill_flee.name, self.skill_flee.status))
        print("技能“{0}”：{1}".format(self.skill_restore.name, self.skill_restore.status))
        print("*****************")


    def flee(self):
        if self.skill_flee.status==True and self.hp>0:
            self.skill_flee.flee_status = True

            print("“{0}”逃跑了".format(self.name))
            print("✈✈✈✈✈✈")

            return True
        elif self.hp > 0:
            print("“{0}”逃跑失败".format(self.name))
            print("☻☻☻☻☻☻☻☻☻☻☻☻")

            return False
        else:
            pass


    def restore(self):
        if self.hp < self.hp_max:
            self.hp += self.skill_restore.restore_amount

            if self.hp >= self.hp_max:
                self.hp = self.hp_max
                self.skill_restore.restore_status = True
                print("“{0}”回复满血".format(self.name))
            else:
                print("“{0}”回复血量 {1}，现在血量：{2}/{3}".format(self.name, self.skill_restore.restore_amount, self.hp, self.hp_max))
        else:
            self.hp = self.hp_max
            self.skill_restore.restore_status = True


    def reentry(self):
        self.skill_flee.flee_status = False
        self.skill_restore.restore_status = False





def gameloop():
    count = 0

    anyhero = False
    herokey = ""
    heros = {}


    LVBU = Hero(name="吕布", damage_base=10, damage_total=10, defense_base=5, defense_total=5, hp=70, hp_max=70, faction="董卓军", weapon=Weapon(name="方天画戟", damage=15), armour=Armour(name="兽面吞头连环铠", defense=10), skill_flee=Flee(status=True, flee_count=0), skill_restore=Restore(status=True, restore_amount=3))

    heros["张飞"] = Hero(name="张飞", damage_base=8, damage_total=8, defense_base=4, defense_total=4, hp=60, hp_max=60, faction="反董卓联盟", weapon=Weapon(name="丈八蛇矛", damage=13), armour=Armour(name="黑光铠", defense=8), skill_flee=Flee(status=True, flee_count=0), skill_restore=Restore(status=True, restore_amount=2))


    while True:
        anyhero = False
        herokey = ""

        for k in heros:
            if heros[k].skill_flee.flee_status==True and heros[k].skill_restore.status==True:
                heros[k].restore()

        if anyhero == False:
            for k in heros:
                if heros[k].skill_flee.flee_status == False:
                    anyhero = True
                    herokey = k
                    print("--------------")
                    print("“{0}”加入战斗".format(heros[herokey].name))
                    print("--------------")
                    break

        if anyhero == False:
            count += 1
            anyhero = True
            herokey = "英雄"+str(count)
            heros[herokey] = Hero(name="英雄"+str(count), damage_base=7, damage_total=7, defense_base=3, defense_total=3, hp=50, hp_max=50, faction="反董卓联盟", weapon=Weapon(name="环首刀", damage=11), armour=Armour(name="环锁铠", defense=6), skill_flee=Flee(status=True, flee_count=0), skill_restore=Restore(status=True, restore_amount=1))
            print("--------------")
            print("“{0}”加入战斗".format(heros[herokey].name))
            print("--------------")


        while True:
            if LVBU.hp <= heros[herokey].damage_total - LVBU.defense_total:
                if LVBU.flee():
                    break

            heros[herokey].attack(LVBU)

            if LVBU.hp <= heros[herokey].damage_total - LVBU.defense_total:
                if LVBU.flee():
                    break

            if LVBU.hp <= 0:
                break


            if heros[herokey].hp <= LVBU.damage_total - heros[herokey].defense_total:
                if heros[herokey].flee():
                    break

            LVBU.attack(heros[herokey])

            if heros[herokey].hp <= LVBU.damage_total - heros[herokey].defense_total:
                if heros[herokey].flee():
                    break

            if heros[herokey].hp <= 0:
                heros[herokey].die()
                del(heros[herokey])
                break


        if LVBU.skill_flee.flee_status == True:
            break

        if LVBU.hp <= 0:
            LVBU.die()
            break


    print("“{0}”打败了“{1}”，“反董卓联盟”胜利了。".format(heros[herokey].name, LVBU.name))
    print("✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿✿")


    del(LVBU)
    del(heros)





gameloop()
