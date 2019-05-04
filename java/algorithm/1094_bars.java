import java.util.*;
public class bars_1094 {
	public static int arraySum(ArrayList<Integer> arr) {
		// 배열의 원소를 더해서 반환한다.
		int output = 0;
		for (int a : arr) {
			output += a;
		}
		return output;
	}
	
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int X = sc.nextInt();
		int bars[] = {32, 16, 8, 4, 2, 1, 1};
		ArrayList<Integer> b_sum = new ArrayList<>();
		
		for(int b : bars) {
			if (b<=X  && arraySum(b_sum) + b <= X) {
				b_sum.add(b);
			}
		}
		
		if (X==64) {
			System.out.println(1);
		} else {
			System.out.println(b_sum.size());
		}
	}
}
