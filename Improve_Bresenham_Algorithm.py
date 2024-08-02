import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.lines as lines

def get_grid_cells(point):
  """
  Get grid cells that the line between a point and the origin passes through.

  Parameters:
  -----------
  point: list or tuple
    A point represented as a list or tuple of coordinates (x, y).
    Both x and y are expected to be floats.

  Returns:
  -----------
  grid_cells: list
    A list or tuple which contains lists or tuples of grid cell.
  """

  # Make empty list for grid cells that the line goes through.
  grid_cells = []

  # Get the absolute value of x and y.
  # We will consider only the first quadrant
  # and later, get the grid cells back to the original quadrant.
  x = abs(point[0])
  y = abs(point[1])

  # Calculate a slope of the line between p and origin.
  slope = y / (x + 1e-6)

  # Get the last grid value of X.
  x_max = np.ceil(x).astype(np.int32)

  # y_min will be updated during iteration.
  y_min = 0

  # Iterate for X
  for i in range(1, x_max + 1):

    # Get the current value at the current X.
    y_value = slope * i

    # Get the last grid value of Y at the current X.
    y_max = np.ceil(y_value).astype(np.int32)

    # Iterate for Y
    for j in range(y_min + 1, y_max + 1):

      # Break if the current grid value of Y is larger than original Y.
      if j >= (y + 1):
        break

      # Get the grid cells back to the original quadrant
      # and append them to the list.
      grid_cells.append([i * np.sign(point[0]), j * np.sign(point[1])])

    # Get the first grid value of Y at the next X.
    y_min = np.floor(y_value).astype(np.int32)
    
  return grid_cells

def draw_grid_cells(point, grid_cells):
  """
  Draw the line between a point and the origin and
  the grid cells that the line passes through.

  Parameters:
  -----------
  point: list or tuple
    A point represented as a list or tuple of coordinates (x, y).
    Both x and y are expected to be floats.

  grid_cells: list
    A list or tuple which contains lists or tuples of grid cell.
  """

  # Get x and y
  x = point[0]
  y = point[1]

  # Make a plot.
  fig, ax = plt.subplots(figsize=(7, 7))

  # Draw the grid cells
  for (i, j) in grid_cells:
    rect = patches.Rectangle((i - 0.5*(np.sign(x) + 1), j - 0.5*(np.sign(y) + 1)), 1, 1, facecolor="gold")
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
