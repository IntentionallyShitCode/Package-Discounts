import cls
from random import randint

text = open("output.txt", "w")

for x in range(100):
    if x + 1 >= 0 and x + 1 <= 9:
        holder = "{" + "{}{}Console.WriteLine(total);{}".format(randint(1,3) * "\n", randint(1,7) * "\t", randint(1,3) * "\n") + "}"
    if x + 1 >= 10 and x + 1 <= 19:
        holder = "{" + "{}{}Console.WriteLine(total * 0.20);{}".format(randint(1,3) * "\n", randint(1,7) * "\t", randint(1,3) * "\n") + "}"
    if x + 1 >= 20 and x + 1 <= 49:
        holder = "{" + "{}{}Console.WriteLine(total * 0.30);{}".format(randint(1,3) * "\n", randint(1,7) * "\t", randint(1,3) * "\n") + "}"
    if x + 1 >= 50 and x + 1 <= 99:
        holder = "{" + "{}{}Console.WriteLine(total * 0.40);{}".format(randint(1,3) * "\n", randint(1,7) * "\t", randint(1,3) * "\n") + "}"
    if x + 1 == 100:
        holder = "{" + "{}{}Console.WriteLine(total * 0.50);{}".format(randint(1,3) * "\n", randint(1,7) * "\t", randint(1,3) * "\n") + "}"

    text.write(
    """
    if {}({}packages{}=={}{}{}){}{}
    """.format(randint(1,15) * " ", randint(1,15) * " ", randint(1,15) * " ", randint(1,15) * " ", x + 1, randint(1,15) * " ", randint(1,15) * " ", holder)
    )
