/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package colasupi;

/**
 *
 * @author Darren
 */
public class Clasecajero2 {
    // Atributos
    private static final int MAXTAM = 10; // variable constante
    private static int frente;
    private static int ultimo;
    private int []cajero2;
    
 public Clasecajero2()
 {
    frente = 0;
    ultimo = -1;
    cajero2 = new int [MAXTAM];
 }   
 
 public void insertar(int elemento)throws Exception
 {
     if (!Cajero2lleno())
         cajero2[++ultimo] = elemento;
    else
         throw new Exception("La caja está llena");
 }
 
  public int eliminar()throws Exception
 {
     if (!Cajero2Vacio())
       return cajero2[frente++];
    else
      throw new Exception("No hay nadie en la caja");
 }

  public void Borrartodoo()
  {
     frente = 0;
     ultimo = -1;
  }
  
  public int frente() throws Exception
  {
      if (!Cajero2Vacio()) 
          return cajero2[frente];
      else
     throw new Exception("El cajero 2 esta vacio");
  }
  
  
 public boolean Cajero2lleno()
 {
   return ultimo == MAXTAM - 1;
 }
 
 public boolean Cajero2Vacio()
 {
   return frente > ultimo;
 }
} 
