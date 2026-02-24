# TEMA 11: CONCEPTOS DE INFORMATICA

---

## 1. INTRODUCCION E HISTORIA

### 1.1. Concepto de informatica

**Informatica** = **INFOR**macion auto**MATICA**. Ciencia que estudia el tratamiento automatico y racional de la informacion mediante maquinas automaticas (ordenadores/computadoras).

- **Padre de la informatica:** Charles Babbage (siglo XIX). Diseno la **Maquina Analitica** (considerada el primer concepto de ordenador programable, nunca llego a construirse completamente).
- **Ada Lovelace:** considerada la primera programadora de la historia (escribio el primer algoritmo para la maquina de Babbage).
- **Alan Turing:** padre de la ciencia de la computacion teorica y la inteligencia artificial. Maquina de Turing. Descifro Enigma (WWII).

### 1.2. Hitos historicos

| Ano | Hito |
|-----|------|
| **1944** | **Mark I** (Harvard/IBM): primera computadora **electromecanica** (reles). Howard Aiken |
| **1945** | **ENIAC** (University of Pennsylvania): primera computadora **electronica** de proposito general. Mauchly y Eckert. 30 toneladas, 18.000 valvulas de vacio |
| **1951** | **UNIVAC I:** primer ordenador comercial |
| **1971** | **Intel 4004:** primer microprocesador comercial |
| **1975** | **Altair 8800:** considerado primer ordenador personal (microcomputador) |
| **1976** | **Apple I:** Steve Jobs y Steve Wozniak |
| **1981** | **IBM PC (Personal Computer):** primer PC de IBM. Estandar de la industria. Sistema operativo MS-DOS (Microsoft, Bill Gates) |

### 1.3. Generaciones de ordenadores

| Generacion | Periodo | Tecnologia | Caracteristicas |
|-----------|---------|-----------|----------------|
| **1a** | 1940-1956 | Valvulas de vacio (tubos) | Enormes, costosos, lentos. ENIAC, UNIVAC |
| **2a** | 1956-1963 | Transistores | Mas pequenos, fiables, rapidos |
| **3a** | 1963-1971 | Circuitos integrados (chips) | Miniaturizacion, IBM 360 |
| **4a** | 1971-actualidad | Microprocesadores (VLSI) | PCs, portatiles, smartphones. Intel 4004, IBM PC |
| **5a** | Actualidad-futuro | Inteligencia Artificial, computacion cuantica | Procesamiento paralelo masivo, redes neuronales |

---

## 2. SISTEMA BINARIO Y UNIDADES DE MEDIDA

### 2.1. Codigo binario

Los ordenadores trabajan internamente con el **sistema binario** (base 2): solo dos digitos, **0 y 1** (encendido/apagado, verdadero/falso, corriente/no corriente).

### 2.2. Unidades de informacion

| Unidad | Equivalencia | Descripcion |
|--------|-------------|-------------|
| **Bit (b)** | 0 o 1 | Unidad MINIMA de informacion. **Unidad teorica mas importante** |
| **Nibble** | **4 bits** | Medio byte. Representa un digito hexadecimal |
| **Byte (B)** | **8 bits** | **Unidad PRACTICA mas importante.** Almacena un caracter (letra, numero, simbolo) |
| **Kilobyte (KB)** | **1.024 bytes** | 2^10 bytes |
| **Megabyte (MB)** | **1.024 KB** | 2^20 bytes = 1.048.576 bytes |
| **Gigabyte (GB)** | **1.024 MB** | 2^30 bytes |
| **Terabyte (TB)** | **1.024 GB** | 2^40 bytes |
| **Petabyte (PB)** | **1.024 TB** | 2^50 bytes |
| **Exabyte (EB)** | 1.024 PB | 2^60 bytes |
| **Zettabyte (ZB)** | 1.024 EB | 2^70 bytes |
| **Yottabyte (YB)** | 1.024 ZB | 2^80 bytes |

### 2.3. Diferencia fundamental: Mb vs MB

