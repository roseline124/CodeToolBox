
public class Overloading {

	public static void overload() {
		System.out.println("I'm original method.");
	}
	
	public static void overload(String str) {
		// 코드 중복을 없애기 위해 원래의 메서드를 호출할 수 있다.
		overload();
		System.out.println(str);
	}
	
	public static void main(String[] args) {
		// 같은 이름, 다른 매개 변수 
		// 이름이 같아도 매개변수가 틀리다면 다른 메서드로 인식한다.
		// 반면, 매개변수는 같지만 리턴타입이 다르면 오류가 발생한다. 
		// 이름이 같고, 매개변수도 같은데 리턴타입이 다르면 자바는
		// 어떤 메서드를 실행시킬지 애매하기 때문에 오류를 발생시킨다. 
		// 매개변수의 이름은 상관없다. 
		overload();
		overload("I'm overloaded method");

	}

}
