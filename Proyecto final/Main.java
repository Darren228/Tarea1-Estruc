
package com.mycompany.ejemploprofe;

import java.util.Scanner;

/**
 *
 * @author Darren
 */
public class Main {
    
    public static void main(String[] argumentos) {
        Arbolcadenas arbolCadenas = new Arbolcadenas();
        arbolCadenas.insertar("Carlos", " M");
        arbolCadenas.insertar("Maria", " F");
        arbolCadenas.insertar("Luis", " M");
        arbolCadenas.insertar("Ana", " F");
        arbolCadenas.insertar("Jorge", " M");
        arbolCadenas.insertar("Alicia", " F");
        arbolCadenas.insertar("Andres", " M");
      
        int menu = 0;
        while (menu != 4) {
            
        System.out.println("Bienvenido al arbol genealogico de carlos ");
        System.out.println("1- Agregar una persona al arbol genealogico");
        System.out.println("2- Mostrar los distintos recorridos del arbol ");
        System.out.println("3- Imprimir el genero femenino");
        System.out.println("4- salida");
        System.out.println(" ");
        Scanner entrada = new Scanner(System.in);
        menu = entrada.nextInt();
            switch (menu) {
                case 1:
                    
                    Scanner nuevonodo = new Scanner(System.in);
                    System.out.println("Digite el nombre: ");
                    String Nombre;
                    Nombre = nuevonodo.nextLine();
                    System.out.println("Digite el genero: F o M");
                    String Genero;
                    Genero = nuevonodo.nextLine();
                    NodoCadena NodoNuevo = new NodoCadena(Nombre, Genero);
                    System.out.println("El nombre de la persona ingresada y su genero es :\n " + NodoNuevo.getDato()+NodoNuevo.getGenero());
                    
                case 2:
                   
                    System.out.println("Recorriendo inorden:");
                    arbolCadenas.inorden();

                     System.out.println("Recorriendo preorden:");
                    arbolCadenas.preorden();

                    System.out.println("Recorriendo postorden:");
                     arbolCadenas.postorden();
                    
                case 3:
                    System.out.println("Imprimir las femeninas");
                    arbolCadenas.Femeninas();
                  
                default:
                    System.out.println("Se ha salido con exito del programa ");
                    
            }
        }
    }
    }

   



    