| Abreviatura | Significado | Uso tipico |
|-------------|------------|-----------|
| **Mb (megabit)** | 1.000.000 de bits | Velocidad de red (100 Mbps = 100 megabits por segundo) |
| **MB (Megabyte)** | 1.024 x 1.024 bytes = 1.048.576 bytes | Tamano de archivos, capacidad de almacenamiento |

> **1 Byte = 8 bits**, por tanto **1 MB = 8 Mb.** La velocidad de internet se mide en Mbps (megabits), el tamano de archivos en MB (megabytes). Por eso una conexion de 100 Mbps descarga a unos 12,5 MB/s.

### 2.4. Sistemas de codificacion de caracteres

- **ASCII:** American Standard Code for Information Interchange. 7 bits = 128 caracteres. ASCII extendido: 8 bits = 256 caracteres.
- **EBCDIC:** Extended Binary Coded Decimal Interchange Code. IBM.
- **Unicode/UTF-8:** estandar moderno. Incluye todos los caracteres de todos los idiomas del mundo.

---

## 3. HARDWARE

### 3.1. Concepto

**Hardware** = parte FISICA, tangible del ordenador. Componentes que se pueden tocar (circuitos, cables, carcasa, teclado, monitor, etc.).

### 3.2. Placa base / Placa madre (Motherboard)

Es el **circuito impreso principal** del ordenador. Sobre ella se conectan TODOS los demas componentes. Elementos principales:

| Componente | Funcion |
|-----------|---------|
| **Zocalo (Socket)** | Donde se inserta el microprocesador/CPU |
| **Ranuras de memoria (DIMM)** | Donde se insertan los modulos de RAM |
| **Slots de expansion** | Para tarjetas adicionales: PCI, PCI Express (grafica, sonido, red) |
| **Chipset** | Conjunto de chips que gestionan la comunicacion entre componentes |
| **BIOS/UEFI** | Firmware basico de arranque (chip ROM en placa base) |
| **Conectores SATA/M.2** | Para discos duros y unidades SSD |
| **Conectores de alimentacion** | Reciben energia de la fuente de alimentacion |
| **Puertos traseros** | USB, video, red, audio, etc. |
| **Pila/Bateria CMOS** | Mantiene la configuracion de la BIOS y el reloj cuando el PC esta apagado |

### 3.3. CPU / Microprocesador (Unidad Central de Proceso)

El **"cerebro" del ordenador.** Ejecuta las instrucciones de los programas. Se compone de:

| Parte de la CPU | Funcion |
|----------------|---------|
| **Unidad de Control (UC)** | Dirige y coordina todas las operaciones del ordenador. Interpreta las instrucciones |
| **Unidad Aritmetico-Logica (UAL/ALU)** | Realiza calculos matematicos y operaciones logicas (comparaciones, AND, OR, NOT) |
| **Registros** | Memoria interna ultra-rapida de la CPU para datos temporales |
| **Bus interno** | Lineas de comunicacion dentro de la CPU |

> **Microprocesador = UC + ALU** (en un unico chip de silicio).

- **Velocidad del procesador:** se mide en **Hz (Hercios).**
  - MHz = Megahercios (millones de ciclos por segundo).
  - GHz = Gigahercios (miles de millones de ciclos por segundo).
- **Reloj del sistema:** genera los impulsos que sincronizan todas las operaciones. A mayor frecuencia de reloj, mayor velocidad de procesamiento (en igualdad de condiciones).
- **Nucleos (cores):** los procesadores modernos son multinucleo (dual-core, quad-core, octa-core). Mas nucleos = mas capacidad de procesamiento simultaneo.

### 3.4. Memoria principal

#### RAM (Random Access Memory - Memoria de Acceso Aleatorio)

- Memoria de **lectura y escritura.**
- **Temporal / Volatil:** pierde su contenido al apagar el ordenador.
- Almacena los datos y programas que el procesador esta usando en ese momento.
- A mas RAM, mayor capacidad de trabajar con varios programas simultaneamente.
- Tipos: DDR3, DDR4, DDR5 (cada generacion mas rapida).
- Se mide en GB (actualmente tipico: 8 GB, 16 GB, 32 GB).

