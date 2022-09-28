testcases = int(input())
for i in range(testcases):
    tables, people = map(int, input().split())

    if tables >= people:
        print(1)
    else:
        PA = people // tables
        PB = PA + 1
        TB = people % tables
        TA = tables - TB

        # Using DP to store factorials pre-hand
        fact = [1]
        for j in range(1, people + 2):
            fact.append(j * fact[j - 1])

        # Dividing people between tables
        divide = fact[people] / (pow(fact[PA], TA) * pow(fact[PB], TB) * fact[TA] * fact[TB])
        if PB >= 4:
            result = divide * (pow(fact[PA - 1] / 2, TA) * pow((fact[PB - 1] / 2), TB))
        else:
            result = divide

    print(int(result))