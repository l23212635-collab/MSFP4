[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=l23212635-collab/MSFP4)
# Práctica 4 — Modelado del sistema endocrino

Repositorio académico de la asignatura **Modelado de Sistemas Fisiológicos**, correspondiente al programa de **Ingeniería Biomédica** del Tecnológico Nacional de México / Instituto Tecnológico de Tijuana. Esta práctica integra modelado matemático, analogías eléctricas de sistemas fisiológicos, análisis temporal y de estabilidad, diseño de controladores PID, simulación computacional y comparación de resultados.

El caso de estudio representa el **sistema endocrino**, específicamente el eje hipotálamo-hipófisis-suprarrenal (HHS), mediante una analogía eléctrica basada en un circuito **RLC de segundo orden**. Se busca representar el comportamiento de la secreción, transporte, almacenamiento y respuesta hormonal, considerando dos condiciones: un caso control, que representa el funcionamiento endocrino de referencia, y un caso patológico, que representa una alteración en la regulación hormonal.

El modelo permite estudiar la relación entre una señal de entrada \(V_e(t)\), que representa el estímulo para la secreción hormonal, y una señal de salida \(V_s(t)\), que representa el nivel hormonal efectivo. También se analiza la respuesta del sistema ante las modificaciones de los componentes eléctricos y la incorporación de un controlador PID para evaluar los cambios en el comportamiento dinámico.

**Docente:** Dr. Paul Antonio Valle Trujillo

**Correo:** paul.valle@tectijuana.edu.mx

**Departamento:** Ingeniería Eléctrica y Electrónica

**Institución:** Tecnológico Nacional de México / Instituto Tecnológico de Tijuana

**Asignatura:** Modelado de Sistemas Fisiológicos

**Programa:** Ingeniería Biomédica

**Estudiante:** Perez Garcia Diego · 23212635 · l23212635@tectijuana.edu.mx

**Repositorio de la práctica:** https://github.com/l23212635-collab/MSFP4

**Sede:** Blvd. Alberto Limón Padilla s/n, Tijuana, C. P. 22454, B. C., México.

---

<a id="contenido"></a>
## Contenido

