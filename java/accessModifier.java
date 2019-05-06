class A {
	public void pulic_method() {
		System.out.println("public method");
	}
	
	private void private_method() {
		System.out.println("private method");
	}
	
	public void public_method2() {
		private_method();
		System.out.println("It calls private_method()");
	}
}
public class AccessController { // Access Modifier

	public static void main(String[] args) {

		A a = new A();
		a.pulic_method();
		a.public_method2();
		// public method로 지정된 것들만 사용함으로써 
		// 더 적은 선택지를 얻게 된다. 의사결정의 효율성이 높아진다. 
		// private은 같은 클래스 내에서만 접근할 수 있다. 
		
		// 접근제어자를 명시하지 않으면 default 접근제어자 
		
		// 같은 클래스 : 접근제어자 상관없이 모두 가능 
		
		// 같은 패키지에 있는 메서드에 접근 가능 : private제외하고 모두 가능
		// 같은 패키지의 클래스를 상속한 경우 : private제외하고 모두 가능 
		
		// 다른 패키지의 클래스를 인스턴스화 시켜 접근하는 경우 : public만 가능 
		// 단, 다른 패키지의 클래스를 상속하는 경우 protected에는 접근 가능
		
		// 같은 패키지도 아니고, 상속도 아닌 경우 : public은 빼고 모두 접근 불가능
		
		// private 은 같은 클래스가 아니면 접근 불가능
		// 같은 패키지도 아니고, 상속도 아니면public 빼고는 안된다.
		// 같은 패키지라면 private빼고는 다 된다.
		// 다른 패키지라도 상속하는 경우, private, default 빼고 된다.
		
		// public class와 class 
		// class : 같은 패키지 내에서만 사용
		// public class : 퍼블릭 클래스의 소스코드 파일 이름은 같아야 한다.
		// 하나의 소스코드에는 하나의 퍼블릭 클래스만 존재한다. 
	}

}
