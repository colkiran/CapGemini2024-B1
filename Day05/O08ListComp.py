
fruits = [
    ('apple', 285),
    ('orange', 160),
    ('grapes', 130),
    ('pineapple', 75),
    ('watermelon', 90),
    ('gauva', 110),
    ('banana', 65),
    ('strawberry', 350)
]

print(f"fruits :{fruits}")
print("-"  * 60)

prices = ["fruits" for fruit in fruits]
print(f"prices :{prices}")
print("-"  * 60)

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")
print("-"  * 60)

prices = [fruit[0] for fruit in fruits]
print(f"prices :{prices}")
print("-"  * 60)

prices = [fruit[1] for fruit in fruits]
print(f"prices :{prices}")
print("-"  * 60)

prices = [fruit[1] * 0.9 for fruit in fruits]
print(f"prices :{prices}")
print("-"  * 60)

prices = [fruit[1] * 0.75 for fruit in fruits]
print(f"prices :{prices}")
print("-"  * 60)

expensiveFrts = [[fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75]
                 for fruit in fruits if fruit[1] > 100]
print(f"expensive fruits :{expensiveFrts}")
print("-"  * 60)

sentence= "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

words = [word for word in sentence.split()]
print(f"words :{words}")
print("-"  * 60)

words = [word for word in sentence.split() if word != 'the']
print(f"words: {words}")
print("-"  * 60)

words = [(word, len(word)) for word in sentence.split() if word != 'the']
print(f"words :{words}")