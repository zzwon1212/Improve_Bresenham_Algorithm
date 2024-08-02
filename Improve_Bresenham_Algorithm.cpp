#include <iostream>
#include <vector>
#include <cmath>
#include <cstdlib>
#include <ctime>

struct Point {
    float x, y;
};

std::vector<std::pair<int, int>> get_grid_cells(Point point) {
    std::vector<std::pair<int, int>> grid_cells;

    float x = std::abs(point.x);
    float y = std::abs(point.y);

    float slope = y / (x + 1e-6);

    int x_max = std::ceil(x);

    int y_min = 0;

    for (int i = 1; i <= x_max; ++i) {
        float y_value = slope * i;
        int y_max = std::ceil(y_value);

        for (int j = y_min + 1; j <= y_max; ++j) {
            if (j >= (y + 1)) {
                break;
            }

            grid_cells.push_back(std::make_pair(i * (point.x > 0 ? 1 : -1), j * (point.y > 0 ? 1 : -1)));
        }

        y_min = std::floor(y_value);
    }

    return grid_cells;
}

void draw_grid_cells(Point point, const std::vector<std::pair<int, int>>& grid_cells) {
    std::cout << "Drawing not implemented in C++ version. Use a suitable graphics library.\n";
    std::cout << "Grid Cells:\n";
    for (const auto& cell : grid_cells) {
        std::cout << "(" << cell.first << ", " << cell.second << ")\n";
    }
}

int main() {
    std::srand(static_cast<unsigned int>(std::time(0)));

    Point point;
    point.x = static_cast<float>(std::rand()) / RAND_MAX * 12 - 6;
    point.y = static_cast<float>(std::rand()) / RAND_MAX * 12 - 6;
    std::cout << "Point: (" << point.x << ", " << point.y << ")\n";

    std::vector<std::pair<int, int>> grid_cells = get_grid_cells(point);
    draw_grid_cells(point, grid_cells);

    return 0;
}

