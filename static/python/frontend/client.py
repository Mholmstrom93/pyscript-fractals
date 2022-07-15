from pyodide import to_js, create_proxy

import numpy as np
import sympy

from palettes import Magma256
from fractals import mandelbrot, julia, newton

from js import (
    console,
    document,
    devicePixelRatio,
    ImageData,
    Uint8ClampedArray,
    CanvasRenderingContext2D as Context2d,
    requestAnimationFrame,
    Element
)

def prepare_canvas(width: int, height: int, canvas: Element) -> Context2d:
    ctx = canvas.getContext("2d")

    canvas.style.width = f"{width}px"
    canvas.style.height = f"{height}px"

    canvas.width = width
    canvas.height = height

    ctx.clearRect(0, 0, width, height)

    return ctx

def color_map(array: np.array, palette: np.array) -> np.array:
    size, _ = palette.shape
    index = (array/array.max()*(size - 1)).round().astype("uint8")

    width, height = array.shape
    image = np.full((width, height, 4), 0xff, dtype=np.uint8)
    image[:, :, :3] = palette[index]

    return image

def draw_image(ctx: Context2d, image: np.array) -> None:
  data = Uint8ClampedArray.new(to_js(image.tobytes()))
  width, height, _ = image.shape
  image_data = ImageData.new(data, width, height)
  ctx.putImageData(image_data, 0, 0)

width, height = 1000, 1000

async def draw_mandelbrot() -> None:
  spinner = document.querySelector("#mandelbrot .loading")
  canvas = document.querySelector("#mandelbrot canvas")

  spinner.style.display = ""
  canvas.style.display = "none"

  ctx = prepare_canvas(width, height, canvas)

  console.log("Computing Mandelbrot set ...")
  console.time("mandelbrot")
  iters = mandelbrot(width, height)
  console.timeEnd("mandelbrot")

  image = color_map(iters, Magma256)
  draw_image(ctx, image)

  spinner.style.display = "none"
  canvas.style.display = "block"


import asyncio

_ = await asyncio.gather(draw_mandelbrot())