#### ROM (Read Only Memory - Memoria de Solo Lectura)

- Memoria de **solo lectura** (no se puede escribir en ella en condiciones normales).
- **Permanente / No volatil:** mantiene su contenido sin corriente electrica.
- Contiene el **firmware** (software basico grabado de fabrica).
- Almacena la **rutina de arranque / POST (Power-On Self Test):** al encender, el ordenador comprueba que todo funciona.
- **BIOS (Basic Input/Output System):** programa basico de entrada/salida almacenado en ROM que permite al ordenador arrancar y comunicarse con los dispositivos.
- **UEFI:** version moderna que sustituye a la BIOS clasica.
- Variantes: PROM (programable una vez), EPROM (borrable con UV), EEPROM (borrable electricamente), Flash ROM.

#### Memoria cache

- Memoria ultra-rapida situada entre la CPU y la RAM.
- Almacena los datos mas frecuentemente usados para acelerar el acceso.
- Niveles: L1 (mas rapida, mas pequena, dentro del procesador), L2, L3 (mas grande, algo mas lenta).

### 3.5. Chipset

Conjunto de circuitos integrados que gestionan las comunicaciones entre los distintos componentes de la placa base:

| Parte | Funcion | Conecta con |
|-------|---------|------------|
| **Puente Norte (Northbridge)** | Comunicaciones de **alta velocidad** | CPU, RAM, tarjeta grafica (AGP/PCIe) |
| **Puente Sur (Southbridge)** | Comunicaciones de **menor velocidad** | Perifericos, discos duros (SATA), puertos USB, sonido, red, BIOS, slots PCI |

> En arquitecturas modernas, muchas funciones del puente norte se han integrado en la propia CPU.

### 3.6. Fuente de alimentacion

- Transforma la corriente alterna (220V/230V CA) de la red electrica en corriente continua (CC/DC) a los voltajes que necesitan los componentes (3.3V, 5V, 12V).
- Potencia medida en vatios (W).

### 3.7. Bus del sistema

- Conjunto de lineas (cables/pistas) que transportan informacion entre componentes.
- **Bus de datos:** transporta datos entre CPU, memoria y perifericos.
- **Bus de direcciones:** indica las posiciones de memoria a las que se accede.
- **Bus de control:** transporta senales de control y sincronizacion.
- Ancho de bus: numero de lineas (bits) que puede transmitir simultaneamente (8, 16, 32, 64 bits).

---

## 4. ALMACENAMIENTO (MEMORIA SECUNDARIA/AUXILIAR)

### 4.1. Concepto

Dispositivos que almacenan informacion de forma **permanente** (no volatil). A diferencia de la RAM, mantienen los datos sin corriente electrica.

### 4.2. Tipos de almacenamiento

#### Almacenamiento magnetico

| Dispositivo | Caracteristicas |
|------------|----------------|
| **Disco duro (HDD)** | Discos rigidos magneticos que giran a alta velocidad. Organizacion: **pistas** (circulos concentricos), **sectores** (divisiones de las pistas), **cilindros** (pistas alineadas en varios platos). Interfaces: **IDE/ATA** (antiguo, cable plano), **SCSI** (servidores), **SATA** (actual). Capacidad: hasta varios TB |
| **Disquete (Floppy disk)** | Disco flexible magnetico. 3,5 pulgadas = **1,44 MB** (HD - High Density). Obsoleto |
| **Cinta magnetica** | Almacenamiento secuencial. Uso: copias de seguridad (backup). Lenta pero gran capacidad y bajo coste. DAT, DLT, LTO |

#### Almacenamiento optico

| Dispositivo | Capacidad | Tecnologia |
|------------|-----------|-----------|
| **CD-ROM** | **700 MB** (80 min musica) | Laser. Solo lectura |
| **CD-R** | 700 MB | Grabable una vez |
| **CD-RW** | 700 MB | Regrabable |
| **DVD** | **4,7 GB** (simple capa) / 8,5 GB (doble capa) | Laser mas fino que CD |
| **Blu-ray** | **25 GB** (simple capa) / 50 GB (doble capa) | Laser azul-violeta |

