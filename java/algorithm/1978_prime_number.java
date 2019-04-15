import java.util.*;

public class Main {
	public static void main(String[] args) {
		// 입력 받기 
		Scanner scanner = new Scanner(System.in);
		String _ = scanner.nextLine();
		String input = scanner.nextLine();
		
		// 숫자 ArrayList 만들기 
		ArrayList<Integer> nums = new ArrayList<>(); // make nums ArrayList
		List<String> inputList = Arrays.asList(input.split(" ")); // split input -> inputList
		for(String s : inputList) nums.add(Integer.valueOf(s)); // for-each
		
		// Filtering 
		nums.removeIf(n -> ((n%3==0)&&(n!=3)) || ((n%2==0)&&(n!=2)) || (n==1) || (n==4));
		
		// Count Prime Numbers
		int count = 0;
			for(int i=0; i<nums.size(); i++) {
				boolean is_prime = true;
				int curr = nums.get(i); // 현재 값
				double sqrt_c = Math.sqrt(curr);
				
				for(int j=2; j<(Math.round(sqrt_c+1)); j++) {
					if(curr%j == 0) {
						is_prime = false;
						break;
					} // if
				} // inner for문 
				
				if(is_prime==true) {
					count += 1;
				} // if
				
			} // outer for문
			
		System.out.println(count);
	}
}