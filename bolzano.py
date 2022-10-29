from prettytable import PrettyTable
import matplotlib.pyplot as plt
import math

table = PrettyTable(["Iterasi", "x1", "x2", "x3", "f(x1)", "f(x2)", "f(x3)"])

# Masukkan banyaknya iterasi yang diinginkan
while True:
  iterate = int(input("Iteration: "))
  if iterate <= 0:
    print("Iteration must be greater than 0")
    continue
  else:
    break

# Masukkan orde dari fungsi polinomial
while True:
  highest_exponent = int(input("Highest exponent: "))
  if highest_exponent <= 0:
    print("Degree must be greater than 0")
    continue
  else:
    break

equation_unsolved = []
x1_arr = []
x2_arr = []
x3_arr = []
y1_arr = []
y2_arr = []
y3_arr = []

# Masukkan koefisien-koefisien persamaan polinomial ke dalam list
count = 0
while count <= highest_exponent:
  string = "_x^" + str(count) + "= "
  buffer = input(string)
  equation_unsolved.append(float(buffer))
  count += 1


# Fungsi f(x) dari polinomial yang dimasukkan
def f(x):
  temp = 0
  exponent = 0
  while exponent <= highest_exponent:
    buffer = math.pow(x, exponent) * equation_unsolved[exponent]
    temp += buffer
    exponent += 1
  return temp


# Input batas awal iterasi
while True:
  lower_x = float(input("Initial lower x: "))
  upper_x = float(input("Initial upper x: "))

  # Cek apakah nilai batas iterasi memenuhi syarat f(x1)*f(x2)<0
  if (f(lower_x) * f(upper_x) < 0):
    break
  else:
    print("Invalid range!")

# Hitung nilai nilai f(x) untuk batas-batas iterasi dan nilai tengah
iterate_counter = 1
while iterate_counter <= iterate:
  y1 = f(lower_x)
  y2 = f(upper_x)

  x3 = (lower_x + upper_x) / 2
  y3 = f(x3)

  tuple = []
  tuple.append(iterate_counter)
  tuple.append(lower_x)
  tuple.append(upper_x)
  tuple.append(x3)
  tuple.append(y1)
  tuple.append(y2)
  tuple.append(y3)
  table.add_row(tuple)

  x1_arr.append(lower_x)
  y1_arr.append(y1)
  x2_arr.append(upper_x)
  y2_arr.append(y2)
  x3_arr.append(x3)
  y3_arr.append(y3)

  # Ubah batas iterasi untuk iterasi berikutnya
  if (y1 * y3 < 0):
    upper_x = x3
  elif (y2 * y3 < 0):
    lower_x = x3
  iterate_counter += 1

print()
print(table)

plt.plot(x1_arr, y1_arr, label="x1")
plt.plot(x2_arr, y2_arr, label="x2")
plt.plot(x3_arr, y3_arr, label="x3")
plt.show()
