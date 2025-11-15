"""
===================================================================
⚡ SYSTEM NOTICE — INTERNAL SECURITY MODULE
This utility operates in a controlled environment and processes
locally‑generated test credentials for diagnostic evaluation.
All credential outputs, breach events, and recovery sequences
are produced within the module’s isolated logic engine.

No external network authentication systems are contacted.
No live service endpoints are queried or accessed.

For authorized testing and operator training only.
===================================================================
"""

import random
import time
import string

# ===== COLOR SETUP =====
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
CYAN = "\033[36m"
RESET = "\033[0m"

gmail_account = ([
    "johnpaul.delacruz.4821@gmail.com",
    "michael.reyes.7392@gmail.com",
    "andrew.santos.9184@gmail.com",
    "paul.romero.5527@gmail.com",
    "jason.martinez.6641@gmail.com",
    "kevin.garcia.2389@gmail.com",
    "christian.torres.9043@gmail.com",
    "daniel.ramos.7712@gmail.com",
    "joshua.mendoza.8450@gmail.com",
    "ryan.gomez.3502@gmail.com",
    "mark.espinosa.9417@gmail.com",
    "james.valdez.1973@gmail.com",
    "steven.castro.2198@gmail.com",
    "patrick.ortega.5630@gmail.com",
    "samuel.flores.7264@gmail.com",
    "joseph.morales.6321@gmail.com",
    "david.vergara.4086@gmail.com",
    "robert.deguzman.1549@gmail.com",
    "angelo.bautista.8142@gmail.com",
    "leo.navarro.0984@gmail.com",
    "brian.salazar.7421@gmail.com",
    "eric.mercado.2883@gmail.com",
    "ian.manalo.6591@gmail.com",
    "marvin.villanueva.3308@gmail.com",
    "julius.rodriguez.5960@gmail.com",
    "adrian.cortez.9055@gmail.com",
    "victor.pascual.1247@gmail.com",
    "edward.santiago.1409@gmail.com",
    "renzo.hermosa.8693@gmail.com",
    "carlo.fernandez.9802@gmail.com",
    "gabriel.herrera.0719@gmail.com",
    "nathan.rivera.0493@gmail.com",
    "richard.almirez.1306@gmail.com",
    "alvin.soriano.5794@gmail.com",
    "romeo.lazaro.8207@gmail.com",
    "francis.montero.2579@gmail.com",
    "justin.delarosa.6691@gmail.com",
    "kenji.magsaysay.0308@gmail.com",
    "miguel.asturias.4417@gmail.com",
    "cedric.barrientos.9906@gmail.com",
    "lance.paraiso.3298@gmail.com",
    "edwin.quintos.7023@gmail.com",
    "noel.buenviaje.2764@gmail.com",
    "jaypee.rosales.6187@gmail.com",
    "jorel.malvar.5342@gmail.com",
    "marvin.lucero.1029@gmail.com",
    "kyle.abadilla.3941@gmail.com",
    "xander.velasco.7580@gmail.com",
    "ethan.simbulan.0506@gmail.com",
    "leo.dominic.cruz.8411@gmail.com",
    "adrian.mandigma.2307@gmail.com",
    "clyde.sarabia.9021@gmail.com",
    "angelo.fabros.1114@gmail.com",
    "sean.delarama.7850@gmail.com",
    "rj.salcedo.9081@gmail.com",
    "kurt.vergara.1540@gmail.com",
    "justine.parungao.2864@gmail.com",
    "allan.mojica.9703@gmail.com",
    "jaylord.cayanan.2251@gmail.com",
    "fernando.manansala.5039@gmail.com",
    "niko.valenciano.8126@gmail.com",
    "marvin.caballero.9254@gmail.com",
    "kevin.salonga.4032@gmail.com",
    "dennis.robles.7736@gmail.com",
    "noah.calimlim.5601@gmail.com",
    "enzo.tabora.4490@gmail.com",
    "jared.mangulabnan.8804@gmail.com",
    "matthew.lopez.2008@gmail.com",
    "trevor.soriano.3056@gmail.com",
    "keith.borja.1147@gmail.com",
    "roland.santosjr.6440@gmail.com",
    "harvey.panlilio.9832@gmail.com",
    "vaughn.delrosario.7561@gmail.com",
    "miguel.sangalang.6998@gmail.com",
    "aldrin.vergara.4320@gmail.com",
    "charles.gutierrez.2144@gmail.com",
    "nicko.hidalgo.7759@gmail.com",
    "brent.escobar.1183@gmail.com",
    "zach.valencia.9927@gmail.com",
    "kristian.bautista.6045@gmail.com",
    "jomar.castrojr.8701@gmail.com",
    "darrel.manrique.5068@gmail.com",
    "neil.santillan.2403@gmail.com",
    "rodel.ventura.9413@gmail.com",
    "romeo.abadjr.3799@gmail.com",
    "ethan.cruzada.6621@gmail.com",
    "jovin.perez.8437@gmail.com",
    "dexter.alcantara.5582@gmail.com",
    "josiah.valdez.7124@gmail.com",
    "rei.gomez.2003@gmail.com",
    "allan.reyesjr.3094@gmail.com",
    "cedrick.santos.9903@gmail.com",
    "jude.almario.4782@gmail.com",
    "rafael.guevarra.8217@gmail.com",
    "antoine.rivera.1392@gmail.com",
    "marcus.delacruzjr.5408@gmail.com",
    "tyrone.mercado.7729@gmail.com"
     "johnpaul.delacruz4821@gmail.com",
    "michael.reyes7392@gmail.com",
    "andrew.santos9184@gmail.com",
    "paul.romero5527@gmail.com",
    "jason.martinez6641@gmail.com",
    "kevin.garcia2389@gmail.com",
    "christian.torres9043@gmail.com",
    "daniel.ramos7712@gmail.com",
    "joshua.mendoza8450@gmail.com",
    "ryan.gomez3502@gmail.com",
    "mark.espinosa9417@gmail.com",
    "james.valdez1973@gmail.com",
    "steven.castro2198@gmail.com",
    "patrick.ortega5630@gmail.com",
    "samuel.flores7264@gmail.com",
    "joseph.morales6321@gmail.com",
    "david.vergara4086@gmail.com",
    "robert.deguzman1549@gmail.com",
    "angelo.bautista8142@gmail.com",
    "leo.navarro0984@gmail.com",
    "brian.salazar7421@gmail.com",
    "eric.mercado2883@gmail.com",
    "ian.manalo6591@gmail.com",
    "marvin.villanueva3308@gmail.com",
    "julius.rodriguez5960@gmail.com",
    "adrian.cortez9055@gmail.com",
    "victor.pascual1247@gmail.com",
    "edward.santiago1409@gmail.com",
    "renzo.hermosa8693@gmail.com",
    "carlo.fernandez9802@gmail.com",
    "gabriel.herrera0719@gmail.com",
    "nathan.rivera0493@gmail.com",
    "richard.almirez1306@gmail.com",
    "alvin.soriano5794@gmail.com",
    "romeo.lazaro8207@gmail.com",
    "francis.montero2579@gmail.com",
    "justin.delarosa6691@gmail.com",
    "kenji.magsaysay0308@gmail.com",
    "miguel.asturias4417@gmail.com",
    "cedric.barrientos9906@gmail.com",
    "lance.paraiso3298@gmail.com",
    "edwin.quintos7023@gmail.com",
    "noel.buenviaje2764@gmail.com",
    "jaypee.rosales6187@gmail.com",
    "jorel.malvar5342@gmail.com",
    "marvin.lucero1029@gmail.com",
    "kyle.abadilla3941@gmail.com",
    "xander.velasco7580@gmail.com",
    "ethan.simbulan0506@gmail.com",
    "leo.cruz8411@gmail.com",
    "adrian.mandigma2307@gmail.com",
    "clyde.sarabia9021@gmail.com",
    "angelo.fabros1114@gmail.com",
    "sean.delarama7850@gmail.com",
    "rj.salcedo9081@gmail.com",
    "kurt.vergara1540@gmail.com",
    "justine.parungao2864@gmail.com",
    "allan.mojica9703@gmail.com",
    "jaylord.cayanan2251@gmail.com",
    "fernando.manansala5039@gmail.com",
    "niko.valenciano8126@gmail.com",
    "marvin.caballero9254@gmail.com",
    "kevin.salonga4032@gmail.com",
    "dennis.robles7736@gmail.com",
    "noah.calimlim5601@gmail.com",
    "enzo.tabora4490@gmail.com",
    "jared.mangulabnan8804@gmail.com",
    "matthew.lopez2008@gmail.com",
    "trevor.soriano3056@gmail.com",
    "keith.borja1147@gmail.com",
    "roland.santos6440@gmail.com",
    "harvey.panlilio9832@gmail.com",
    "vaughn.delrosario7561@gmail.com",
    "miguel.sangalang6998@gmail.com",
    "aldrin.vergara4320@gmail.com",
    "charles.gutierrez2144@gmail.com",
    "nicko.hidalgo7759@gmail.com",
    "brent.escobar1183@gmail.com",
    "zach.valencia9927@gmail.com",
    "kristian.bautista6045@gmail.com",
    "jomar.castro8701@gmail.com",
    "darrel.manrique5068@gmail.com",
    "neil.santillan2403@gmail.com",
    "rodel.ventura9413@gmail.com",
    "romeo.abad3799@gmail.com",
    "ethan.cruzada6621@gmail.com",
    "jovin.perez8437@gmail.com",
    "dexter.alcantara5582@gmail.com",
    "josiah.valdez7124@gmail.com",
    "rei.gomez2003@gmail.com",
    "allan.reyes3094@gmail.com",
    "cedrick.santos9903@gmail.com",
    "jude.almario4782@gmail.com",
    "rafael.guevarra8217@gmail.com",
    "antoine.rivera1392@gmail.com",
    "marcus.delacruz5408@gmail.com",
    "tyrone.mercado7729@gmail.com",
     "aaron.delacruz9321@gmail.com",
    "angelo.soriano7410@gmail.com",
    "brent.oliveros5532@gmail.com",
    "cedric.manansala8824@gmail.com",
    "darren.mabini2309@gmail.com",
    "emman.felix6028@gmail.com",
    "francis.robledo9117@gmail.com",
    "gabriel.alcantara7743@gmail.com",
    "hector.valmores6682@gmail.com",
    "ivan.castillo3045@gmail.com",
    "jacob.sangalang9571@gmail.com",
    "kevin.gavieres4419@gmail.com",
    "leo.quijano2153@gmail.com",
    "marvin.delarama9935@gmail.com",
    "noel.sarabia5074@gmail.com",
    "oscar.montemayor8042@gmail.com",
    "paolo.delapaz6197@gmail.com",
    "quentin.robles1130@gmail.com",
    "ramon.balagtas2301@gmail.com",
    "sean.galura4589@gmail.com",
    "tristan.fuentes9040@gmail.com",
    "ulysses.pascua7713@gmail.com",
    "vincent.reclusado6208@gmail.com",
    "wyatt.bernardino4450@gmail.com",
    "xander.bautista9514@gmail.com",
    "yuri.martinez7026@gmail.com",
    "zachary.reyes3307@gmail.com",
    "adrian.almario7720@gmail.com",
    "bryan.dizon1043@gmail.com",
    "charles.vergara6801@gmail.com",
    "daryl.lopez5520@gmail.com",
    "edrian.cruz9447@gmail.com",
    "felix.mercado8104@gmail.com",
    "gino.ferrer9361@gmail.com",
    "harvey.gutierrez7719@gmail.com",
    "isaac.magsino2085@gmail.com",
    "jerome.castro5063@gmail.com",
    "kristian.soriano4436@gmail.com",
    "lester.magalang3304@gmail.com",
    "mark.hernandez9072@gmail.com",
    "nathan.santos4402@gmail.com",
    "owen.delacruz9851@gmail.com",
    "patrick.santiago3215@gmail.com",
    "quincy.rosal4174@gmail.com",
    "romeo.salcedo7764@gmail.com",
    "stephen.pizarro6419@gmail.com",
    "timothy.valencia1173@gmail.com",
    "ulysses.rivera9980@gmail.com",
    "vaughn.escoto5593@gmail.com",
    "wayne.mercado8803@gmail.com",
    "xyris.abadilla2495@gmail.com",
    "yves.mendino7431@gmail.com",
    "zandro.cayanan3318@gmail.com",
    "andrei.cunanan5279@gmail.com",
    "bruce.manalad6648@gmail.com",
    "chris.parungao3741@gmail.com",
    "dominic.paner4366@gmail.com",
    "elijah.cadiz1142@gmail.com",
    "franco.almirez9981@gmail.com",
    "george.morales7030@gmail.com",
    "hans.meralco3507@gmail.com",
    "isaiah.navarro8423@gmail.com",
    "jaycee.rosales2211@gmail.com",
    "keith.hidalgo7725@gmail.com",
    "larry.perez6148@gmail.com",
    "miguel.cervantes8110@gmail.com",
    "noah.simbulan7430@gmail.com",
    "orion.flores6542@gmail.com",
    "philip.barrientos9047@gmail.com",
    "quentin.cajilig5581@gmail.com",
    "rafael.pinlac9020@gmail.com",
    "samuel.yap3317@gmail.com",
    "terrence.delarosa7796@gmail.com",
    "ulrich.robles6609@gmail.com",
    "victor.lazaro4233@gmail.com",
    "wesley.vergara8821@gmail.com",
    "xavier.mojica7392@gmail.com",
    "yohan.torres3117@gmail.com",
    "zane.espiritu5018@gmail.com",
    "alexis.manuel5742@gmail.com",
    "brando.ramos9934@gmail.com",
    "cyrus.carranza8410@gmail.com",
    "denzel.valenton6631@gmail.com",
    "emilio.hernando2094@gmail.com",
    "floyd.gomez4406@gmail.com",
    "gerald.tampus7202@gmail.com",
    "harold.diaz5049@gmail.com",
    "isaak.sanpedro7403@gmail.com",
    "jordan.villanueva2986@gmail.com",
    "kyle.malabanan2175@gmail.com",
    "lloyd.pangan7350@gmail.com",
    "marco.bituin6614@gmail.com",
    "neo.ignacio3195@gmail.com",
    "orlando.castro9913@gmail.com",
    "paul.cayanan7204@gmail.com",
     "luis.montero.4829@gmail.com",
    "rafael.cabral.1937@gmail.com",
    "daniel.nava.8502@gmail.com",
    "miguel.barrera.3741@gmail.com",
    "sebastian.quintero.6158@gmail.com",
    "gabriel.estrella.9025@gmail.com",
    "emilio.suarez.4702@gmail.com",
    "antonio.rey.2386@gmail.com",
    "carlos.valle.5190@gmail.com",
    "fernando.delgado.6843@gmail.com",
    "jorge.martin.3174@gmail.com",
    "alejandro.fuentes.9602@gmail.com",
    "ricardo.camacho.4519@gmail.com",
    "jesus.cortes.8271@gmail.com",
    "manuel.romero.3948@gmail.com",
    "andres.garcia.7620@gmail.com",
    "victor.arias.1357@gmail.com",
    "edgar.lopez.9041@gmail.com",
    "oscar.mendoza.5762@gmail.com",
    "jorge.salazar.2839@gmail.com",
    "juan.cabrera.6184@gmail.com",
    "roberto.nunez.4512@gmail.com",
    "fabian.reyes.8793@gmail.com",
    "jose.morales.3647@gmail.com",
    "daniel.gutierrez.5931@gmail.com",
    "miguel.castro.7280@gmail.com",
    "sebastian.ruiz.2406@gmail.com",
    "emilio.perez.9674@gmail.com",
    "antonio.fernandez.1825@gmail.com",
    "carlos.vargas.5107@gmail.com",
    "fernando.ramirez.6382@gmail.com",
    "jorge.martinez.8943@gmail.com",
    "alejandro.silva.3721@gmail.com",
    "ricardo.lopez.6058@gmail.com",
    "jesus.velasco.4819@gmail.com",
    "manuel.gomez.9307@gmail.com",
    "andres.dominguez.2540@gmail.com",
    "victor.martin.7864@gmail.com",
    "edgar.ruiz.3198@gmail.com",
    "oscar.torres.7425@gmail.com",
    "jorge.bautista.8601@gmail.com",
    "juan.caballero.4957@gmail.com",
    "roberto.estrella.6384@gmail.com",
    "fabian.salinas.1205@gmail.com",
    "jose.montero.9573@gmail.com",
    "daniel.nava.4831@gmail.com",
    "miguel.cabral.7504@gmail.com",
    "sebastian.arias.6187@gmail.com",
    "gabriel.lopez.2048@gmail.com",
    "emilio.ruiz.9761@gmail.com",
    "antonio.delgado.8429@gmail.com",
    "carlos.valle.1730@gmail.com",
    "fernando.martin.5612@gmail.com",
    "jorge.camacho.9384@gmail.com",
    "alejandro.fuentes.4025@gmail.com",
    "ricardo.rey.7150@gmail.com",
    "jesus.mendoza.2841@gmail.com",
    "manuel.cabrera.6902@gmail.com",
    "andres.salazar.5371@gmail.com",
    "victor.garcia.8210@gmail.com",
    "edgar.nunez.4163@gmail.com",
    "oscar.romero.9057@gmail.com",
    "jorge.gutierrez.2748@gmail.com",
    "juan.castro.6381@gmail.com",
    "roberto.perez.9712@gmail.com",
    "fabian.lopez.5426@gmail.com",
    "jose.velasco.1830@gmail.com",
    "daniel.gomez.7049@gmail.com",
    "miguel.ruiz.2184@gmail.com",
    "sebastian.torres.4958@gmail.com",
    "gabriel.bautista.3671@gmail.com",
    "emilio.caballero.9283@gmail.com",
    "antonio.salinas.6742@gmail.com",
    "carlos.montero.8317@gmail.com",
    "fernando.nava.2056@gmail.com",
    "jorge.cabral.9473@gmail.com",
    "alejandro.arias.3162@gmail.com",
    "ricardo.lopez.7804@gmail.com",
    "jesus.ruiz.4950@gmail.com",
    "manuel.delgado.6137@gmail.com",
    "andres.valle.1829@gmail.com",
    "victor.martin.9546@gmail.com",
    "edgar.camacho.3075@gmail.com",
    "oscar.fuentes.6408@gmail.com",
    "jorge.rey.2197@gmail.com",
    "juan.mendoza.8732@gmail.com",
    "roberto.cabrera.4158@gmail.com",
    "fabian.salazar.7960@gmail.com",
    "jose.garcia.2387@gmail.com",
    "daniel.nunez.5601@gmail.com",
    "miguel.romero.8124@gmail.com",
    "sebastian.gutierrez.3942@gmail.com",
    "gabriel.castro.6250@gmail.com",
    "emilio.perez.1873@gmail.com",
    "antonio.lopez.9402@gmail.com",
    "carlos.velasco.5721@gmail.com",
    "fernando.gomez.3184@gmail.com",
    "jorge.dominguez.7649@gmail.com",
    "alejandro.martin.4318@gmail.com",
    "ricardo.ruiz.9056@gmail.com",
    "jesus.torres.2149@gmail.com",
    "manuel.bautista.6873@gmail.com",
    "andres.caballero.5920@gmail.com",
    "victor.salinas.4307@gmail.com",
    "edgar.montero.7261@gmail.com",
    "oscar.nava.1593@gmail.com",
    "jorge.cabral.8420@gmail.com",
    "juan.arias.3675@gmail.com",
    "roberto.lopez.9512@gmail.com",
    "fabian.ruiz.2047@gmail.com",
    "jose.delgado.7831@gmail.com",
    "daniel.valle.6194@gmail.com",
    "miguel.martin.4857@gmail.com",
    "sebastian.camacho.1308@gmail.com",
    "gabriel.fuentes.9674@gmail.com",
    "emilio.rey.5728@gmail.com",
    "antonio.mendoza.8041@gmail.com",
    "carlos.cabrera.3150@gmail.com",
    "fernando.salazar.6905@gmail.com",
    "jorge.garcia.4729@gmail.com",
    "alejandro.nunez.1038@gmail.com",
    "ricardo.romero.8516@gmail.com",
    "jesus.gutierrez.2490@gmail.com",
    "manuel.castro.6371@gmail.com",
    "andres.perez.4082@gmail.com",
    "victor.lopez.7923@gmail.com",
    "edgar.velasco.5341@gmail.com",
    "oscar.gomez.2168@gmail.com",
    "jorge.dominguez.9840@gmail.com"
])  

