
public class EmployeeTest {

	public static void main(String[] args) {
		Employee employee1 = new Employee("Suzan Meyers", 47899, "Accounting", "Vice President");
		Employee employee2 = new Employee("Mark Jones", 39119, "IT", "Programmer");
		Employee employee3 = new Employee("Joy Rogers",81774, "Manufacturing", "Engineer");
		
		System.out.println("Employee #1");
		System.out.println("Name: "+employee1.getName());
		System.out.println("ID: "+employee1.getIdNumber());
		System.out.println("Department: "+employee1.getDepartment());
		System.out.println("Positon: "+employee1.getPosition());
		
		System.out.println();
		
		System.out.println("Employee #2");
		System.out.println("Name: "+employee2.getName());
		System.out.println("ID: "+employee2.getIdNumber());
		System.out.println("Department: "+employee2.getDepartment());
		System.out.println("Positon: "+employee2.getPosition());
		
		System.out.println();
		
		System.out.println("Employee #3");
		System.out.println("Name: "+employee3.getName());
		System.out.println("ID: "+employee3.getIdNumber());
		System.out.println("Department: "+employee3.getDepartment());
		System.out.println("Positon: "+employee3.getPosition());
		
		
		

	}

}
