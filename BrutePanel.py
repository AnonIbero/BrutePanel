class brute:

    def logo():
        logo ="""
+------------------------------------------------------------+
|MMMMMMMMMMMMMMMMMMMMMMKdc,.      .,cdKMMMMMMMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMWOocccldk0KXNNNNXKOkdc:::oOWMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMKo::d0WMWNMMMMXdWxkxXOKNXWMW0d:;lKMMMMMMMMMMMMM|
|MMMMMMMMMMXl;l0MMXWkOolXMMMNxWxOxOdOK;lxOKXMW0c,lXMMMMMMMMMM|
|MMMMMMMMK;;OMMK0koxxX0XMMMMMMMMMMMMMWWKKkOdkoMMWk';KMMMMMMMM|
|MMMMMMK;;KMNk:lk0XMMMMWNNNXXXXKXXXNNNWMMMMX0ok:kNMO,;KMMMMMM|
|MMMMMo'0MNkkkxNMMMWNNNWNNNWNWNNMWNNNNWNNNWMMMNxloOWMk.oMMMMM|
|MMMX'cWMXdOdXMMMNXXNWWNWMMNMMNNMMWMMNXWNNNNWMMM0OKx0MW;'XMMM|
|MMN.dMM0cckMMMWXWMMWXNNNNXNNlxc;0NXNNNXNMMMNXWMMMO:lKMMl.XMM|
|MW'dMM0OdKMMMNXMMMMNWMMMNNMWd0l kMNWMMMNNMMMMXNMMMKXOkMMl.WM|
|M:;MMWxkOMMMXNWWWWNXWMMMXWMMMKdWMMMXMMMWXNNWWWNNMMMkK0MMM,;M|
|O XMMx:oWMMNNMMMMWXWWNNXKNNNN:cNNNNXNNNWWKMMMMMNNMMMoOkMMK O|
|;cMMMkdOMMWXMMMMMNWMMMMNXMMMM00MMMMNNMMMMXNMMMMMXMMMOKkMMM;;|
|.OMMK:cNMMNNMMMMMXMMMMMNNMMMNOONWMMWNMMMMNXMMMMMNWMMNc:XMMx.|
| XMMMKxNMMNXWWWWWXNWWWNXOl;MX;,0W:l0XWWWWNXWWWWWXWMMNxOWMM0 |
| XMMk,MMMMNNMMMMMXMO;'.   lMMdlWMl  .';coXXMMMMMNWMMMW.xMM0 |
|.OMM: xMMMMXMMMMMNN.      lMM:.MM:       oNMMMMMXMMMWo :MMd.|
|::MNd 'kOMMNNMMMMNd       .NM. XX        ;WMMMMNWMMok. dXM,;|
|O XO'o.O KWMNNWWWW;        .X. k.        .NWWWNNMWO O,o.00 O|
|M:;Wl :K dl0MNNMMX     ;;,.;;'            KMMNWMkol.O'.kW':M|
|MW'okoc. ,0 kMWNNx    ;lol.;,.            dNNMMx O. ;xxkc'WM|
|MMN.oc.cl:N' ONWW:    o;,;,...            cWWNk ,Xdd:.oc.NMM|
|MMMN,:k;  ':. xcl;         :;:c.          ,lcd .:. .:O,'XMMM|
|MMMMMd'OXccc;'.do          .:l;dcll;:      dd',:lclNk.oMMMMM|
|MMMMMMX:,xc..,;::;          :,.c:o:',    .;::;,..lx';KMMMMMM|
|MMMMMMMMK;,kKl:odxdol.       .,.;co.  :lodxdo:oKx';KMMMMMMMM|
|MMMMMMMMMMXl,ccc,.  .        .lcdl,   ..  .,cc:'lXMMMMMMMMMM|
|MMMMMMMMMMMMMKo;:o0Nd        .ocl'    xMNOo;;oKMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMW0o:'         c:.     .;:oOWMMMMMMMMMMMMMMMM|
|MMMMMMMMMMMMMMMMMMMMMM0o;.        .;o0WMMMMMMMMMMMMMMMMMMMMM|
+------------------------------------------------------------+
                    ANONYMOUS IBEROAMERICA\n"""
        print(logo)
    
    def requisitos():
        try:
            import os
            import sys
            import requests
            brute.bruteadmin()
        except ModuleNotFoundError as a:
            try:
                os.system("sudo pip3 install requests")
            except:
                os.system("sudp apt-get install python3-pip")
    def ayuda():
        ayuda = """
Parametros:

-d [Indicar un diccionario]
-requisitos [Intentar instalar los requerimientos]

Ejemplo de uso:

python3 BrutePanel.py -d <diccionario> <direccion>

python3 BrutePanel.py -d diccionario.txt https://paginavictima.com/

Importante:

Verificar si la pagina victima tiene Certificado SSL, si no tiene, se escribe http://,
de lo contrario, te devolvera error

    """
        print(ayuda)

    def bruteadmin():
        try:
            try:
                import os
                import sys
                import requests
                from requests.exceptions import HTTPError

                
                argumento1 = sys.argv[1]
                if argumento1 == "-requisitos":
                    brute.requisitos()

                if argumento1 == "-d":
                    brute.logo()
                    argumento2 = sys.argv[2]
                    argumento3 = sys.argv[3]
                    if os.path.exists(f"{argumento2}") == False:
                        print("Indica un directorio valido")
                        exit()
                    txt  = open(f"{argumento2}","r")

                    numero = 0
                    lineas = txt.readlines()
                    for leer in lineas:
                        try:
                            if argumento3.endswith("/"):
                                a = requests.get(f"{argumento3}"+str(leer))
                                a.raise_for_status()
                                if a.status_code == 200:
                                    txt1 = open("Panel_Admin_encontrado","a+")
                                    txt1.write(str(argumento3)+str(leer))
                                    print(f"Correcto > {str(argumento3)+str(leer)}")
                            else:
                                z = str(argumento3) + "/"
                                a = requests.get(str(z)+str(leer))
                                a.raise_for_status()
                                if a.status_code == 200:
                                    txt1 = open("Panel_Admin_encontrado","a+")
                                    txt1.write(str(argumento3)+str(leer))
                                    print(f"Correcto > {str(z)+str(leer)}")

                        except HTTPError as error:
                            if argumento3.endswith("/"):
                                print(f"Incorrecto > {str(argumento3)+str(leer)}")
                            else:
                                print(f"Incorrecto > {str(argumento3)}"+ "/" +f"{str(leer)}")
                      
            except IndexError:
                brute.ayuda()
                os.sys.exit()

        
        except KeyboardInterrupt:
            os.sys.exit()



if __name__ == "__main__":
    brute = brute
    brute.requisitos()