1. [Resumen](#resumen)
2. [Competencia y objetivos](#objetivos)
3. [Relación con el temario](#temario)
4. [Modelo físico y analogía eléctrica](#analogia)
5. [Formulación matemática](#modelo)
6. [Análisis temporal y de estabilidad](#analisis)
7. [Señales de entrada y condiciones de simulación](#senales)
8. [Implementación en MATLAB, Simulink y Simscape](#matlab)
9. [Control en lazo cerrado y sintonización PID](#pid)
10. [Reproducción en Python](#python)
11. [Controlador analógico y laboratorio](#laboratorio)
12. [Resultados y verificación cruzada](#resultados)
13. [Flujo de trabajo](#flujo)
14. [Actividades del estudiante](#actividades)
15. [Estructura del repositorio](#estructura)
16. [Requisitos](#requisitos)
17. [Reproducibilidad y entregables](#reproducibilidad)
18. [Diagrama del sistema endocrino](#diagrama-del-sistema-endocrino)
19. [Referencias](#referencias)

---

<a id="resumen"></a>
## 1. Resumen

La práctica tiene como propósito **desarrollar y analizar un modelo matemático simplificado del sistema endocrino**, utilizando una analogía eléctrica RLC para representar determinados procesos relacionados con la secreción, transporte, almacenamiento y utilización de hormonas.

El sistema fisiológico seleccionado corresponde al eje hipotálamo-hipófisis-suprarrenal (HHS), encargado de regular la respuesta hormonal ante estímulos como el estrés. Este eje involucra la participación del hipotálamo, la hipófisis anterior y la corteza suprarrenal, mediante la liberación secuencial de CRH, ACTH y cortisol, respectivamente. Además, cuenta con un mecanismo de retroalimentación negativa que permite regular la secreción hormonal.

Para representar su comportamiento dinámico se utiliza un circuito eléctrico RLC, donde la resistencia representa la oposición durante el transporte y la utilización hormonal, la capacitancia representa la acumulación temporal de la hormona y la inductancia representa la inercia o el retardo asociado con la respuesta del tejido.

Se consideran dos condiciones de funcionamiento: **caso control**, que representa una regulación hormonal normal, y **caso patológico**, que representa una alteración caracterizada por un incremento en la acumulación hormonal y una disminución en la resistencia de salida, produciendo una respuesta de mayor magnitud.

A partir del circuito equivalente se desarrollan las ecuaciones integro-diferenciales, la función de transferencia y la representación mediante ecuaciones diferenciales ordinarias. Posteriormente, se analiza el error en estado estacionario, la ubicación de los polos y la estabilidad del sistema.

Finalmente, se estudia la respuesta temporal mediante MATLAB, Simulink, Simscape Electrical y Python. También se contempla la incorporación de un controlador PID para modificar el comportamiento del caso patológico y comparar los resultados obtenidos.

**Palabras clave:** sistema endocrino; eje hipotálamo-hipófisis-suprarrenal; cortisol; CRH; ACTH; circuito RLC; función de transferencia; estabilidad; controlador PID; MATLAB; Simulink; Python.

[Volver al contenido](#contenido)

---

<a id="objetivos"></a>
## 2. Competencia y objetivos

### Competencia a desarrollar

Comprender los conceptos básicos de Ingeniería de Control, modelado matemático de sistemas fisiológicos, respuesta temporal y criterios de estabilidad mediante la representación eléctrica del sistema endocrino. La práctica permite aplicar herramientas matemáticas y computacionales para estudiar el comportamiento de un modelo fisiológico, comparar condiciones normales y patológicas e implementar estrategias de control.

### Objetivo general

Desarrollar y analizar un modelo matemático simplificado del sistema endocrino mediante una analogía eléctrica RLC, implementando simulaciones computacionales y un controlador PID para comparar el comportamiento de una condición hormonal normal con una condición alterada.

### Objetivos específicos

- Describir el funcionamiento del eje hipotálamo-hipófisis-suprarrenal y su participación en la regulación hormonal.
- Identificar las variables de entrada y salida del modelo, así como los parámetros eléctricos equivalentes.
- Representar el comportamiento del sistema endocrino mediante un circuito RLC de segundo orden.
- Obtener las ecuaciones integro-diferenciales a partir de las leyes de Kirchhoff.
- Obtener la función de transferencia del sistema mediante la transformada de Laplace.
- Expresar el modelo mediante ecuaciones diferenciales ordinarias.
- Calcular el error en estado estacionario para una entrada escalón unitario.
- Determinar los polos del sistema y analizar su estabilidad.
- Elaborar un bosquejo de la respuesta temporal antes de realizar las simulaciones.
- Comparar la respuesta del caso control con la del caso patológico.
- Implementar el modelo matemático en MATLAB, Simulink y Simscape Electrical.
- Diseñar e implementar un controlador PID para modificar la respuesta del sistema.
- Reproducir y comparar los resultados mediante Python.
- Documentar los resultados matemáticos, computacionales y gráficos en un repositorio de GitHub.

[Volver al contenido](#contenido)

---

<a id="temario"></a>
## 3. Relación con el temario

La práctica integra contenidos correspondientes a las áreas de la asignatura **Modelado de Sistemas Fisiológicos**:

| Área | Contenidos aplicados |
|---|---|
| Sistemas fisiológicos | Descripción del eje hipotálamo-hipófisis-suprarrenal y regulación hormonal |
| Modelado matemático | Analogía eléctrica RLC, leyes de Kirchhoff, ecuaciones integro-diferenciales y función de transferencia |
| Análisis de sistemas | Respuesta temporal, error en estado estacionario, polos y estabilidad |
| Sistemas de control | Diagramas de bloques, retroalimentación negativa y respuesta en lazo abierto y cerrado |
| Controladores | Diseño, implementación y sintonización de un controlador PID |
| Simulación computacional | Implementación del modelo en MATLAB, Simulink, Simscape Electrical y Python |

El enfoque combina **Fisiología, Ingeniería Biomédica, Electrónica Analógica, Ingeniería de Control y Ciencias de la Computación**, mediante la aplicación de herramientas matemáticas y computacionales para estudiar el comportamiento de un sistema biológico.

[Volver al contenido](#contenido)

---

<a id="analogia"></a>
## 4. Modelo físico y analogía eléctrica

### 4.1. Descripción fisiológica del sistema endocrino

El sistema endocrino está formado por glándulas y órganos que producen y liberan hormonas para regular diferentes funciones del organismo. Estas sustancias químicas se transportan a través del torrente sanguíneo y actúan sobre órganos y tejidos específicos.

Para esta práctica se utiliza como referencia el **eje hipotálamo-hipófisis-suprarrenal (HHS)**, que participa en la regulación de la respuesta fisiológica ante situaciones de estrés.

Su funcionamiento general se describe mediante la siguiente secuencia:

1. El **hipotálamo** libera la hormona liberadora de corticotropina (CRH).
2. La **hipófisis anterior** responde a la CRH liberando la hormona adrenocorticotropa (ACTH).
3. La **glándula suprarrenal**, específicamente la corteza suprarrenal, responde a la ACTH liberando cortisol.
4. El **cortisol** actúa sobre diferentes órganos diana, participando en la regulación del metabolismo de la glucosa, la respuesta al estrés y la movilización de energía.
5. Cuando aumenta el cortisol, se activa un mecanismo de **retroalimentación negativa**, que inhibe la liberación de CRH y ACTH.

Este mecanismo permite mantener regulada la concentración hormonal y evitar una respuesta excesiva.

### 4.2. Analogía eléctrica del sistema endocrino

Para estudiar el comportamiento dinámico del sistema se utiliza un circuito RLC. Cada componente eléctrico representa una propiedad simplificada del proceso fisiológico.


| Símbolo | Equivalente eléctrico | Interpretación fisiológica |
|---|---|---|
| $V_e(t)$ | Voltaje de entrada | Estímulo para la secreción hormonal |
| $F_e(t)$ | Corriente de entrada | Flujo de secreción y transporte hormonal |
| $R_1$ | Resistencia | Pérdidas y oposición durante el transporte hormonal |
| $C$ | Capacitancia | Acumulación temporal de hormona |
| $L$ | Inductancia | Retardo o inercia de la respuesta del tejido |
| $R_2$ | Resistencia | Utilización, disipación o eliminación de la señal hormonal |
| $F_s(t)$ | Corriente de salida | Flujo asociado a la respuesta del tejido |
| $V_s(t)$ | Voltaje de salida | Nivel hormonal efectivo disponible |


La señal de entrada \(V_e(t)\) representa el estímulo que inicia la respuesta endocrina, mientras que la salida \(V_s(t)\) representa el nivel hormonal efectivo obtenido después de considerar la dinámica del modelo.

### 4.3. Parámetros para la emulación eléctrica

El circuito considera los siguientes componentes eléctricos:


| Parámetro | Caso control | Caso patológico | Unidad |
|---|---:|---:|---|
| $R_1$ | 1 | 1 | kΩ |
| $L$ | 100 | 100 | mH |
| $C$ | 1 | 1000 | μF |
| $R_2$ | 100 | 1 | kΩ |


La diferencia entre las dos condiciones se representa mediante la modificación de la capacitancia y de la resistencia de salida.

En el caso control se considera una acumulación hormonal moderada y una utilización o eliminación regulada. En el caso patológico se incrementa la capacitancia y disminuye la resistencia de salida, representando una mayor acumulación y una menor oposición a la utilización o eliminación de la señal.

> **Alcance de la analogía:** el circuito RLC representa una aproximación matemática y eléctrica del comportamiento dinámico del sistema endocrino. Los componentes no representan literalmente las estructuras anatómicas ni reproducen todos los mecanismos bioquímicos y fisiológicos involucrados en la regulación hormonal.

[Volver al contenido](#contenido)

---

<a id="modelo"></a>
## 5. Formulación matemática

### 5.1. Ecuaciones integro-diferenciales

Para obtener el modelo matemático se utiliza el circuito RLC equivalente del sistema endocrino y se aplican las leyes de Kirchhoff.

Se consideran las siguientes relaciones eléctricas:

- $V_e(t)$: voltaje de entrada.
- $V_s(t)$: voltaje de salida.
- $I_1(t)$: corriente de entrada.
- $I_2(t)$: corriente de salida.
- $R_1$: resistencia de entrada.
- $R_2$: resistencia de salida.
- $L$: inductancia.
- $C$: capacitancia.


Aplicando la ley de corrientes de Kirchhoff en el nodo principal:

$$
I_C(t)=I_1(t)-I_2(t)
$$

La relación de voltaje en el capacitor es:

$$
V_C(t)=\frac{1}{C}\int [I_1(t)-I_2(t)]\,dt
$$

La relación de voltaje en el inductor es:

$$
V_L(t)=L\frac{dI_2(t)}{dt}
$$

El voltaje en la resistencia de salida es:

$$
V_{R_2}(t)=R_2I_2(t)
$$

Aplicando la ley de voltajes de Kirchhoff en la rama de entrada:

$$
V_e(t)=R_1I_1(t)+\frac{1}{C}\int[I_1(t)-I_2(t)]\,dt
$$

Para la rama de salida:

$$
\frac{1}{C}\int[I_1(t)-I_2(t)]\,dt=L\frac{dI_2(t)}{dt}+R_2I_2(t)
$$

Estas ecuaciones describen el comportamiento eléctrico del circuito equivalente utilizado para representar el sistema endocrino.

### 5.2. Función de transferencia

La función de transferencia se obtiene mediante la transformada de Laplace, considerando condiciones iniciales nulas.

A partir de las ecuaciones del circuito se obtiene:

$$
V_e(s)=R_1I_1(s)+\frac{I_1(s)-I_2(s)}{Cs}
$$

Para la rama de salida:

$$
\frac{I_1(s)-I_2(s)}{Cs}=(Ls+R_2)I_2(s)
$$

Despejando la corriente de entrada:

$$
I_1(s)=[1+Cs(Ls+R_2)]I_2(s)
$$

Sustituyendo en la ecuación de entrada:

$$
V_e(s)=R_1[1+Cs(Ls+R_2)]I_2(s)+(Ls+R_2)I_2(s)
$$

Agrupando términos:

$$
V_e(s)=[R_1LCs^2+(L+R_1R_2C)s+(R_1+R_2)]I_2(s)
$$

El voltaje de salida se expresa como:

$$
V_s(s)=(Ls+R_2)I_2(s)
$$

Por lo tanto, la función de transferencia del sistema es:

$$
\boxed{G(s)=\frac{V_s(s)}{V_e(s)}=\frac{Ls+R_2}{R_1LCs^2+(L+R_1R_2C)s+(R_1+R_2)}}
$$

Donde:


- $V_s(s)$: voltaje de salida del sistema.
- $V_e(s)$: voltaje de entrada.
- $R_1$: resistencia de entrada.
- $R_2$: resistencia de salida.
- $L$: inductancia.
- $C$: capacitancia.
- $s$: variable compleja del dominio de Laplace.

Esta función de transferencia representa la relación entre el estímulo aplicado y la respuesta hormonal equivalente del sistema.

### 5.3. Ecuación diferencial ordinaria (EDO)

Partiendo de la función de transferencia:

$$
\frac{V_s(s)}{V_e(s)}=\frac{Ls+R_2}{R_1LCs^2+(L+R_1R_2C)s+(R_1+R_2)}
$$

Se realiza el producto cruzado:

$$
[R_1LCs^2+(L+R_1R_2C)s+(R_1+R_2)]V_s(s)=(Ls+R_2)V_e(s)
$$

Aplicando la transformada inversa de Laplace, considerando condiciones iniciales nulas, se obtiene:

$$
\boxed{R_1LC\frac{d^2V_s(t)}{dt^2}+(L+R_1R_2C)\frac{dV_s(t)}{dt}+(R_1+R_2)V_s(t)=L\frac{dV_e(t)}{dt}+R_2V_e(t)}
$$

Esta ecuación diferencial ordinaria describe la relación dinámica entre la señal de entrada y la señal de salida del sistema endocrino.

### 5.4. Representación en espacio de estados

Para representar el sistema mediante ecuaciones diferenciales de primer orden se definen las variables de estado:

$$
x_1(t)=V_C(t)
$$

$$
x_2(t)=I_2(t)
$$

A partir de las relaciones del circuito:

$$
I_1(t)=\frac{V_e(t)-x_1(t)}{R_1}
$$

La primera ecuación de estado es:

$$
\boxed{
\dot{x}_1(t)=\frac{1}{C}\left[\frac{V_e(t)-x_1(t)}{R_1}-x_2(t)\right]}
$$

La segunda ecuación de estado es:

$$
\boxed{
\dot{x}_2(t)=\frac{x_1(t)-R_2x_2(t)}{L}}
$$

La salida del sistema se obtiene mediante:

$$
\boxed{V_s(t)=R_2x_2(t)}
$$

Esta representación permite implementar el modelo mediante integradores y bloques matemáticos en Simulink.

[Volver al contenido](#contenido)

---

<a id="analisis"></a>
## 6. Análisis temporal y de estabilidad

### 6.1. Error en estado estacionario

Para calcular el error en estado estacionario se considera una entrada escalón unitario:

$$
V_e(s)=\frac{1}{s}
$$

El error se define como la diferencia entre la entrada y la salida:

$$
e(t)=V_e(t)-V_s(t)
$$

En el dominio de Laplace:

$$
E(s)=V_e(s)-V_s(s)
$$

Como:

$$
V_s(s)=G(s)V_e(s)
$$

Se obtiene:

$$
E(s)=[1-G(s)]V_e(s)
$$

Aplicando el teorema del valor final:

$$
e_{ss}=\lim_{s\to0}sE(s)
$$

Sustituyendo la entrada escalón:

$$
e_{ss}=\lim_{s\to0}s[1-G(s)]\frac{1}{s}
$$

Por lo tanto:

$$
e_{ss}=1-G(0)
$$

Evaluando la función de transferencia en \(s=0\):

$$
G(0)=\frac{R_2}{R_1+R_2}
$$

Finalmente:

$$
\boxed{
e_{ss}=\frac{R_1}{R_1+R_2}}
$$

**Caso control:**

Con:

$$
R_1=1\,k\Omega
$$

$$
R_2=100\,k\Omega
$$

Se obtiene:

$$
e_{ss}=\frac{1}{1+100}
$$

$$
{e_{ss}=0.0099\approx0.99\%}
$$

**Caso patológico:**

Con:

$$
R_1=1\,k\Omega
$$

$$
R_2=1\,k\Omega
$$

Se obtiene:

$$
e_{ss}=\frac{1}{1+1}
$$

$$
e_{ss}=0.5=50\%}
$$

Los resultados muestran que el caso control presenta un error estacionario considerablemente menor que el caso patológico. Esto se relaciona con la diferencia entre las resistencias de salida de ambos modelos.

### 6.2. Polos y estabilidad

Para determinar la estabilidad del sistema se iguala a cero el denominador de la función de transferencia:

$$
R_1LCs^2+(L+R_1R_2C)s+(R_1+R_2)=0
$$

Aplicando la fórmula general:

$$
\boxed{s_{1,2}=\frac{-(L+R_1R_2C)\pm\sqrt{(L+R_1R_2C)^2-4R_1LC(R_1+R_2)}}{2R_1LC}}
$$

Los polos permiten identificar la estabilidad y el comportamiento transitorio del sistema.

**Caso control:**

Los parámetros utilizados son:

- $R_1 = 1\,k\Omega$
- $R_2 = 100\,k\Omega$
- $L = 100\,mH$
- $C = 1\,\mu F$


Los polos aproximados son:

$$
s_1\approx-1010.01
$$

$$
s_2\approx-999989.99
$$

Ambos polos son reales y negativos, por lo que el sistema es estable y presenta una respuesta sobreamortiguada.

**Caso patológico:**

Los parámetros utilizados son:


- $R_1 = 1\,k\Omega$
- $R_2 = 1\,k\Omega$
- $L = 100\,mH$
- $C = 1000\,\mu F$


Los polos aproximados son:

$$
s_1\approx-2.0002
$$

$$
s_2\approx-9997.9998
$$

Los dos polos también son reales y negativos. Por lo tanto, el sistema continúa siendo estable y presenta una respuesta sobreamortiguada.

### 6.3. Interpretación de la estabilidad

Para ambos modelos se cumple que los polos se encuentran en el semiplano izquierdo del plano complejo.

Esto significa que las respuestas naturales del sistema disminuyen con el tiempo y que el sistema es estable en lazo abierto.

Sin embargo, la ubicación de los polos cambia entre el caso control y el patológico, modificando la velocidad de respuesta del sistema.

El caso control presenta una respuesta más rápida, mientras que el caso patológico presenta una dinámica más lenta debido al incremento de la capacitancia.

### 6.4. Predicción y bosquejo de la respuesta

Antes de realizar las simulaciones se elabora un bosquejo cualitativo de la respuesta al escalón, considerando la estabilidad, la ubicación de los polos y el valor final de cada condición.

Se espera observar:

- **Entrada \(V_e(t)\):** señal escalón que alcanza el valor de referencia.
- **Salida del control \(V_s(t)\):** respuesta rápida que se aproxima al valor final de la entrada.
- **Salida del caso \(V_s(t)\):** respuesta más lenta y de menor magnitud final.
- **Estabilidad:** ambas respuestas se mantienen acotadas y convergen a un valor constante.

El bosquejo debe permitir comparar visualmente las diferencias entre las dos condiciones antes de ejecutar los modelos computacionales.

### 6.5. Ejemplo de verificación en MATLAB

```matlab
clc;
clear;
close all;

% Parámetros del caso control
R1_control = 1e3;
R2_control = 100e3;
L_control = 100e-3;
C_control = 1e-6;

% Parámetros del caso patológico
R1_caso = 1e3;
R2_caso = 1e3;
L_caso = 100e-3;
C_caso = 1000e-6;

% Funciones de transferencia
G_control = tf([L_control R2_control], ...
    [R1_control*L_control*C_control, ...
    L_control + R1_control*R2_control*C_control, ...
    R1_control + R2_control]);

G_caso = tf([L_caso R2_caso], ...
    [R1_caso*L_caso*C_caso, ...
    L_caso + R1_caso*R2_caso*C_caso, ...
    R1_caso + R2_caso]);

% Cálculo de polos
polos_control = pole(G_control)
polos_caso = pole(G_caso)

% Error en estado estacionario
ess_control = 1 - dcgain(G_control)
ess_caso = 1 - dcgain(G_caso)

% Respuesta al escalón
figure;
step(G_control, G_caso);
grid on;
legend('Control', 'Caso');
title('Respuesta al escalón del sistema endocrino');
xlabel('Tiempo (s)');
ylabel('Voltaje (V)');
```

[Volver al contenido](#contenido)

---

<a id="senales"></a>
## 7. Señales de entrada y condiciones de simulación

Para estudiar el comportamiento dinámico del sistema endocrino se utiliza una señal de entrada \(V_e(t)\), que representa el estímulo que inicia la respuesta hormonal.

La misma señal debe aplicarse a las dos condiciones para realizar una comparación adecuada entre el caso control y el caso patológico.

Se consideran las siguientes señales para el análisis del sistema:

| Señal | Descripción | Propósito |
|---|---|---|
| Escalón | Cambio instantáneo de la señal de entrada | Analizar el valor final, el error y la respuesta transitoria |
| Pulso | Señal aplicada durante un intervalo definido | Observar la respuesta ante un estímulo de duración limitada |
| Rampa | Señal que aumenta progresivamente | Analizar la respuesta ante un estímulo creciente |
| Senoidal | Señal periódica | Observar el comportamiento ante una entrada variable |

### Condiciones de simulación

La configuración de referencia utilizada para el análisis considera:

| Parámetro | Valor |
|---|---|
| Tiempo inicial | 0 s |
| Tiempo final | 10 s |
| Solver | `ode15s` |
| Paso máximo de referencia | \(1\times10^{-3}\) s |
| Condiciones iniciales | Cero |

El paso máximo debe revisarse de acuerdo con las escalas temporales del circuito, debido a que los polos presentan magnitudes muy diferentes.

Las señales de entrada deben aplicarse de manera equivalente en MATLAB, Simulink y Python para que los resultados puedan compararse.

[Volver al contenido](#contenido)

---

<a id="matlab"></a>
## 8. Implementación en MATLAB, Simulink y Simscape

Se utilizan herramientas de MATLAB y Simulink para implementar el modelo matemático del sistema endocrino y estudiar su respuesta dinámica.

La implementación contempla las siguientes representaciones:

| Implementación | Descripción | Aspecto por verificar |
|---|---|---|
| Ecuaciones integro-diferenciales | Construcción del modelo mediante bloques de suma, ganancias e integradores | Correspondencia con las leyes de Kirchhoff |
| Función de transferencia | Representación de la planta mediante el bloque Transfer Fcn | Correspondencia con la función de transferencia obtenida |
| Simscape Electrical | Representación del circuito mediante resistencias, capacitor e inductor | Correspondencia entre los componentes y el modelo matemático |
| Comparación de respuestas | Simulación del caso control y patológico | Diferencias en la respuesta temporal |

### 8.1. Parámetros del modelo

Los parámetros deben definirse en MATLAB utilizando las unidades eléctricas correspondientes:

```matlab
% Parámetros del caso control
R1_control = 1e3;
R2_control = 100e3;
L_control = 100e-3;
C_control = 1e-6;

% Parámetros del caso patológico
R1_caso = 1e3;
R2_caso = 1e3;
L_caso = 100e-3;
C_caso = 1000e-6;

% Tiempo de simulación
t = 0:1e-3:10;
```

### 8.2. Funciones de transferencia

Las funciones de transferencia se construyen mediante los parámetros eléctricos:

```matlab
% Caso control
num_control = [L_control R2_control];

den_control = [R1_control*L_control*C_control, ...
    L_control + R1_control*R2_control*C_control, ...
    R1_control + R2_control];

G_control = tf(num_control, den_control);

% Caso patológico
num_caso = [L_caso R2_caso];

den_caso = [R1_caso*L_caso*C_caso, ...
    L_caso + R1_caso*R2_caso*C_caso, ...
    R1_caso + R2_caso];

G_caso = tf(num_caso, den_caso);
```

### 8.3. Simulación en Simulink

El modelo puede representarse mediante dos métodos:

1. **Modelo por ecuaciones:** utilizando integradores, sumadores y ganancias para implementar las ecuaciones diferenciales del sistema.
2. **Modelo por función de transferencia:** utilizando el bloque Transfer Fcn e ingresando los coeficientes del numerador y denominador.

También se contempla la construcción del circuito equivalente mediante componentes de Simscape Electrical.

### 8.4. Parámetros de simulación

La configuración de referencia utilizada en el modelo contempla:


| Parámetro | Configuración |
|---|---|
| Tiempo de simulación | 10 s |
| Solver | `ode15s` |
| Paso máximo | $1\times10^{-3}$ s |
| Condición inicial | Cero |


Debido a las diferencias entre las escalas temporales de los polos, se debe verificar que el paso de simulación permita representar adecuadamente la respuesta del circuito.

### 8.5. Señales que deben registrarse


1. Señal de entrada $V_e(t)$.
2. Respuesta de salida del caso control.
3. Respuesta de salida del caso patológico.
4. Respuesta del caso patológico con el controlador PID.


Las señales deben almacenarse para generar las gráficas comparativas correspondientes.

[Volver al contenido](#contenido)

---

<a id="pid"></a>
## 9. Control en lazo cerrado y sintonización PID

### 9.1. Retroalimentación negativa

El controlador PID se incorpora para modificar el comportamiento dinámico del sistema endocrino y evaluar la posibilidad de mejorar la respuesta del caso patológico.

La señal de error se define como la diferencia entre la referencia y la salida:

$$
e(t)=r(t)-y(t)
$$

Donde:


- $e(t)$: error del sistema.
- $r(t)$: señal de referencia.
- $y(t)$: salida del sistema.


En este modelo, la salida se retroalimenta para compararse con la señal de entrada y generar una señal de error.

### 9.2. Ley de control PID

El controlador PID combina tres acciones de control:


- $K_p$: ganancia proporcional.
- $K_i$: ganancia integral.
- $K_d$: ganancia derivativa.


La expresión general del controlador en el dominio del tiempo es:

$$
u(t)=K_p e(t)+K_i\int_0^t e(\tau)\,d\tau+K_d\frac{de(t)}{dt}
$$

En el dominio de Laplace:

$$
K(s)=K_p+\frac{K_i}{s}+K_ds
$$

Para una retroalimentación negativa unitaria, la función de transferencia de lazo cerrado es:

$$
\boxed{
T(s)=\frac{K(s)G(s)}{1+K(s)G(s)}}
$$

### 9.3. Sintonización del controlador

La sintonización del controlador permite modificar el comportamiento del sistema mediante el ajuste de las ganancias proporcional, integral y derivativa.

En MATLAB y Simulink se utiliza el bloque PID Controller para ajustar las ganancias y observar el comportamiento de la respuesta en lazo cerrado.

Los valores obtenidos deben registrarse en la siguiente tabla:


| Ganancia | Valor obtenido |
|---|---|
| $K_p$ | Registrar valor de la simulación |
| $K_i$ | Registrar valor de la simulación |
| $K_d$ | Registrar valor de la simulación |


Las ganancias definitivas deben corresponder a las utilizadas en el modelo y comprobarse mediante las gráficas obtenidas.

### 9.4. Comparación del sistema con PID

Se comparan tres respuestas:

1. Caso control sin controlador.
2. Caso patológico sin controlador.
3. Caso patológico con controlador PID.

La comparación permite observar los cambios en la rapidez de respuesta, el valor final, el comportamiento transitorio y el error del sistema.

### 9.5. Realización mediante componentes analógicos

El modelo eléctrico del sistema endocrino utiliza resistencias, inductores y capacitores para representar la dinámica del circuito equivalente.

Los componentes considerados son:


| Componente | Función dentro del circuito |
|---|---|
| Resistencia $R_1$ | Representa las pérdidas y oposición durante el transporte hormonal |
| Inductor $L$ | Representa la inercia o retardo de la respuesta |
| Capacitor $C$ | Representa la acumulación temporal de la hormona |
| Resistencia $R_2$ | Representa la utilización, disipación o eliminación hormonal |
| Fuente $V_e(t)$ | Representa el estímulo para la secreción hormonal |
| Salida $V_s(t)$ | Representa el nivel hormonal efectivo |


La implementación analógica del controlador debe realizarse mediante el diseño correspondiente con amplificadores operacionales y los componentes calculados para las ganancias deseadas.

Los valores finales de los componentes deben corresponder al diseño efectivamente utilizado y verificarse mediante simulación antes de realizar el montaje físico.

[Volver al contenido](#contenido)

---

<a id="python"></a>
## 10. Reproducción en Python

Python se utiliza como herramienta complementaria para reproducir el modelo matemático y comparar sus resultados con MATLAB y Simulink.

La implementación permite estudiar el comportamiento del sistema endocrino bajo las condiciones control y patológica, utilizando los mismos parámetros y señales de entrada.

### 10.1. Parámetros principales

```python
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Parámetros del caso control
R1_control = 1e3
R2_control = 100e3
L_control = 100e-3
C_control = 1e-6

# Parámetros del caso patológico
R1_caso = 1e3
R2_caso = 1e3
L_caso = 100e-3
C_caso = 1000e-6

# Vector de tiempo
t = np.arange(0, 10.001, 1e-3)
```

### 10.2. Construcción de las funciones de transferencia

```python
# Caso control
num_control = [L_control, R2_control]

den_control = [
    R1_control * L_control * C_control,
    L_control + R1_control * R2_control * C_control,
    R1_control + R2_control
]

sys_control = ctrl.tf(num_control, den_control)

# Caso patológico
num_caso = [L_caso, R2_caso]

den_caso = [
    R1_caso * L_caso * C_caso,
    L_caso + R1_caso * R2_caso * C_caso,
    R1_caso + R2_caso
]

sys_caso = ctrl.tf(num_caso, den_caso)
```

### 10.3. Cálculo de polos

```python
polos_control = ctrl.poles(sys_control)
polos_caso = ctrl.poles(sys_caso)

print("Polos del caso control:")
print(polos_control)

print("Polos del caso patológico:")
print(polos_caso)
```

### 10.4. Respuesta del sistema

La respuesta del sistema se calcula utilizando las funciones de transferencia y las señales de entrada definidas para la simulación.

Se deben obtener las respuestas correspondientes al caso control y al caso patológico, manteniendo los mismos parámetros temporales.

### 10.5. Controlador PID

Para reproducir el comportamiento del sistema con PID se utilizan las ganancias obtenidas durante la sintonización en MATLAB y Simulink.

La función del controlador es:

$$
K(s)=K_p+\frac{K_i}{s}+K_ds
$$

La función de transferencia de lazo cerrado se obtiene mediante:

$$
T(s)=\frac{K(s)G(s)}{1+K(s)G(s)}
$$

### 10.6. Gráficas

El programa debe generar las figuras necesarias para observar:

- Señal de entrada.
- Respuesta del caso control.
- Respuesta del caso patológico.
- Respuesta del caso patológico con PID.

Las gráficas deben incluir título, etiquetas de los ejes, unidades y leyenda.

[Volver al contenido](#contenido)

---

<a id="laboratorio"></a>
## 11. Controlador analógico y laboratorio

La representación eléctrica permite establecer una relación entre el modelo matemático del sistema endocrino y su implementación mediante componentes físicos.

El circuito RLC se construye utilizando resistencias, inductores y capacitores que corresponden a los parámetros definidos para el caso control y el caso patológico.

### Materiales y equipo

**Componentes:**

- Resistencias de 1 kΩ.
- Resistencia de 100 kΩ.
- Inductor de 100 mH.
- Capacitor de 1 μF.
- Capacitor de 1000 μF.
- Amplificadores operacionales para el controlador PID.
- Resistencias y capacitores adicionales según el diseño del controlador.
- Protoboard.
- Cables de conexión.

**Instrumentos:**

- Generador de funciones.
- Fuente de alimentación.
- Osciloscopio.
- Multímetro digital.
- Computadora para la simulación y registro de resultados.

### 11.1. Circuito RLC en lazo abierto

Se construye el circuito equivalente del sistema endocrino utilizando los valores correspondientes al caso control.

Posteriormente, se modifica la capacitancia y la resistencia de salida para representar el caso patológico.

Se aplican señales de entrada y se registra la respuesta de salida utilizando el osciloscopio.

Se deben conservar las capturas correspondientes a cada condición para realizar la comparación.

### 11.2. Controlador y circuito en lazo cerrado

El controlador PID se incorpora al circuito mediante una configuración de retroalimentación negativa.

La señal de salida se compara con la referencia para obtener el error que utiliza el controlador.

La señal de control se aplica a la planta para modificar su respuesta dinámica.

Antes de realizar el montaje físico se deben verificar las conexiones, polaridades, valores nominales y límites eléctricos de los componentes.

### 11.3. Comparación con la simulación

Los resultados experimentales deben compararse con las respuestas obtenidas mediante MATLAB, Simulink y Python.

Las diferencias pueden estar relacionadas con:

- Tolerancias de las resistencias.
- Variaciones de los valores de inductancia y capacitancia.
- Características reales de los amplificadores operacionales.
- Limitaciones de los instrumentos de medición.
- Condiciones iniciales del circuito.
- Diferencias entre el modelo matemático y la implementación física.

[Volver al contenido](#contenido)

---

<a id="resultados"></a>
## 12. Resultados y verificación cruzada

Los resultados permiten contrastar el comportamiento del sistema endocrino bajo dos condiciones: caso control y caso patológico.

La comparación se realiza mediante las respuestas obtenidas en MATLAB, Simulink, Python y, cuando corresponda, mediante el circuito físico.

### 12.1. Comparación de parámetros

| Característica | Control | Caso |
|---|---:|---:|
| \(R_1\) | 1 kΩ | 1 kΩ |
| \(R_2\) | 100 kΩ | 1 kΩ |
| \(L\) | 100 mH | 100 mH |
| \(C\) | 1 μF | 1000 μF |
| Error estacionario | 0.99 % | 50 % |
| Comportamiento | Respuesta de referencia | Condición alterada |
| Estabilidad | Estable | Estable |
| Amortiguamiento | Sobreamortiguado | Sobreamortiguado |

### 12.2. Interpretación de los resultados

El caso control presenta un error en estado estacionario menor debido a que la resistencia de salida es considerablemente mayor que la resistencia de entrada.

En el caso patológico, la disminución de \(R_2\) produce un incremento del error estacionario. Además, el aumento de la capacitancia modifica la dinámica del circuito y provoca una respuesta más lenta.

Ambos modelos son estables debido a que sus polos se encuentran en el semiplano izquierdo del plano complejo.

La comparación permite observar cómo los cambios en los parámetros eléctricos modifican la respuesta del sistema y representan diferentes condiciones de funcionamiento del modelo endocrino.

### 12.3. Convención de colores para las gráficas

Se recomienda conservar una convención de colores uniforme:

- **Azul:** señal de entrada \(V_e(t)\).
- **Amarillo:** respuesta de salida del caso control.
- **Rojo:** respuesta de salida del caso patológico.
- **Verde:** respuesta del caso patológico con PID.

### 12.4. Archivos de resultados

Los nombres siguientes representan una propuesta de organización y deben ajustarse a los archivos reales del repositorio.

| Resultado | Archivo sugerido |
|---|---|
| Análisis matemático | `Analisis_Matematico_Endocrino.pdf` |
| Comparación control y caso | `Control_vs_Caso.pdf` |
| Respuesta con PID | `Endocrino_Control_Caso_PID.pdf` |
| Modelo fisiológico | `Sistema_Endocrino.png` |
| Modelo de Simulink | `Sistema_Endocrino.slx` |
| Simulación en MATLAB | `Practica4_Endocrino.mlx` |
| Simulación en Python | `Practica4_Endocrino.py` |

### 12.5. Aspectos para discutir

- Diferencias entre los parámetros eléctricos del caso control y patológico.
- Efecto del incremento de la capacitancia sobre la respuesta temporal.
- Efecto de la disminución de la resistencia de salida sobre el error estacionario.
- Ubicación de los polos y su relación con la estabilidad.
- Correspondencia entre el comportamiento fisiológico y la analogía eléctrica.
- Diferencias entre la respuesta del sistema sin controlador y con PID.
- Consistencia entre las gráficas obtenidas mediante MATLAB, Simulink y Python.
- Limitaciones de representar un sistema endocrino mediante un circuito RLC.

**Resultados del estudiante:** incorporar las gráficas y evidencias reales, así como una interpretación propia de los resultados obtenidos durante las simulaciones.

[Volver al contenido](#contenido)

---

<a id="flujo"></a>

## Flujo de trabajo

```text
       Descripción del sistema endocrino
                    |
                    v
          Analogía eléctrica RLC
                    |
                    v
       Desarrollo del modelo matemático
                    |
                    v
    Obtención de la función de transferencia
                    |
                    v
    Definición de parámetros y señal de entrada
                    |
                    v
                  MATLAB
                    |
                    v
                 Simulink
                    |
                    v
       Análisis del caso control y patológico
                    |
                    v
          Diseño del controlador PID
                    |
                    v
          Simulación del sistema en lazo cerrado
                    |
                    v
           Reproducción del modelo en Python
                    |
                    v
       Comparación y análisis de resultados
                    |
                    v
              Conclusiones finales
```


El flujo integra la descripción fisiológica, la formulación matemática, la simulación computacional, el análisis de control y la documentación de los resultados.

[Volver al contenido](#contenido)

---

<a id="actividades"></a>
## 14. Actividades del estudiante

La práctica sigue una secuencia de **modelado, análisis, simulación, comparación y documentación**, enfocada en el estudio del comportamiento del sistema endocrino.

### Etapa 1. Descripción y formulación

- [ ] Describir el funcionamiento del eje hipotálamo-hipófisis-suprarrenal.
- [ ] Identificar las variables de entrada y salida del sistema.
- [ ] Identificar los componentes eléctricos del circuito RLC.
- [ ] Establecer los parámetros del caso control y patológico.
- [ ] Derivar las ecuaciones integro-diferenciales.
- [ ] Obtener la función de transferencia.
- [ ] Expresar el modelo mediante ecuaciones diferenciales ordinarias.
- [ ] Calcular el error en estado estacionario.
- [ ] Determinar los polos del sistema.
- [ ] Analizar la estabilidad.
- [ ] Elaborar el bosquejo de la respuesta al escalón.

### Etapa 2. Simulación de la planta

- [ ] Implementar el modelo por ecuaciones en Simulink.
- [ ] Implementar la función de transferencia en Simulink.
- [ ] Construir el circuito equivalente mediante Simscape Electrical.
- [ ] Definir las señales de entrada.
- [ ] Simular la respuesta del caso control.
- [ ] Simular la respuesta del caso patológico.
- [ ] Generar las gráficas comparativas.
- [ ] Comparar los resultados de las diferentes implementaciones.

### Etapa 3. Diseño y comprobación del controlador

- [ ] Implementar la retroalimentación negativa.
- [ ] Incorporar el controlador PID.
- [ ] Sintonizar las ganancias \(K_p\), \(K_i\) y \(K_d\).
- [ ] Registrar los valores obtenidos.
- [ ] Analizar el comportamiento del sistema en lazo cerrado.
- [ ] Comparar la respuesta del caso sin PID y con PID.
- [ ] Evaluar el tiempo de establecimiento y el sobreimpulso.
- [ ] Reproducir las simulaciones mediante Python.
- [ ] Verificar la consistencia entre MATLAB y Python.

### Etapa 4. Comprobación y documentación

- [ ] Incorporar las gráficas generadas en MATLAB.
- [ ] Incorporar el modelo de Simulink.
- [ ] Incorporar el modelo de Simscape Electrical.
- [ ] Incorporar el código de Python.
- [ ] Agregar evidencia del análisis matemático.
- [ ] Agregar la representación fisiológica del sistema endocrino.
- [ ] Documentar los resultados y las diferencias observadas.
- [ ] Verificar los nombres y enlaces de los archivos.
- [ ] Publicar los archivos correspondientes en GitHub.

[Volver al contenido](#contenido)

---

<a id="estructura"></a>
## 15. Estructura del repositorio

Se propone la siguiente organización para mantener los archivos de la práctica ordenados:

```text
MSFP4/
│
├── README.md
│
├── MATLAB/
│   └── Practica4_Endocrino.mlx
│
├── Simulink/
│   └── Sistema_Endocrino.slx
│
├── Simscape/
│   └── Circuito_RLC_Endocrino.slx
│
├── Python/
│   └── Practica4_Endocrino.py
│
├── Resultados/
│   ├── Analisis_Matematico_Endocrino.pdf
│   ├── Control_vs_Caso.pdf
│   └── Endocrino_Control_Caso_PID.pdf
│
├── Evidencias/
│   ├── Modelo_Endocrino.png
│   ├── Circuito_RLC.png
│   ├── Controlador_PID.png
│   └── Simulaciones/
│
└── Referencias/
```

**Criterio de nombres:** los nombres anteriores son propuestas de organización. Deben coincidir con los nombres reales de los archivos incluidos en el repositorio. Si se utilizan otras denominaciones o subcarpetas, actualizar las rutas del README para que los enlaces funcionen correctamente.

[Volver al contenido](#contenido)

---

<a id="requisitos"></a>
## 16. Requisitos

### Software

- **MATLAB:** para la definición y análisis de las funciones de transferencia.
- **Simulink:** para la construcción y simulación del modelo dinámico.
- **Simscape Electrical:** para la representación del circuito RLC mediante componentes eléctricos.
- **Python:** para reproducir el modelo y generar las gráficas.
- **Visual Studio Code** u otro entorno compatible para ejecutar Python.
- Bibliotecas de Python utilizadas por el código, entre ellas NumPy, Matplotlib y `control`, si están incluidas en el script.
- **Git y GitHub:** para organizar y publicar el repositorio.
- **BioRender:** para elaborar la representación fisiológica del sistema endocrino, si se utiliza en la evidencia entregada.

### Requisitos de reproducibilidad

- Mantener los mismos parámetros eléctricos en MATLAB y Python.
- Utilizar las mismas señales de entrada.
- Conservar las condiciones iniciales.
- Documentar el solver y el paso temporal.
- Registrar las ganancias PID realmente utilizadas.
- Identificar las versiones y dependencias necesarias para ejecutar los programas.
- Conservar las gráficas y evidencias correspondientes a cada condición.

[Volver al contenido](#contenido)

---

<a id="reproducibilidad"></a>
## 17. Reproducibilidad y entregables

### Secuencia de reproducción

1. Revisar la descripción fisiológica del eje hipotálamo-hipófisis-suprarrenal.
2. Identificar los componentes eléctricos del circuito RLC.
3. Definir los parámetros correspondientes al caso control y patológico.
4. Obtener las ecuaciones integro-diferenciales.
5. Obtener la función de transferencia y las ecuaciones diferenciales ordinarias.
6. Calcular el error en estado estacionario.
7. Calcular los polos y analizar la estabilidad.
8. Elaborar el bosquejo de la respuesta al escalón.
9. Construir los modelos del sistema en MATLAB y Simulink.
10. Implementar el circuito equivalente en Simscape Electrical.
11. Aplicar las señales de entrada definidas para la práctica.
12. Obtener las respuestas del caso control y patológico.
13. Implementar y sintonizar el controlador PID.
14. Reproducir las simulaciones en Python utilizando los mismos parámetros.
15. Comparar los resultados de las diferentes herramientas.
16. Incorporar las gráficas y evidencias al repositorio.
17. Documentar la interpretación de los resultados.

### Entregables

| Entregable | Archivo o evidencia |
|---|---|
| Descripción fisiológica | Representación del eje endocrino |
| Modelo matemático | Ecuaciones integro-diferenciales y función de transferencia |
| Modelo diferencial | Ecuaciones diferenciales ordinarias |
| Análisis del sistema | Error estacionario, polos y estabilidad |
| Bosquejo de respuesta | Representación previa de la respuesta al escalón |
| Simulación MATLAB | Archivo `.mlx` |
| Modelo Simulink | Archivo `.slx` |
| Circuito equivalente | Modelo de Simscape Electrical |
| Implementación Python | Archivo `.py` |
| Gráficas comparativas | Archivos PDF o imágenes |
| Controlador PID | Ganancias y evidencia de simulación |
| Documentación | `README.md` y evidencias correspondientes |

### Criterios de presentación académica

El repositorio debe distinguir entre los parámetros definidos en el modelo, los resultados obtenidos mediante simulación y las modificaciones realizadas durante el desarrollo.

Las gráficas deben incluir título, ejes, unidades cuando correspondan y leyenda. La interpretación debe explicar la relación entre los parámetros del modelo eléctrico y el comportamiento dinámico observado.

Los resultados deben corresponder a las simulaciones y evidencias efectivamente obtenidas por el estudiante.

[Volver al contenido](#contenido)

---

<a id="diagrama-del-sistema-endocrino"></a>
## 18. Diagrama del sistema endocrino

El sistema fisiológico utilizado como referencia corresponde al eje hipotálamo-hipófisis-suprarrenal.

Su representación contempla:

- Hipotálamo y liberación de CRH.
- Hipófisis anterior y liberación de ACTH.
- Glándula suprarrenal y producción de cortisol.
- Órganos diana y respuesta fisiológica.
- Mecanismo de retroalimentación negativa.
- Correspondencia entre las variables fisiológicas y los componentes eléctricos RLC.
- Comparación entre el caso control y el caso patológico.

### Representación del modelo

Agregar en esta sección la imagen elaborada en BioRender o el diagrama fisiológico del sistema endocrino.

Ejemplo de enlace para GitHub:

```markdown
![Modelo fisiológico del sistema endocrino](Evidencias/Modelo_Endocrino.png)
```

La imagen debe permitir identificar la relación entre el eje endocrino y su representación mediante el circuito eléctrico equivalente.

[Volver al contenido](#contenido)

---

<a id="referencias"></a>
## 19. Referencias

[1] M. C. Khoo, *Physiological Control Systems: Analysis, Simulation, and Estimation*, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018.

[2] J. E. Hall, *Guyton and Hall Textbook of Medical Physiology*, 14th ed. Philadelphia, USA: Elsevier, 2021.

[3] F. C. Hoppensteadt y C. S. Peskin, *Modeling and Simulation in Medicine and the Life Sciences*. New York, USA: Springer.

[4] K. Ogata, *Ingeniería de Control Moderna*, 5.ª ed. Madrid, España: Pearson Educación, 2010.

[5] N. S. Nise, *Control Systems Engineering*, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.

[6] P. A. Valle, *Syllabus para Modelado de Sistemas Fisiológicos*, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B. C., México, 2026. Disponible en: https://biomath.xyz/course/

---

## Uso académico

Este repositorio constituye la documentación de la **Práctica 4: Sistema Endocrino**, desarrollada en la asignatura Modelado de Sistemas Fisiológicos.

El modelo RLC representa una aproximación simplificada del comportamiento dinámico del eje hipotálamo-hipófisis-suprarrenal, permitiendo estudiar la relación entre los parámetros eléctricos y la respuesta hormonal equivalente.

La práctica integra el análisis matemático, la simulación computacional, el diseño de controladores y la comparación entre condiciones fisiológicas de referencia y alteradas. Los resultados deben corresponder a las simulaciones y evidencias efectivamente obtenidas por el estudiante.

