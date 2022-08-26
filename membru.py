class Member:       # Numele class-ului pe care il faci. Atunci cand importam acest class o sa apeleze functia de mai jos
    def __init__(self, nume, varsta, localitate):       # Functia aceasta imi poate creea objects pe care le definesc scriind parametri doriti.
        self.nume = nume                                # Objectul nou va lua numele pe care il introduc.
        self.varsta = varsta                            # Objectul nou va lua varsta pe care o introduc.
        self.localitate = localitate                    # Objectul noi va lua localitatea pe care o introduc.