from PIL import Image

# roblox to polytoria shirt

# load the template

roblox_img = Image.open("input.png").convert("RGBA")

# create canvas for polytoria

poly_img = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))

extrasize = 2  # this expands each piece to remove any gaps (2 is probably best)

# roblox positions (topleftX, topleftY, bottomrightX, bottomrightY)

TORSO_ROBLOX = {
    "front":  (231, 74, 358, 201),
    "back":   (427, 74, 554, 201),
    "left":   (361, 74, 424, 201),
    "right":  (165, 74, 228, 201),
    "top":    (231, 8, 358, 71),
    "bottom": (231, 204, 358, 267),
}

LEFT_ARM_ROBLOX = {
    "front":  (308, 355, 371, 482),
    "back":   (440, 355, 503, 482),
    "left":   (374, 355, 437, 482),
    "right":  (506, 355, 569, 482),
    "top":    (308, 289, 371, 352),
    "bottom": (308, 485, 371, 548),
}

RIGHT_ARM_ROBLOX = {
    "front":  (217, 355, 280, 482),
    "back":   (85, 355, 148, 482),
    "left":   (19, 355, 82, 482),
    "right":  (151, 355, 214, 482),
    "top":    (217, 289, 280, 352),
    "bottom": (217, 485, 280, 548),
}

# polytoria positions (topleftX, topleftY, bottomrightX, bottomrightY)

TORSO_POLY = {
    "front":  (439, 103, 584, 392),
    "back":   (439, 519, 584, 808),
    "left":   (585, 103, 672, 392),
    "right":  (351, 103, 438, 392),
    "top":    (439, 30, 584, 102),
    "bottom": (439, 393, 584, 488),
}

LEFT_ARM_POLY = {
    "front":  (754, 71, 819, 360),
    "back":   (886, 71, 951, 360),
    "left":   (820, 71, 885, 360),
    "right":  (952, 71, 1017, 360),
    "top":    (754, 7, 819, 70),
    "bottom": (754, 361, 819, 424),
}

RIGHT_ARM_POLY = {
    "front":  (204, 71, 269, 360),
    "back":   (72, 71, 137, 360),
    "left":   (6, 71, 71, 360),
    "right":  (138, 71, 203, 360),
    "top":    (204, 7, 269, 70),
    "bottom": (204, 361, 269, 424),
}

# apply extra size

def expand_coords(coords, extrasize):
    x1, y1, x2, y2 = coords
    return (x1 - extrasize, y1 - extrasize, x2 + extrasize, y2 + extrasize)

# process the piece

def transfer_part(roblox_coords, poly_coords, part_name):
    for face in roblox_coords:
        
        # crop roblox piece

        crop = roblox_img.crop(roblox_coords[face])
        
        # expand piece

        target_coords = expand_coords(poly_coords[face], extrasize // 2)
        target_width = target_coords[2] - target_coords[0]
        target_height = target_coords[3] - target_coords[1]
        
        # resize

        resized = crop.resize((target_width, target_height), Image.NEAREST)
        
        # paste

        poly_img.paste(resized, (target_coords[0], target_coords[1]))
        print(f"✅ {part_name} {face} converted.")

# process all parts

transfer_part(TORSO_ROBLOX, TORSO_POLY, "Torso")
transfer_part(LEFT_ARM_ROBLOX, LEFT_ARM_POLY, "Left Arm")
transfer_part(RIGHT_ARM_ROBLOX, RIGHT_ARM_POLY, "Right Arm")

# save output

poly_img.save("output.png")
print("done converting parts")