#### Almacenamiento de estado solido (sin partes moviles)

| Dispositivo | Caracteristicas |
|------------|----------------|
| **SSD (Solid State Drive)** | Memoria flash. Mucho mas rapido que HDD, sin partes moviles, silencioso, resistente a golpes. Interfaces: SATA, M.2, NVMe |
| **Memoria USB (Pendrive)** | Memoria flash portatil. Conexion USB. Multiples capacidades (desde MB hasta TB) |
| **Tarjetas de memoria** | SD, microSD, CF. Camaras, moviles, tabletas |

#### Almacenamiento magneto-optico

- Combina tecnologia magnetica y laser.
- Ejemplo: discos MO (Magneto-Optical).
- **ZIP:** disco magnetico de alta capacidad (100 MB, 250 MB, 750 MB). Fabricante: Iomega. Obsoleto.
- **JAZ:** similar al ZIP pero mayor capacidad (1 GB, 2 GB). Obsoleto.

### 4.3. Estructura logica del disco duro

- **Pista (Track):** circunferencia concentrica en la superficie del disco.
- **Sector:** subdivision de una pista. Unidad minima de lectura/escritura. Generalmente **512 bytes** (o 4 KB en discos modernos).
- **Cilindro:** conjunto de pistas en la misma posicion vertical en todos los platos.
- **Cluster:** agrupacion de sectores. Unidad minima de asignacion del sistema operativo.

---

## 5. UNIDADES DE VELOCIDAD

| Ambito | Unidad | Descripcion |
|--------|--------|-------------|
| **Procesador (reloj)** | Hz, MHz, GHz | Ciclos por segundo. GHz = miles de millones de hercios |
| **Red / Internet** | bps, Kbps, Mbps, Gbps | Bits por segundo. Ojo: bits (b minuscula), no bytes |
| **Impresora** | **ppm** (paginas por minuto) | Velocidad de impresion |
| **Disco duro** | rpm (revoluciones por minuto) | Velocidad de giro: 5400, 7200, 10000, 15000 rpm |
| **Transferencia datos** | MB/s, GB/s | Megabytes/Gigabytes por segundo (USB, SATA) |

---

## 6. CONECTORES E INTERFACES

### 6.1. Conectores clasicos

| Conector | Tipo | Caracteristicas |
|----------|------|----------------|
| **PS/2** | Circular miniDIN, 6 pines | **Verde = raton, Lila/Morado = teclado.** En desuso, sustituido por USB |
| **Puerto paralelo (LPT1)** | **DB-25 hembra, 25 pines** | Impresoras principalmente. Transmision en paralelo (varios bits simultaneos). Obsoleto |
| **Puerto serie (COM)** | **DB-9 macho, 9 pines** (antes DB-25) | Raton antiguo, modem. Transmision en serie (bit a bit). Obsoleto para periferico comun, aun usado en industria |
| **VGA** | **DB-15 (HD-15), 15 pines en 3 hileras** | Video analogico. Conector azul tipicamente. Siendo sustituido por HDMI/DisplayPort |
| **DVI** | Digital/analogico | Video digital (y analogico en variantes DVI-I). Conector blanco |
| **HDMI** | Digital | Video + audio digital. Estandar actual en TVs y monitores |
| **DisplayPort** | Digital | Video + audio. Uso profesional y gaming |
| **RJ-45** | 8 pines | Red Ethernet (cable de red). Conector del cable de par trenzado |
| **RJ-11** | 4-6 pines | Telefono / modem. Mas pequeno que RJ-45 |
| **Jack 3.5mm** | Clavija circular | Audio (auriculares, microfono) |

### 6.2. USB (Universal Serial Bus)

- **Conector universal** que ha sustituido a la mayoria de conectores anteriores.
- Permite conectar perifericos **en caliente** (sin apagar el ordenador): Plug and Play / Hot Plug.
- Suministra corriente electrica al dispositivo conectado.

