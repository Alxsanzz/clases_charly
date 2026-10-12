# Tipos de Robots Móviles

## 1. Conceptos Básicos

### ¿Qué es un robot móvil?
Un robot movil es una maquina programable que puede desplazarse de un lugar a otro por medio de reuedas, orugas o patas

### ¿Qué diferencia existe entre un robot móvil y un robot manipulador fijo?
Un robot movil puede cambiar de posición y deslazarse por su entorno, en cambio un manipulador fijo permanece quieto en su base y mueve solo sus articulaciónes para realizar la actividad para la que fue creado

### ¿Qué función cumple el sistema de locomoción de un robot?
Permite que el robot se mueva, etsa formado por elementos como ruedas, sensores y actuadores. Estos determinan el la velocidad, estabilidadu direcci´nes que podra tener el robot

### ¿Qué significa que un robot tenga movilidad omnidireccional?
Significa que este puede moverse hacia adelante, atras, lateralmente y en diagonal sin tener que girar primero todo el chasis para apuntar hacia la dirección deseada

### ¿Qué relación existe entre la disposición de las ruedas y los movimientos?
La posición, orientación y tipo de ruedas determinan que movimientos puede realizar el robot 

## Robot diferencial con rueda de castor
El robot diferencial es una configuración que utiliza dos ruedas motrices independientes, una a cada lado del chasis, y una rueda rueda loca que sirve como apoyo

###  ¿Cómo están colocadas las ruedas motrices?
Las dor ruedas se colocan a los lados del chasis, aineadas sobre un mismo eje. Cada motor controla una rueda, lo que permite que ambas giren a velocidades o direcciones diferentes

### ¿Para qué sirve la rueda de castor?
Es una rueda libre que no necesita un motor propio y sostiene parte del peso del robot y le da estabilidad, puede orientarse de acuerdo al movimiento

### ¿Cómo avanza en línea recta?
Las dor ruedas giran hacia adelante a la misma velocidad, como ambas van a la misma velocidad el robot mantiene la misma orientación

### ¿Cómo gira hacia la izquierda o hacia la derecha?
- Izquierda: La rueda derecha gira mas rapido que la izquierda
- Derecha: La rueda izquierda gira mas rapido que la derecha
- Si una rueda avanza y la ptra se detiene el robot gira alrededor dela rueda detenida

### ¿Qué sucede cuando una rueda gira más rápido que la otra?
El robot comienza a hacer una curva hacia el lado de la rueda mas lenta. El angulo de la curva es mas cerrado dependiendo de que tan grande sea la diferencia de velocidades entr las ruedas

### ¿Cómo gira sobre su propio eje?
Una rueda gira hacia adelante y la otra hacia atras a la misma velocidad, el ronot gira en su propio eje hacia a dirección de la rueda que gira hacia atras

## Ventajas
- Es económico y sencillo de construir
- Solo nececita 2 motores
- Fácil de programar
- Puede girar sobre su propio eje

## Limitaciónes
- No puede desplazarse hacia los costados
- La rueda loca puede tener problemas con un terreno irregular 
- Las diferencias entre motores puede hacer que el robor no avance perfectamente recto

## Aplicaciónes
Se utilizan como robots educativos, aspiradoras automaticas y robots de transporte que trabajan en interiores

## Diagrama 

                  FRENTE
                    ↑
              Sentido de avance

        ┌──────────────────────┐
        │                      │
        │       CHASIS         │
        │                      │
        O                      O
    Rueda izquierda       Rueda derecha
      motriz                 motriz
        │                      │
        └──────────┬───────────┘
                   o
               Rueda loca

        Eje de giro aproximado:
        centro entre las dos ruedas motrices

## Movimientos

| Rueda Izquierda | Rueda Derecha | Movimiento del robot |
|-|-|-|
Avanza | Avanza | Avanza recto si ambas tienen la misma velocidad
Detenida | Avanza | Gira hacia la izquierda
Avanza | Detenida| Gira hacia la derecha
Avanza | Retrocede | Gira sobre su propio eje hacia la derecha
Retrocede | Avanza | Gira sobre su propi eje hacia la izquierda
Retrocede | Retrocede | Retrocede recto si ambaas tienen la misma velocidad