def accounts():
    print(f"\n{CYAN}[ ACCOUNT BREACH MODULE BOOTING... ]{RESET}")
    time.sleep(0.7)
    print(f"{GREEN}[ STATUS: ONLINE ]{RESET}")
    time.sleep(0.4)
    print(f"{GREEN}[ CHANNEL SECURED ]{RESET}")
    time.sleep(0.4)
    print("------------------------------------------")
    print(f"{YELLOW}     G M A I L    C A P T U R E    N O D E{RESET}")
    print("------------------------------------------")
    print("→ Specify the Gmail you want the system to compromise.\n")
   
    while True:
        start = input(f"{RED}💀 Are you prepared to launch the Gmail breach? (yes/no){RESET} ")

        if start.lower() != "yes":
            print(f"{RED}Exited program!{RESET}")
            break

        print(f"{YELLOW}⏳ Initializing covert breach protocol...{RESET}", end="\r", flush=True)
        time.sleep(2)

        print(f"{YELLOW}⏳ Establishing encrypted backdoor channel...{RESET}", end="\r", flush=True)
        time.sleep(1.95)

        print(f"{YELLOW}⏳ Penetrating multi‑layer security firewalls...{RESET}", end="\r", flush=True)
        time.sleep(1.80)

        print(f"{YELLOW}⏳ Deploying stealth exploit package...{RESET}", end="\r", flush=True)
        time.sleep(1.60)

        print(f"{YELLOW}⏳ Extracting authentication tokens...{RESET}", end="\r", flush=True)
        time.sleep(1.30)

        print(f"\n{GREEN}🔓 BREACH CONFIRMED. Compromised Gmail accounts incoming...{RESET}")

        loops = random.randint(1, 6)

        for _ in range(loops):
            result = random.choice(gmail_account)
            print(f"{CYAN}Account compromised → {GREEN}{result}{RESET}")

        break
  


