```mermaid
 classDiagram
      Peli "1" --> "2..8" Pelaaja
      Pelaaja "1" --> "1" Pelinappula
      Peli "1" --> "1" Pelilauta
      Pelinappula "1" --> "1" Pelilauta
      Pelilauta "1" --> "40" Ruutu
      Ruutu "1" --> "1" Ruutu
