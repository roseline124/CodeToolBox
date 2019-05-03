
public class method_190503 {
	public static String numbering(int limit) {
		String output = "";
		for(int i=0; i<limit; i++) {
			System.out.println(i);
			output += i;
		}
		
		return output;
	}
	
	public static void main(String[] args) {
		String output = numbering(10);
		System.out.println(output);
	}
}
