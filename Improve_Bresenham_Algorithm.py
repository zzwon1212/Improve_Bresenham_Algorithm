import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

def get_grid_cells(point):
  """
  Get grid cells that the line between a point and the origin passes through.

  Parameters:
  - point (list or tuple): A point represented as a list or tuple of coordinates (x, y).
                           Both x and y are expected to be floats.
  """

  # Make empty list for grid cells that the line goes through
  grid_cells = []

  # Get x and y
  x = point[0]
  y = point[1]

  # Calculate a slope of the line between p and origin.
  slope = y / (x + 1e-6)

  # Get sign of X and Y.
  x_sign = 1 if x >= 0 else -1
  y_sign = 1 if y >= 0 else -1

  # Get the last grid value of X.
  if x >= 0:
    x_max = np.ceil(x).astype(np.int32)
  else:
    x_max = np.floor(x).astype(np.int32)

  # y_min will be updated during iteration.
  y_min = 0

  # Iterate for X
  for i in range(0 + x_sign, x_max + x_sign, x_sign):

    # Get the current value at the current X.
    y_value = slope * i

    # Get the last grid value of Y at the current X.
    if y >= 0:
      y_max = np.ceil(y_value).astype(np.int32)
    else:
      y_max = np.floor(y_value).astype(np.int32)

    # Iterate for Y
    for j in range(y_min + y_sign, y_max + y_sign, y_sign):

      # Break if the current grid value of Y is bigger than original Y.
      if y >= 0:
        if j >= (y + 1):
          break
      else:
        if j < (y - 1):
          break

      # Append the grid cells
      grid_cells.append([i, j])

    # Get the first grid value of Y at the next X.
    if y >= 0:
      y_min = np.floor(y_value).astype(np.int32)
    else:
      y_min = np.ceil(y_value).astype(np.int32)
    
  return grid_cells

def draw_grid_cells(point, grid_cells):
  """
  Draw the line between a point and the origin and
  the grid cells that the line passes through.

  Parameters:
  - point (list or tuple): A point represented as a list or tuple of coordinates (x, y).
                           Both x and y are expected to be floats.
  - grid_cells (list or tuple): A list or tuple which contains the grid cell list or tuple.
  """

  # Get x and y
  x = point[0]
  y = point[1]

  # Get sign of X and Y.
  x_sign = 1 if x >= 0 else -1
  y_sign = 1 if y >= 0 else -1

  # Make a plot.
  fig, ax = plt.subplots(figsize=(7, 7))

  # Draw the grid cells
  for (i, j) in grid_cells:
    rect = patches.Rectangle((i - 0.5*(x_sign + 1), j - 0.5*(y_sign + 1)), 1, 1, facecolor="gold")
    ax.add_patch(rect)
  
  # Draw the line
  line = lines.Line2D([0, x], [0, y], color="red")
  ax.add_line(line)

  # For plot
  ax.set_xlim(-6, 6)
  ax.set_ylim(-6, 6)
  ax.set_xticks(range(-6, 6 + 1))
  ax.set_yticks(range(-6, 6 + 1))
  ax.grid(True, which='both', linestyle='--')
  ax.axhline(0, color='black', linewidth=2)
  ax.axvline(0, color='black', linewidth=2)
  plt.show()

if __name__ == "__main__":
  point = np.random.uniform(-6.0, 6.0, 2).astype(np.float32)
  # point = [3, 6]
  # point = (3, 6)

  grid_cells = get_grid_cells(point)
  draw_grid_cells(point, grid_cells)

  print("Point:", point)
  print("Grid Cell:", grid_cells)
