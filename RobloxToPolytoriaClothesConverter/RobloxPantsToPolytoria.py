from PIL import Image

# 204 7 206 597, 754, 7 754 597

# Load Roblox template
roblox_img = Image.open("input.png").convert("RGBA")

# Create Polytoria canvas
poly_img = Image.new("RGBA", (1024, 1024), (0, 0, 0, 0))

extrasize = 2  # how much to expand each face to remove gaps

# -----------------------------
# ROBLOX COORDS (top-left x,y and bottom-right x,y)
# -----------------------------
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

# -----------------------------
# POLYTORIA COORDS (top-left x,y and bottom-right x,y)
# -----------------------------
TORSO_POLY = {
    "front":  (439, 103, 584, 392),
    "back":   (439, 519, 584, 808),
    "left":   (585, 103, 672, 392),
    "right":  (351, 103, 438, 392),
    "top":    (439, 30, 584, 102),
    "bottom": (439, 393, 584, 488),
}

LEFT_ARM_POLY = {
    "front":  (754, 71 + 590, 819, 360 + 590),
    "back":   (886, 71 + 590, 951, 360 + 590),
    "left":   (820, 71 + 590, 885, 360 + 590),
    "right":  (952, 71 + 590, 1017, 360 + 590),
    "top":    (754, 7 + 590, 819, 70 + 590),
    "bottom": (754, 361 + 590, 819, 424 + 590),
}

RIGHT_ARM_POLY = {
    "front":  (204 + 2, 71 + 590, 269 + 2, 360 + 590),
    "back":   (72 + 2, 71 + 590, 137 + 2, 360 + 590),
    "left":   (6 + 2, 71 + 590, 71 + 2, 360 + 590),
    "right":  (138 + 2, 71 + 590, 203 + 2, 360 + 590),
    "top":    (204 + 2, 7 + 590, 269 + 2, 70 + 590),
    "bottom": (204 + 2, 361 + 590, 269 + 2, 424 + 590),
}

# -----------------------------
# FUNCTION TO APPLY extrasize
# -----------------------------
def expand_coords(coords, extrasize):
    x1, y1, x2, y2 = coords
    return (x1 - extrasize, y1 - extrasize, x2 + extrasize, y2 + extrasize)

# -----------------------------
# FUNCTION TO PROCESS A PART
# -----------------------------
def transfer_part(roblox_coords, poly_coords, part_name):
    for face in roblox_coords:
        # Crop from Roblox
        crop = roblox_img.crop(roblox_coords[face])
        
        # Expand target coordinates to remove gaps
        target_coords = expand_coords(poly_coords[face], extrasize // 2)
        target_width = target_coords[2] - target_coords[0]
        target_height = target_coords[3] - target_coords[1]
        
        # Resize
        resized = crop.resize((target_width, target_height), Image.NEAREST)
        
        # Paste into Polytoria canvas
        poly_img.paste(resized, (target_coords[0], target_coords[1]))
        print(f"✅ {part_name} {face} converted.")

# -----------------------------
# PROCESS ALL PARTS
# -----------------------------
transfer_part(TORSO_ROBLOX, TORSO_POLY, "Torso")
transfer_part(LEFT_ARM_ROBLOX, LEFT_ARM_POLY, "Left Arm")
transfer_part(RIGHT_ARM_ROBLOX, RIGHT_ARM_POLY, "Right Arm")

# Save final output
poly_img.save("output.png")
print("🎉 All parts converted successfully!")