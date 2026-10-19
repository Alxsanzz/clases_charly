## 1. Resumen ejecutivo

Las metodologías ágiles son formas de organizar proyectos mediante entregas frecuentes, colaboración y adaptación a los cambios. Surgieron para mejorar el desarrollo de software, donde los requisitos pueden cambiar durante el proyecto. En 2001 se publicó el Manifiesto Ágil, que estableció valores y principios para trabajar de manera más flexible.

## 2. Principios ágiles

El Manifiesto Ágil establece cuatro valores principales:

- **Personas e interacciones:** priorizar la comunicación
- **Software funcional:** entregar resultados que puedan utilizarse
- **Colaboración con el cliente:** mantener una comunicación constante
- **Adaptación al cambio:** modificar los planes cuando sea necesario

## 3. Panorama de los enfoques ágiles

| Enfoque | Características | Cuándo utilizarlo |
|-|-|-|
| Scrum | Organiza el trabajo en ciclos llamados Sprints | Desarrollo de productos que requieren revisiones frecuentes |
| Kanban | Visualiza tareas y limita el trabajo en proceso | Atención de solicitudes y trabajo continuo |
| Design Thinking | Investiga necesidades y prueba soluciones mediante prototipos | Problemas que todavía necesitan definirse |

## 4. Ventajas y limitaciones

| Ventajas | Limitaciones |
|-|-|
| Detecta errores tempranamente | Requiere comunicación constante |
| Permite adaptarse a cambios | Los cambios excesivos pueden desorganizar el proyecto |
| Mejora la colaboración | Las reuniones pueden consumir tiempo |
| Facilita la retroalimentación | Depende de la participación de los usuarios |


# 5. Scrum

## 5.1 Conceptos básicos

Scrum es un marco de trabajo que permite desarrollar productos mediante periodos cortos llamados **Sprints**, que duran un mes o menos. Se utiliza cuando el equipo necesita revisar resultados frecuentemente y adaptarse a nuevos requisitos

## 5.2 Roles

| Rol | Responsabilidad | Error frecuente |
|-|-|-|
| Product Owner | Prioriza el trabajo y maximiza el valor del producto | No establecer prioridades claras |
| Scrum Master | Ayuda a aplicar Scrum y mejorar el trabajo del equipo | Actuar como jefe que controla todas las tareas |
| Developers | Construyen el producto y verifican su calidad | No comunicar problemas o entregar trabajo incompleto |

## 5.3 Artefactos

| Artefacto | Definición |
|-|-|
| Product Backlog | Lista ordenada de necesidades y mejoras del producto |
| Sprint Backlog | Trabajo seleccionado y plan para alcanzar el objetivo del Sprint |
| Increment | Resultado funcional que cumple con los requisitos de calidad |

La **Definition of Done** establece las condiciones generales de calidad, como completar pruebas y revisar el código. Los **criterios de aceptación** indican las condiciones específicas que debe cumplir una funcionalidad.

## 5.4 Eventos de Scrum

| Evento | Objetivo | Duración orientativa | Antipatrón |
|-|-|-|-|
| Sprint | Desarrollar un incremento | 1 a 4 semanas | Cambiar constantemente el objetivo |
| Sprint Planning | Planificar el trabajo | 2 h por semana de Sprint, como referencia | Seleccionar demasiado trabajo |
| Daily Scrum | Revisar el avance y ajustar el plan | 15 minutos | Convertirlo en un reporte al jefe |
| Sprint Review | Revisar el producto con los interesados | Hasta 4 h por Sprint mensual | No recibir comentarios |
| Retrospective | Identificar mejoras para el equipo | Hasta 3 h por Sprint mensual | No acordar acciones de mejora |

## 5.5 Métricas

- **Velocity:** cantidad de trabajo completado en un Sprint. Ayuda a planificar, pero no sirve para comparar equipos ni medir el desempeño individual
- **Burndown chart:** gráfica del trabajo pendiente durante un periodo. Permite observar avances y posibles retrasos, pero no mide por sí sola la calidad
- **Work in Progress (WIP):** cantidad de tareas que están en proceso. Un WIP excesivo puede indicar que el equipo inicia demasiadas actividades sin terminarlas

# 6. Kanban

## 6.1 Fundamentos

Kanban permite visualizar el trabajo y mejorar su flujo mediante seis prácticas principales:

1. Visualizar las tareas
2. Limitar el trabajo en proceso
3. Gestionar el flujo
4. Establecer políticas explícitas
5. Utilizar retroalimentación
6. Mejorar continuamente

## 6.2 Tablero Kanban

Ejemplo para un equipo de desarrollo de software:

