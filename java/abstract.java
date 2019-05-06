
abstract class Abstract_Class {
	// 추상 메서드는 중괄호로 로직을 쓰면 안된다.
	// 멤버 중 하나라도 추상 메서드가 있으면 그 클래스는 자동으로 추상 클래스가 된다. 
	public abstract int b(); 
	
	// 추상 메서드가 아닌 메서드가 존재할 수 있다. 
	public void d() {
		System.out.println("world");
	}
	
}

class B extends Abstract_Class {
	// A 클래스의 b메서드를 상속해야 한다. 
	// b 메서드 역시 추상 메서드 : 중괄호{}가 존재하지 않고, 껍데기만 있다. 
	// 추상 클래스를 상속하는 경우, 추상메서드를 구현해야 한다.
	
	public int b() {
		// 추상 메서드 구현 
		return 0;
	}
}

public class Abstract_0506 {

	public static void main(String[] args) {
		// abstract : 상속해서 사용하도록 강제하는 코드 
		B obj = new B();
		obj.b();
	}

}
