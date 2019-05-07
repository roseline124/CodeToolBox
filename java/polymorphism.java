
class AA{
	public String x() {
		return "A.x";
	}
}

class BB extends AA{
	public String x() {
		// 우선 순위가 더 높다. 
		return "B.x";
	}
	public String y() {
		return "y";
	}
}

class B2 extends AA{
	public String x() {
		return "B2.x";
	}
}


public class Polymorphism_0507 {

	public static void main(String[] args) {
		// 하나의 메서드들이 다양한 방법으로 동작하는 것을 의미한다.
		// 같은 조작 방법이지만 다른 결과를 발생시키는 것 
		// 예를 들어, 키보드는 '누른다'는 같은 조작 방법이라도
		// esc는 취소, enter는 실행한다. 

		// ex) 오버로딩 : 같은 이름, 다른 동작 방법 
		
		
		/* 클래스와 다형성 */
		AA obj = new BB(); 
		// 클래스 BB를 오브젝트화 시키는데 
		// 이 객체는 타입을 AA로 할 수 있다. 
		obj.x();
//		obj.y(); // 오류 발생. 
		// obj는 실질적으로 AA 행세를 하고 있기 때문에 
		// 클래스 BB의 메서드는 인지하지 x 
		
		// 왜 쓸까? 
		// B.x() 출력 : obj의 타입은 AA지만 '오버라이딩'한다면
		// 클래스 B의 메서드를 사용할 수 있다.  
		System.out.println(obj.x());
		
		/*클래스와 다형성2*/
		
		AA obj2 = new B2();
		
		// B2.x() 출력 
		System.out.println(obj2.x());
		
		
		/* 실전 예제 : abstract */
//		부모클래스타입 변수이름 = new 자식클래스(); 
		
		/* 인터페이스와 다형성 */
//		인터페이스타입 변수이름 = new 인터페이스를 구현하는 클래스();
		
	}

}
