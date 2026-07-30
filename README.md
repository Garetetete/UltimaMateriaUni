# API de validación con pruebas BDD

Proyecto de práctica centrado en **estrategia de pruebas**, no en la complejidad del dominio. Expone una API mínima en **FastAPI** y la cubre con tres niveles de prueba: unitarias, **BDD en Gherkin** y **end-to-end con Playwright**, todo ejecutable en Docker.

El dominio es deliberadamente simple —validar que un número tenga 4 dígitos y que todos sean distintos— para que el foco esté en cómo se prueba.

---

## Stack

- **API:** FastAPI + Uvicorn
- **Pruebas:** pytest, **pytest-bdd** (escenarios Gherkin), **Playwright** (E2E de navegador), pytest-cov, httpx
- **Plantillas:** Jinja2
- **Entorno:** Docker y docker-compose (un servicio para la app y otro para ejecutar la suite)

## El endpoint

```http
GET /validate/{number}
```

Devuelve `200` con `{"number": "1234", "valid": true}` si el número es válido, o `400` con el detalle del error si no lo es.

## Estrategia de pruebas

**Unitarias** sobre la función de validación, cubriendo los casos límite: longitud incorrecta, caracteres no numéricos y dígitos repetidos.

**BDD con Gherkin.** El escenario se escribe en lenguaje natural y se alimenta con una tabla de ejemplos, de modo que agregar un caso nuevo no requiere tocar código de prueba:

```gherkin
Feature: Number Validation API
    Scenario: Validating a correct Number
    Given I have a number <number>
    When I validate the number
    Then the result should be <result>
    Examples:
    | number | result |
    | 1234   | true   |
    | 1123   | false  |
    | 12a4   | false  |
    | 123    | false  |
```

**End-to-end con Playwright**, ejerciendo la aplicación desde un navegador real.

`pytest.ini` deja la cobertura activada por defecto (`--cov=app`), con reporte en terminal y en HTML.

---

## Cómo correrlo

### Con Docker

```bash
docker compose up --build webapp     # API en http://localhost:8000
docker compose run --rm unittests    # ejecuta toda la suite
```

La documentación interactiva de FastAPI queda en <http://localhost:8000/docs>.

### En local

Requisitos: Python 3.11+.

```bash
pip install -r requirements.txt
playwright install --with-deps

uvicorn app.main:app --reload    # servidor
pytest                           # pruebas con cobertura
```

---

## Contexto

Trabajo desarrollado en el marco de una asignatura de ingeniería de software, orientado a practicar diseño de pruebas en varios niveles y su automatización en contenedores.
