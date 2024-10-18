import java.util.Scanner;

public class Question1 {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        String resume = "yes";
        boolean[] seatsAvailable = {true, false, false, //0 set to index 0 to prevent user from selecting it
        						          false, false, 
        						          false, false, 
        						          false, false, 
        						          false, false};

        int seatType = 0;

        while (resume.equals("yes")) {
            System.out.println("Type 1 for First Class or 2 for Economy Class:");
            seatType = in.nextInt();

            if (seatType == 1) { //first class
                String seatTypeName = "First Class";
                System.out.println("Select a Seat 1-5:");
                int seat = in.nextInt();

                if (seat < 1 || seat > 5) {
                    System.out.println("These seats do not exist.");
                } else if (seatsAvailable[seat] == true) {
                    int totalUnavailable = 0;
                    System.out.println("The seat you selected is taken or not available!");
                    System.out.println("Here are all the available seats:");
                    for (int i = 1; i < 6; i++) {
                        if (seatsAvailable[i] == true) {
                            totalUnavailable += 1;
                        } else {
                            System.out.printf("Seat %d is available.%n", i);
                        }
                    }
                    if (totalUnavailable == 5) {
                        noSeats(seatTypeName, seat, seatsAvailable, in);
                    } else {
                        System.out.println("Select a new seat from the available list:");
                        seat = in.nextInt();
                        if (seat < 1 || seat > 5 || seatsAvailable[seat]) {
                            System.out.println("Invalid seat selection. Please select an available seat.");
                        } else {
                            seatsAvailable[seat] = true;
                            printBoardingPass(seatTypeName, seat);
                        }
                    }
                } else {
                    printBoardingPass(seatTypeName, seat);
                    seatsAvailable[seat] = true;
                }

            } else if (seatType == 2) { //economy class
                String seatTypeName = "Economy";
                System.out.println("Select a Seat 6-10:");
                int seat = in.nextInt();

                if (seat < 6 || seat > 10) {
                    System.out.println("These seats do not exist.");
                } else if (seatsAvailable[seat] == true) {
                    int totalUnavailable = 0;
                    System.out.println("The seat you selected is taken or not available!");
                    System.out.println("Here are all the available seats:");
                    for (int i = 6; i < 11; i++) {
                        if (seatsAvailable[i] == true) {
                            totalUnavailable += 1;
                        } else {
                            System.out.printf("Seat %d is available.%n", i);
                        }
                    }
                    if (totalUnavailable == 5) {
                        noSeats(seatTypeName, seat, seatsAvailable, in);
                    } else {
                        System.out.println("Select a new seat from the available list:");
                        seat = in.nextInt();
                        if (seat < 6 || seat > 10 || seatsAvailable[seat]) {
                            System.out.println("Invalid seat selection. Please select an available seat.");
                        } else {
                            seatsAvailable[seat] = true;
                            printBoardingPass(seatTypeName, seat);
                        }
                    }
                } else {
                    printBoardingPass(seatTypeName, seat);
                    seatsAvailable[seat] = true;
                }
            }
            
            else {
            	System.out.println("The class does not exist.");
            }

            in.nextLine();
            System.out.println("Would you like to book another seat? Answer yes or no:");
            resume = in.nextLine();
        }

        System.out.println();
        System.out.println("Thank you for booking with us!");
    }

    public static void printBoardingPass(String seatType, int seat) {
        if (seatType.equals("First Class")) {
            System.out.println("Here is your boarding pass:");
            System.out.printf("-------------------------%n|    TICKET             |%n|    CLASS: %s |%n|    SEAT: %d            |%n"
                    + "-------------------------%n%n", seatType, seat);
        } else if (seatType.equals("Economy")) {
            System.out.println("Here is your boarding pass:");
            System.out.printf("-------------------------%n|    TICKET             |%n|    CLASS: %s     |%n|    SEAT: %d            |%n"
                    + "-------------------------%n%n", seatType, seat);
        }
    }

    public static void noSeats(String seatType, int seat, boolean[] seatsAvailable, Scanner in) {
        if (seatType.equals("First Class")) {
            System.out.println("Would you be interested in changing classes? Enter yes or no");
            in.nextLine();
            String change = in.nextLine();
            if (change.equals("yes")) {
                seatType = "Economy";
                System.out.println("Here are all the available seats:");
                for (int i = 6; i <= 10; i++) {
                    if (!seatsAvailable[i]) {
                        System.out.println(i);
                    }
                }
                System.out.println("Select one of the available seats:");
                seat = in.nextInt();
                if (seat < 6 || seat > 10 || seatsAvailable[seat]) {
                    System.out.println("Invalid seat selection. Please select an available seat.");
                } else {
                    seatsAvailable[seat] = true;
                    printBoardingPass(seatType, seat);
                }
                in.nextLine(); 
            } else {
                System.out.println("Next flight leaves in 3 hours!");
            }
        } else if (seatType.equals("Economy")) {
            System.out.println("Would you be interested in changing classes? Enter yes or no");
            in.nextLine();
            String change = in.nextLine();
            if (change.equals("yes")) {
                seatType = "First Class";
                System.out.println("Here are all the available seats:");
                for (int i = 1; i <= 5; i++) {
                    if (!seatsAvailable[i]) {
                        System.out.println(i);
                    }
                }
                System.out.println("Select one of the available seats:");
                seat = in.nextInt();
                if (seat < 1 || seat > 5 || seatsAvailable[seat]) {
                    System.out.println("Invalid seat selection. Please select an available seat.");
                } else {
                    seatsAvailable[seat] = true;
                    printBoardingPass(seatType, seat);
                }
                in.nextLine(); 
            } else {
                System.out.println("Next flight leaves in 3 hours!");
            }
        }
    }
}