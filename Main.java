import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner consola = new Scanner(System.in);
        while(true){
            System.out.println("*** CALCULADORA ***");
            mostrarMenu();

            System.out.print("¿QUE OPERACION DESEAS REALIZAR?: ");
            try {
                var operacion = Integer.parseInt(consola.nextLine());
                if (operacion >= 1 && operacion <= 4) {
                    ejecutarOperacion(operacion, consola);
                } else if (operacion == 5) {
                    System.out.println("Hasta pronto!");
                    break;
                } else {
                    System.out.println("Operacion erronea");
                }
                System.out.println();//ESTO ES UN SALTO DE LINEA ENTRE LA ANTERIOR OPERACION Y LA NUEVA
            }
            catch (Exception e) {
                System.out.println("Ocurrio un error: " + e.getMessage());
            }
        }//Fin while
    }//Fin main
    private static void mostrarMenu (){
        System.out.println("""
                    1. SUMA
                    2. RESTA
                    3. MULTIPLICACION
                    4. DIVISION
                    5. SALIR""");
    }
    private static void ejecutarOperacion (int operacion, Scanner consola){
        System.out.print("PROPORCIONA EL PRIMER VALOR: ");
        var operando1 = Double.parseDouble(consola.nextLine());
        System.out.print("PROPORCIONA EL SEGUNDO VALOR: ");
        var operando2 = Double.parseDouble(consola.nextLine());
        double resultado;
        switch (operacion) {
            case 1 -> {
                resultado = operando1 + operando2;
                System.out.println("El resultado de la suma es: " + resultado);
            }
            case 2 -> {
                resultado = operando1 - operando2;
                System.out.println("El resultado de la resta es: " + resultado);
            }
            case 3 -> {
                resultado = operando1 * operando2;
                System.out.println("El resultado de la multiplicacion es: " + resultado);
            }
            case 4 -> {
                resultado = operando1 / operando2;
                System.out.println("El resultado de la division es: " + resultado);
            }
            default -> {
                System.out.println("Operacion erronea");
            }
        }
    }
}//Fin class