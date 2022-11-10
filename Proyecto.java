
/**
 *listamedicamentos.contains
 *
 * @author Darren
 */
import java.util.Scanner;
import java.util.LinkedList;

public class Proyecto {

    public static void AgregarMedicamento(LinkedList<String> listamedicamentos, Scanner entrada) {

        System.out.println("Ingresar el nuevo medicamento");
        listamedicamentos.push(entrada.next());
        listamedicamentos.add("paracetamol");
        listamedicamentos.add("ibuprofeno");

    }

    public static void AgregarPaciente(LinkedList<String> listapacientes, Scanner entrada) {
        System.out.println("Ingresar el nombre del paciente");
        listapacientes.push(entrada.next());
        System.out.println("ingrese el medeicamento del paciente");
        listapacientes.push(entrada.next());

        listapacientes.add("Felipe, Paracetamol");
        listapacientes.add("Adrian, ibuprofeno");
    }

    public static void Imprimirdatos(LinkedList<String> listamedicamentos) {
        System.out.println("La lista de medicamentos son:" + listamedicamentos);

    }

    public static void Imprimirdatos2(LinkedList<String> listapacientes) {
        System.out.println("La lista de pacientes es: " + listapacientes);
    }

    public static void EliminarMedicamento(LinkedList<String> listamedicamentos, Scanner entrada) {
        String nombre;
        System.out.println("Intriduce el dato a eliminar");
        nombre = entrada.next();
        if (listamedicamentos.contains(nombre)) {
            listamedicamentos.remove(nombre);
            System.out.println("El nombre:  " + nombre + "fue eliminado");

        } else {
            System.out.println("El nombre no se encuentra en la lista");
        }

    }

    public static void main(String[] ddg) {
        LinkedList<String> listapacientes = new LinkedList();
        LinkedList<String> listamedicamentos = new LinkedList();
        Scanner entrada = new Scanner(System.in);
        int opcion = 0;

        do {
            System.out.println("Elige una opción");
            System.out.println("1- Agregar medicamento");
            System.out.println("2- Agregar un paciente");
            System.out.println("3- Eliminar medicamento");
            System.out.println("4- Imprimir los datos");
            System.out.println("5- salir");
            System.out.println("Digite una opción: ");
            opcion = entrada.nextInt();

            switch (opcion) {
                case 1:
                    System.out.println("Estas introduciendo los datos");
                    AgregarMedicamento(listamedicamentos, entrada);

                    break;
                case 2:
                    System.out.println("Agregar un paciente");
                    AgregarPaciente(listapacientes, entrada);
                    System.out.println("inserte el medicamento al paciente" + listamedicamentos);

                    break;
                case 3:
                    System.out.println("Eliminar medicamentos");
                    EliminarMedicamento(listamedicamentos, entrada);
                    break;
                case 4:
                    System.out.println("imprimir");
                    Imprimirdatos(listamedicamentos);
                    Imprimirdatos2(listapacientes);

                    break;
                case 5:
                    System.out.println("Salir");
                default:
                    System.out.println("Opcion invalida, digite una opcion mostrada en pantalla");

            }

        } while (opcion != 5);

    }

}
