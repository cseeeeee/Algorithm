import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
	public static void main(String[] args) throws IOException{
		BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
		String[] input = bf.readLine().split("");
		int num = Integer.parseInt(bf.readLine());
		
		System.out.println(input[num-1]);
		
	}
}
