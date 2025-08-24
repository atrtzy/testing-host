import turtle

# Mengatur layar
screen = turtle.Screen()
screen.bgcolor("black")  # Mengubah warna latar belakang menjadi hitam

# Membuat objek penyu
t = turtle.Turtle()
t.speed(0)  # Mengatur kecepatan menggambar ke kecepatan maksimal
t.pensize(2) # Mengatur ketebalan garis

# Fungsi untuk menggambar kelopak
def draw_petal(t, size):
    t.circle(size, 60)
    t.left(120)
    t.circle(size, 60)

# Menggambar bunga
colors = ["red", "yellow", "blue", "green", "orange", "purple"]
for _ in range(60):
    t.color(colors[_ % 6])
    draw_petal(t, 100)
    t.left(6)

t.hideturtle()  # Menyembunyikan objek penyu setelah selesai menggambar
screen.exitonclick()  # Menutup jendela saat diklik
