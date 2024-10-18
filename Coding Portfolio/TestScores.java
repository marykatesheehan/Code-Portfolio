import java.util.Scanner;
public class Question2 {

	public static void main(String[] args) {
		double score1, score2, score3, score4, score5;
		
		Scanner input = new Scanner(System.in);
		
		System.out.println("Enter your score:");
		score1 = input.nextDouble();
		System.out.println("Enter your score:");
		score2 = input.nextDouble();
		System.out.println("Enter your score:");
		score3 = input.nextDouble();
		System.out.println("Enter your score:");
		score4 = input.nextDouble();
		System.out.println("Enter your score:");
		score5 = input.nextDouble();
		
		System.out.printf("The average of your test scores is: %.2f percent\n", calcAverage(score1, score2, score3, score4, score5));
		
		System.out.println("Which score do you want to use? Enter 1, 2, 3, 4, or 5:");
		int whichScore = input.nextInt();
		if (whichScore == 1)
			System.out.println("Your grade is "+determineGrade(score1));
		else if (whichScore == 2)
			System.out.println("Your grade is "+determineGrade(score2));
		else if (whichScore == 3)
			System.out.println("Your grade is "+determineGrade(score3));
		else if (whichScore == 4)
			System.out.println("Your grade is "+determineGrade(score4));
		else if (whichScore == 5)
			System.out.println("Your grade is "+determineGrade(score5));
		else
			System.out.println("Score does not exist");

		
	}
	public static double calcAverage(double v, double w, double x, double y, double z) {
		double gradeAverage = (v + w + x + y + z) / 5;
		return gradeAverage;
	}
	
	public static String determineGrade(double grade) {
		if (grade >= 90 && grade <=100)
			return "A";
		else if (grade >= 80 && grade <=89)
			return "B";
		else if (grade >= 70 && grade <=79)
			return "C";
		else if (grade >= 60 && grade <=69)
			return "D";
		else
			return "F";
	}
}
