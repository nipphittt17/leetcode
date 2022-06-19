package easyQuestion.src;


//733. Flood Fill

public class Floodfill {

    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        
        boolean[][] visited = new boolean[image.length][image[0].length];

        int old_color = image[sr][sc];

        if (old_color == color) return image;

        dfs(visited, image, sr, sc, old_color, color);
        return image;
        
    }
    
    void dfs(boolean[][] visited,int[][] image,int i,int j,int old_color,int new_color){
        
        if(i < 0 || j < 0 || i >= image.length || j >= image[0].length || 
           visited[i][j] == true || image[i][j] != old_color) return;
        
        visited[i][j] = true;
        dfs(visited,image,i+1,j,old_color,new_color);
        dfs(visited,image,i-1,j,old_color,new_color);
        dfs(visited,image,i,j+1,old_color,new_color);
        dfs(visited,image,i,j-1,old_color,new_color);
        image[i][j] = new_color;   
    }

    public static void main(String[] args) {
        
    }
}
