/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
arbol arbolito = new arbol();
        arbolito.insertar(1);
        arbolito.insertar(2);
        arbolito.insertar(3);
        arbolito.insertar(4);
        arbolito.insertar(0);
        System.out.println("Recorriendo inorden:");
        arbolito.inorden();
        System.out.println("Recorriendo postorden:");
        arbolito.postorden();
        System.out.println("Recorriendo preorden:");
        arbolito.preorden();
System.out.println(arbolito.existe(1)); // true
        System.out.println(arbolito.existe(7)); // false
        System.out.println(arbolito.existe(0)); // true
 */
package com.mycompany.ejemploprofe;

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
        System.out.println("Recorriendo inorden:");
        arbolCadenas.inorden();
        System.out.println("Recorriendo postorden:");
        arbolCadenas.postorden();
        System.out.println("Recorriendo preorden:");
        arbolCadenas.preorden();
        System.out.println("Imprimir las femeninas");
        arbolCadenas.Femeninas();
        
    }

   }



    
