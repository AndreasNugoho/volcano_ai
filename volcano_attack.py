from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
import easygui
from graph import *
from binarySearch import *

input_file_png = easygui.fileopenbox(msg="EDIT GAMBAR",filetypes=["*.png"])
input_file_jpg = input_file_png.rpartition('.')[0] + ".jpg"
print(input_file_jpg)


def mouse_pos(event):
    global posSatuY, posSatuX
    posSatuX, posSatuY = event.x, event.y

def update_sel_rect(event):
    global rect_id
    global posSatuY, posSatuX, posDuaX, posDuaY
    global cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower
    posDuaX, posDuaY = event.x, event.y
    canvas.coords(rect_id,posSatuX,posSatuY,posDuaX,posDuaY)
    if posSatuX < posDuaX:
        if posSatuY < posDuaY:
            cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = posSatuX, posSatuY, posDuaX, posDuaY
        else:
            cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = posSatuX, posDuaY, posDuaX, posSatuY
    elif posSatuX > posDuaX:
        if posSatuY < posDuaY:
            cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = posDuaX, posSatuY, posSatuX, posDuaY
        else:
            cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = posDuaX, posDuaY, posSatuX, posSatuY

cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower = 0, 0, 0, 0
posSatuX, posSatuY, posDuaX, posDuaY = 0, 0, 0, 0
rect_id = None
WINDOWWIDTH, WINDOWHEIGHT = 900, 900
window = tk.Tk()
window.title("pilih area")
window.geometry('%sx%s' % (WINDOWWIDTH, WINDOWHEIGHT))
window.configure(background='grey')
img = ImageTk.PhotoImage(Image.open(input_file_png))
canvas = tk.Canvas(window, width=img.width(), height=img.height(),
                   borderwidth=0, highlightthickness=0)
canvas.pack(expand=True)
canvas.img = img
canvas.create_image(0, 0, image=img, anchor=tk.NW)
rect_id = canvas.create_rectangle(posSatuX, posSatuY, posSatuX, posSatuY,
                                  dash=(2, 2), fill='', outline='white')
canvas.bind('<Button-1>', mouse_pos)
canvas.bind('<B1-Motion>', update_sel_rect)
window.mainloop()

def imageCut(inputJpg, inputPng):
    jpg = Image.open(inputJpg)
    png = Image.open(inputPng)
    png.crop((cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower)).save('png_crop.png', "PNG")
    jpg.crop((cutBoundaryLeft, cutBoundaryUpper, cutBoundaryRight, cutBoundaryLower)).save('jpg_crop.jpg', "JPEG")

imageCut(input_file_jpg, input_file_png)

bukaGambar = Image.open('jpg_crop.jpg')
draw = ImageDraw.Draw(bukaGambar)
lebar = bukaGambar.size[0]
tinggi = bukaGambar.size[1]
pix = bukaGambar.load()

bukaGambar = Image.open('png_crop.png')
postPix = list(bukaGambar.getdata())

canvasLebar = lebar * 20
canvasTinggi = tinggi * 20
gambarBaru = Image.new('RGB', (canvasLebar, canvasTinggi), 'white')
data = list(bukaGambar.getdata())
dx = 0
dy = 0
counter = 0
for y in range(tinggi):
    for x in range(lebar):
        draw.rectangle((dx, dy, dx + 20, dy + 20), fill=data[counter])
        font = ImageFont.truetype("arial.ttf", 10)
        fillage = str(data[counter])
        if postPix[counter][0] - postPix[counter][1] > 10:
            draw.text((dx + 1, dy + 5), fillage[1:4], 'green', font=font)
        else:
            draw.text((dx + 1, dy + 5), fillage[1:4], 'red', font=font)
        draw = ImageDraw.Draw(gambarBaru)
        dx = dx + 20
        counter = counter + 1
    dy = dy + 20
    print("Identifikasi = ",dy)
    dx = 0

goal=""
if(dy < 500):
    print("status gunung normal")
    goal = "Kegiatan Normal"
