
class Parent {
	public void parent_say() {
		System.out.println("내가 니 부모다.");
	}
}

class Child extends Parent {
	public void parent_say() {
		
		// 부모 클래스의 메서드 로직을 그대로 가져오려면?
		super.parent_say();
		
		// 부모 메서드와 자식 메서드 형식이 일치해야 한다.
		// 메서드의 시그니처(서명) : return 타입 / 메서드의 이름 / 파라미터 (타입, 개수, 순서)
		System.out.println("아직도 내가 니 부모로 보이니?");
	}
}

public class Overriding_0505 {
	// 오버라이딩 : 재정의 
	public static void main(String[] args) {
		Child c = new Child();
		c.parent_say();
	}

}
