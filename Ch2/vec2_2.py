from vector_drawing import *

func_vectors = []
for x in range(-10,12):
   func_vectors.append((x, x**2))

draw(
   Points(*func_vectors),
   grid=(1,10),
   nice_aspect_ratio=False
)
