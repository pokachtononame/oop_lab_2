#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pair:
    def __init__(self, a=0.0, b=0.0):
        if isinstance(a, (float, int)) and isinstance(b, (float, int)):
            self.first = float(a)
            self.second = float(b)
        else:
            raise ValueError('Некорректный тип аргументов')

    # --- Строковое представление ---

    def __str__(self):
        return f"({self.first}, {self.second})"
        
    def __repr__(self):
        return f"Pair({self.first}, {self.second})"
        
    # --- Арифметические операции ---
    
    # Сложение (+)
    def __add__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first + other.first, self.second + other.second)
        if isinstance(other, (int, float)):
            return Pair(self.first + float(other), self.second + float(other))
        raise ValueError('Некорректный тип аргумента')
        
    def __radd__(self, other):
        return self.__add__(other)
        
    # Вычитание (-)
    def __sub__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first - other.first, self.second - other.second)
        if isinstance(other, (int, float)):
            return Pair(self.first - float(other), self.second - float(other))
        raise ValueError('Некорректный тип аргумента')
        
    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Pair(float(other) - self.first, float(other) - self.second)
        raise ValueError('Некорректный тип аргумента')
        
    # Умножение (*)
    def __mul__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first * other.first, self.second * other.second)
        if isinstance(other, (int, float)):
            return Pair(self.first * float(other), self.second * float(other))
        raise ValueError('Некорректный тип аргумента')
        
    def __rmul__(self, other):
        return self.__mul__(other)
        
    # Деление (/)
    def __truediv__(self, other):
        if isinstance(other, Pair):
            if other.first == 0.0 or other.second == 0.0:
                raise ZeroDivisionError("Деление на ноль")
            return Pair(self.first / other.first, self.second / other.second)
        if isinstance(other, (int, float)):
            if float(other) == 0.0:
                raise ZeroDivisionError("Деление на ноль")
            return Pair(self.first / float(other), self.second / float(other))
        raise ValueError('Некорректный тип аргумента')
        
    def __rtruediv__(self, other):
        if self.first == 0 or self.second == 0:
            raise ZeroDivisionError("Деление на ноль")
        if isinstance(other, (int, float)):
            return Pair(float(other) / self.first, float(other) / self.second)
        raise ValueError('Некорректный тип аргумента')
        
    # Возведение в степень (**)
    def __pow__(self, other):
        if isinstance(other, Pair):
            return Pair(self.first ** other.first, self.second ** other.second)
        if isinstance(other, (int, float)):
            return Pair(self.first ** float(other), self.second ** float(other))
        raise ValueError('Некорректный тип аргумента')
        
    # --- Унарные операции ---
    
    def __neg__(self):
        return Pair(-self.first, -self.second)
        
    def __abs__(self):
        return Pair(abs(self.first), abs(self.second))
        
    # --- Операции сравнения ---
    
    def __eq__(self, other):
        if not isinstance(other, Pair):
            return False
        return self.first == other.first and self.second == other.second
        
    def __lt__(self, other):
        if not isinstance(other, Pair):
            raise ValueError('Некорректный тип аргумента')
        return (self.first, self.second) < (other.first, other.second)
        
    def __le__(self, other):
        if not isinstance(other, Pair):
            raise ValueError('Некорректный тип аргумента')
        return (self.first, self.second) <= (other.first, other.second)

    # --- Индексирование ---

    def __getitem__(self, index):
        if index == 0: return self.first
        if index == 1: return self.second
        raise ValueError("Индекс может быть только 0 или 1")

    def __setitem__(self, index, value):
        if not isinstance(value, (int, float)):
            raise ValueError("Значение должно быть числом")
        if index == 0:
            self.first = float(value)
        elif index == 1:
            self.second = float(value)
        else:
            raise ValueError("Индекс может быть только 0 или 1")


    def read(self, prompt=None):
        if not isinstance(prompt, str):
            raise ValueError('Приглашение должно быть строкой')
        if prompt is None:
            text = input()
        else:
            text = input(prompt)
        parts = text.split()
        if len(parts) != 2:
            raise ValueError('Ожидается два значения')
        self.first = float(parts[0])
        self.second = float(parts[1])

    def display(self):
        print(f'First: {self.first}, Second: {self.second}')

    def power(self):
        return pow(self.first, self.second)


def make_pair(first, second):
    try:
        return Pair(first, second)
    except ValueError as error:
        print(f'Ошибка создания пары: {error}')
        return None


if __name__ == "__main__":
    p1 = Pair(4, 8)
    p2 = Pair(2, 2)

    print(p1 + p2)
    print(p1 / p2)

    print(p1 + 10)
    print(10 + p1)
    print(20 - p1)

    print(p1 < p2)
    print(p2 <= p1)

    print(p1[0])