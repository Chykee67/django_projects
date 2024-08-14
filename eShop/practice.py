

class Doctor():
    def __init__(dr, name, specialty):
        dr.name = name
        dr.specialty = specialty

    def get_dr(dr):
        return f'Dr. {dr.specialty}'

    def __repr__(dr):
        return dr.get_dr()

    

def main():

    doctor = Doctor('okoye', 3)

    doctor.specialty = 4

    l = ['garri', 'fish', doctor]

    for item in l:
        print(item)

if __name__ == '__main__':
    main()