# Taller 3 – Buenas prácticas de programación

Proyecto de la guía 3-3. Refactorizamos el sistema de pedidos que venía en la
guía 3-2 aplicándole buenas prácticas: separamos el código por responsabilidades
(MVC), le metimos SOLID, lo dejamos bien documentado, que pase el Ruff y le
escribimos pruebas con pytest.

## Integrantes

- Andres Espinosa - 20242020114
- David Alejandro Quiñones - 20251020120

## De qué trata el proyecto

Es un sistema de pedidos simple: recibes una lista de productos, dependiendo del
tipo de cliente se aplica un descuento (regular, vip, empleado o estudiante),
después se le suma el IVA del 19 % y listo. También puede procesar el pago,
guardar el pedido y generar un reporte.

Antes todo estaba en una sola clase (`OrderSystem`) que hacía de todo, y eso
estaba mal porque si querías cambiar algo tocabas de todo. Al final quedó bien
separado en módulos y estrategias, y se puede añadir un descuento nuevo o un
formato de reporte sin romper nada.

El caso de ejemplo (cliente VIP con productos que suman 40000) tiene que dar
**38080** después del descuento del 20 % y el IVA del 19 %. Ese valor se usa de
referencia en las pruebas para verificar que no rompimos el comportamiento
original.

## Cómo correrlo

Primero creamos el entorno virtual (una sola vez):

```bash
python -m venv .venv
```

Lo activamos. En Windows (PowerShell):

```powershell
.\.venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source .venv/bin/activate
```

Instalamos lo que necesitamos:

```bash
python -m pip install ruff pytest
```

Para ejecutar el programa:

```bash
python main.py
```

## Comandos para revisar

Para ver que el código esté bien (estilo, imports, etc.):

```bash
ruff check .
ruff format --check .
```

Para correr las pruebas:

```bash
pytest -v
```

## Cómo está organizado (MVC)

Separamos el proyecto en carpetas según la arquitectura Modelo-Vista-Controlador:

```
|-- main.py                  # El principal, arranca todo y conecta las partes
|-- model/                   # Acá va la lógica y los datos del negocio
|   |-- order.py             # El pedido y el cálculo del total (impuesto incluido)
|   |-- discount.py          # Los descuentos (regular, vip, empleado, estudiante)
|   |-- payment.py           # Los métodos de pago
|   |-- repository.py        # El guardado del pedido (MySQL)
|   `-- report.py            # Los formatos de reporte
|-- view/
|   `-- console_view.py      # Muestra la info en la consola (las impresiones)
|-- controller/
|   `-- order_controller.py  # Coordina el modelo con la vista
|-- tests/                   # Las pruebas con pytest
```

- **Model**: la lógica. Acá están el pedido, los descuentos, el pago, el
  guardado y los reportes.
- **View**: solo muestra las cosas, o sea hace las impresiones. No calcula
  descuentos ni nada de eso.
- **Controller**: el que organiza. Le pide al modelo los cálculos y le dice a la
  vista que muestre el resultado. No tiene toda la lógica del negocio.
- **main.py**: el de arranque. Crea los objetos, los conecta y ejecuta.

La idea es que la vista no calcule y el modelo no imprima, cada uno en lo suyo.

## Los 5 principios SOLID (cómo los aplicamos)

- **SRP (Responsabilidad Única)**: cada clase hace una sola cosa. Antes
  `OrderSystem` se encargaba de todo (pedido, descuento, impuesto, pago, guardar
  y reportar), ahora eso está separado en `Order`, `discount.py`, `payment.py`,
  `repository.py`, `report.py`, etc.
- **OCP (Abierto/Cerrado)**: puedes agregar descuentos nuevos, métodos de pago,
  formatos de reporte o repositorios sin tocar el código que ya funciona. Por
  ejemplo metimos `StudentDiscount` sin tocar la clase `Order`.
- **LSP (Sustitución de Liskov)**: todas las implementaciones (los descuentos,
  los pagos, los reportes, el repositorio) se pueden cambiar por otras que
  implementen la misma interfaz y todo sigue funcionando igual.
- **ISP (Segregación de Interfaces)**: las interfaces son chiquitas y
  específicas (`DiscountStrategy`, `PaymentMethod`, `ReportGenerator`). Ninguna
  clase se ve obligada a implementar métodos que no usa.
- **DIP (Inversión de Dependencias)**: lo de alto nivel depende de abstracciones
  y no de detalles. Por ejemplo el controlador usa un `OrderRepository` y no
  depende directamente de MySQL, así que se puede cambiar de base de datos sin
  tocar todo lo demás.

## Función nueva que agregamos

Le metimos el descuento de **`StudentDiscount`** (15 % para estudiantes). Lo
elegimos para demostrar que se puede alargar el sistema agregando una clase
nueva sin tocar lo que ya estaba, y además tiene sus pruebas.
