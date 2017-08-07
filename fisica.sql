-- phpMyAdmin SQL Dump
-- version 4.4.13.1deb1
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 25-06-2017 a las 15:48:37
-- Versión del servidor: 5.6.31-0ubuntu0.15.10.1
-- Versión de PHP: 5.6.11-1ubuntu3.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `fisica`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ayuda`
--

CREATE TABLE IF NOT EXISTS `ayuda` (
  `id` int(4) unsigned NOT NULL,
  `detalle` text COLLATE utf8_unicode_ci NOT NULL,
  `ejercicio_id` int(4) unsigned NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `campo`
--

CREATE TABLE IF NOT EXISTS `campo` (
  `id` int(4) unsigned NOT NULL,
  `nombre` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `estado` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `campo`
--

INSERT INTO `campo` (`id`, `nombre`, `estado`) VALUES
(1, 'distancia_total', 'i'),
(2, 'distancia_u_A', 'i'),
(3, 'distancia_v_B', 'i'),
(4, 'velocidad_u', 'i'),
(5, 'velocidad_v', 'i'),
(6, 'tiempo', 'r'),
(7, 'min', 'c'),
(8, 'max', 'c'),
(9, 'tiempo_transcurrido', 'i'),
(10, 'distancia_adicional', 'r'),
(11, 'velocidad_auto_u', 'r'),
(12, 'altura_iceberg', 'i'),
(13, 'velocidad_pingui', 'i'),
(14, 'alcance_horizontal', 'r'),
(15, 'altura_colina', 'i'),
(16, 'angulo_elevacion', 'i'),
(17, 'velocidad_auto', 'r'),
(18, 'longitud_cable', 'i'),
(19, 'periodo_pendulo', 'r'),
(20, 'tiempo_caida', 'i'),
(21, 'distancia_recorrida', 'r'),
(22, 'velocidad_inicial', 'i'),
(23, 'altura_helicoptero', 'i'),
(24, 'velocidad_final', 'r'),
(25, 'velocidad_pelota', 'i'),
(26, 'altura_maxima', 'r');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ejercicio`
--

