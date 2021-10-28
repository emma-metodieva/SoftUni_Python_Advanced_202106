from canvas import shop


def clean_screen():
    for i in shop.grid_slaves():
        i.destroy()