| Version | Velocidad maxima teorica | Nombre comercial |
|---------|------------------------|-----------------|
| **USB 1.0** | 1.5 Mbps (Low Speed) | - |
| **USB 1.1** | 12 Mbps (Full Speed) | - |
| **USB 2.0** | **480 Mbps** (High Speed) | Hi-Speed USB |
| **USB 3.0** | **5 Gbps** (Super Speed) | SuperSpeed USB (conector azul) |
| **USB 3.1** | 10 Gbps | SuperSpeed USB 10Gbps |
| **USB 3.2** | 20 Gbps | SuperSpeed USB 20Gbps |
| **USB 4** | 40 Gbps | - |

- **Tipos de conector USB:** A (rectangular clasico), B (cuadrado para impresoras), Mini USB, Micro USB, **USB-C** (reversible, moderno, estandar actual).

### 6.3. FireWire (IEEE 1394)

- Conexion de alta velocidad (400 Mbps - 800 Mbps).
- Desarrollado por Apple.
- Uso: camaras de video digital, discos duros externos.
- Actualmente en desuso, sustituido por USB 3.0 y Thunderbolt.

### 6.4. Thunderbolt

- Desarrollado por Intel y Apple.
- Thunderbolt 3 y 4: usa conector USB-C, hasta 40 Gbps.

---

## 7. PERIFERICOS

### 7.1. Clasificacion general

| Tipo | Funcion | Ejemplos |
|------|---------|----------|
| **Entrada** | Introducir datos en el ordenador | Teclado, raton, escaner, microfono, webcam, lector codigos barras, tableta digitalizadora |
| **Salida** | El ordenador muestra/emite informacion al exterior | Monitor, impresora, altavoces, auriculares, plotter, proyector |
| **Entrada/Salida (E/S)** | Bidireccional, introducen y extraen datos | Disco duro, USB/pendrive, pantalla tactil, modem, tarjeta de red, impresora multifuncion |
| **Comunicaciones** | Conectan el ordenador con otros o con redes | Tarjeta de red (NIC), modem, hub, switch, router, punto de acceso WiFi |

### 7.2. Perifericos de entrada

#### Teclado

- Periferico de entrada **mas utilizado junto con el raton.**
- **Disposicion QWERTY** (nombre por las 6 primeras letras de la fila superior de letras). Creada por Christopher Latham Sholes (1873) para la maquina de escribir.
- **Teclas principales:**
  - Alfanumericas: letras y numeros.
  - Funcion: F1-F12.
  - Especiales: Esc, Tab, Bloq Mayus, Shift, Ctrl, Alt, Alt Gr, Enter, Supr, Insert, Inicio, Fin, Re Pag, Av Pag.
  - Teclado numerico (derecha).
  - Flechas de direccion.
- **Conexion:** PS/2 (lila), USB, inalambrico (Bluetooth/radiofrecuencia).

#### Raton (Mouse)

- Dispositivo apuntador.
- Mide el desplazamiento en **mickeys.**
- Tipos: mecanico (bola, obsoleto), optico (LED), laser.
- **Conexion:** PS/2 (verde), USB, inalambrico.

#### Escaner

- Digitaliza documentos e imagenes (convierte a formato digital).
- Resolucion medida en **ppp (puntos por pulgada) / dpi (dots per inch).**
- Tipos: plano (de sobremesa), de mano, de alimentacion automatica.

#### Otros perifericos de entrada

- **Webcam:** captura video/imagenes.
- **Microfono:** captura sonido.
- **Lector de codigo de barras:** lee codigos de barras/QR.
- **Tableta digitalizadora/graficadora:** para diseno grafico.
- **Joystick/gamepad:** para juegos.
- **Lector de huella dactilar.**

### 7.3. Perifericos de salida

#### Monitor / Pantalla

