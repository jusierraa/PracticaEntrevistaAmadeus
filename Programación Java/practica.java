import java.util.Scanner;

public class practica{
    public static void main(String args[]){
        Scanner text = new Scanner(System.in);
        String texto = text.nextLine();
        int longitud = texto.length(), a = 0;
        for (int i = 0; i != longitud; i++){
            if (texto.charAt(i) == 'a'){
                a += 1;
            }
        }
        System.out.println("La cantidad de As que tiene la cadena es: " + a);
    }
}