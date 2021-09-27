def make_division_by(n:int) -> float:
    """This closure return a dunction that returns the division of a number x by n
    """
    def division(x:int) -> float:
        assert type(x) != str, "No se supone que escribas algo que no sea un numero."
        assert type(x) != 0, "Divicion entre cero -> inf"
        return x / n 
    return division

def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == '__main__':
    run()