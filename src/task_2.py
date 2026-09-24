#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Decimal:
    MAX_SIZE = 100

    def __init__(self, size, value=0):
        if not (1 <= size <= Decimal.MAX_SIZE):
            raise ValueError(f"Размер списка должен быть от 1 до {Decimal.MAX_SIZE}")

        self._size = size
        self.digits = [0] * Decimal.MAX_SIZE

        val_str = str(value)[::-1]
        self.count = max(1, min(len(val_str), size))

        for i in range(min(len(val_str), size)):
            self.digits[i] = int(val_str[i])

    def size(self):
        return self._size

    def __getitem__(self, index):
        if not (0 <= index < self._size):
            raise IndexError("Индекс вышел за пределы size")
        return self.digits[index]

    def __setitem__(self, index, value):
        if not (0 <= index < self._size):
            raise IndexError("Индекс вышел за пределы size")
        if not (0 <= value <= 9):
            raise ValueError("Должна быть цифра от 0 до 9")

        self.digits[index] = value

        if index >= self.count and value > 0:
            self.count = index + 1
        elif index == self.count - 1 and value == 0:
            while self.count > 1 and self.digits[self.count - 1] == 0:
                self.count -= 1

    def __add__(self, other):
        if not isinstance(other, Decimal): raise ValueError('Некорректный тип аргумента')

        len_digits = max(self._size, other._size)
        res = Decimal(len_digits, 0)
        carry = 0

        for i in range(len_digits):
            full_sum = self.digits[i] + other.digits[i] + carry
            partial_sum = full_sum % 10
            carry = full_sum // 10
            res.digits[i] = partial_sum

        res.count = len_digits
        if carry > 0:
            if res.count >= Decimal.MAX_SIZE:
                raise OverflowError("Переполнение: число превышает 100 знаков")
            res.digits[res.count] = carry
            res.count += 1

        if res.count > res._size:
            res._size = res.count

        while res.count > 1 and res.digits[res.count - 1] == 0:
            res.count -= 1

        return res

    def __sub__(self, other):
        if not isinstance(other, Decimal): raise ValueError('Некорректный тип аргумента')

        if self < other:
            raise ValueError('Результат вычитания не может быть отрицательным')
        len_digits = max(self._size, other._size)
        res = Decimal(len_digits, 0)
        borrow = 0

        for i in range(len_digits):
            diff = self.digits[i] - other.digits[i] - borrow
            if diff < 0:
                diff += 10
                borrow = 1
            else:
                borrow = 0
            res.digits[i] = diff

        res.count = len_digits

        while res.count > 1 and res.digits[res.count - 1] == 0:
            res.count -= 1
        return res

    def __mul__(self, other):
        if not isinstance(other, Decimal): raise ValueError('Некорректный тип аргумента')

        res = Decimal(Decimal.MAX_SIZE, 0)

        counter = Decimal(Decimal.MAX_SIZE, 0)
        for i in range(other.count):
            counter.digits[i] = other.digits[i]
        counter.count = other.count

        one = Decimal(Decimal.MAX_SIZE, 1)
        zero = Decimal(Decimal.MAX_SIZE, 0)

        while not (counter == zero):
            res = res + self
            counter = counter - one

            if res.count > Decimal.MAX_SIZE:
                raise OverflowError("Переполнение: результат умножения превышает 100 знаков")

        res._size = res.count
        return res

    def __eq__(self, other):
        if not isinstance(other, Decimal):
            return False

        if self.count != other.count:
            return False

        for i in range(self.count):
            if self.digits[i] != other.digits[i]:
                return False

        return True

    def __lt__(self, other):
        if not isinstance(other, Decimal): raise ValueError('Некорректный тип аргумента')

        if self.count != other.count:
            return self.count < other.count

        for i in range(self.count - 1, -1, -1):
            if self.digits[i] != other.digits[i]:
                return self.digits[i] < other.digits[i]

        return False

    def __le__(self, other):
        return self < other or self == other

    def __str__(self):
        active_digits = self.digits[:self.count]
        return "".join(map(str, active_digits[::-1]))

if __name__ == "__main__":
    a = Decimal(5, 99999)
    b = Decimal(5, 12345)

    print(a + b)
    print(a - b)
    print(a * b)
    b[0] = 6
    print(a + b)
    print(a - b)
    print(a * b)
    print(a < b)
    print(b <= a)