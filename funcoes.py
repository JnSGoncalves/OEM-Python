from math import pi, sin, cos, sqrt
vLuz = 3 * 10 ** 8
h = 4.135667696e-15  # Constante de Planck em eV·s
e = 1.602176634e-19  # Carga do elétron 
u = 4 * pi * 10 ** -7 # Constante Magnética em H/m


# f = 1\ t              t-> período.
# k = 2pi/ comprimento  k-> perído.
# 


def freqInput(freq):
    comprimento = vLuz / freq
    k = 2 * pi / comprimento
    w = 2 * pi * freq
    
    return comprimento, k, w

def comprimentoInput(comprimento):
    f = vLuz / comprimento
    k = 2 * pi / comprimento
    w = 2 * pi * f

    return f, k, w

def nOndaInput(k):
    comprimento = (2*pi)/k
    f = vLuz / comprimento
    w = 2*pi * f

    return comprimento, f, w

def freqAngInput(w):
    f = w/(2*pi)
    comprimento = vLuz / f
    k = 2 * pi / comprimento

    return comprimento, f, k

def emInput(em):
    bm = em / vLuz
    intensidade = vLuz / (2 * u) * (bm ** 2)
    
    return bm, intensidade

def intensidadeInput(intensidade):
    bm = sqrt((intensidade * (2 * u)) / vLuz)
    em = vLuz * bm

    return bm, em
  
def bmInput(bm):
    em = vLuz * bm
    intensidade = vLuz / (2 * u) * (bm ** 2)
    
    return em, intensidade


def tabelaConversoes():
    print("de rad/s -> rad/m = W(frequência angular)/Vluz = W/3x10^8")
    print()
    print("nm -> m  = nm * E-9")
    print("m -> nm = m * E+9")
    print("um -> m = um * E-6")
    print("m -> um = m * E+6")
    print("mc -> m  = mc * E-6")
    print("m -> mc = m * E+6") 
    print()
    print("Hz -> KHz = Hz *e-3")
    print("Khz -> Hz = Khz*e+3")
    print("Hz -> mHz = Hz * E-6")
    print("mHz -> Hz = mHz * E+6")
    print("Hz -> THz = Hz * E-12")
    print("THz -> Hz = THz * E+12")
    print("Hz -> GHz = Hz * E-9")
    print("GHz - > Hz = Hz * E+9")
    print()
    print("V/m -> MV/m = V/m * E-6")
    print("MV/m -> V/m = MV/m * E+6")
    print()
    print("mT -> T = mT * E-3")
    print("T -> mT = T * E+3")
    print("uT -> T = uT * E-6")
    print("T -> uT = T * E+6")

def dadosEnunciado():
    print("Módulo máximo = amplitude do campo")
    print("Campo elétrico ou magnético máximo -> amplitude do campo")
    print()
    print("Paralelo ao eixo: Sentido positivo")
    print("Anti paralelo ao eixo: Sentido negativo")
    print()
    print("E = (Amplitude V/m) * cos((N de onda(k) rad/m) * x -(sentido +) (fre angular(w) rad/s)t)")
    print("B = (Amplitude T) * cos((N de onda(k) rad/m) * x +(sentido -) (fre angular(w) rad/s)t)")
    print()
    print("i x j = k  |  -i x -j = k")
    print("-i x j = -k  |  i x -j = -k")
    print("X(i), Y(j), Z(k)")
    print()
    
