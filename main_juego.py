import sys 
import ataque
import estadisticas

def inicio():
    print("Bienvenido al juego")
    print("Elige ua dificultad")
    print("[1]Noob [2]Pro [3]Hacker [#]Soy gei")
    numero = int(input("=> "))
    return numero

def dificultad(num):
    if num == 1:
        print("Tremendo noob")
        print("Pelearas contra un gei")
        return 100
    elif num == 2:
        print("Alto Pro")
        print("Pelearas contra una 8 de elixir")
        return 200
    elif num == 3:
        print("Hacker pro papu :v")
        print("Pelearas contra otro hacker pro papuh :v")
        return 300
    else:
        sys.exit


def main():
    numero = inicio()
    hp_enemy = dificultad(numero)
    print("******")
    hp = 100
    turno = True
    print("Listo pa, a pelear")
    while hp_enemy > 0 and hp > 0:
        ataque_enemigo = ataque.atk_enemy(numero)
        print("Te hizo {} de daño".format(ataque_enemigo))
        hp = hp - ataque_enemigo
        if hp > 0:
            if turno == True:
                estadisticas.status(hp,hp_enemy)
                print("Vas prro")
                print("Escogen tu ataque")
                print("El ataque chingon baja entre 20 y 60 de vida")
                print("El ataque chill baja entre 10 y 30 de vida")
                print("[1]. Ataque Chingon [2]. Ataque Chill")
                mi_ataque = int(input("=> "))
                el_ataque = ataque.atk(mi_ataque)
                mi_dano = el_ataque[0]
                turno = el_ataque[1]
                print("Tu ataque bajo {}".format(mi_dano))
                hp_enemy = hp_enemy - mi_dano
                if hp_enemy <= 0 :
                    print("Ganaste pa, felicidades")
                    sys.exit()
                else:
                    estadisticas.status(hp,hp_enemy)
                    pass
            else:
                turno = True
                pass
               
        else:
            print("Mamaste")
            sys.exit



if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
        
