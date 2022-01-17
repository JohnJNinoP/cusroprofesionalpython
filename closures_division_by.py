def make_division_by(n):
    def division_by(x):
        return x/n
    
    return division_by

def run():
    division_1 = make_division_by(3)
    division_2 = make_division_by(5)
    print(division_1(18))
    print(division_2(100))

if __name__ == '__main__':
    run()