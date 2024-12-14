#!/usr/bin/python
# -*- coding: utf-8 -*-
from code.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity
import math


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]

    def move(self):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))


class Enemy3(Enemy):  # Nova classe para Enemy3
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.angle = 0  # Ângulo inicial para o movimento senoidal

    def move(self):
        # Movimento horizontal básico
        self.rect.centerx -= ENTITY_SPEED[self.name]

        # Movimento vertical senoidal
        amplitude = 50  # Amplitude do movimento
        frequency = 0.1  # Frequência do movimento
        self.rect.centery += int(amplitude * math.sin(self.angle))
        self.angle += frequency

        # Restringir o ângulo para evitar valores muito grandes
        if self.angle > 2 * math.pi:
            self.angle -= 2 * math.pi


