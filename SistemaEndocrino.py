"""
Práctica 4: Modelado y control del sistema endocrino.

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Perez Garcia Diego
Número de control: 23212635
Correo institucional: l23212635@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

"""

import numpy as np
import math as m
import control as ctrl
import matplotlib.pyplot as plt

# Datos generales de la simulación
x0, t0, tend, dt, w, h = 0, 0, 10, 1E-3, 10, 5
N = round(tend/dt) + 1
t = np.linspace(t0, tend, N)
u = np.ones(N)


# Función de transferencia de los sistemas
def sis(C, R2, nombre):
    R1, L = 1E3, 100E-3
    num = [L, R2]
    den = [C*L*R1, C*R1*R2+L, R1+R2]
    sys = ctrl.tf(num, den)
    print(f"Función de transferencia {nombre}: {sys}\n")
    return sys


# Sistemas
sysControl = sis(1E-6, 100E3, "Control")
sysCaso = sis(1000E-6, 1E3, "Caso")


# Componentes del controlador PID
kP, kI, kD = 13209.9564, 32316525.9285, 0.18118

Cr = 1E-6
Re = 1/(Cr*kI)
Rr = kP*Re
Ce = kD/Rr

numPID = [Re*Rr*Ce*Cr, Re*Ce+Rr*Cr, 1]
denPID = [Re*Cr, 0]

PID = ctrl.tf(numPID, denPID)


# Sistema de control en lazo cerrado
sysPID = ctrl.feedback(
    ctrl.series(PID, sysCaso),
    1,
    sign=-1
)

print(f"Función de transferencia en lazo cerrado: {sysPID}\n")


# Colores de las gráficas
clr1 = np.array([(118, 196, 87)])/255
clr2 = np.array([(27, 44, 193)])/255
clr3 = np.array([(147, 112, 219)])/255
clr4 = np.array([(221, 113, 113)])/255

# Funciones del sistema en lazo abierto y lazo cerrado
def openloop(t, sys, u):
    _, Vs = ctrl.forced_response(sys, t, u, x0)
    return Vs


def closedloop(t, sys, u):
    _, tratamientoPID = ctrl.forced_response(sys, t, u, x0)
    return tratamientoPID


# Respuestas: Simulaciones numéricas
Control = openloop(t, sysControl, u)
Caso = openloop(t, sysCaso, u)
Tratamiento = closedloop(t, sysPID, Control)


# Configuración de la figura
fg = plt.figure()
fg.set_size_inches(w, h)

plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']


# Gráficas con leyendas
plt.plot(t, u, '-', linewidth=1.5, color=clr1,
         label=r'$V_e(t)$')

plt.plot(t, Control, '-', linewidth=1.5, color=clr2,
         label=r'$V_{sx}(t)$')

plt.plot(t, Caso, '-', linewidth=1.5, color=clr3,
         label=r'$V_{sy}(t)$')

plt.plot(t, Tratamiento, ':', linewidth=1.5, color=clr4,
         label=r'$PID(t)$')


# Límites y divisiones de los ejes
plt.xlim(-0.1, 10)
plt.xticks(np.arange(0, 11, 1))

plt.ylim(0, 1.2)
plt.yticks(np.arange(0, 1.2, 0.1))


# Etiquetas de los ejes
plt.xlabel('t [s]')
plt.ylabel('V(t) [V]')


# Título
plt.title('Control y Caso', fontweight='bold')


# Leyenda en la parte superior
plt.legend(
    loc='upper center',
    bbox_to_anchor=(0.5, -0.15
                    ),
    ncol=4,
    frameon=False
)


# Ajustes finales
plt.tight_layout()

# Guardar y mostrar gráfica
fg.savefig('Control_caso_python4.pdf', bbox_inches='tight')
plt.show()