- Dispositivo de salida visual principal.
- **Pixel:** unidad minima de imagen en pantalla (punto de luz). A mayor numero de pixeles = mayor resolucion = mayor nitidez.
- **Resolucion:** numero de pixeles en horizontal x vertical (ej: 1920x1080 = Full HD, 3840x2160 = 4K UHD).
- **Tecnologias:**
  - **CRT (tubo de rayos catodicos):** antiguo, voluminoso. Obsoleto.
  - **LCD (Liquid Crystal Display):** pantalla plana, cristal liquido.
  - **LED:** variante de LCD con retroiluminacion LED.
  - **OLED:** pixeles que emiten luz propia, mejor contraste.
  - **TFT:** tecnologia de transistores de pelicula fina (tipo de LCD).
- **Tamano:** se mide en **pulgadas** de la diagonal.

#### Plotter (Trazador grafico)

- Impresora de gran formato.
- Uso: planos de arquitectura/ingenieria, carteles, banners.
- Imprime en papel de gran tamano (rollos).

#### Proyector

- Proyecta la imagen del ordenador sobre una superficie (pantalla, pared).

### 7.4. Perifericos de comunicaciones

| Dispositivo | Funcion |
|------------|---------|
| **NIC (Network Interface Card) / Tarjeta de red** | Permite conectar el ordenador a una red. Ethernet (cable RJ-45) o WiFi (inalambrica) |
| **Modem** | **MO**dulador-**DEM**odulador. Convierte senal digital en analogica (y viceversa). Para conexion telefonica a internet. En desuso para ADSL puro |
| **Hub (Concentrador)** | Conecta varios dispositivos en red. Envia datos a TODOS los puertos (no inteligente). Capa 1 OSI |
| **Switch (Conmutador)** | Similar al hub pero INTELIGENTE: envia datos solo al puerto de destino (usa direcciones MAC). Mas eficiente. Capa 2 OSI |
| **Router (Encaminador/Enrutador)** | Conecta diferentes redes entre si. Enruta paquetes de datos al destino correcto (usa direcciones IP). Capa 3 OSI. Conecta la red local a internet |
| **Punto de acceso WiFi (AP)** | Proporciona conexion inalambrica WiFi |
| **Repetidor** | Amplifica la senal para cubrir mayor distancia |
| **Firewall (Cortafuegos)** | Filtra el trafico de red segun reglas de seguridad |

### 7.5. Comunicacion inalambrica

| Tecnologia | Caracteristicas |
|-----------|----------------|
| **Bluetooth** | Corto alcance (hasta ~10-100 m). Frecuencia **2,4 GHz**. Para perifericos (auriculares, teclado, raton, altavoz). IEEE 802.15 |
| **Infrarrojo (IrDA)** | Linea de vision directa, muy corto alcance. Obsoleto (antes en mandos TV, moviles antiguos) |
| **WiFi** | Red inalambrica de area local (WLAN). Estandares IEEE 802.11: a/b/g/n/ac/ax(WiFi 6). Frecuencias 2,4 GHz y 5 GHz |
| **NFC (Near Field Communication)** | Muy corto alcance (< 10 cm). Pagos contactless, identificacion |

---

## 8. IMPRESORAS

### 8.1. Clasificacion principal

#### Segun mecanismo de impresion

| Tipo | Subtipo | Descripcion |
|------|---------|-------------|
| **Con impacto** | Matricial (agujas), Margarita | Golpean el papel a traves de cinta entintada. Ruidosas. Permiten copias con papel autocopiativo (calco) |
| **Sin impacto** | Inyeccion de tinta, Laser, Termica | No golpean el papel. Mas silenciosas |

#### Segun unidad de impresion

| Tipo | Descripcion | Ejemplo |
|------|-------------|---------|
| **De caracteres** | Imprimen caracter a caracter | Margarita |
| **De lineas** | Imprimen linea completa cada vez | Impresoras de cadena (uso industrial) |
| **De paginas** | Imprimen pagina completa cada vez | **Laser** |

### 8.2. Tipos de impresora detallados

#### Impresora de margarita

- **Con impacto, de caracteres.**
- Cabezal con forma de margarita (rueda con petalos, cada uno con un caracter).
- Calidad tipo maquina de escribir (letter quality).
- Solo texto, no graficos.
- Obsoleta.

