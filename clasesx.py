# # class SDA:
# #     studenti = 7
# #
# # obiect_1 = SDA()
# # print(obiect_1.studenti)
#
#
#
#
# class SDA:
#     def __init__(self, nume, prenume):
#         self.nume = nume
#         self.prenume = prenume
#
#     def intro(self):
#         print(f"Salutare, numele meu este {self.nume.lower()} si prenumele este {self.prenume.upper()}")
#
#
#     def __str__(self):
#         return f"Numele studentului este {self.nume} si prenumele este {self.prenume}"
#
#
# student_1 = SDA("Andreea", "Stefan")
#
# print(student_1.nume)
# print(student_1.prenume)
# print(student_1)
# student_1.intro()
#
# student_1.nume = "Elena"
# print(student_1)
#
#
# del student_1.prenume
# print(student_1.nume)
#
# class Masina:
#     pass
#
# class Persoana:
#     pass
#
#
# """ cel mai simplu exemplu de enharitance - clasa copil care mosteneste de laclasa parinte"""
#
# class SDA_41(SDA):
#     def __init__(self, first_name, last_name, varsta):
#         # super().__init__(first_name, last_name)
#         self.first_name = first_name
#         self.last_name = last_name
#         self.varsta = varsta
#
#     def despre_student(self):
#         strx = f"Studentul are prenumele {self.first_name} cu {len(self.last_name)} litere si are varsta de {self.varsta}"
#         return strx
#
#
# persoana_3 = SDA_41("Vasile", "Ionescu", 41)
# print(persoana_3.nume)
# print(persoana_3.prenume)
# print(persoana_3.varsta)
# print(persoana_3)
# print(persoana_3.despre_student())


# #  exercitiu:
# class Masini:
#     def __init__(self, marca, culoare):
#         self.marca = marca
#         self.culoare = culoare
#
#
# class Nume_masini(Masini):
#     def __init__(self, marca, culoare, motor, tractiune):
#         super().__init__(marca, culoare)
#         self.motor = motor
#         self.tractiune = tractiune
#
#     def despre_masini(self):
#         return f"Masina {self.marca} are tractiune {self.tractiune}"
#
#     def __str__(self):
#         return f"Masina {self.marca} are culoarea {self.culoare}, tractiune {self.tractiune} si motorul {self.motor}"
#
# nume_masina = Nume_masini(marca = "Ford", culoare = "albastru", tractiune = "4x4", motor = 2.2)
#
# print(nume_masina)
#
#
# class Numere:
#     def __init__(self, a):
#         self.a = a
#
#     def __add__(self, other):
#         return(len(str(self.a) + len(str(other.a)))
#
#     def __str__(self):
#         return f"Numarul ales este {self.a}"
#
# numar_1 = Numere("Ion")
# numar_2 = Numere("Maria")
# print(numar_1)
# print(numar_2)
# print(numar_1+numar_2)


# class Whatever:
#     def __init__(self):
#         self.var_publica = "10"
#         self.var_privata = "20"
#
#     def get_public_variable(self):
#         return self.var_publica
#
#     def get_private_variable(self):
#         return self.var_privata
#
# obiect_1 = Whatever()
# print(obiect_1.get_public_variable())
# print(obiect_1.get_private_variable())





class SDA:
    def __init__(self, nume, prenume):
        self.nume = nume
        self.prenume = prenume

    # helper/util type of function
    @staticmethod
    def transform_to_lowecase(strx):
        return strx.lower()


    def intro(self):
        print(f"Salutare, numele meu este {self.nume.lower()} si prenumele este {self.prenume.upper()}")

    def __str__(self):
        return f"Numele studentului este {self.nume} si prenumele este {self.prenume}"

student_1 = SDA("Andreea", "Stefan")
print(student_1.nume)
print(student_1.prenume)
print(student_1)
student_1.intro()

