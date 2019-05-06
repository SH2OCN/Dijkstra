
public class Dijkstra {

    //迪杰斯特拉：计算单源最短路径
    public static void dijkstra(int[][] graph, int src) {
        final int N = graph.length;
        int[] dist = new int[N];
        boolean[] sptSet = new boolean[N];
        for(int i = 0; i < N; i++) {
            dist[i] = Integer.MAX_VALUE;
            sptSet[i] = false;
        }
        dist[src] = 0;

        for(int i = 0; i < N-1; i++) {
            int u = minDistance(dist, sptSet);
            sptSet[u] = true;
            for (int j = 0; j < N; j++) {
                if( !sptSet[j] && graph[u][j] != 0 && dist[u]+graph[u][j] < dist[j]) {
                    dist[j] = dist[u]+graph[u][j];
                }
            }
        }
        printSolution(dist);
    }

    //选出没在sptSet中的、且距离最近的顶点u
    public static int minDistance(int[] dist, boolean[] sptSet) {
        int minDist = Integer.MAX_VALUE;
        int u = -1;
        for (int i = 0; i < dist.length; i++) {
            if(!sptSet[i] && dist[i] < minDist) {
                minDist = dist[i];
                u = i;
            }
        }
        return u;
    }

    //打印输出
    public static void printSolution(int[] dist) {
        System.out.println("Vertex\tDistance");
        for (int i = 0; i < dist.length; i++) {
            System.out.println(i + "\t\t" + dist[i]);
        }
    }

    public static void main(String[] args) {
        //一个包含9个顶点的图，用邻接矩阵形式表示：
        int[][] graph = {{0, 4, 0, 0, 0, 0, 0, 8, 0},
                         {4, 0, 8, 0, 0, 0, 0, 11, 0},
                         {0, 8, 0, 7, 0, 4, 0, 0, 2},
                         {0, 0, 7, 0, 9, 14, 0, 0, 0},
                         {0, 0, 0, 9, 0, 10, 0, 0, 0},
                         {0, 0, 4, 14, 10, 0, 2, 0, 0},
                         {0, 0, 0, 0, 0, 2, 0, 1, 6},
                         {8, 11, 0, 0, 0, 0, 1, 0, 7},
                         {0, 0, 2, 0, 0, 0, 6, 7, 0} };
        int src = 0;
        dijkstra(graph, src);
    }
}
