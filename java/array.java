public class Array_190503 {
	public static void main(String[] args) {
		String[] Astro = {"차은우", "문빈", "진진", "MJ", 
							"윤산하", "라키"};
		
		for(int i=0; i <Astro.length; i++) {
			String member = Astro[i];
			System.out.println("안녕하세요, "+member+"입니다.");
		}
		
		
		// for-each문 
		for (String m: Astro) { // m : 반복 변수
			System.out.println("안녕하세요, "+m+"입니다.");
		}
		
		// error : ArrayIndexOutOfBoundException  
		// collection : array의 한계를 극복하기 위해 쓰는 기능 (array의 사이즈를 정할 필요가 없다.) 
		
		
		
	}
}
