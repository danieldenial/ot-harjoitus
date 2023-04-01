```mermaid
 classDiagram
      Peli "1" --> "2-8" Pelaaja
      Pelaaja "1" --> "1" Pelinappula
      Pelaaja "1" --> "*" Raha
      Pelaaja "1" --> "*" KatuRuudut
      Peli "1" --> "1" Pelilauta
      Pelinappula "1" --> "1" Pelilauta
      Pelilauta "1" --> "40" Ruudut
      Ruudut --> "1" AloitusRuutu
      Ruudut --> "1" VankilaRuutu
      Ruudut --> SattumaYhteismaaRuudut
      SattumaYhteismaaRuudut --> "*" Kortit
      Kortit --> "*" SattumaKortit
      SattumaKortit "1" --> "*" Toiminnot
      Kortit --> "*" YhteismaaKortit
      YhteismaaKortit "1" --> "*" Toiminnot
      Ruudut --> AsematLaitoksetRuudut
      Ruudut --> KatuRuudut
      KatuRuudut "1" --> "0..4" Talot
      KatuRuudut "1" --> "0..1" Hotellit
      Peli "1" --> "1" AloitusRuutu
      Peli "1" --> "1" VankilaRuutu
      Ruudut "1" --> "1" Ruudut
