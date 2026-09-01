# API de Inventario - Mini Juguetería

Proyecto académico simulado para aplicar control de versiones, registro de
estados de configuración y trazabilidad mediante Git y GitHub.

## Funcionalidades

- `GET /products`: listar juguetes.
- `POST /products`: agregar un juguete.
- `GET /products?entry_date=AAAA-MM-DD`: filtrar por fecha de ingreso.

## Integrantes y responsabilidades

- William Cortez: estructura, listado, filtro por fecha y liberación.
- Karina Barragán: registro de productos, pruebas y configuración segura.

## Cómo ejecutar

No se requiere despliegue real. El código representa una API simplificada para
la práctica de Gestión de Configuración del Software.

## Convenciones

- Ramas: `feature/`, `fix/`, `docs/` y `release/`.
- Commits: `chore`, `docs`, `feat` o `fix`.
- Trazabilidad: cambios vinculados mediante `ISSUE-xx` y `#n`.
- Versiones: SemVer con formato `vMAJOR.MINOR.PATCH`.

## Versiones

- `v1.0.0`: línea base funcional.
- `v1.0.1`: parche de configuración sensible.
- `v1.1.0`: filtro por fecha y repositorio auditado.

## Auditoría

La auditoría utiliza `v1.1.0` como línea base.

* Auditoría física: Issue #1.
* Auditoría funcional: Issue #2.
* Release planificado: `v1.1.1`.

Ejecución de pruebas:

```bash
py -m pytest -q
```

##Examen Parcial II GCS
Elabore checklist de pre-release, justificando ítems.
