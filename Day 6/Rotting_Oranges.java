class Solution {

    public int orangesRotting(int[][] grid) {

        Queue<int[]> queue = new LinkedList<>();

        int fresh = 0;

        int rows = grid.length;
        int cols = grid[0].length;

        // Find all rotten oranges
        // and count fresh oranges
        for (int r = 0; r < rows; r++) {

            for (int c = 0; c < cols; c++) {

                if (grid[r][c] == 2) {
                    queue.offer(new int[]{r, c});
                }

                if (grid[r][c] == 1) {
                    fresh++;
                }
            }
        }

        // No fresh oranges
        if (fresh == 0) {
            return 0;
        }

        int minutes = 0;

        int[][] directions = {
            {1, 0},   // down
            {-1, 0},  // up
            {0, 1},   // right
            {0, -1}   // left
        };

        while (!queue.isEmpty() && fresh > 0) {

            int size = queue.size();

            // Process one level
            // One level = one minute
            for (int i = 0; i < size; i++) {

                int[] current = queue.poll();

                int row = current[0];
                int col = current[1];

                for (int[] dir : directions) {

                    int newRow = row + dir[0];
                    int newCol = col + dir[1];

                    // Check boundaries
                    if (newRow < 0 ||
                        newRow >= rows ||
                        newCol < 0 ||
                        newCol >= cols) {
                        continue;
                    }

                    // Only process fresh oranges
                    if (grid[newRow][newCol] == 1) {

                        // Make it rotten
                        grid[newRow][newCol] = 2;

                        fresh--;

                        queue.offer(
                            new int[]{newRow, newCol}
                        );
                    }
                }
            }

            minutes++;
        }

        return fresh == 0 ? minutes : -1;
    }
}
