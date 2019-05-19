import java.io.*;

// 나만의 예외 만들기

class DivideException extends RuntimeException { // 또는 ArithmeticException으로 좀 더 특화시켜 처리할 수 있다. 
	DivideException() {
		super();
	}
	DivideException(String message){
		super(message);
	}
}

// checked exception

class CheckedException extends Exception {
	CheckedException() {
		super();
	}
	CheckedException(String message2){
//		throws 로 사용자에게 예외처리를 맡기거나 try catch를 해야 한다. 
		super(message2);
	}
}



class AAA {
	
	void run() throws FileNotFoundException {
//		이 함수의 사용자에게 에러 핸들링을 맡긴다. 
	}
	
	private int[] arr = new int[3];
	
	AAA() {
		arr[0] = 0;
		arr[1] = 10;
		arr[2] = 20;
	}
	
	public void z (int first, int second) {
		try {
			System.out.println(arr[first]/arr[second]);
		} catch(ArrayIndexOutOfBoundsException e) {
			System.out.println("ArrayIndexOutOfBoundsException");
		} catch(ArithmeticException e) { // Exception 정보를 보려면 Ctrl 누른 상태로 클릭
			
			System.out.println("ArithmeticException");
		} catch(Error e) {
			System.out.println("OtherExceptions");
		} finally {
//			오류 발생과 관계없이 언제나 실행된다. 
			System.out.println("Finally");
		}
		
	}
}

public class ExceptionEx {
	public static void divide(int left, int right) {
		
		if (right==0) {
//			throw new IllegalArgumentException("0으로 나눌 수 없습니다.");
			throw new ArithmeticException("0으로 나눌 수 없습니다."); // 생성자에 에러 메시지 전달
		}
		
		
			try {
				System.out.println(left/right);
			} catch(ArithmeticException e) {
				System.out.println("오류 발생 : " + e.getMessage());
				e.printStackTrace();
			}
			
			System.out.println("divide end"); // catch 실행 후, 실행
		}

	public static void main(String[] args) {
		// divide(1, 0); // ArithmeticException 
		
//		AAA a = new AAA();
//		a.z(10, 1); // ArrayIndexOutOfBoundsException
//		a.z(1,  0); // ArithmeticException 
//		a.z(2, 1); // 정상 실행 
		
		
//		주의 : 객체 생성 시, try 문 안에 넣으면 지역 변수가 되므로 try문 밖으로 빼야 한다. 
		BufferedReader bReader = new BufferedReader(new FileReader("out.txt"));
		String input = bReader.readLine();
		System.out.println(input);
		
//		Throwable의 자식 : Error와 Exception 
//		Error : 개발자가 할 수 있는 게 없다. 메모리가 부족하다든지 하는 오류들을 다룬다. 
//		IOException : 부모 클래스 중 RuntimeException x -> checked : throw한 후, try-catch로 반드시 예외를 처리하거나 throws로 사용자에게 에러 핸들링을 맡겨야 한다. 
//		Arithmetic Exception : 부모 클래스 중 RuntimeException o -> unchecked
	
//		나만의 예외 만들기 
//		1. checked, unchecked 예외인지 정하기. (unchecked : 이후, 로직에 계속해서 영향을 주는 경우)
//		2. unckecked 라면 extends RuntimeException 
	
	}

	
}
