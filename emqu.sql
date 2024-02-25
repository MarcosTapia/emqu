-- phpMyAdmin SQL Dump
-- version 5.0.2
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 25-02-2024 a las 02:50:48
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.2.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `emqu`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `equipos`
--

CREATE TABLE `equipos` (
  `idEquipo` int(11) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `ipv4` varchar(15) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `equipos`
--

INSERT INTO `equipos` (`idEquipo`, `nombre`, `ipv4`) VALUES
(26, 'Google', '8.8.8.8'),
(27, 'localhost', '127.0.0.1'),
(29, 'xbtech', '112.1.43.45'),
(30, 'externo01', '190.17.45.10');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `pruebas_latencia`
--

CREATE TABLE `pruebas_latencia` (
  `idPrueba` int(11) NOT NULL,
  `idEquipo` int(11) NOT NULL,
  `resultado_prueba` varchar(20) NOT NULL,
  `fecha_prueba` datetime NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `pruebas_latencia`
--

INSERT INTO `pruebas_latencia` (`idPrueba`, `idEquipo`, `resultado_prueba`, `fecha_prueba`) VALUES
(1, 26, '0.024946212768554688', '2024-02-24 17:52:30'),
(2, 27, '0.0', '2024-02-24 17:52:30'),
(3, 29, 'None', '2024-02-24 17:52:30'),
(4, 30, 'None', '2024-02-24 17:52:30'),
(5, 26, '0.02491307258605957', '2024-02-24 18:03:26'),
(6, 27, '0.0', '2024-02-24 18:03:26'),
(7, 29, 'None', '2024-02-24 18:03:26'),
(8, 30, 'None', '2024-02-24 18:03:26'),
(9, 26, '0.024962663650512695', '2024-02-24 18:04:17'),
(10, 27, '0.0', '2024-02-24 18:04:17'),
(11, 29, 'None', '2024-02-24 18:04:17'),
(12, 30, 'None', '2024-02-24 18:04:17'),
(13, 26, '0.024932861328125', '2024-02-24 18:07:44'),
(14, 27, '0.000967264175415039', '2024-02-24 18:07:44'),
(15, 29, 'None', '2024-02-24 18:07:44'),
(16, 30, 'None', '2024-02-24 18:07:44'),
(17, 26, '0.024936437606811523', '2024-02-24 18:08:36'),
(18, 27, '0.0', '2024-02-24 18:08:36'),
(19, 29, 'None', '2024-02-24 18:08:36'),
(20, 30, 'None', '2024-02-24 18:08:36'),
(21, 26, '0.024962663650512695', '2024-02-24 18:13:04'),
(22, 27, '0.0', '2024-02-24 18:13:04'),
(23, 29, 'None', '2024-02-24 18:13:04'),
(24, 30, 'None', '2024-02-24 18:13:04'),
(25, 26, '0.024961233139038086', '2024-02-24 18:13:50'),
(26, 27, '0.0', '2024-02-24 18:13:50'),
(27, 29, 'None', '2024-02-24 18:13:50'),
(28, 30, 'None', '2024-02-24 18:13:50'),
(29, 26, '0.024932861328125', '2024-02-24 18:14:28'),
(30, 27, '0.0', '2024-02-24 18:14:28'),
(31, 29, 'None', '2024-02-24 18:14:28'),
(32, 30, 'None', '2024-02-24 18:14:28'),
(33, 26, '0.02496170997619629', '2024-02-24 18:15:14'),
(34, 27, '0.0', '2024-02-24 18:15:14'),
(35, 29, 'None', '2024-02-24 18:15:14'),
(36, 30, 'None', '2024-02-24 18:15:14'),
(37, 26, '0.024970293045043945', '2024-02-24 18:15:53'),
(38, 27, '0.0', '2024-02-24 18:15:53'),
(39, 29, 'None', '2024-02-24 18:15:53'),
(40, 30, 'None', '2024-02-24 18:15:53'),
(41, 26, '0.02496170997619629', '2024-02-24 18:16:51'),
(42, 27, '0.0', '2024-02-24 18:16:51'),
(43, 29, 'None', '2024-02-24 18:16:51'),
(44, 30, 'None', '2024-02-24 18:16:51'),
(45, 26, '0.025929927825927734', '2024-02-24 18:42:47'),
(46, 27, '0.0', '2024-02-24 18:42:47'),
(47, 29, 'None', '2024-02-24 18:42:47'),
(48, 30, 'None', '2024-02-24 18:42:47'),
(49, 26, '0.024934053421020508', '2024-02-24 19:17:12'),
(50, 27, '0.0', '2024-02-24 19:17:12'),
(51, 29, 'None', '2024-02-24 19:17:12'),
(52, 30, 'None', '2024-02-24 19:17:12'),
(53, 26, '0.02592921257019043', '2024-02-24 19:22:11'),
(54, 27, '0.0', '2024-02-24 19:22:11'),
(55, 29, 'None', '2024-02-24 19:22:11'),
(56, 30, 'None', '2024-02-24 19:22:11'),
(57, 26, '0.02496170997619629', '2024-02-24 19:24:55'),
(58, 27, '0.000999689102172851', '2024-02-24 19:24:55'),
(59, 29, 'None', '2024-02-24 19:24:55'),
(60, 30, 'None', '2024-02-24 19:24:55');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `user`
--

CREATE TABLE `user` (
  `id` int(11) NOT NULL,
  `username` varchar(20) NOT NULL,
  `password` varchar(162) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `idAplicacion` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `user`
--

INSERT INTO `user` (`id`, `username`, `password`, `fullname`, `idAplicacion`) VALUES
(1, 'prueba@gmail.com', 'scrypt:32768:8:1$TumVpgcBKHwIGY7e$4d9ffe224c951be169cc12f6e2ff2cf6d89d797c4862b1bc24088ae73ea5b2da5afd0dcb896d517e70c59638a3464092e9b999464068530c1e64c320254c8b54', 'Usuario Prueba', 5);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `equipos`
--
ALTER TABLE `equipos`
  ADD PRIMARY KEY (`idEquipo`);

--
-- Indices de la tabla `pruebas_latencia`
--
ALTER TABLE `pruebas_latencia`
  ADD PRIMARY KEY (`idPrueba`),
  ADD KEY `idEquipo` (`idEquipo`);

--
-- Indices de la tabla `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `equipos`
--
ALTER TABLE `equipos`
  MODIFY `idEquipo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `pruebas_latencia`
--
ALTER TABLE `pruebas_latencia`
  MODIFY `idPrueba` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT de la tabla `user`
--
ALTER TABLE `user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `pruebas_latencia`
--
ALTER TABLE `pruebas_latencia`
  ADD CONSTRAINT `pruebas_latencia_ibfk_1` FOREIGN KEY (`idEquipo`) REFERENCES `equipos` (`idEquipo`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
