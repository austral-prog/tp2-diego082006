import io
import unittest.mock
import exercise_math


class MyTestCase(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_math(self, mock_stdout):
        exercise_math.main()
        results = mock_stdout.getvalue().splitlines()
        self.assertEqual(results[0], "64")  # suma
        self.assertEqual(results[1], "50")  # diferencia
        self.assertEqual(results[2], "399")  # producto
        self.assertEqual(results[3], "32.0")  # promedio
        self.assertEqual(results[4], "8")  # cociente entero
        self.assertEqual(results[5], "1")  # resto
        self.assertEqual(results[6], "8.142857142857142")  # division real


if __name__ == '__main__':
    unittest.main()

# Ejercicio 2

i1 = 2
i2 = 4
i3 = i1 + i2
print("valor de i1")
print(i1)
print("valor de i2")
print(i2)
print("valor de i3")
print(i3)
print("valor total")
print(i1 + i2 + i3)

s1, s2, s3 = "Python", " is ", 'awesome'
print(s1 + s2 + s3)

x = "Naranja"
y = z = ", Naranja"
print(x + y + z)

z1 = i3 / i2
print(z1)
z2 = i3 % i2
print(z2)
f1 = 0.5
f2 = 10
f3 = f1 + f2
i3 = int(f3)
print("entero de i3:")
print(i3)
print("variable de f3:")
print(f3)
f2 += i1
print("el valor de i1 es igual a:")
print(f2)
print("más")
print(f1)
print("es:")
print(f2 + f1)