#### Impresora matricial (de agujas)

- **Con impacto, de caracteres/lineas.**
- Cabezal con **agujas** (9 o 24 pines) que golpean una cinta entintada contra el papel.
- Puede imprimir graficos basicos (matriz de puntos).
- **Ventaja principal:** permite imprimir en papel **autocopiativo** (multipart forms) por el impacto. Uso en tickets, facturas con copia, albaranes.
- Ruidosa, baja calidad, lenta.
- Aun en uso en determinados entornos (farmacias, talleres, TPV antiguos).

#### Impresora de inyeccion de tinta (inkjet)

- **Sin impacto.**
- Expulsa **micro-gotas de tinta** liquida sobre el papel a traves de inyectores (boquillas).
- **Cartuchos de tinta** (normalmente 4: CMYK = Cian, Magenta, Amarillo, Negro).
- Buena calidad para texto y graficos/fotos.
- Relativamente economica de compra.
- Coste por pagina medio-alto (tinta cara).
- Velocidad media.
- Riesgo de secado de cabezales si no se usa.

#### Impresora laser

- **Sin impacto, de paginas.** La mas utilizada en entornos profesionales/oficinas.
- Usa **toner** (polvo fino) + **tambor fotoconductor** + laser + calor (fusor).
- **Proceso:** el laser "dibuja" la imagen en el tambor cargado electricamente -> el toner se adhiere a la imagen -> se transfiere al papel -> el fusor aplica calor y presion para fijar el toner.
- **Alta velocidad** (muchas ppm).
- **Alta calidad** de impresion.
- **Bajo coste por pagina** (toner rinde mas que cartucho de tinta).
- Mas cara de compra que la de inyeccion.
- **Color o monocromo (blanco y negro).**

#### Impresora termica

- **Sin impacto.**
- Usa calor sobre papel termosensible (papel termico especial que cambia de color con el calor).
- Uso: tickets de compra (TPV), etiquetas, recibos de cajero automatico.
- No necesita tinta ni toner.
- La impresion se desvanece con el tiempo.
- **Termica directa:** el calor actua sobre el papel termico.
- **Transferencia termica:** usa cinta de cera/resina que se funde sobre el papel. Mas duradera.

#### Plotter (trazador)

- Impresora de **gran formato.**
- Para planos, carteles, dibujo tecnico.
- De inyeccion de tinta o de corte.

### 8.3. Resolucion de impresora

- Se mide en **ppp (puntos por pulgada) / dpi (dots per inch).**
- A mayor ppp, mayor calidad de impresion.
- Tipico: 300 dpi (basica), 600 dpi (buena), 1200 dpi o mas (alta calidad, fotos).

---

## 9. SOFTWARE

### 9.1. Concepto

**Software** = parte LOGICA, intangible del ordenador. Programas e instrucciones que le dicen al hardware que hacer. No se puede tocar.

### 9.2. Tipos de software

| Tipo | Funcion | Ejemplos |
|------|---------|----------|
| **Software de sistema (SO)** | Gestiona el hardware y proporciona plataforma para el software de aplicacion | Windows, Linux, macOS, Android, iOS |
| **Software de aplicacion** | Programas para tareas especificas del usuario | Word, Excel, navegador web, correo, etc. |
| **Software de desarrollo** | Herramientas para crear otros programas | Compiladores, editores de codigo, IDEs |
| **Firmware** | Software grabado en hardware (ROM) | BIOS/UEFI, firmware de impresora |

### 9.3. Sistema operativo (SO)

- Programa fundamental que gestiona los recursos del ordenador (CPU, memoria, discos, perifericos).
- Hace de intermediario entre el usuario/aplicaciones y el hardware.
- **Ejemplos:** Windows (Microsoft), macOS (Apple), Linux (libre/open source), Android (Google, para moviles), iOS (Apple, para iPhone).
- **Funciones:** gestion de memoria, gestion de procesos, gestion de archivos, gestion de dispositivos, interfaz de usuario.