def password():
    print(f"\n{CYAN}========================================{RESET}")
    print(f"{YELLOW}   W  E  L  C  O  M  E    O P E R A T O R{RESET}")
    print(f"{CYAN}========================================{RESET}")
    print(f"{GREEN}System Status: ONLINE{RESET}")
    print("Protocol: Credential Breach Simulation")
    print("Target Input Required...\n")
    
    while True:
        start = input(f"{RED}Proceed? yes/no — you're one step from the password:{RESET} ")
        if start.lower() != "yes":
            print(f"{RED}Exited program{RESET}")
            break

        # VALIDATION LOOP
        while True:
            gmails = input(f"{CYAN}Enter the Gmail accounts you've captured:{RESET} ").lower()
            print(f"Data received: {YELLOW}{gmails}{RESET}")

            if gmails.endswith("@gmail.com"):
                break

            print(f"{RED}❌ Gmail not found.{RESET}")
            again = input("Do you want to re-enter a valid Gmail? (yes/no): ")

            if again.lower() != "yes":
                print(f"{RED}Exited program.{RESET}")
                return

        # HACKING SEQUENCE
        print(f"{YELLOW}⏳ Initiating deep-scan breach sequence...{RESET}", end="\r", flush=True)
        time.sleep(1.9)

        print(f"{YELLOW}⏳ Mapping hidden security layers...{RESET}", end="\r", flush=True)
        time.sleep(1.8)

        print(f"{YELLOW}⏳ Injecting silent intrusion vectors...{RESET}", end="\r", flush=True)
        time.sleep(1.7)

        print(f"{YELLOW}⏳ Bypassing encrypted credential vault...{RESET}", end="\r", flush=True)
        time.sleep(1.5)

        print(f"{YELLOW}⏳ Stabilizing access tunnel... hold your breath...{RESET}", end="\r", flush=True)
        time.sleep(1.4)

        print(f"{YELLOW}⏳ Extracting password hash… almost there...{RESET}", end="\r", flush=True)
        time.sleep(1.2)

        print(f"\n{GREEN}🔓 BREACH VERIFIED. Password retrieval sequence unlocked...{RESET}")

        letters = string.ascii_letters.lower()
        hex = string.hexdigits
        specials = '~!@#$[]%^&*()|}{":><;'
        oct = string.octdigits
        numbers = string.digits
        chars = letters + numbers + specials + hex + oct
      
        print(f"{GREEN}🔓 Breach complete — credentials extracted.{RESET}")
        password_value = "".join(random.choice(chars) for _ in range(16))

        print(f"{RED}💀 Password exposed:{RESET} {YELLOW}{password_value}{RESET}")
        print(f"Target Gmail: {GREEN}{gmails}{RESET}")
        break


def main_menu():
 while True: 
        print(f"{CYAN}\n[ MAIN CONTROL PANEL ]{RESET}")
        print("1) Start Breach")
        print("2) Extract Password")
        print("0) Exit")

        choice = input(">>> ")
   
        if choice == "1":
           accounts()
       
        elif choice == "2":
           password()
       
        else:
            print(f"{RED}Exited program!{RESET}")
            break

if __name__ == "__main__":     
   main_menu()