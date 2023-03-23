
import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.kortti500 = Maksukortti(500)
        self.kortti200 = Maksukortti(200)

    def test_raha_alkuun_ok(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullisia_lounaita_myyty(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaita_lounaita_myyty(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_kateinen_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)
    
    def test_maukas_kateinen_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_kateinen_myydyt(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_kateinen_myydyt(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_kateinen_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(500)
        self.assertEqual(vaihtoraha, 260)

    def test_maukas_kateinen_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihtoraha, 100)
    
    def test_edullinen_kateinen_ei_riita_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
    
    def test_maukas_kateinen_ei_riita_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_kateinen_ei_riita_myydyt(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_kateinen_ei_riita_myydyt(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_kateinen_ei_riita_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)
    
    def test_maukas_kateinen_ei_riita_vaihtoraha(self):
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual(vaihtoraha, 100)

    def test_edullinen_korttiveloitus_saldo(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti500)
        self.assertEqual(str(self.kortti500), "Kortilla on rahaa 2.60 euroa")

    def test_maukas_korttiveloitus_saldo(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti500)
        self.assertEqual(str(self.kortti500), "Kortilla on rahaa 1.00 euroa")

    def test_edullinen_korttiveloitus_kassa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_korttiveloitus_kassa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_korttiveloitus_lounaat_ok(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti500)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_korttiveloitus_lounaat_ok(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti500)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_korttiveloitus_True(self):
        onnistuu = self.kassapaate.syo_edullisesti_kortilla(self.kortti500)
        self.assertEqual(onnistuu, True)

    def test_maukas_korttiveloitus_True(self):
        onnistuu = self.kassapaate.syo_maukkaasti_kortilla(self.kortti500)
        self.assertEqual(onnistuu, True)

    def test_edullinen_korttiveloitus_saldo_pysyy(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti200)
        self.assertEqual(str(self.kortti200), "Kortilla on rahaa 2.00 euroa")

    def test_maukas_korttiveloitus_saldo_pysyy(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti200)
        self.assertEqual(str(self.kortti200), "Kortilla on rahaa 2.00 euroa")

    def test_edullinen_korttiveloitus_lounaat_ei_ok(self):
        self.kassapaate.syo_edullisesti_kortilla(self.kortti200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukas_korttiveloitus_lounaat_ei_ok(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.kortti200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_edullinen_korttiveloitus_False(self):
        onnistuu = self.kassapaate.syo_edullisesti_kortilla(self.kortti200)
        self.assertEqual(onnistuu, False)

    def test_edullinen_korttiveloitus_False(self):
        onnistuu = self.kassapaate.syo_maukkaasti_kortilla(self.kortti200)
        self.assertEqual(onnistuu, False)

    def test_lataa_rahaa_kortti(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti200, 1000)
        self.assertEqual(self.kortti200.saldo, 1200)

    def test_lataa_rahaa_kortti_negatiivinen(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti200, -100)
        self.assertEqual(self.kortti200.saldo, 200)

    def test_lataa_rahaa_kassa(self):
        self.kassapaate.lataa_rahaa_kortille(self.kortti200, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)
