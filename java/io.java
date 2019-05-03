import java.io.File;
import java.io.FileNotFoundException;
import java.util.*;

public class IO_190503 {
	public static void main(String[] args) {
		
//		Scanner sc = new Scanner(System.in);
//		
//		while(sc.hasNextInt()) { //사용자가 입력한 값이 숫자인 경우 True, 아닌 경우 False
//			System.out.println(sc.nextInt()*1000);
//		}
//		sc.close();
	
		try {
			File file = new File("out.txt");
			Scanner sc = new Scanner(file);
			while(sc.hasNextInt()) {
				System.out.println(sc.nextInt()*1000);
			}
			sc.close();
		} catch(FileNotFoundException e) {
			e.printStackTrace();
			System.out.println("냥");
		}
	}
}
