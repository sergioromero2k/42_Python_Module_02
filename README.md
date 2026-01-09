# 42_Python_Module_02
Project: Python Module 02

### Ingeniería de Datos para Agricultura Inteligente (Guarda del Huerto)
Este proyecto se enfoca en la creación de pipelines de datos resilientes para sistemas agrícolas. El objetivo principal es aprender a gestionar fallos de sensores, procesar flujos de datos y garantizar la integridad del sistema incluso ante imprevistos o datos corruptos.

#### Estructura del Módulo
El proyecto evoluciona desde la validación básica hasta sistemas integrales de monitorización agrícola.

| Ejercicio | Archivo                      | Concepto Clave       | Objetivo Técnico                                                   |
|-----------|------------------------------|----------------------|-------------------------------------------------------------------|
| Ex00      | ft_first_exception.py        | Validación Básica    | Capturar errores de conversión de tipos (ValueError).             |
| Ex01      | ft_different_errors.py       | Tipos de Errores     | Gestionar ZeroDivision, FileNotFound y KeyError.                  |
| Ex02      | ft_custom_errors.py          | Excepciones Propias  | Crear jerarquías de error personalizadas (GardenError).           |
| Ex03      | ft_finally_block.py          | Limpieza de Recursos  | Asegurar el cierre de sistemas usando el bloque finally.          |
| Ex04      | ft_raise_errors.py           | Lanzamiento de Alertas| Validar reglas de negocio y lanzar errores con raise.             |
| Ex05      | ft_garden_management.py      | Sistema Integrado     | Construir un gestor robusto que combine todas las técnicas.       |

#### Desglose de Competencias

1. **Validación y Resiliencia (Ex00 - Ex01)**
   - **Filtrado de Datos:** Implementar capas de validación para evitar que datos corruptos (como texto en campos numéricos) afecten la analítica.
   - **Control de Flujo:** Garantizar que el programa no se cierre de forma inesperada ante entradas inválidas.

2. **Personalización y Jerarquía (Ex02)**
   - **Herencia de Excepciones:** Crear una estructura donde PlantError y WaterError hereden de un GardenError común, permitiendo capturas genéricas o específicas según la necesidad.

3. **Gestión de Recursos (Ex03)**
   - **Garantía de Cierre:** El bloque finally se utiliza para asegurar que acciones críticas, como cerrar un sistema de riego, ocurran siempre, haya o no un error en el proceso.

4. **Lógica de Negocio Agrícola (Ex04)**
   - **Validación de Sensores:** El sistema debe verificar que los niveles de agua (1-10) y horas de luz (2-12) sean razonables, lanzando excepciones con mensajes útiles si se detectan anomalías.

#### Requisitos de Entrega
- **Lenguaje:** Python 3.10+.
- **Estilo:** El código debe respetar los estándares de linter flake8.
- **Documentación:** Incluir docstrings sencillos para cada función y clase.
- **Evaluación:** Durante la defensa, se debe ser capaz de explicar el flujo de ejecución y cómo el sistema recupera la integridad tras un fallo.

**Nota sobre la IA:** Se fomenta el uso de herramientas de IA para reducir tareas tediosas, pero es obligatorio entender cada línea de código generada. No poder explicar la lógica durante la evaluación es motivo de suspenso.