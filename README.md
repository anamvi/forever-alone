# Forever Alone
ForeverAlone es un lenguaje procedural simple que soporta operaciones aritméticas, lógicas, condicionales, así como el manejo de ciclos, condiciones, funciones, recursión y arreglos de una dimensión.

# Equipo
Ana Marcela Villarreal - A00818631

## Ejecución de programa
Este lenguaje está hecho con Python 3, por lo que se requiere tener al menos esa versión instalada en el sistema de cómputo. La manera de ejecutar un archivo es la siguiente:

```
python3 foreveralone.py test.alone
```
## Manual de Usuario

### Tipo de datos

El lenguaje ForeverAlone utiliza los tipos de dato entero (int), punto flotante (float) y cadena (string) para sus operaciones.

### Estructura básica

Un programa básico de ForeverAlone sigue la siguiente estructura 
```
programa forever_alone;
var int i; 
    float j;
    string k;
    
principal() {
    escribe('Hello World!");
}
```

Las variables globales se declaran después del nombre del programa y se pueden utilizar en cualquier contexto.

En el caso de las funciones, la declaración sería como la siguiente:
```
programa forever_alone;
var int i; 
    float j;
    string k;
    
funcion string saluda();
var string cadena;
{
  cadena = 'Hello World!';
  regresa(cadena);
}
principal() {
    escribe(saluda());
}
```

### Elementos del lenguaje

A continuación se listan los elementos principales del lenguaje y su implementación. Estos segmentos de código se pueden utilizar dentro de cualquier función, dado que los tipos de retorno sean compatibles.

** Imprimir a consola **

```
escribe("hola",'/endl');
```
Como se puede ver, se puede utilizar comillas simples o dobles para crear una cadena. 
* La cadena '/endl' o "/endl" se traduce en un 'enter'

** Leer de consola **
```
  lee(x);
```

** Ciclos condicionales **
```
  mientras (i==0) hacer {
    lee(n);
    i = i+1;
  }
```

** Ciclos no-condicionales **
```
  desde i = 0 hasta 9 hacer {
    arr[i] = i+2;
  }
```

** Ciclos no-condicionales **
```
  desde i = 0 hasta 9 hacer {
    arr[i] = i+2;
  }
```

** Estatuto de decisión **
```
    si (i==num) entonces{
      regresa(i);
    }
    sino {
      regresa(j);
    }
```

** Acceso a arreglos **
```
    funcion void prueba();
    var int arreglo[5];
    {
      arreglo[3] = 1;
      escribe(arreglo[3]);
    }
```

Un arreglo solo puede tener una dimensión, la cual al ser declarada denota su límite superior. Al acceder a él se usan índices donde 0 <= índice < límite_superior.



** Llamadas a funciones **
```
    funcion int prueba2();
    {
      regresa(1);
    }
    funcion void prueba();
    {
      escribe(prueba2());
    }
    principal() {
        prueba();
    }
    
```

El código pasado escribiría '1' en la pantalla. Se pueden llamar funciones con tipo (prueba2) al utilizarlas como su valor de retorno, y funciones void (prueba) directo desde el cuerpo de la función.

