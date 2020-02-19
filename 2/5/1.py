# -*- coding: UTF-8 -*-



class People:
    def __init__(self, name, damage, hp):
        self.name = name
        self.damage = damage
        self.hp = hp



class Hero(People):
    def __init__(self, name, damage, hp, country):
        People.__init__(self, name, damage, hp)
        self.country = country

    def get_inf(self):
        print("姓名：{}".format(self.name))
        print("攻击力：{}".format(self.damage))
        print("当前血量：{}".format(self.hp))
        print("阵营：{}".format(self.country))
        print("**********")

    def attack(self,enemy):
        print(self.name)
        print("攻击力为：{}".format(self.damage))
        print("“{}”目前血量为：{}".format(enemy.name, enemy.hp))
        print("“{}”攻击“{}”".format(self.name,enemy.name))
        enemy.hp-=self.damage
        print("“{}”剩余血量为：{}".format(enemy.name, enemy.hp))
        print("********************")



# 练习1
# 这部分需要同学们新建一个武器类,同时能够将武器赋予某个实例，用以提升攻击力。
# 属性：武器名称、武器伤害值
# 方法：把武器给予某位英雄，赠予后该英雄攻击力为基础攻击力加武器伤害值
class Weapon:
    def __init__(self, name, damage):
        """武器基础属性"""
        # Please code here
        self.name = name
        self.damage = damage

    def get_inf(self):
        print("武器名称：{}".format(self.name))
        print("武器伤害：{}".format(self.damage))
        print("***************")

    def take_weapon(self, hro):
        """将武器给予英雄，英雄攻击力提升"""
        print("将武器“{}”装备给英雄“{}”".format(self.name, hro.name))
        hro.damage+=self.damage
        print("“{}”的攻击力变为 {}".format(hro.name, hro.damage))
        print("********************")



LB = Hero("吕布", 20, 100, "群雄")
ZF = Hero("张飞", 7, 80, "蜀国")


# 练习2
# 新建武器实例,其中包含属性：名称（丈八蛇矛）、伤害值（3）
# 将武器赠与张飞
ZBSM = Weapon("丈八蛇矛", 3)
ZBSM.get_inf()

ZBSM.take_weapon(ZF)


print("\n")


# 练习3
# 显示“ZF”目前信息
# 令“ZF”攻击“LB”
ZF.get_inf()

ZF.attack(LB)
