"""
() Ejercicio 9.***

La Agencia Espacial Internacional desea mejorar su servicio de comunicación por satélite de Tokio a Florida. En el sistema actual, los mensajes pueden enviarse de Tokio hacia Florida utilizando la red de satélites que se muestra a continuación.


       .----> S1 ---.
      /              \
     /0.90            \0.80
    /                  \
   /                    '--->
Tokio                         Florida
   \                    .--->
    \                  /
     \0.90            /0.70
      \              /
       '----> S2 ---'

La ruta superior implica enviar un mensaje de Tokio a Florida por medio del satélite S1. La segunda alternativa es enviar un mensaje de Tokio a Florida por medio del satélite S2. Debido a las órbitas actuales estos satélites pueden conectarse entre sí y entre las ciudades solo una fracción del tiempo. Estas fracciones se escriben junto a cada nodo de la red. Por ejemplo el valor de 0.90 que une a Tokio con S1 significa que esta conexión tiene un 90% de probabilidad de que un mensaje enviado de Tokio llegue a S1.


a. Determine utilizando probabilidades, cuál es la probabilidad total que un mensaje enviado desde Tokio llegue a Florida, dada la red actual de satélites. Es decir, la probabilidad para el evento T -> F, dada por P(T -> F).

Por regla de bayes tenemos lo siguiente:
Ruta de Tokio a Florida por S1: 0.90 * 0.80 = 0.72 (q: 1 - 0.72 = 0.28)
Ruta de Tokio a Florida por S2: 0.90 * 0.70 = 0.63 (q: 1 - 0.63 = 0.37)
Probabilidad de fallo total = 0.28 * 0.37 = 0.1036
Probabilidad de acierto total = 1 - 0.1036 = 0.8964

Lo que nos dice que la ruta mas segura es la que va por S1 que hace que el mensaje llegue a florida con un 72% de probabilidad, se podria decir que la probalilidad
es baja para tener confianza en un funcionamiento correcto, tambien se puede inferir que los envios a cada satelite son independientes ya que no se cumple la propiedad de suma 
de una distribucion de probabilidad por lo que la probabilidad total es de casi un 90% de que el mensaje de Tokio llegue a Florida.


b. Se desea mejorar al nivel actual de comunicaciones, para ello se están evaluando algunas posibilidades. El personal ha descubierto dos opciones para tratar de mejorar el actual sistema de satélites. La primera consiste en alterar la órbita de S2, lo que aumentaría las probabilidades de comunicarse con Florida a un nuevo valor de  0.80.

Se mejora el satelite S2 para aumentar su probabilidad

       .----> S1 ---.
      /              \
     /0.90            \0.80
    /                  \
   /                    '--->
Tokio                         Florida
   \                    .--->
    \                  /
     \0.90            /0.80
      \              /
       '----> S2 ---'

Por regla de bayes tenemos lo siguiente:
Ruta de Tokio a Florida por S1: 0.90 * 0.80 = 0.72 (q: 1 - 0.72 = 0.28)
Ruta de Tokio a Florida por S1: 0.90 * 0.80 = 0.72 (q: 1 - 0.72 = 0.28)
Probabilidad de fallo total = 0.28 * 0.28 = 0.0784
Probabilidad de acierto total = 1 - 0.0784 = 0.9216

Al aumentar la probabilidad de S2 hace que la probabilidad aumente a aproximadamente 92% de que llegue el mensaje

c. Con un esfuerzo sustancialmente mayor, se puede modificar la órbita de S1 para que S1 y S2 puedan comunicarse hacia adelante y hacia atrás con una probabilidad de 0.80. Bajo estas condiciones, ¿qué tan fácil es calcular las nuevas probabilidades?
El agregar un camino extra hace que aumente drasticamente el calcular una probabilidad con la regla de bayes ya que aparece dependencia 
entre eventos en vez de seguir un camino simple como en los ejercicios anteriores.

       .----> S1 ---.
      /       |      \
     /0.90    |       \0.80
    /         |        \
   /          |         '--->
Tokio         |0.80           Florida
   \          |         .--->
    \         |        /
     \0.90    |       /0.70
      \       |      /
       '----> S2 ---'

"""