## 3. Robots omnidireccionales con ruedas Omni

### ¿Cómo está construida?
Con un cuerpo circular, un eje de montaje y varios pequeños rodillos al rededor de toda la cricunferencia. Estos rodillos giran sobre sus propios ejes y facilitan el desplazamiento en una direccion diferente a la tracción principal

### ¿Para qué sirven los pequeños rodillos colocados alrededor de la rueda?
Permiten que al tener cierto movimiento de las ruedas el chasis se mueva en una dirección lateral sin nececidad de que el chasis gire

### ¿En qué dirección puede generar fuerza la rued?
La rueda produce fuerza principalmente en la dirección en la que rueda su cuerpo principal. En la direccion lateral, los pequeños rodillos giran y permiten que la rueda se deslice

### ¿Por qué puede deslizarse libremente en otra dirección?
Las ruedas omnidireccionales tienen pequeños rodillos alrededor de su circunferencia, colocados perpendicularmente a la dirección principal de giro. Estos rodillos pueden girar libremente y permiten que la rueda se desplace lateralmente con poca resistencia, sin necesidad de cambiar la orientación del chasis

### ¿Cómo esta característica permite generar movimientos que una rueda convencional no puede realizar?
Gracias a los pequeños rodillos, con estos y una combinación de dirección de las ruedas permite avanzar en diagonal o lateralmente

## Configuración de tres ruedas omnidireccionales
Un robot omnidireccional de tres ruedas utiliza tres ruedas Omni, cada una conectada a un motor independiente. Esto permite controlar la velocidad y el sentido de giro de cada rueda para conseguir diferentes movimientos.
### ¿Cómo se distribuyen normalmente las ruedas?
Las tres ruedas se colocan alrededor del chasis, generalmente formando un triángulo y separadas aproximadamente por 120°. Esta distribución permite generar movimientos en distintas direcciones y girar sobre el propio eje del robot.
### ¿Cuál es la orientación aproximada entre ellas?
Las ruedas se distribuyen con una separación angular de aproximadamente 120° entre sí. Cada una tiene una orientación específica para que las fuerzas generadas por los motores puedan combinarse y controlar el movimiento del robot.
### ¿Cómo puede desplazarse hacia adelante y hacia atrás?
Para avanzar, los tres motores giran a velocidades y sentidos coordinados para que las fuerzas resultantes impulsen el robot hacia adelante. Para retroceder, se invierte la combinación de velocidades y sentidos de giro.
### ¿Cómo puede desplazarse lateralmente?
El robot coordina el giro de las tres ruedas para que las componentes de fuerza hacia los lados se sumen, permitiendo desplazarse hacia la izquierda o hacia la derecha sin cambiar la orientación del chasis.
### ¿Cómo puede moverse en diagonal?
Combina el movimiento hacia adelante o hacia atrás con el desplazamiento lateral. Para conseguirlo, los motores giran a velocidades diferentes, de modo que las fuerzas resultantes produzcan un desplazamiento diagonal.
### ¿Cómo puede girar sobre su propio eje?
Las tres ruedas generan fuerzas que producen una rotación alrededor del centro del chasis. Para lograrlo, cada motor gira a una velocidad y en un sentido determinados según la orientación de su rueda.
### ¿Qué sucede cuando las tres ruedas giran a diferentes velocidades?
El robot combina los efectos de las tres ruedas y puede desplazarse en una dirección determinada mientras gira al mismo tiempo. La trayectoria depende de la velocidad, el sentido de giro y la orientación de cada rueda. Por eso, controlar correctamente los tres motores es fundamental para conseguir movimientos precisos.

       FRENTE
          ↑
          O
       Rueda 1
         / \
        /   \
       /  ●  \
      /       \
     O---------O
    Rueda 2    Rueda 3

  ● = centro del chasis
 Las tres ruedas se distribuyen aproximadamente
 cada 120 grados alrededor del centro.

## Configuración de cuatro ruedas Omni
En una configuración de cuatro ruedas, estas se colocan normalmente cerca de las cuatro esquinas del chasis

Su orientación permite combinar las fuerzas de las ruedas para producir movimiento lateral y diagonal, además de avance y giro

En comparación con la configuración de tres ruedas, cuatro ruedas pueden repartir mejor el peso y proporcionar más puntos de apoyo. Pero, nececitan un motor adicional y mantener un contacto adecuado entre todas las ruedas y el suelo

Ventajas:
- Permiten desplazarse lateralmente
- Facilitan los movimientos diagonales
- Pueden girar sobre su propio eje
- Son útiles para maniobrar en lugares estrechos

Limitaciones:
- Su control es más complejo que el de un robot diferencial
- Los rodillos pueden reducir la adherencia y la precisión
- Funcionan mejor en superficies planas
- La orientación de las ruedas debe diseñarse correctamente

## 4. Robot omnidireccional con ruedas Mecanum

Son un tipo de ruedas que permiten que el robot se desplaze en cualquier dirección sin necesidad de cambiar la orientación del chasis 

### ¿Cómo estan construidas?
Tiene pequeños rodillos al rededor de su circunferencia

### ¿Cómo estan colocados sus rodillos
Inclinados, generalmente a unos 45 grads respect al eje de la rueda

### Diferencias entre Mecanum y Omni convencional
Las ruedas Omni permiten deslizarse lateralmente gracias a sus rodillos, mientras que las ruedas Mecanum tienen rodillos montados en diagonal, generalmente a unos 45 grados. Esa inclinación permite generar componentes de fuerza diagonales que, al combinarse entre cuatro ruedas, producen desplazamientos laterales y diagonales

### ¿Por qué generalmente se utilizan cuatro ruedas?
Porque esta configuración permite combinar las fuerzas de las cuatro ruedas para controlar los movimientos de traslación y rotación, ademas permite una mayor estabilidad

### ¿Cómo se orientan respecto al chasis?
Normalmente se colocan cuatro ruedas, una en cada esquina del chasis, sus rodillos deben instalarse en una disposición simétrica, como un patrón en forma de X visto desde arriba

### ¿Cómo se combinan los movimientos de las cuatro ruedas?
- Avance: las cuatro ruedas giran en el sentido definido como avance
- Retroceso: las cuatro ruedas giran en sentido contrario
- Movimiento hacia la izquierda: las ruedas se coordinan para que sus componentes de fuerza laterales se sumen hacia la izquierda y las longitudinales se compensen
- Movimiento hacia la derecha: se invierte la combinación del movimiento lateral
- Movimiento diagonal: se  |combinan el avance y el desplazamiento lateral
- Giro sobre el eje: las ruedas de un lado y del otro producen fuerzas que generan rotación alrededor del centro del chasis

## Diagrama

           FRENTE
              ↑
    ┌─────────────────────┐
    │  DI            DD   │
    │   \ \         / /   │
    │    \ \       / /    │
    │                     │
    │    / /       \ \    │
    │   / /         \ \   │
    │  TI             TD  │
    └─────────────────────┘

- DI = Delantera izquierda 
- DD = Delantera derecha
- TI = Trasera izquierda
- TD = Trasera derecha
- Las líneas representan la orientación diagonal de los rodillos, no el sentido de giro del motor
---
| Movimiento | Delantera I | Delantera D | Trasera I | Trasera D |
|-|-|-|-|-|
Avanzar | + | + | + | + |
Retroceder | - | - | - | - |
Despazarse a la Izq | - | + | + | - |
Desplazarse a la Der | + | - | - | + |
Girar a la Izq | - | + | - | + |
Girar a la Der | + | - | + | - |
---

## 5. Robot con dirección Ackermann

### Cómo se distribuyen las ruedas
La geometría de dirección Ackermann se utiliza en automóviles y vehículos móviles que necesitan seguir trayectorias curvas

### Qué ruedas normalmente proporcionan la dirección
Las ruedas delanteras son las que cambian de orientación para dirigir el vehiculo 

### Qué ruedas pueden proporcionar la tracción
Las traseras, aunque tambien pueden ser las delanteras o las cuatro dependiendo del diseño

