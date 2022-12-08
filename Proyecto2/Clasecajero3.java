
package colasupi;
/**
 *
 * @author Darren
 */
public class Clasecajero3 {
    // Atributos
    private static final int MAXTAM = 10; // variable constante
    private static int frente;
    private static int ultimo;
    private int []cajero3;
    
 public Clasecajero3()
 {
    frente = 0;
    ultimo = -1;
    cajero3 = new int [MAXTAM];
 }   
 
 public void insertar(int elemento)throws Exception
 {
     if (!Cajero3lleno())
         cajero3[++ultimo] = elemento;
    else
         throw new Exception("La caja está llena");
 }
 
  public int eliminar()throws Exception
 {
     if (!Cajero3Vacio())
       return cajero3[frente++];
    else
      throw new Exception("No hay nadie en la caja");
 }

  public void Borrartodo()
  {
     frente = 0;
     ultimo = -1;
  }
  
  public int frente() throws Exception
  {
      if (!Cajero3Vacio()) 
          return cajero3[frente];
      else
     throw new Exception("El cajero 2 esta vacio");
  }
  
  
 public boolean Cajero3lleno()
 {
   return ultimo == MAXTAM - 1;
 }
 
 public boolean Cajero3Vacio()
 {
   return frente > ultimo;
 }
}
