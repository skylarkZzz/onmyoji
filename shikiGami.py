#coding=utf-8

import collections

Transition = collections.namedtuple("Transition",
                                    ["state", "action", "reward", "next_state", "done"])
# Status = collections.namedtuple("status", ["probability", """reward"])
Proper = collections.namedtuple("properties", {"speed", "gongji", "baoji", "baoshang", "blood", "defense", "shield", "yuhun", "mingzhong", "dikan", "debuff"})

class tamasii():
    def __init__(self):
        pass

    def valid(self):
        pass

    def action(self):
        pass

class shikiGami():
    def __init__(self, prop, extra_action=False, before_round=False, after_round=False):
        self.prop: Proper = prop
        self.extra_action = extra_action
        self.before_round = before_round
        self.after_round = after_round

    @property
    def speed(self):
        return self.prop.speed

    @property
    def alive(self):
        return self.prop.blood > 0 and self.extra_action

    def updateStatus(self):
        pass

    def action_1(self):
        pass

    def action_2(self):
        pass

    def action_3(self):
        pass

    def before_Actor(self):
        pass

    def after_Actor(self):
        pass

    def effect_blood(self, delta):
        self.prop.blood += delta

    def effect_speed(self, delta):
        if delta < 1:
            self.prop.speed += self.prop.speed * delta
        else:
            self.prop.speed += delta


class environment():
    def __init__(self, red, blue):
        self.oninohi = 4
        self.red = red
        self.blue = blue

    def before_status(self, queue):
        actor_gami = None
        for gami in queue:
            if gami.alive and gami.before_round:
                actor_gami = gami
                break
        return actor_gami

    def after_status(self, queue):
        actor_gami = None
        for gami in queue:
            if gami.alive and gami.after_round:
                actor_gami = gami
                break
        return actor_gami

    def action(self):
        statuses = []
        isOver, shikigami = self.select_action_onRound()
        if isOver:
            return statuses
        for candi in shikigami.updateStatus():
            assert isinstance(candi, Transition)

        shikigami.updateStatus()


    def beforeRound(self):
        pass

    def afterRound(self):
        pass

    def select_action_onRound(self):
        def actor(queue, alive, cur, shikigami=None):
            for gami in queue:
                if not gami.alive:
                    alive = alive - 1
                if gami.speed > cur:
                    cur = gami.speed
                    shikigami = gami
            return cur, shikigami, alive
        cur_speed, shikigami, red_alive = actor(self.red, 5, 0, None)
        if red_alive == 0:
            return True, None
        _, shikigami, blue_alive = actor(self.blue, 5, cur_speed, shikigami)
        if blue_alive == 0:
            return True, None
        return False, shikigami


def calcQFunction(env):
    QValue = 0.0
    hasStatus = True
    while hasStatus:



