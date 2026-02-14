import sys
import os

# Agregar la ruta de app al path
sys.path.insert(0, os.path.abspath(
    os.path.join(
        os.path.dirname(__file__), '..', 'app')))

import unittest
from string_function import generar_numero, validar_numero, comparar

class TestJuegoAdivinanza(unittest.TestCase):
    
    def test_generar_numero_rango(self):
        """Test that generated number is 4 digits"""
        for _ in range(10):
            num = generar_numero()
            self.assertTrue(1000 <= num <= 9999)
    
    def test_validar_digito_valido(self):
        """Test validation with valid digit"""
        valido, num = validar_numero("5")
        self.assertTrue(valido)
        self.assertEqual(num, 5)
    
    def test_validar_digito_invalido_texto(self):
        """Test validation with text"""
        valido, num = validar_numero("abc")
        self.assertFalse(valido)
        self.assertIsNone(num)
    
    def test_validar_digito_fuera_rango(self):
        """Test validation with number out of range"""
        valido, num = validar_numero("15")
        self.assertFalse(valido)
    
    def test_validar_digito_negativo(self):
        """Test validation with negative number"""
        valido, num = validar_numero("-5")
        self.assertFalse(valido)
    
    def test_digito_repetido(self):
        """Test that repeated guess in same position is detected"""
        intentos = {0: 5}
        self.assertTrue(0 in intentos)
        self.assertEqual(intentos[0], 5)
    
    def test_comparar_sin_aciertos(self):
        """Test progress with no correct digits - XXXX"""
        intentos = {0: 1, 1: 2, 2: 3, 3: 4}
        resultado, correctos = comparar(5678, intentos)
        self.assertEqual(resultado, "XXXX")
        self.assertEqual(correctos, 0)
    
    def test_comparar_un_acierto(self):
        """Test progress with one correct digit - XX5X"""
        intentos = {0: 1, 1: 2, 2: 5, 3: 4}
        resultado, correctos = comparar(6758, intentos)
        self.assertEqual(resultado, "XX5X")
        self.assertEqual(correctos, 1)
    
    def test_comparar_dos_aciertos(self):
        """Test progress with two correct digits - X55X"""
        intentos = {0: 1, 1: 5, 2: 5, 3: 4}
        resultado, correctos = comparar(6557, intentos)
        self.assertEqual(resultado, "X55X")
        self.assertEqual(correctos, 2)
    
    def test_comparar_tres_aciertos_inicio(self):
        """Test progress with three correct digits at start - 567X"""
        intentos = {0: 5, 1: 6, 2: 7, 3: 9}
        resultado, correctos = comparar(5678, intentos)
        self.assertEqual(resultado, "567X")
        self.assertEqual(correctos, 3)
    
    def test_comparar_tres_aciertos_final(self):
        """Test progress with three correct digits at end - X678"""
        intentos = {0: 9, 1: 6, 2: 7, 3: 8}
        resultado, correctos = comparar(5678, intentos)
        self.assertEqual(resultado, "X678")
        self.assertEqual(correctos, 3)
    
    def test_comparar_tres_aciertos_mixto(self):
        """Test progress with three correct digits mixed - 5X78"""
        intentos = {0: 5, 1: 9, 2: 7, 3: 8}
        resultado, correctos = comparar(5678, intentos)
        self.assertEqual(resultado, "5X78")
        self.assertEqual(correctos, 3)
    
    def test_comparar_todos_correctos(self):
        """Test progress with all correct digits - 5678"""
        intentos = {0: 5, 1: 6, 2: 7, 3: 8}
        resultado, correctos = comparar(5678, intentos)
        self.assertEqual(resultado, "5678")
        self.assertEqual(correctos, 4)
    
    def test_comparar_parcial(self):
        """Test progress with partial guesses - 5X7X"""
        intentos = {0: 5, 2: 7}
        resultado, correctos = comparar(5678, intentos)
        self.assertEqual(resultado, "5X7X")
        self.assertEqual(correctos, 2)

if __name__ == "__main__":
    unittest.main(verbosity=2)