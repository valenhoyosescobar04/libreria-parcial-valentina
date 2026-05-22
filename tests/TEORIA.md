# TEORIA.md

# Sección teórica - Parcial Corte 1

## SM-1

Respuesta correcta: C. Es desarrollo tradicional con pruebas al final, porque primero se construye toda la funcionalidad y despues se empieza a probar. El problema es que los errores se descubren tarde, cuando ya hay más código construido y corregirlos puede ser mucho más costoso, tanto en tiempo como en dinero y eso es desgastante para todos.

## SM-2

Respuesta correcta: B. Está violando la primera regla de TDD, porque en TDD no se debe escribir código de producción sin tener primero una prueba que falle. En este caso vemos que el desarrollador implementó la función completa antes de que existieran tests que justificaran ese código.

## PA-1

En TDD, el paso green obliga a escribir el código minimo necesario porque el objetivo de ese momento no es dejar el sistema perfecto, sino lograr que la prueba que escribimos en el red y evidentemente estaba fallando pase. Eso ayuda a que el desarrollo avance poco a poco y evita crear lógica que todavía no ha sido solicitada por una prueba. Si la persona aprovecha el green para hacer código limpio y completo desde el inicio, puede terminar programando de más, cubriendo casos que aún no están totalmente definidos o no estan contemplados o agregando complejidad innecesaria. Además, se pierde la escencia del ciclo TDD, porque ya no se avanza desde una necesidad concreta, sino desde lo que el programador imagina que puede necesitar después. La limpieza del código debe hacerse en el paso refactor, cuando ya hay pruebas que protegen el comportamiento.

## PA-2

TDD y BDD se parecen porque ambos buscan construir software con pruebas, pero no resuelven exactamente el mismo problema. TDD está más enfocado en el desarrollador y en guiar la implementación técnica mediante ciclos pequeños: primero una prueba que falla, luego se escribe el código mínimo y después una mejora. BDD, en cambio, busca describir el comportamiento esperado del sistema en lenguaje de negocio, para que personas técnicas y no técnicas puedan entender qué debe hacer la funcionalidad. TDD ayuda a que el código quede bien construido internamente, mientras que BDD ayuda a validar que el sistema haga lo que el usuario realmente necesita. Por eso lo mencinado anteriormente

## PA-3

Esa afirmación es incorrecta porque tener 95% de cobertura solo significa que muchas líneas de código fueron ejecutadas durante las pruebas, pero no significa que las pruebas estén verificando bien el comportamiento. Por ejemplo, una prueba puede llamar una función de cálculo de precio final y cubrir casi todo el código, pero no revisar si el resultado incluye primero el descuento y luego el IVA. También puede probar solo casos positivos y dejar por fuera errores importantes (solo probaron el "camino feliz"), como descuentos mayores al 40%. Entonces, una cobertura alta puede dar confianza, pero no garantiza que el sistema no tenga bugs. Lo importante es qué casos se prueban y qué se está validando, no solo las lineas de codigo.

## PA-4

Esa lógica es incorrecta porque probar solo el 20% revisa un valor normal dentro del rango, pero no confirma qué pasa en los límites ni fuera de ellos. En este caso, los valores más importantes son los bordes del rango permitido: 0% y 40%, porque ambos deberían ser válidos. También se deben probar valores justo fuera del rango, como -1% y 41%, porque deberían ser rechazados. Además, de probar un valor intermedio como 20% para confirmar el comportamiento normal. Si solo pruebo 20%, no sabría si el sistema acepta por error un descuento de 41% o rechaza incorrectamente un descuento de 0%.

## PA-5

Las prácticas de TDD y BDD se conectan con CI/CD porque un pipeline necesita pruebas automatizadas para validar cada cambio antes de integrarlo o desplegarlo. TDD permite tener pruebas técnicas que revisan la lógica del código, mientras que BDD permite validar comportamientos importantes desde el punto de vista del negocio. Si el equipo no tiene una suite sólida de tests automatizados, el pipeline de CI/CD pierde gran parte de su valor, porque podría integrar o desplegar código con errores sin detectarlos. En ese caso, CI/CD solo movería cambios más rápido, pero no necesariamente con calidad. Por eso las pruebas ágiles son una base importante para automatizar entregas de forma confiable.