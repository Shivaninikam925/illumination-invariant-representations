import numpy as np

def generate_image(size=32):
    img = np.zeros((size, size))
    x0, y0 = np.random.randint(8, size-8, size=2)
    img[x0-3:x0+3, y0-3:y0+3] = 1.0  # simple square object
    return img

def apply_illumination(img, scale=1.0, bias=0.0):
    return np.clip(scale * img + bias, 0.0, 1.0)

def generate_pair():
    img = generate_image()
    img_illum = apply_illumination(
        img,
        scale=np.random.uniform(0.5, 1.5),
        bias=np.random.uniform(-0.2, 0.2)
    )
    return img, img_illum

if __name__ == "__main__":
    a, b = generate_pair()
    print(a.shape, b.shape)
