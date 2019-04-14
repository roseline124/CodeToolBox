import java.util.*; // Scanner 클래스를 사용하기 위해 추가

public class Main {
	public static void main(String args[]) {

		// 입력 받기
		Scanner scanner = new Scanner(System.in); // Scanner 클래스 객체 생성 
		String input = scanner.nextLine();
		int M = Integer.parseInt(input);		
		
		String input2 = scanner.nextLine();
		int N = Integer.parseInt(input2);
		
		// 완전제곱수 Arraylist
		ArrayList<Integer> perfectSquare = new ArrayList<>();
		
		for(int i=1;i<=100;i++) {
			int s = i*i;
			if((s>=M) && (s<=N)) {
				perfectSquare.add(s);
			}
		}
		
		// 합 구하기 
		int sum = 0;
		
		for(int j=0; j < perfectSquare.size(); j++) {
			sum += perfectSquare.get(j);
		}
		
		if (perfectSquare.size() == 0 ) {
			System.out.println(-1);
		} else {
			System.out.println(sum); // 합
			System.out.println(perfectSquare.get(0)); // 최소값 : index : arraylist.get(index)
		}
	}
}

