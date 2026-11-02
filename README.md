<div align="center">

<h1>🧪 Taller Integral de TDD, BDD y Calidad Ágil con Python</h1>

<p>
  <img src="https://img.shields.io/badge/Python-3.15.2-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.15" />
  <img src="https://img.shields.io/badge/Pytest-33%20Passed-0A9EDC?style=for-the-badge&logo=pytest&logoColor=white" alt="Pytest" />
  <img src="https://img.shields.io/badge/Behave-11%20Passed-0075A8?style=for-the-badge" alt="Behave" />
  <img src="https://img.shields.io/badge/Coverage-97%25-2A9D8F?style=for-the-badge" alt="Coverage" />
</p>

<p><strong>Universidad de Cundinamarca</strong><br>
<em>Facultad de Ingeniería · Ingeniería de Sistemas y Computación</em></p>

</div>

<hr>

<h2>👥 Equipo de Trabajo</h2>

<table>
  <thead>
    <tr>
      <th align="left">Integrante</th>
      <th align="left">Rol / Responsabilidad</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>Paula Ramírez</strong></td>
      <td>TDD &amp; CRUD de Proveedores, inventario y validaciones core</td>
    </tr>
    <tr>
      <td><strong>Anderson Fuel</strong></td>
      <td>BDD (Behave) &amp; Cotizaciones</td>
    </tr>
    <tr>
      <td><strong>Valentina Cristancho</strong></td>
      <td>Órdenes de Compra, Inventario &amp; Cobertura</td>
    </tr>
    <tr>
      <td><strong>Javier Cano</strong></td>
      <td>Desarrollo &amp; Pruebas Unitarias</td>
    </tr>
    <tr>
      <td><strong>Edwin Hernández</strong></td>
      <td>Calidad &amp; Análisis Estático</td>
    </tr>
  </tbody>
</table>

<hr>

<h2>📌 Resumen del Proyecto</h2>

<p>
Implementación de un sistema modular de compras e inventario aplicando prácticas rigurosas de desarrollo ágil y aseguramiento de calidad de software:
</p>

<ul>
  <li><strong>TDD (Test-Driven Development):</strong> Ciclo Rojo ➔ Verde ➔ Refactorizar implementado con <code>unittest</code> y <code>pytest</code>.</li>
  <li><strong>BDD (Behavior-Driven Development):</strong> Especificación formal de requerimientos en lenguaje Gherkin ejecutada con <code>behave</code>.</li>
  <li><strong>Aseguramiento de Calidad:</strong> Medición cuantitativa con <code>coverage.py</code> superando el Quality Gate del 80%.</li>
</ul>

<hr>

<h2>🚀 Instalación y Ejecución Local</h2>

<h3>1. Clonar y configurar entorno</h3>
<pre><code># Clonar el repositorio
git clone https://github.com/MariaPaula2095/Taller_Integral_TDD_BDD_y_Calidad_-gil.git
cd Taller_Integral_TDD_BDD_y_Calidad_-gil

# Crear y activar entorno virtual (Windows PowerShell)
python -m venv venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1

# Instalar dependencias
pip install -r requirements.txt
</code></pre>

<h3>2. Ejecutar Pruebas Unitarias (TDD)</h3>
<pre><code>pytest -v
</code></pre>

<h3>3. Ejecutar Pruebas de Comportamiento (BDD)</h3>
<pre><code>behave
</code></pre>

<h3>4. Medir Cobertura de Código</h3>
<pre><code>coverage run -m pytest
coverage report -m
</code></pre>

<hr>

<h2>📊 Resultados y Evidencia de Calidad</h2>

<h3>1. Pruebas Unitarias (Pytest)</h3>
<p><strong>Resultado:</strong> <code>33 passed in 0.35s</code> (100% de éxito)</p>

<h3>2. Pruebas BDD (Behave)</h3>
<p><strong>Resultado:</strong> <code>3 features passed, 11 scenarios passed, 51 steps passed</code> (0 fallos)</p>

<h3>3. Reporte de Cobertura de Código (Coverage.py)</h3>

