import qrcode
img = qrcode.make("https://github.com/gtrmichaels/")
img.save("qr.png", "PNG")