CREATE TABLE IF NOT EXISTS `ejercicio` (
  `id` int(4) unsigned NOT NULL,
  `nivel_id` int(4) unsigned NOT NULL,
  `descripcion` text COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=91 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `ejercicio`
--

INSERT INTO `ejercicio` (`id`, `nivel_id`, `descripcion`) VALUES
(1, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 200 Km de distancia. Juan viaja en su Auto(u) a 30 Km/h  ubicado  a 10 Km de A y Pedro que viaja en su Auto(v) a 45 Km/h ubicado a 22 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?'),
(2, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 500 Km de distancia. Juan viaja en su Auto(u) a 20 Km/h  ubicado  a 15 Km de A y Pedro que viaja en su Auto(v) a 40 Km/h ubicado a 20 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?\r\n'),
(3, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 800 Km de distancia. Juan viaja en su Auto(u) a 40 Km/h  ubicado  a 30 Km de A y Pedro que viaja en su Auto(v) a 23 Km/h ubicado a 10 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?'),
(4, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 450 Km de distancia. Juan viaja en su Auto(u) a 45 Km/h  ubicado  a 15 Km de A y Pedro que viaja en su Auto(v) a 32 Km/h ubicado a 20 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?'),
(5, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 336 Km de distancia. Juan viaja en su Auto(u) a 26 Km/h  ubicado  a 12 Km de A y Pedro que viaja en su Auto(v) a 12 Km/h ubicado a 19 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?'),
(6, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 468 Km de distancia. Juan viaja en su Auto(u) a 34 Km/h  ubicado  a 21 Km de A y Pedro que viaja en su Auto(v) a 52 Km/h ubicado a 8 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?\r\n'),
(7, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 550 Km de distancia. Juan viaja en su Auto(u) a 33 Km/h  ubicado  a 12 Km de A y Pedro que viaja en su Auto(v) a 25 Km/h ubicado a 40 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?'),
(8, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 537 Km de distancia. Juan viaja en su Auto(u) a 42 Km/h  ubicado  a 18 Km de A y Pedro que viaja en su Auto(v) a 23 Km/h ubicado a 5 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?'),
(9, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 420 Km de distancia. Juan viaja en su Auto(u) a 60 Km/h  ubicado  a 17 Km de A y Pedro que viaja en su Auto(v) a 47 Km/h ubicado a 28 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?'),
(10, 1, 'El Colegio(A) y el Parque(B) se encuentran separados por 238 Km de distancia. Juan viaja en su Auto(u) a 43 Km/h  ubicado  a 9 Km de A y Pedro que viaja en su Auto(v) a 38 Km/h ubicado a 32 Km de B.\r\n\r\n¿Cuánto tiempo transcurre para que Juan y Pedro se encuentren?'),
(11, 2, 'Marcos navega en un  barco(u) a 50 km/h que flota a 30 km del Faro(A), Luis navega en un segundo barco(v) a 30 km/h  que flota a 80 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 2,5 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(12, 2, 'Marcos navega en un  barco(u) a 20 km/h que flota a 35 km del Faro(A), Luis navega en un segundo barco(v) a 40 km/h  que flota a 56 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 3 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(13, 2, 'Marcos navega en un  barco(u) a 10 km/h que flota a 15 km del Faro(A), Luis navega en un segundo barco(v) a 32 km/h  que flota a 23 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 0,5 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(14, 2, 'Marcos navega en un  barco(u) a 15 km/h que flota a 22 km del Faro(A), Luis navega en un segundo barco(v) a 28 km/h  que flota a 43 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 1 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(15, 2, 'Marcos navega en un  barco(u) a 47 km/h que flota a 28 km del Faro(A), Luis navega en un segundo barco(v) a 24 km/h  que flota a 34 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 3,7 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(16, 2, 'Marcos navega en un  barco(u) a 12 km/h que flota a 38 km del Faro(A), Luis navega en un segundo barco(v) a 16 km/h  que flota a 50 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 2,8 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(17, 2, 'Marcos navega en un  barco(u) a 23 km/h que flota a 38 km del Faro(A), Luis navega en un segundo barco(v) a 23 km/h  que flota a 41 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 1,5 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(18, 2, 'Marcos navega en un  barco(u) a 53 km/h que flota a 27 km del Faro(A), Luis navega en un segundo barco(v) a 23 km/h  que flota a 19 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 0,8 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(19, 2, 'Marcos navega en un  barco(u) a 80 km/h que flota a 9 km del Faro(A), Luis navega en un segundo barco(v) a 16 km/h  que flota a 2 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 4,2 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(20, 2, 'Marcos navega en un  barco(u) a 17 km/h que flota a 60 km del Faro(A), Luis navega en un segundo barco(v) a 31 km/h  que flota a 28 km de la Playa(B). Si Marcos y Luis se encuentran transcurridas 0,9 h. \r\n\r\n¿Qué distancia adicional debe navegar Luis para llegar al Faro?'),
(21, 3, 'Sergio maneja su tractor(v) a una velocidad de 50 km/h se encuentra a 10 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 30 km del Molino(A), se cruza con Sergio transcurridas 1,5 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 200 km?'),
(22, 3, 'Sergio maneja su tractor(v) a una velocidad de 20 km/h se encuentra a 15 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 32 km del Molino(A), se cruza con Sergio transcurridas 1 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 500 km?'),
(23, 3, 'Sergio maneja su tractor(v) a una velocidad de 23 km/h se encuentra a 20 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 25 km del Molino(A), se cruza con Sergio transcurridas 2 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 800 km?'),
(24, 3, 'Sergio maneja su tractor(v) a una velocidad de 32 km/h se encuentra a 17 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 22 km del Molino(A), se cruza con Sergio transcurridas 1,8 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 290 km?'),
(25, 3, 'Sergio maneja su tractor(v) a una velocidad de 40 km/h se encuentra a 19 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 35 km del Molino(A), se cruza con Sergio transcurridas 2,3 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 320 km?'),
(26, 3, 'Sergio maneja su tractor(v) a una velocidad de 14 km/h se encuentra a 37 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 14 km del Molino(A), se cruza con Sergio transcurridas 1,6 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 380 km?'),
(27, 3, 'Sergio maneja su tractor(v) a una velocidad de 35 km/h se encuentra a 9 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 5 km del Molino(A), se cruza con Sergio transcurridas 2,2 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 600 km??'),
(28, 3, 'Sergio maneja su tractor(v) a una velocidad de 19 km/h se encuentra a 29 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 39 km del Molino(A), se cruza con Sergio transcurridas 3,4 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 720 km?'),
(29, 3, 'Sergio maneja su tractor(v) a una velocidad de 34 km/h se encuentra a 2 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 17 km del Molino(A), se cruza con Sergio transcurridas 2,8 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 615 km?'),
(30, 3, 'Sergio maneja su tractor(v) a una velocidad de 47 km/h se encuentra a 42 km del Granero(B); Pablo maneja otro tractor(u) que se encuentra a 26 km del Molino(A), se cruza con Sergio transcurridas 1,2 h. \r\n\r\n¿A qué velocidad viaja Pablo si la distancia total entre molino y el granero es de 629 km?'),
(31, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 47,2 m de altura, el pingüino se lanza horizontalmente con una velocidad de 1,2 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(32, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 24 m de altura, el pingüino se lanza horizontalmente con una velocidad de 2,2 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(33, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 7 m de altura, el pingüino se lanza horizontalmente con una velocidad de 3,9 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(34, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 28,8 m de altura, el pingüino se lanza horizontalmente con una velocidad de 10 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(35, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 15,2 m de altura, el pingüino se lanza horizontalmente con una velocidad de 9,5 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(36, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 26 m de altura, el pingüino se lanza horizontalmente con una velocidad de 22 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú. '),
(37, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 3,7 m de altura, el pingüino se lanza horizontalmente con una velocidad de 19,3 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(38, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg (Bloque de Hielo) de 33 metros de altura, el pingüino se lanza horizontalmente con una velocidad de 24,6 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(39, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 18,3 m de altura, el pingüino se lanza horizontalmente con una velocidad de 13 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(40, 4, 'Un pingüino es perseguido por un león marino, al llegar a la orilla de un iceberg(Bloque de Hielo) de 5,5 m de altura, el pingüino se lanza horizontalmente con una velocidad de 37,2 km/h.\r\n\r\n¿Cuál es el alcance horizontal del pingüino al saltar? Ayúdalo a estar a salvo en su iglú.'),
(41, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 20 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 30°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(42, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 53 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 40°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(43, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 38 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 25°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(44, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 27 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 12°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(45, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 13 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 15°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(46, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 23 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 32°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(47, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 35 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 22°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(48, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 24 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 19°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(49, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 23,2 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 39°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(50, 5, 'Francisco participa en un duelo de camionetas monster, uno de los retos es saltar un abismo de 37,5 Metros de alto, al cruzar por un montículo de piedra sale con una elevación de 42°.\r\n\r\n¿Qué velocidad debe generar la camioneta para saltar el precipicio?'),
(51, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 10 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(52, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 27 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(53, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 17.9 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(54, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 42.4 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(55, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 18.3 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(56, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 33.12 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(57, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 29.5 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(58, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 31.01 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(59, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 9.19 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(60, 6, 'Una bola de demolición esta suspendida de una grúa por un cable de 11.7 Metros de longitud.\r\n\r\n¿Cuál es el periodo del péndulo de demolición; es decir, el tiempo que gasta la bola de demolición en ir de un punto de inicio A hasta el punto B (Edificio) y regresar nuevamente al punto A? '),
(61, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 7 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo?'),
(62, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 5 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo?'),
(63, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 2 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo? '),
(64, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 3,6 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo?  '),
(65, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 4,4 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo? '),
(66, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 1,19 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo?'),
(67, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 0,72 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo? '),
(68, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 3 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo?'),
(69, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 2,23 Segundos después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo? '),
(70, 7, 'Una manzana cae desde un árbol golpeando en la cabeza a Samuel que se encontraba recostado sobre el manzano, toca el suelo 6,38 después de la caída.\r\n\r\n¿Cuál es la distancia que ha recorrido la manzana hasta llegar al suelo?'),
(71, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 2,3 m/s, desde un helicóptero suspendido en el aire a 6708 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(72, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 5 m/s, desde un helicóptero suspendido en el aire a 9000 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(73, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 3,8 m/s, desde un helicóptero suspendido en el aire a 7500 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(74, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 1,77 m/s, desde un helicóptero suspendido en el aire a 5719 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(75, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 4,2 m/s, desde un helicóptero suspendido en el aire a 8898 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(76, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 2,51 m/s, desde un helicóptero suspendido en el aire a 6216 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(77, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 3,9 m/s, desde un helicóptero suspendido en el aire a 4972 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(78, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 5,12 m/s, desde un helicóptero suspendido en el aire a 9300 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(79, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 2,2 m/s, desde un helicóptero suspendido en el aire a 10000 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(80, 8, 'Un paracaidista se lanza al vació con una velocidad inicial de 4,24 m/s, desde un helicóptero suspendido en el aire a 15500 m.\r\n\r\n¿Qué velocidad posee el paracaidista al llegar a tierra?  '),
(81, 9, 'Amanda esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad de 15 m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(82, 9, 'Helena esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad de 9 m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(83, 9, 'Gabriela esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad 22 de m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(84, 9, 'Isabel esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad 19 de m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(85, 9, 'Ingrid esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad de 28 m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(86, 9, 'Carolina esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad 10 de m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(87, 9, 'Tania esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad de 7 m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(88, 9, 'Lucia esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad 25 de m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(89, 9, 'María esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad de 16 m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?'),
(90, 9, 'Mónica esta de vacaciones en la playa jugando con su pelota, la arroja hacia arriba con una velocidad de 30 m/s.\r\n\r\n¿Cuál es la altura máxima que alcanza la pelota?');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `nivel`
--

CREATE TABLE IF NOT EXISTS `nivel` (
  `id` int(4) unsigned NOT NULL,
  `nombre` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
  `dificultad` varchar(20) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `nivel`
--

INSERT INTO `nivel` (`id`, `nombre`, `dificultad`) VALUES
(1, 'Movimiento Rectilineo Uniforme Ejercicio 1', 'Baja'),
(2, 'Movimiento Rectilineo Uniforme Ejercicio 2', 'Media'),
(3, 'Movimiento Rectilineo Uniforme Ejercicio 3', 'Alta'),
(4, 'Movimiento Semi Parabolico Ejercicio 1', 'Baja'),
(5, 'Movimiento Parabolico Ejercicio 2', 'Media'),
(6, 'Movimiento Pendular Ejercicio 3', 'Alta'),
(7, 'Caida Libre Ejercicio 1', 'Baja'),
(8, 'Caida Libre Ejercicio 2', 'Media'),
(9, 'Lanzamiento Vertical Ejercicio 3', 'Alta');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `operando`
--

CREATE TABLE IF NOT EXISTS `operando` (
  `id` int(4) unsigned NOT NULL,
  `numeros` double NOT NULL,
  `ejercicio_id` int(4) unsigned NOT NULL,
  `campo_id` int(4) unsigned NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=523 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `operando`
--

INSERT INTO `operando` (`id`, `numeros`, `ejercicio_id`, `campo_id`) VALUES
(1, 200000, 1, 1),
(2, 10000, 1, 2),
(3, 22000, 1, 3),
(4, 8.33, 1, 4),
(5, 12.5, 1, 5),
(6, 8065.29, 1, 6),
(7, 500000, 2, 1),
(8, 15000, 2, 2),
(9, 20000, 2, 3),
(10, 5.55, 2, 4),
(11, 11.11, 2, 5),
(12, 27911.16, 2, 6),
(13, 800000, 3, 1),
(14, 30000, 3, 2),
(15, 10000, 3, 3),
(16, 11.11, 3, 4),
(17, 6.38, 3, 5),
(18, 43453.4, 3, 6),
(19, 1, 1, 7),
(20, 4, 1, 8),
(21, 2, 2, 7),
(22, 8, 2, 8),
(23, 11, 3, 7),
(24, 18, 3, 8),
(25, 450000, 4, 1),
(26, 15000, 4, 2),
(27, 20000, 4, 3),
(28, 12.5, 4, 4),
(29, 8.88, 4, 5),
(30, 19410.66, 4, 6),
(31, 3, 4, 7),
(32, 11, 4, 8),
(33, 550000, 7, 1),
(34, 12000, 7, 2),
(35, 40000, 7, 3),
(36, 9.16, 7, 4),
(37, 6.94, 7, 5),
(38, 30931.67, 7, 6),
(39, 6, 7, 7),
(40, 10, 7, 8),
(41, 537000, 8, 1),
(42, 18000, 8, 2),
(43, 5000, 8, 3),
(44, 11.66, 8, 4),
(45, 6.38, 8, 5),
(46, 28492.23, 8, 6),
(47, 2, 8, 7),
(48, 8, 8, 8),
(49, 336000, 5, 1),
(50, 12000, 5, 2),
(51, 12000, 5, 3),
(52, 7.22, 5, 4),
(53, 5.27, 5, 5),
(54, 24979.98, 5, 6),
(55, 6, 5, 7),
(56, 9, 5, 8),
(57, 468000, 6, 1),
(58, 21000, 6, 2),
(59, 8000, 6, 3),
(60, 9.44, 6, 4),
(61, 14.44, 6, 5),
(62, 18383.58, 6, 6),
(63, 3, 6, 7),
(64, 10, 6, 8),
(65, 420000, 9, 1),
(66, 17000, 9, 2),
(67, 28000, 9, 3),
(68, 16.66, 9, 4),
(69, 13.05, 9, 5),
(70, 12622.01, 9, 6),
(71, 1, 9, 7),
(72, 5, 9, 8),
(73, 238000, 10, 1),
(74, 9000, 10, 2),
(75, 32000, 10, 3),
(76, 11.94, 10, 4),
(77, 10.55, 10, 5),
(78, 8759.44, 10, 6),
(79, 1, 10, 7),
(80, 6, 10, 8),
(81, 30000, 11, 2),
(82, 80000, 11, 3),
(83, 13.88, 11, 4),
(84, 8.33, 11, 5),
(85, 9000, 11, 9),
(86, 154920, 11, 10),
(87, 150, 11, 7),
(88, 161, 11, 8),
(89, 35000, 12, 2),
(90, 56000, 12, 3),
(91, 5.55, 12, 4),
(92, 11.11, 12, 5),
(93, 10800, 12, 9),
(94, 94940, 12, 10),
(95, 90, 12, 7),
(96, 96, 12, 8),
(97, 15000, 13, 2),
(98, 23000, 13, 3),
(99, 2.77, 13, 4),
(100, 8.88, 13, 5),
(101, 1800, 13, 9),
(102, 19986, 13, 10),
(103, 10, 13, 7),
(104, 29, 13, 8),
(105, 22000, 14, 2),
(106, 43000, 14, 3),
(107, 4.16, 14, 4),
(108, 7.77, 14, 5),
(109, 3600, 14, 9),
(110, 36976, 14, 10),
(111, 30, 14, 7),
(112, 38, 14, 8),
(113, 28000, 15, 2),
(114, 34000, 15, 3),
(115, 13.05, 15, 4),
(116, 6.66, 15, 5),
(117, 13320, 15, 9),
(118, 201826, 15, 10),
(119, 193, 15, 7),
(120, 205, 15, 8),
(121, 38000, 16, 2),
(122, 50000, 16, 3),
(123, 3.33, 16, 4),
(124, 4.44, 16, 5),
(125, 10080, 16, 9),
(126, 71566.4, 16, 10),
(127, 69, 16, 7),
(128, 80, 16, 8),
(129, 38000, 17, 2),
(130, 41000, 17, 3),
(131, 6.38, 17, 4),
(132, 6.38, 17, 5),
(133, 5400, 17, 9),
(134, 72452, 17, 10),
(135, 69, 17, 7),
(136, 80, 17, 8),
(137, 27000, 18, 2),
(138, 19000, 18, 3),
(139, 14.72, 18, 4),
(140, 6.38, 18, 5),
(141, 2880, 18, 9),
(142, 69393.6, 18, 10),
(143, 63, 18, 7),
(144, 77, 18, 8),
(145, 9000, 19, 2),
(146, 2000, 19, 3),
(147, 22.22, 19, 4),
(148, 4.44, 19, 5),
(149, 15120, 19, 9),
(150, 344966.4, 19, 10),
(151, 340, 19, 7),
(152, 350, 19, 8),
(153, 60000, 20, 2),
(154, 28000, 20, 3),
(155, 4.72, 20, 4),
(156, 8.61, 20, 5),
(157, 3240, 20, 9),
(158, 75292.8, 20, 10),
(159, 67, 20, 7),
(160, 81, 20, 8),
(161, 200000, 21, 1),
(162, 10000, 21, 3),
(163, 30000, 21, 2),
(164, 13.88, 21, 5),
(165, 5400, 21, 9),
(166, 15.74, 21, 11),
(167, 500000, 22, 1),
(168, 15000, 22, 3),
(169, 32000, 22, 2),
(170, 5.55, 22, 5),
(171, 3600, 22, 9),
(172, 120.28, 22, 11),
(173, 430, 22, 7),
(174, 437, 22, 8),
(175, 50, 21, 7),
(176, 58, 21, 8),
(177, 800000, 23, 1),
(178, 20000, 23, 3),
(179, 25000, 23, 2),
(180, 6.38, 23, 5),
(181, 7200, 23, 9),
(182, 98.48, 23, 11),
(183, 353, 23, 7),
(184, 359, 23, 8),
(185, 290000, 24, 1),
(186, 17000, 24, 3),
(187, 22000, 24, 2),
(188, 8.88, 24, 5),
(189, 6480, 24, 9),
(190, 29.85, 24, 11),
(191, 100, 24, 7),
(192, 107, 24, 8),
(193, 320000, 25, 1),
(194, 19000, 25, 3),
(195, 35000, 25, 2),
(196, 11.11, 25, 5),
(197, 8280, 25, 9),
(198, 21.01, 25, 11),
(199, 72, 25, 7),
(200, 80, 25, 8),
(203, 380000, 26, 1),
(204, 37000, 26, 3),
(205, 14000, 26, 2),
(206, 3.88, 26, 5),
(207, 5760, 26, 9),
(208, 53.23, 26, 11),
(209, 184, 26, 7),
(210, 198, 26, 8),
(211, 600000, 27, 1),
(212, 9000, 27, 3),
(213, 5000, 27, 2),
(214, 9.72, 27, 5),
(215, 7920, 27, 9),
(216, 64.26, 27, 11),
(217, 230, 27, 7),
(218, 236, 27, 8),
(221, 720000, 28, 1),
(222, 29000, 28, 3),
(223, 39000, 28, 2),
(224, 5.27, 28, 5),
(225, 12240, 28, 9),
(226, 47.99, 28, 11),
(227, 169, 28, 7),
(228, 180, 28, 8),
(229, 615000, 29, 1),
(230, 2000, 29, 3),
(231, 17000, 29, 2),
(232, 9.44, 29, 5),
(233, 10080, 29, 9),
(234, 49.68, 29, 11),
(235, 170, 29, 7),
(236, 180, 29, 8),
(237, 629000, 30, 1),
(238, 42000, 30, 3),
(239, 26000, 30, 2),
(240, 13.05, 30, 5),
(241, 4320, 30, 9),
(242, 116.81, 30, 11),
(243, 415, 30, 7),
(244, 429, 30, 8),
(245, 47.2, 31, 12),
(246, 0.33, 31, 13),
(247, 1.02, 31, 14),
(248, 1, 31, 7),
(249, 9, 31, 8),
(250, 24, 32, 12),
(251, 0.61, 32, 13),
(252, 1.34, 32, 14),
(253, 0.5, 32, 7),
(254, 3, 32, 8),
(255, 7, 33, 12),
(256, 1.08, 33, 13),
(257, 1.28, 33, 14),
(258, 1, 33, 7),
(259, 7, 33, 8),
(260, 28.8, 34, 12),
(261, 2.77, 34, 13),
(262, 6.7, 34, 14),
(263, 4, 34, 7),
(264, 10, 34, 8),
(265, 15.2, 35, 12),
(266, 2.63, 35, 13),
(267, 4.62, 35, 14),
(268, 2, 35, 7),
(269, 7, 35, 8),
(270, 26, 36, 12),
(271, 6.11, 36, 13),
(272, 14.05, 36, 14),
(273, 9, 36, 7),
(274, 16, 36, 8),
(275, 3.7, 37, 12),
(276, 5.36, 37, 13),
(277, 4.6, 37, 14),
(278, 2, 37, 7),
(279, 8, 37, 8),
(280, 33, 38, 12),
(281, 6.83, 38, 13),
(282, 17.68, 38, 14),
(283, 11, 38, 7),
(284, 20, 38, 8),
(285, 18.3, 39, 12),
(286, 3.61, 39, 13),
(287, 6.96, 39, 14),
(288, 3, 39, 7),
(289, 10, 39, 8),
(290, 5.5, 40, 12),
(291, 10.33, 40, 13),
(292, 10.84, 40, 14),
(293, 4, 40, 7),
(294, 12, 40, 8),
(295, 20, 41, 15),
(296, 30, 41, 16),
(297, 196, 41, 17),
(298, 190, 41, 7),
(299, 200, 41, 8),
(300, 53, 42, 15),
(301, 40, 42, 16),
(302, 405.78, 42, 17),
(303, 400, 42, 7),
(304, 408, 42, 8),
(305, 38, 43, 15),
(306, 25, 43, 16),
(307, 443.33, 43, 17),
(308, 440, 43, 7),
(309, 446, 43, 8),
(310, 27, 44, 15),
(311, 12, 44, 16),
(312, 661.5, 44, 17),
(313, 660, 44, 7),
(314, 669, 44, 8),
(315, 13, 45, 15),
(316, 15, 45, 16),
(317, 254.8, 45, 17),
(318, 250, 45, 7),
(319, 260, 45, 8),
(320, 23, 46, 15),
(321, 32, 46, 16),
(322, 216.73, 46, 17),
(323, 210, 46, 7),
(324, 220, 46, 8),
(325, 35, 47, 15),
(326, 22, 47, 16),
(327, 463.51, 47, 17),
(328, 460, 47, 7),
(329, 469, 47, 8),
(330, 24, 48, 15),
(331, 19, 48, 16),
(332, 367.5, 48, 17),
(333, 360, 48, 7),
(334, 370, 48, 8),
(335, 23.2, 49, 15),
(336, 39, 49, 16),
(337, 183.35, 49, 17),
(338, 176, 49, 7),
(339, 185, 49, 8),
(340, 37.5, 50, 15),
(341, 42, 50, 16),
(342, 278.4, 50, 17),
(343, 270, 50, 7),
(344, 280, 50, 8),
(345, 10, 51, 18),
(346, 6.28, 51, 19),
(347, 3, 51, 7),
(348, 10, 51, 8),
(349, 27, 52, 18),
(350, 10.36, 52, 19),
(351, 5, 52, 7),
(352, 16, 52, 8),
(353, 17.9, 53, 18),
(354, 8.41, 53, 19),
(355, 2, 53, 7),
(356, 10, 53, 8),
(357, 42.4, 54, 18),
(358, 12.99, 54, 19),
(359, 6, 54, 7),
(360, 15, 54, 8),
(361, 18.3, 55, 18),
(362, 8.56, 55, 19),
(363, 2, 55, 7),
(364, 10, 55, 8),
(365, 33.12, 56, 18),
(366, 11.49, 56, 19),
(367, 5, 56, 7),
(368, 13, 56, 8),
(369, 29.5, 57, 18),
(370, 10.86, 57, 19),
(371, 7, 57, 7),
(372, 13, 57, 8),
(381, 31.01, 58, 18),
(382, 11.11, 58, 19),
(383, 3, 58, 7),
(384, 13, 58, 8),
(385, 9.19, 59, 18),
(386, 6.02, 59, 19),
(387, 5, 59, 7),
(388, 12, 59, 8),
(389, 11.7, 60, 18),
(390, 6.84, 60, 19),
(391, 1, 60, 7),
(392, 8, 60, 8),
(393, 7, 61, 20),
(394, 240.1, 61, 21),
(395, 235, 61, 7),
(396, 245, 61, 8),
(397, 5, 62, 20),
(398, 122.5, 62, 21),
(399, 120, 62, 7),
(400, 130, 62, 8),
(401, 2, 63, 20),
(402, 19.6, 63, 21),
(403, 15, 63, 7),
(404, 25, 63, 8),
(405, 3.6, 64, 20),
(406, 63.5, 64, 21),
(407, 60, 64, 7),
(408, 70, 64, 8),
(409, 4.4, 65, 20),
(410, 94.86, 65, 21),
(411, 89, 65, 7),
(412, 99, 65, 8),
(413, 1.19, 66, 20),
(414, 6.9, 66, 21),
(415, 1, 66, 7),
(416, 10, 66, 8),
(417, 0.72, 67, 20),
(418, 2.49, 67, 21),
(419, 1, 67, 7),
(420, 10, 67, 8),
(421, 3, 68, 20),
(422, 44.1, 68, 21),
(423, 40, 68, 7),
(424, 50, 68, 8),
(425, 2.23, 69, 20),
(426, 24.35, 69, 21),
(427, 20, 69, 7),
(428, 30, 69, 8),
(429, 6.38, 70, 20),
(430, 199.43, 70, 21),
(431, 195, 70, 7),
(432, 205, 70, 8),
(433, 2.3, 71, 22),
(434, 6708, 71, 23),
(435, 362.6, 71, 24),
(436, 360, 71, 7),
(437, 370, 71, 8),
(438, 5, 72, 22),
(439, 9000, 72, 23),
(440, 420.02, 72, 24),
(441, 415, 72, 7),
(442, 425, 72, 8),
(443, 3.8, 73, 22),
(444, 7500, 73, 23),
(445, 383.42, 73, 24),
(446, 380, 73, 7),
(447, 390, 73, 8),
(448, 1.77, 74, 22),
(449, 5719, 74, 23),
(450, 334.8, 74, 24),
(451, 330, 74, 7),
(452, 340, 74, 8),
(453, 4.2, 75, 22),
(454, 8898, 75, 23),
(455, 417.63, 75, 24),
(456, 410, 75, 7),
(457, 420, 75, 8),
(458, 2.51, 76, 22),
(459, 6216, 76, 23),
(460, 349.05, 76, 24),
(461, 345, 76, 7),
(462, 355, 76, 8),
(463, 3.9, 77, 22),
(464, 4972, 77, 23),
(465, 312.19, 77, 24),
(466, 310, 77, 7),
(467, 320, 77, 8),
(468, 5.12, 78, 22),
(469, 9300, 78, 23),
(470, 426.97, 78, 24),
(471, 420, 78, 7),
(472, 430, 78, 8),
(473, 2.2, 79, 22),
(474, 10000, 79, 23),
(475, 442.72, 79, 24),
(476, 440, 79, 7),
(477, 450, 79, 8),
(478, 4.24, 80, 22),
(479, 15500, 80, 23),
(480, 551.19, 80, 24),
(481, 545, 80, 7),
(482, 555, 80, 8),
(483, 15, 81, 25),
(484, 11.49, 81, 26),
(485, 10, 81, 7),
(486, 20, 81, 8),
(487, 9, 82, 25),
(488, 4.18, 82, 26),
(489, 1, 82, 7),
(490, 10, 82, 8),
(491, 22, 83, 25),
(492, 24.74, 83, 26),
(493, 20, 83, 7),
(494, 30, 83, 8),
(495, 19, 84, 25),
(496, 18.45, 84, 26),
(497, 10, 84, 7),
(498, 20, 84, 8),
(499, 28, 85, 25),
(500, 40.02, 85, 26),
(501, 35, 85, 7),
(502, 45, 85, 8),
(503, 10, 86, 25),
(504, 5.11, 86, 26),
(505, 1, 86, 7),
(506, 10, 86, 8),
(507, 7, 87, 25),
(508, 2.52, 87, 26),
(509, 1, 87, 7),
(510, 10, 87, 8),
(511, 25, 88, 25),
(512, 31.9, 88, 26),
(513, 25, 88, 7),
(514, 35, 88, 8),
(515, 16, 89, 25),
(516, 13.1, 89, 26),
(517, 10, 89, 7),
(518, 20, 89, 8),
(519, 30, 90, 25),
(520, 45.94, 90, 26),
(521, 40, 90, 7),
(522, 50, 90, 8);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `resultado`
--

CREATE TABLE IF NOT EXISTS `resultado` (
  `id` int(4) unsigned NOT NULL,
  `puntos` int(4) unsigned NOT NULL,
  `usuario_id` int(4) unsigned NOT NULL,
  `ejercicio_id` int(4) unsigned NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE IF NOT EXISTS `rol` (
  `id` int(4) unsigned NOT NULL,
  `tipo` varchar(30) COLLATE utf8_unicode_ci NOT NULL,
  `permiso` varchar(40) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `tipo`, `permiso`) VALUES
(1, 'ESTUDIANTE', 'USE'),
(2, 'PROFESOR', 'ALL');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuario`
--

CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(4) unsigned NOT NULL,
  `nombre` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `apellido` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `correo` varchar(40) COLLATE utf8_unicode_ci NOT NULL,
  `clave` varchar(255) COLLATE utf8_unicode_ci NOT NULL,
  `rol_id` int(4) unsigned NOT NULL,
  `grado` char(15) COLLATE utf8_unicode_ci NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

--
-- Volcado de datos para la tabla `usuario`
--

INSERT INTO `usuario` (`id`, `nombre`, `apellido`, `correo`, `clave`, `rol_id`, `grado`) VALUES
(1, 'po', 'popo', 'popopo@po.po', '3627909a29c3138', 2, '3'),
(2, 'qw', 'qw', 'qw', '51b40bbbfb88261ed6b616025a7c15a61f282d58614e6a216156b770250fee51206924989671299d8a0cadd476a1e8e465066ff2451a589360e940a3709cf40e', 1, 'qw'),
(3, 'Ivette Carolina', 'Vargas Castillo', '1', '4dff4ea340f0a823f15d3f4f01ab62eae0e5da579ccb851f8db9dfe84c58b2b37b89903a740e1ee172da793a6e79d560e5f7f9bd058a12a280433ed6fa46510a', 2, '1'),
(4, 's', 's', 's', '2c1ee68372215b1ce064426b5cdbd4ef2581ace0dd3b21fa2be27f364827242e83f68b68be03f5b3e24be5d1b4315f98a0a96d19713fb3a19dc455fb6adc3431', 2, 'ssss'),
(5, 'carolina', 'vargas', 'vargas19carolina@gmail.com', '3627909a29c31381a071ec27f7c9ca97726182aed29a7ddd2e54353322cfb30abb9e3a6df2ac2c20fe23436311d678564d0c8d305930575f60e2d3d048184d79', 2, '11');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `ayuda`
--
ALTER TABLE `ayuda`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ejercicio_id` (`ejercicio_id`),
  ADD KEY `ejercicio_id_2` (`ejercicio_id`);

--
-- Indices de la tabla `campo`
--
ALTER TABLE `campo`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ejercicio`
--
ALTER TABLE `ejercicio`
  ADD PRIMARY KEY (`id`),
  ADD KEY `nivel_id` (`nivel_id`);

--
-- Indices de la tabla `nivel`
--
ALTER TABLE `nivel`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `operando`
--
ALTER TABLE `operando`
  ADD PRIMARY KEY (`id`),
  ADD KEY `campo_id` (`campo_id`),
  ADD KEY `campo_id_2` (`campo_id`),
  ADD KEY `ejercicio_id` (`ejercicio_id`);

--
-- Indices de la tabla `resultado`
--
ALTER TABLE `resultado`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ejercicio_id` (`ejercicio_id`),
  ADD KEY `ejercicio_id_2` (`ejercicio_id`),
  ADD KEY `usuario_id` (`usuario_id`),
  ADD KEY `ejercicio_id_3` (`ejercicio_id`),
  ADD KEY `usuario_id_2` (`usuario_id`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD PRIMARY KEY (`id`),
  ADD KEY `rol_id` (`rol_id`),
  ADD KEY `rol_id_2` (`rol_id`),
  ADD KEY `rol_id_3` (`rol_id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `ayuda`
--
ALTER TABLE `ayuda`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `campo`
--
ALTER TABLE `campo`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=27;
--
-- AUTO_INCREMENT de la tabla `ejercicio`
--
ALTER TABLE `ejercicio`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=91;
--
-- AUTO_INCREMENT de la tabla `nivel`
--
ALTER TABLE `nivel`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=10;
--
-- AUTO_INCREMENT de la tabla `operando`
--
ALTER TABLE `operando`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=523;
--
-- AUTO_INCREMENT de la tabla `resultado`
--
ALTER TABLE `resultado`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=3;
--
-- AUTO_INCREMENT de la tabla `usuario`
--
ALTER TABLE `usuario`
  MODIFY `id` int(4) unsigned NOT NULL AUTO_INCREMENT,AUTO_INCREMENT=6;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `ayuda`
--
ALTER TABLE `ayuda`
  ADD CONSTRAINT `ayuda_ibfk_1` FOREIGN KEY (`ejercicio_id`) REFERENCES `ejercicio` (`id`);

--
-- Filtros para la tabla `ejercicio`
--
ALTER TABLE `ejercicio`
  ADD CONSTRAINT `ejercicio_ibfk_1` FOREIGN KEY (`nivel_id`) REFERENCES `nivel` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `operando`
--
ALTER TABLE `operando`
  ADD CONSTRAINT `operando_ibfk_1` FOREIGN KEY (`campo_id`) REFERENCES `campo` (`id`),
  ADD CONSTRAINT `operando_ibfk_2` FOREIGN KEY (`ejercicio_id`) REFERENCES `ejercicio` (`id`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Filtros para la tabla `resultado`
--
ALTER TABLE `resultado`
  ADD CONSTRAINT `resultado_ibfk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`),
  ADD CONSTRAINT `resultado_ibfk_2` FOREIGN KEY (`ejercicio_id`) REFERENCES `ejercicio` (`id`);

--
-- Filtros para la tabla `usuario`
--
ALTER TABLE `usuario`
  ADD CONSTRAINT `usuario_ibfk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