| Pendiente | Desarrollo (WIP 3) | Pruebas (WIP 2) | Terminado |
|-|-|-|-|
| Diseñar pantalla | Programar búsqueda | Probar acceso | Revisar documentación |
| Crear reporte | Corregir errores | Verificar resultados |

## 6.3 Métricas de flujo

- **Lead time:** tiempo desde que se solicita o acepta un trabajo hasta que termina, según la política definida
- **Cycle time:** tiempo desde que comienza el trabajo hasta que se completa
- **Throughput:** cantidad de tareas terminadas durante un periodo
- **Diagrama de flujo acumulado (CFD):** gráfica que muestra las tareas en cada estado a lo largo del tiempo. Si una banda aumenta de grosor, puede indicar acumulación de trabajo

## 6.4 Políticas y clases de servicio

Las políticas explícitas establecen cuándo una tarea puede comenzar, avanzar o considerarse terminada.

Las clases de servicio permiten organizar el trabajo según su prioridad:

- **Urgente:** resolver una falla crítica
- **Fecha fija:** completar una entrega antes de una fecha límite
- **Estándar:** realizar tareas habituales
- **Intangible:** mejorar el código o actualizar dependencias para prevenir problemas futuros

# 7. Design Thinking

## 7.1 Concepto

Design Thinking es un enfoque centrado en las personas que permite comprender problemas, generar ideas y probar soluciones antes de desarrollarlas completamente. Se utiliza para reducir el riesgo de construir algo que no satisfaga las necesidades del usuario

## 7.2 Fases

| Fase | Objetivo | Técnica y entregable |
|-|-|-|
| Empatizar | Comprender al usuario. | Entrevistas y registro de necesidades |
| Definir | Delimitar el problema | Redacción del problema principal |
| Idear | Generar alternativas | Lluvia de ideas y selección de propuestas |
| Prototipar | Representar una solución | Boceto o maqueta sencilla |
| Probar | Obtener retroalimentación | Prueba con usuarios y mejoras |


## 7.3 Mini-caso: préstamo de herramientas

**Problema:** los estudiantes de un laboratorio no saben qué herramientas están disponibles

- **Empatizar:** entrevistar estudiantes y al encargado del laboratorio.
- **Definir:** identificar la falta de información sobre disponibilidad y ubicación
- **Idear:** proponer un catálogo digital, un tablero físico o códigos QR.
- **Prototipar:** dibujar una pantalla sencilla
- **Probar:** pedir a varios estudiantes que busquen una herramienta y registrar sus dificultades

Ejemplo de prototipo de baja fidelidad:

```text
+---------------------------+
| INVENTARIO DEL LABORATORIO|
+---------------------------+
| Buscar: [_____________]   |
|                           |
| Multímetro M-014          |
| Estado: Disponible        |
| Ubicación: Gabinete A     |
|                           |
| Taladro T-006             |
| Estado: Prestado          |
+---------------------------+
```

El prototipo permite identificar mejoras antes de programar el sistema completo

## 7.4 Relación con el SDLC y los enfoques ágiles

Design Thinking ayuda a investigar necesidades durante la planificación y el análisis de requisitos. Sus prototipos permiten evaluar ideas antes de invertir recursos en la implementación

Después, Scrum puede organizar el desarrollo por Sprints y Kanban puede controlar el flujo de tareas y mejoras. Así, los enfoques se complementan: Design Thinking ayuda a descubrir qué construir, Scrum organiza el desarrollo y Kanban mejora el flujo de trabajo

# 8. Conclusiones

Las metodologías ágiles permiten organizar proyectos de manera flexible, obtener retroalimentación y detectar errores durante el desarrollo. Scrum facilita trabajar por objetivos y ciclos cortos; Kanban ayuda a controlar tareas y mejorar el flujo; y Design Thinking permite comprender las necesidades antes de elegir una solución.

# 9. Referencias

1. Beck, K., et al. (2001). *Manifesto for Agile Software Development*. https://agilemanifesto.org/

2. Schwaber, K., & Sutherland, J. (2020). *The Scrum Guide*. https://scrumguides.org/scrum-guide.html

3. Kanban University. (s. f.). *The Official Guide to The Kanban Method*. https://kanban.university/kanban-guide/

4. Stanford University, School of Engineering. (s. f.). *A Design Thinking Process*. https://web.stanford.edu/class/me113/d_thinking.html

5. Stanford d.school. (2018). *Design Thinking Bootleg*. https://dschool.sfo3.digitaloceanspaces.com/documents/dschool_bootleg_deck_2018_final_sm2-6.pdf
