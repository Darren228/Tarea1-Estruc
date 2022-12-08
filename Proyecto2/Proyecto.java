
package colasupi;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.logging.Level;
import java.util.logging.Logger;


public class Proyecto {

   static int opcion  = 0;
   static int elemento = 0;
    public static void main(String[] args) {
      Clasecajero cajero1 = new Clasecajero();
      Clasecajero2 cajero2 = new Clasecajero2();
      Clasecajero3 cajero3 = new Clasecajero3();
      BufferedReader leer = new BufferedReader
                
        (new InputStreamReader(System.in));      
      
        do {
          try {
              System.out.println("**** Bienvenido al Banco Central de Turrialba ****");
              System.out.println("1- Ingresar elementos");
              System.out.println("2-Eliminar elementos");
              System.out.println("3- Ver si la cola esta vacia");
              System.out.println("4- Ver el frente de la cola");
              System.out.println("5- Borrar todo");
              System.out.println("6- Ver si la cola esta llena");
              System.out.println("7- Salir");
              opcion = Integer.parseInt(leer.readLine());
              
              if (opcion==1) {
                  if (cajero1.Cajerolleno()){
                     if(cajero2.Cajero2lleno()){
                     if(cajero3.Cajero3lleno()){
                          
                     
                      System.out.println("COLA ESTA LLENA NO SE PUEDEN INGRESAR ELEMENTOS");
                   }}} else
                  {
                      System.err.print("Digite un elemento: ");
                      elemento = Integer.parseInt(leer.readLine());
                      try {
                          cajero1.insertar(elemento);
                      } catch (Exception ex) {
                          Logger.getLogger(Proyecto.class.getName()).log(Level.SEVERE, null, ex);
                      }
                  }
              }
          } catch (IOException ex) {
              Logger.getLogger(Proyecto.class.getName()).log(Level.SEVERE, null, ex);
          }
            
            if (opcion==2) {
                if (cajero1.CajeroVacio()) {
                  if(cajero2.Cajero2Vacio()){
                  if(cajero3.Cajero3Vacio()){
                    System.err.println("LA COLA ESTA VACIA NO PUEDE ELIMINAR ELEMENTOS");
                }}} else
                {   try {
                    System.out.println(cajero1.eliminar());
                    } catch (Exception ex) {
                        Logger.getLogger(Proyecto.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }
            }
            
            if (opcion==3) {
                if (cajero1.CajeroVacio()){
                  if(cajero2.Cajero2Vacio()){
                  if(cajero3.Cajero3Vacio()){
                    System.err.println("Los cajeros estan vacios");
             }}}else
                    System.err.println("hay personas en los cajeros");
            }
            
            if (opcion == 4) {
                if (cajero1.CajeroVacio())
                if(cajero2.Cajero2lleno()){
                if(cajero3.Cajero3lleno()){{
                    System.err.println("LA COLA ESTA VACIA");
            }}} else
                {
                    try {
                        System.out.println("El frente es: " + cajero1.frente());
                    } catch (Exception ex) {
                        Logger.getLogger(Proyecto.class.getName()).log(Level.SEVERE, null, ex);
                    }
                }
            }
            
            if (opcion == 5) {
                cajero1.Borrartodo();
            }
            
            if (opcion == 6) {
                if (cajero1.Cajerolleno())
                    System.err.println("LA COLA ESTA LLENA");
                   else
                    System.err.println("LA COLA NO ESTA LLENA");
            }
            if(opcion ==7){
                System.out.println("Las personas del cajero numero 1 son: "+cajero1.Cajerolleno());
                System.out.println("Las personas del cajero 2 son: "+cajero2.Cajero2lleno());
                System.out.println("Las personas del cajero 3 son: "+cajero3.Cajero3lleno());
            }
            
        } while (opcion!=7);

    }

}
