
public class Scope_190503 {
	static int j = 0; // 전역 변수  
	
	static void a() {
		int i = 0; // 지역 변수 
	}
	
	public static void main(String[] args) {
		for(int i = 0; i<5; i++) {
			a(); // a의 i는 a 내에서만 존재한다.
			System.out.println(i);
		}
	}
}
