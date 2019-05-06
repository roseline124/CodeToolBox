class C {
	static final double PI = 3.14;
	
	final void b() {
		System.out.println("You can't change this method");
	}
}

public class Final_0506 {

	public static void main(String[] args) {
		C c = new C();
		System.out.println(c.PI);
		c.b();
	}
}