### Por qué las ruedas interiores y exteriores no giran exactamente con el mismo ángulo durante una curva
Cuando el vehículo gira, la rueda interior recorre una curva más pequeña que la exterior. Para que ambas ruedas sigan sus trayectorias sin arrastrarse excesivamente de lado, la rueda interior debe girar con un ángulo mayor que la exterior

### Qué es el radio de giro
Es la distancia entre el centro instantáneo de rotación y un punto de referencia del vehículo

### Por qué un vehículo Ackermann no puede desplazarse directamente hacia un costado
Las ruedas convencionales están diseñadas para rodar hacia delante o hacia atrás, no permiten el deslizamiento lateral libre que ofrecen las ruedas Omni o Mecanum

### Qué semejanzas tiene con la dirección de un automóvil convencional
Ambos utilizan ruedas convencionales y un mecanismo de dirección que cambia la trayectoria del vehículo. Para desplazarse hacia un costado primero necesitan seguir una curva
---

                        Dirección de avance
                               ↗

              Rueda exterior  /
                    O---------/
                     \       /
                      \     /
                       \   /
                 O------\------O
             Rueda interior   Rueda trasera

                           ●
                  Centro aproximado
                      de giro

      La rueda interior gira con un ángulo mayor
      que la rueda exterior.

---

### Aplicación
- Automóviles autónomos de investigación
- Vehículos autónomos pequeños para pruebas
- Robots de reparto que circulan por exteriores
- Plataformas de conducción autónoma con apariencia y comportamiento similares a un automóvil
---

## 6. Comparación de configuraciones

|Configuración | Número de ruedas | Movimiento lateral |Giro sobre su propio eje | Complejidad mecánica  | Complejidad de control | Aplicaciónes |
|-|-|-|-|-|-|-|
Diferencial + ruedaloca|3: 2 motrices y una loca|No|Si|Baja|Baja|Educación, aspiradoras|
Omni de 3 ruedas|3 motrices|Si|Si|Media|Media-alta|Investigación y competencias|
Omni de 4 ruedas|4 motrices|Si|Si|Media-alta|Alta|Plataformas de lavoratorio y transporte|
Mecanum|4 motrices|Si|Si|Alta|Alta|Almacenes y robotica industrial|
Ackerman|Normalmente 4|No|No|Media-alta|Media-alta|Vehiculos autonomos y robots de exterior|

---
### 1. Robot pequeño para aprender programación y control 
Elegiría el diferencial con rueda loca porque es económico, sencillo de construir y solo necesita dos motores

### 2. Robot que debe desplazarse dentro de un almacén con espacios reducidos
Elegiría Mecanum, porque puede moverse lateralmente y maniobrar entre estantes sin orientar primero todo el chasis

### 3. Plataforma que necesita moverse lateralmente sin cambiar su orientación
También elegiria el mecanum por su facilidad al desplazarse lateralmente y en diagonal

### 4. Vehículo autónomo que debe circular de manera similar a un automóvil
Elegiria el ackerman porque su forma de dirección es muy parecida a la de los autos

### 5. Robot para una competencia donde sea necesario cambiar rápidamente de dirección
Elegiria el omni de 4 ruedas, por su estabilidad y que es ligeramente mas sencillo de hacer que un mecanum

### 6. Robot móvil sencillo que utilice únicamente dos motores
Elegiria el diferencial con rueda loca, porque cada motor controla solo una rueda y puede avanzar, retroceder y girar sin mecanismos tan complejos

## 7. Análisis del movimiento

### Diferencial: ¿qué debe hacer cada rueda para girar sobre su propio eje?
Una rueda debe girar hacia delante mientras la otra gira hacia atrás, a la misma velocidad

### Omni: ¿por qué los rodillos permiten generar movimiento lateral?
Los rodillos pueden girar libremente sobre sus propios ejes, lo que reduce la resistencia cuando la rueda se desplaza lateralmente, y al colocar varias ruedas con distintas orientaciones, sus fuerzas se combinan para producir el movimiento lateral

