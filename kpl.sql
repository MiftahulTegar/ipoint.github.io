-- phpMyAdmin SQL Dump
-- version 5.1.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Waktu pembuatan: 03 Jan 2022 pada 01.58
-- Versi server: 10.4.18-MariaDB
-- Versi PHP: 8.0.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `kpl`
--

-- --------------------------------------------------------

--
-- Struktur dari tabel `forum`
--

CREATE TABLE `forum` (
  `id` int(20) NOT NULL,
  `judul_forum` varchar(100) NOT NULL,
  `id_user` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `forum`
--

INSERT INTO `forum` (`id`, `judul_forum`, `id_user`) VALUES
(20, 'Analisis Desain Software 2', 5),
(21, 'Diskusi 1', 4),
(22, 'Diskusi 2', 1),
(23, 'Diskusi 3', 3),
(24, 'Praktikum Aplikasi Komputer', 7),
(25, 'Komunikasi Interpersonal', 6);

-- --------------------------------------------------------

--
-- Struktur dari tabel `mengirim_pesan`
--

CREATE TABLE `mengirim_pesan` (
  `id` int(20) NOT NULL,
  `isi_pesan` varchar(100) NOT NULL,
  `id_forum` int(20) NOT NULL,
  `id_user` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `mengirim_pesan`
--

INSERT INTO `mengirim_pesan` (`id`, `isi_pesan`, `id_forum`, `id_user`) VALUES
(69, 'Contoh pesan berhasil', 20, 5);

-- --------------------------------------------------------

--
-- Struktur dari tabel `modul`
--

CREATE TABLE `modul` (
  `id` int(20) NOT NULL,
  `judul` varchar(100) NOT NULL,
  `file` varchar(100) NOT NULL,
  `id_forum` int(20) NOT NULL,
  `id_user` int(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `modul`
--

INSERT INTO `modul` (`id`, `judul`, `file`, `id_forum`, `id_user`) VALUES
(32, 'Contoh Modul', 'Komunikasi Interpersonal.pptx', 20, 5);

-- --------------------------------------------------------

--
-- Struktur dari tabel `user`
--

CREATE TABLE `user` (
  `id` int(20) NOT NULL,
  `nama` varchar(100) NOT NULL,
  `jabatan` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `telp` varchar(100) NOT NULL,
  `alamat` varchar(100) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data untuk tabel `user`
--

INSERT INTO `user` (`id`, `nama`, `jabatan`, `email`, `telp`, `alamat`, `username`, `password`) VALUES
(1, 'Miftahul Tegar Pangestu ', 'Mahasiswa', 'tegarmiftahul2@gmail.com', '085728669512', 'Purworejo, Jawa Tengah, Indonesia', 'Tegar', '$5$rounds=535000$e0weeXrHIW27VFXf$tCXOfB1TqQflxWa/lMtPOx9U6cm7gk82rOGf4AwEFlD'),
(3, 'Pipit Ayu Fitria ', 'Mahasiswa', 'pipit@gmail.com', '081222333444', 'Sleman, Yogyakarta, Indonesia', 'pipit', '$5$rounds=535000$3afbZa62fMskqqNn$jTYFdsOFKm5bxGFs4VqUHBwR5KB/b1cPqjyCLcuW6YD'),
(4, 'Tri Kurniawan', 'Mahasiswa', 'tri@gmail.com', '089222333444', 'Bantul, Yogyakarta, Indonesia', 'tri', '$5$rounds=535000$dk2bsxHYK37Ht9VV$nKrO7IJM24cv7f0sykkqmU6mvaIl42oru6CK6bZQK47'),
(5, 'Retno Widowati PA., M.Si., Ph.D', 'Dosen', 'retno@gmail.com', '088222333444', 'Surabaya, Jawa Timur, Indonesia', 'retno', '$5$rounds=535000$T0fcTRS8or2/ocX7$rXCmbnJeC9OUUbmSDWsUQyIAMOMMUnnqCrnHd08UlDD'),
(6, 'Taufik Akhbar, SE., MBA.', 'Dosen', 'taufik@gmail.com', '087222333444', 'Magelang, Jawa Tengah, Indonesia', 'taufik', '$5$rounds=535000$uYfD7RygHdfv270z$zkW/WT8nOQYjfkgYiZy8WCIXhzUBVatier5IdEXuze3'),
(7, 'Ade Hikmah Nur Rizki A.Md.Farm', 'Dosen', 'adehikmah20@gmail.com', '08123456789', 'Bandung, Jawa Barat, Indonesia', 'ade', '$5$rounds=535000$JOZoW/buCiS2FcR6$ixBxmOMJXiabf72YGbrfKBtiFP9zoKmVpU3noNtSwm4');

--
-- Indexes for dumped tables
--

--
-- Indeks untuk tabel `forum`
--
ALTER TABLE `forum`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_user` (`id_user`);

--
-- Indeks untuk tabel `mengirim_pesan`
--
ALTER TABLE `mengirim_pesan`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_forum` (`id_forum`),
  ADD KEY `id_dosen` (`id_user`);

--
-- Indeks untuk tabel `modul`
--
ALTER TABLE `modul`
  ADD PRIMARY KEY (`id`),
  ADD KEY `id_forum` (`id_forum`),
  ADD KEY `id_dosen` (`id_user`);

--
-- Indeks untuk tabel `user`
--
ALTER TABLE `user`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT untuk tabel yang dibuang
--

--
-- AUTO_INCREMENT untuk tabel `forum`
--
ALTER TABLE `forum`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=30;

--
-- AUTO_INCREMENT untuk tabel `mengirim_pesan`
--
ALTER TABLE `mengirim_pesan`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT untuk tabel `modul`
--
ALTER TABLE `modul`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=35;

--
-- AUTO_INCREMENT untuk tabel `user`
--
ALTER TABLE `user`
  MODIFY `id` int(20) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- Ketidakleluasaan untuk tabel pelimpahan (Dumped Tables)
--

--
-- Ketidakleluasaan untuk tabel `forum`
--
ALTER TABLE `forum`
  ADD CONSTRAINT `forum_ibfk_1` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`);

--
-- Ketidakleluasaan untuk tabel `mengirim_pesan`
--
ALTER TABLE `mengirim_pesan`
  ADD CONSTRAINT `mengirim_pesan_ibfk_1` FOREIGN KEY (`id_forum`) REFERENCES `forum` (`id`),
  ADD CONSTRAINT `mengirim_pesan_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`);

--
-- Ketidakleluasaan untuk tabel `modul`
--
ALTER TABLE `modul`
  ADD CONSTRAINT `modul_ibfk_1` FOREIGN KEY (`id_forum`) REFERENCES `forum` (`id`),
  ADD CONSTRAINT `modul_ibfk_2` FOREIGN KEY (`id_user`) REFERENCES `user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
