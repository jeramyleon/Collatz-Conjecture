def collatz_conjecture(n=5):
    steps = 0 

    if n == 1:
        print('Zero steps required, number is already one')
        return

    while True:
        if n == 1:
            print('Done')
            break     

        elif n % 2 == 0:
            steps += 1 
            print(f"""
step {steps}: {n} / 2 = {n / 2}""")
            n = n / 2

        else:
            steps += 1
            print(f"""
step {steps}: {n} * 3 + 1 = {n * 3 + 1}""")
            n = n * 3 + 1 

collatz_conjecture(1000)