elif(dy > 500 and dy < 1000):
    print("status gunung waspada")
    goal = "Masyarakat Tidak Perlu Mengungsi"
elif(dy > 1000 and dy < 1800):
    print("status gunung siaga")
    goal = "Masyarakat Mulai Mengungsi"
elif(dy > 1800 and dy < 2000):
    print("status gunung awas")
    goal = "Masyarakat Sudah Mengungsi"
elif(dy > 2000):
    goal = "Erupsi"
print(goal)



graph = Graph()
graph.addVertex('Start')
graph.addVertex('Gunung Stabil')
graph.addVertex('Muncul Aktivitas')
graph.addVertex('Status Normal')
graph.addVertex('Aktivitas Seismik')
graph.addVertex('Aktivitas Kawah')
graph.addVertex('Muncul Uap dan Abu')
graph.addVertex('Kegiatan Normal')
graph.addVertex('Status Waspada')
graph.addVertex('Status Siaga')
graph.addVertex('Status Awas')
graph.addVertex('Erupsi')
graph.addVertex('Masyarakat Tidak Perlu Mengungsi')
graph.addVertex('Masyarakat Perlu Waspada')
graph.addVertex('Kegiatan Dikurangi')
graph.addVertex('Kegiatan Diberhentikan')
graph.addVertex('Masyarakat Siap Mengungsi')
graph.addVertex('Masyarakat Mulai Mengungsi')
graph.addVertex('Masyarakat Sudah Mengungsi')

# Sambung - Sambung
graph.addEdge('Start', 'Gunung Stabil')
graph.addEdge('Start', 'Muncul Aktivitas')
graph.addEdge('Gunung Stabil', 'Status Normal')
graph.addEdge('Status Normal', 'Kegiatan Normal')
graph.addEdge('Kegiatan Normal', 'Masyarakat Tidak Perlu Mengungsi')
graph.addEdge('Muncul Aktivitas', 'Aktivitas Seismik')
graph.addEdge('Aktivitas Seismik', 'Status Waspada')
graph.addEdge('Status Waspada', 'Masyarakat Perlu Waspada')
graph.addEdge('Masyarakat Perlu Waspada', 'Masyrakat Siap Mengungsi')
graph.addEdge('Muncul Aktivitas', 'Aktivitas Kawah')
graph.addEdge('Aktivitas Kawah', 'Status Siaga')
graph.addEdge('Status Siaga', 'Kegiatan Dikurangi')
graph.addEdge('Kegiatan Dikurangi', 'Masyarakat Mulai Mengungsi')
graph.addEdge('Muncul Aktivitas', 'Muncul Uap dan Abu')
graph.addEdge('Muncul Uap dan Abu', 'Status Awas')
graph.addEdge('Status Awas', 'Kegiatan Diberhentikan')
graph.addEdge('Kegiatan Diberhentikan', 'Masyarakat Sudah Mengungsi')
graph.addEdge('Muncul Uap dan Abu', 'Erupsi')


print("DFS")
graph.findPath('Start', goal)

print(30*"=")


root = getNode('Start')
root.left = getNode('Gunung Stabil')
root.left.left = getNode('Status Normal')
root.left.left.left = getNode('Kegiatan Normal')
root.left.left.left.left = getNode('Masyarakat Tidak Perlu Mengungsi')
root.right = getNode('Muncul Aktivitas')
root.right.left = getNode('Aktivitas Seismik')
root.right.mid = getNode('Aktivitas Kawah')
root.right.right = getNode('Masyarakat Mulai Mengungsi')
root.right.right.right = getNode('Erupsi')
root.right.right.left = getNode('Status Awas')
root.right.right.left.left = getNode('Kegiatan Diberhentikan')
root.right.right.left.left.left = getNode('Masyarakat Sudah Mengungsi')


print("Path Yang Ditemukan : ")
printPath(root, goal)

draw.rectangle((0, 0, 19, 19), fill=data[0])
draw.text((1, 5), str(data[0])[1:4], 'red', font=font)
draw = ImageDraw.Draw(gambarBaru)
gambarBaru.show()