### Mecanum: ¿por qué el robot puede desplazarse lateralmente aunque ninguna rueda esté orientada directamente hacia el costado?
Los rodillos inclinados producen fuerzas con componentes longitudinales y laterales. Al controlar los cuatro motores, se pueden cancelar las componentes que empujan hacia delante y sumar las que empujan hacia un costado. Así, el chasis se desplaza lateralmente sin necesidad de orientar las ruedas principales hacia ese lado.

### Ackermann: ¿por qué necesita avanzar o retroceder para cambiar de posición lateral?
Las ruedas convencionales no pueden deslizarse lateralmente de manera libre. Cuando las ruedas directrices giran, cambian la trayectoria del vehículo, pero este debe avanzar o retroceder para recorrer esa curva y cambiar su posición. Esta restricción se conoce como condición no holonómica.

## 8. Análisis de un robot real

### Robot aspirador automático iRobot Roomba 600 Series

- Fabricante: iRobot.

- Tipo de locomoción: Dirección diferencial.

- Número y tipo de ruedas: Cuenta con dos ruedas motrices independientes y una rueda de apoyo que ayuda a mantener la estabilidad

- Sensores: Incorpora sensores para detectar obstáculos y desniveles. Los sensores y sus funciones específicas pueden variar según el modelo

- Actuadores: Motores eléctricos para mover las ruedas

- Aplicación: Limpieza automática de pisos en viviendas

- Imagen:
![Robot Diferencial](https://http2.mlstatic.com/D_NQ_NP_669078-MLA46926596525_072021-O.webp)

- Concidero que esta configuración es adecuada a este robot, ya que lo unico que nececita es avanzar para limpiar y si nececitara girar solo bastaria con que gire sobre su propio eje

## Reflexión Final

### ¿Qué configuración te pareció más sencilla de comprender?
La diferencial ya que al solo nececitar dos motores es mas sencilla de contruir  controlar

### ¿Cuál ofrece mayor libertad de movimiento?
La configuración con ruedas Mecanum, ya que permite desplazarse a todas las direcciónes sin cmbiar antes la orientación del chasis

### ¿Qué configuración utilizarías para construir tu primer robot móvil?
Ya he construido robots oviles antes, como un evasor de obstaculos con configuración diferencial. Asi que, me gustaria ahora hacer uno Omni, para el proyecto del fin de cuatri

### ¿Por qué no existe una sola configuración de ruedas adecuada para todos los robots?
Porque cada aplicación tiene necesidades diferentes. Algunos requieren bajo costo y sencillez, mientras que otros necesitan moverse lateralmente, transportar cargas o circular por caminos como un automóvil

## Referencias

1. Lynch, K. M., y Park, F. C. (2017). Modern Robotics: Mechanics, Planning, and Control. Cambridge University Press. Capítulo 13: Wheeled Mobile Robots.
https://modernrobotics.northwestern.edu/nu-gm-book-resource/13-1-wheeled-mobile-robots/ 


2. Lynch, K. M., y Park, F. C. (s. f.). 13.2. Omnidirectional Wheeled Mobile Robots (Part 1 of 2). Modern Robotics, Northwestern University.
https://modernrobotics.northwestern.edu/nu-gm-book-resource/13-2-omnidirectional-wheeled-mobile-robots-part-1-of-2/ 

3. ROBOTIS. (s. f.). TurtleBot3: Features and specifications. Documentación técnica oficial.
https://emanual.robotis.com/docs/en/platform/turtlebot3/features/ 

4. ROBOTIS. (s. f.). TurtleBot3: Compatible devices and sensors. Documentación técnica oficial.
https://emanual.robotis.com/docs/en/platform/turtlebot3/compatible_devices/
 
6. Gfrerrer, A. (2008). Geometry and kinematics of the Mecanum wheel. Computer Aided Geometric Design, 25(9), 784–791.
https://doi.org/10.1016/j.cagd.2008.07.008

7. Northwestern University. (s. f.). Modern Robotics: Omnidirectional Wheeled Mobile Robots (Part 2 of 2).
https://modernrobotics.northwestern.edu/nu-gm-book-resource/13-2-omnidirectional-wheeled-mobile-robots-part-2-of-2/
