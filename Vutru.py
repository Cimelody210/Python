def Weight_in_Universe():
    def Planet_str(w):
        s =''
        for i in range(len(w)):
            s= s+str(i+1)+'/ '+w[i] + '\n'
        return s
    planet = ['Moon','Venus','Mars','Jupiter','Pluto','TRAPPIST-1b','TRAPPIST-1c','TRAPPIST-1d','TRAPPIST-1e','TRAPPIST-1f','TRAPPIST-1g','Kepler-1649c','Kepler-186f','Kepler-442b',"Kepler-452b",'Gliese-832c','Gliese-1214b:Hành tinh chứa đầy nước','TrES-4b','HD-100546b: Giant Jupiter','TOI-1789b','Nibiru: The 9th Planet in Orion','OGLE-2018-BLG-0677Lb',"K2-373b","Kepler-1983b"]
    gravity = [1.6,8.9,3.7,24.8,0.6,7.95,9.37,4.85,9.09,8.27,8.5,10.44,11.426,12.74,18.4,15.96,10.678,7.4,3.76,9.26,14.05,12.07,11.52,10.8]
    P_planet = float(input("Nhap trong luong cua may: "))
    print(Planet_str(planet))
    k = int(input("nhap thu tu hanh tinh:"))
    Gr = gravity[k-1]
    print(f'\nPlanet {planet[k-1]} with gravity: {gravity[k-1]}')
    print(f"Trong luong la: {round(P_planet * Gr / 9.8,2)} kg")