---

## 10. DATOS CLAVE PARA EXAMEN

### Historia y conceptos basicos

1. **Padre de la informatica:** Charles Babbage (Maquina Analitica).
2. **Mark I (1944):** primera computadora **electromecanica.**
3. **ENIAC (1945):** primera computadora **electronica.**
4. **Primer PC IBM:** 1981. Sistema operativo MS-DOS (Microsoft).
5. **Informatica** = INFORmacion autoMATICA.

### Unidades de medida

6. **Bit:** unidad teorica mas importante (0 o 1).
7. **Byte:** unidad practica mas importante (8 bits = 1 caracter).
8. **Nibble:** 4 bits.
9. **1 KB = 1.024 bytes. 1 MB = 1.024 KB. 1 GB = 1.024 MB. 1 TB = 1.024 GB. 1 PB = 1.024 TB.**
10. **Mb (megabit) es distinto de MB (Megabyte). 1 Byte = 8 bits.**
11. **Velocidad red:** en Mbps (megabits). **Tamano archivos:** en MB/GB (megabytes/gigabytes).

### Hardware

12. **CPU = UC (Unidad Control) + ALU (Unidad Aritmetico-Logica) = microprocesador.**
13. **Velocidad CPU:** se mide en **Hz (MHz, GHz).**
14. **RAM:** lectura/escritura, TEMPORAL (volatil), almacena datos en uso.
15. **ROM:** solo lectura, PERMANENTE (no volatil), contiene firmware/BIOS, rutina arranque (POST).
16. **Chipset:** Puente Norte (CPU, RAM, grafica) + Puente Sur (perifericos, discos, USB, BIOS).
17. **Disco duro:** pistas + sectores. Interfaces: IDE (antiguo), SCSI (servidores), SATA (actual).
18. **Disquete 3,5":** 1,44 MB.
19. **CD-ROM:** 700 MB. **DVD:** 4,7 GB (simple capa). **Blu-ray:** 25 GB (simple capa).

### Conectores

20. **PS/2:** VERDE = raton, LILA/MORADO = teclado.
21. **Puerto paralelo LPT1:** 25 pines. Para impresoras antiguas.
22. **Puerto serie COM:** 9 pines (DB-9).
23. **VGA:** 15 pines, 3 hileras. Video analogico.
24. **USB:** universal, plug and play, hot plug. USB 2.0 = 480 Mbps, USB 3.0 = 5 Gbps.
25. **FireWire:** IEEE 1394. Desarrollado por Apple. 400-800 Mbps.
26. **RJ-45:** red Ethernet. **RJ-11:** telefono.

### Perifericos

27. **Teclado QWERTY:** disposicion mas extendida. Creada por Sholes (1873).
28. **Pixel:** unidad minima de imagen en pantalla.
29. **Velocidad impresora:** ppm (paginas por minuto).
30. **Hub:** envia a TODOS (no inteligente). **Switch:** envia solo al destino (inteligente, usa MAC). **Router:** conecta REDES distintas (usa IP).

### Impresoras

31. **Con impacto:** margarita, matricial (agujas). **Sin impacto:** inyeccion tinta, laser, termica.
32. **Matricial:** unica que permite papel autocopiativo (calco). 9 o 24 agujas.
33. **Laser:** toner + tambor + fusor. De PAGINAS. Mas rapida y economica por pagina. La mas usada en oficinas.
34. **Inyeccion tinta:** cartuchos CMYK. Buena para fotos.
35. **Termica:** papel termosensible, sin tinta. Tickets TPV.
36. **Bluetooth:** 2,4 GHz, corto alcance.
37. **NIC:** tarjeta de red. **Modem:** MOdulador-DEModulador.
38. **Hardware:** parte FISICA. **Software:** parte LOGICA.
39. **Sistema operativo:** gestiona recursos, intermediario entre usuario y hardware.
40. **ASCII:** codificacion de caracteres, 7 bits = 128 caracteres, extendido 8 bits = 256 caracteres.
