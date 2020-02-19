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



class Weapon:
    def __init__(self, name, damage):
        """武器基础属性"""
        # Please code here
        self.name = name
        self.damage = damage

    def take_weapon(self, hro):
        """将武器给予英雄，英雄攻击力提升"""
        print("将武器“{}”装备给英雄“{}”".format(self.name, hro.name))
        hro.damage+=self.damage
        print("“{}”的攻击力变为 {}".format(hro.name, hro.damage))
        print("********************")



LB = Hero("吕布", 20, 100, "群雄")
ZF = Hero("张飞", 7, 80, "蜀国")

ZF.get_inf()
LB.get_inf()

ZF.attack(LB)


# 新建武器实例,其中包含属性：名称（丈八蛇矛）、伤害值（3）
ZBSM = Weapon("丈八蛇矛", 3)
# 将武器赠与张飞
ZBSM.take_weapon(ZF)


# 显示“ZF”目前信息
ZF.get_inf()
# 令“ZF”攻击“LB”
ZF.attack(LB)
