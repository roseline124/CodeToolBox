class Calculator {
	static double PI = 3.14; // final을 쓰면 상수로 지정할 수 있다. 
	int left, right;
	
	public void setOprands(int left, int right) {
		this.left = left;
		this.right = right;
	}
	
	public int sum() {
		int summation = this.left + this.right;
		System.out.println(summation);
		return summation;
	}
	
	public void avg() {
		System.out.println(this.sum()/2);
	}
}

class Calculator2 {
	public static int sum(int left, int right) {
		return (left + right);
	}
	
	public static float avg(int left, int right) {
		return (sum(left, right)/2);
	}
}

class Class1 {
	static int static_var = 1;
	int instance_var = 2;
	static void static_static() {
		System.out.println(static_var);
	}
	
	static void static_instance() {
		// 클래스 메서드에서 인스턴스 변수에 접근할 수 없다.
//		 System.out.println(instance_var); // 오류 발생
	}
	
	void instance_static() {
		System.out.println(static_var);
	}
	
	void instance_instance() {
		System.out.println(instance_var);
	}
}

public class OOP {
	public static void main(String[] args) {
		Calculator c1 = new Calculator();
		c1.setOprands(30, 50);
		c1.sum();
		c1.avg();
		System.out.println(Calculator.PI);
		System.out.println(Calculator2.sum(20, 10));
		// class 소속의 메서드를 바로 사용할 수 있다. 
		// 대신 static을 써야 한다. 
		
		// 인스턴스 메서드(static이 붙어있지 x)는 클래스 멤버에 접근 가능
		// 클래스 메서드는 인스턴스 멤버에 접근할 수 없다. 
		// 왜냐, 클래스 메서드는 항상 인스턴스보다 먼저 존재하기 때문이다.
		
		// static : 전역에서 접근 가능 
	}
}
