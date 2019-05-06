interface I {
	// 인터페이스의 변수, 메서드들은 public이어야 한다. 
	public void z ();
}

class Interface_A implements I{
	public void z() {
		// 본체의 로직은 없지만 z() 메서드를 구현 
		// 반드시 구현하도록 강제 
		// A는 인터페이스 I를 구현한다. 
		
		// 왜 사용? 두 개발자가 동시에 개발을 진행할 때 (빠른 개발을 위해)
		// A 개발자는 B 개발자가 구체적인 내용을 구현할 것이라고 믿고
		// 틀만 만들어 놓는다.
		
		// 자바 코딩을 할 때 인터페이스 규칙에 맞춰서 
		// 서로 동시에 개발을 할 수 있어 편하다. 
		
		// 하나의 클래스는 여러 인터페이스를 구현할 수 있다.
		// 단, 반드시 그 안의 메서드들을 모두 구현해야 한다. 
		// ex) class A implements I1, I2 
	}
}

public class Interface_0506 {

	public static void main(String[] args) {
		
	}

}
