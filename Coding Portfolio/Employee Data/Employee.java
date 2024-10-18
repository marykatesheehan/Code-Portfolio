
public class Employee {
	String name;
	int idNumber;
	String department;
	String position;
	
	public Employee(String name, int number, String department, String position) {
		this.name = name;
		this.idNumber = number;
		this.department = department;
		this.position = position;
	}
	
	public String getName() {
		return this.name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public int getIdNumber() {
		return this.idNumber;
	}
	
	public void setIdNumber(int number) {
		this.idNumber = number;
	}
	
	public String getDepartment() {
		return this.department;
	}
	
	public void setDepartment(String department) {
		this.department = department;
	}
	
	public String getPosition() {
		return this.position;
	}
	
	public void setPostition(String position) {
		this.position = position;
	}
	
}