<table>
  <thead>
    <tr>
      <th align="left">Módulo / Archivo</th>
      <th align="center">Sentencias</th>
      <th align="center">No Cubiertas</th>
      <th align="center">Cobertura (%)</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>src/__init__.py</code></td>
      <td align="center">0</td>
      <td align="center">0</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td><code>src/cotizacion_service.py</code></td>
      <td align="center">33</td>
      <td align="center">0</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td><code>src/inventario_service.py</code></td>
      <td align="center">18</td>
      <td align="center">1</td>
      <td align="center">94%</td>
    </tr>
    <tr>
      <td><code>src/proveedor_service.py</code></td>
      <td align="center">42</td>
      <td align="center">3</td>
      <td align="center">93%</td>
    </tr>
    <tr>
      <td><code>tests/test_cotizaciones.py</code></td>
      <td align="center">46</td>
      <td align="center">0</td>
      <td align="center">100%</td>
    </tr>
    <tr>
      <td><code>tests/test_inventario.py</code></td>
      <td align="center">18</td>
      <td align="center">1</td>
      <td align="center">94%</td>
    </tr>
    <tr>
      <td><code>tests/test_proveedores.py</code></td>
      <td align="center">57</td>
      <td align="center">1</td>
      <td align="center">98%</td>
    </tr>
    <tr>
      <td><strong>TOTAL</strong></td>
      <td align="center"><strong>214</strong></td>
      <td align="center"><strong>6</strong></td>
      <td align="center"><strong>97%</strong></td>
    </tr>
  </tbody>
</table>

<p><em>El proyecto alcanza un <strong>97%</strong> de cobertura, cumpliendo con creces el Quality Gate del 80% exigido.</em></p>

<hr>

<h2>📝 Cuestionario de Autoevaluación Resuelto</h2>

<ol>
  <li>
    <strong>¿Cuál es el orden correcto del ciclo TDD?</strong><br>
    <em>Rojo → Verde → Refactorizar</em> (Escribir la prueba que falla, programar el código mínimo para pasarla y refactorizar).
  </li>
  <br>
  <li>
    <strong>En Gherkin, ¿qué palabra clave se utiliza para describir las precondiciones de un escenario?</strong><br>
    <em>Given</em> (o <em>Dado que</em> en español).
  </li>
  <br>
  <li>
    <strong>En Python, ¿cuál es la biblioteca estándar para pruebas unitarias que no requiere instalación previa?</strong><br>
    <em>unittest</em>.
  </li>
  <br>
  <li>
    <strong>¿Qué herramienta se recomienda para ejecutar pruebas con sintaxis de pytest directamente en celdas de Google Colab?</strong><br>
    <em>ipytest</em>.
  </li>
  <br>
  <li>
    <strong>En Behave, ¿dónde se escriben los pasos que conectan Gherkin con el código Python?</strong><br>
    En el directorio <code>features/steps/</code>.
  </li>
  <br>
  <li>
    <strong>¿Cuál es la distribución recomendada en la pirámide de pruebas ágil?</strong><br>
    <em>70% pruebas unitarias, 20% pruebas de integración y 10% pruebas E2E (End-to-End)</em>.
  </li>
  <br>
  <li>
    <strong>¿Qué comando se usa para medir la cobertura de pruebas en Python?</strong><br>
    <code>coverage run -m pytest</code> seguido de <code>coverage report -m</code>.
  </li>
  <br>
  <li>
    <strong>En el contexto del CRUD de proveedores, ¿cuál sería una prueba unitaria adecuada?</strong><br>
    <em>Verificar que no se pueda crear un proveedor con NIT duplicado o NIT inválido</em>.
  </li>
  <br>
  <li>
    <strong>¿Qué diferencia principal existe entre TDD y BDD?</strong><br>
    <em>BDD se enfoca en el comportamiento y requerimientos de negocio desde la perspectiva del usuario/negocio, mientras que TDD se enfoca en la verificación técnica del diseño y funcionamiento de las unidades de código</em>.
  </li>
  <br>
  <li>
    <strong>En el inventario, ¿qué escenario Gherkin verifica correctamente la regla de stock insuficiente?</strong><br>
    <em>Dado que el stock es 2, Cuando se solicita retirar 5, Entonces el sistema muestra 'Stock insuficiente' y el stock permanece en 2</em>.
  </li>
</ol>

<hr>

<div align="center">
  <small>© 2026 · Ingeniería de Software · Universidad de Cundinamarca</small>
</div>