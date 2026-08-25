namespace ProjetoCalculadora.code 
{
    public class Calculadora // criando nosso codigo e permitindo usar na GUI
    {
        // SOMA
        public double Somar(double numero1, double numero2) //double permite uso de numero com virgula
        {
            return numero1 + numero2; //n esquecer do ";" return devolve o resultado no final
        }

        //SUBTRAÇÃO
        public double Subtrair(double numero1, double numero2)
        {
            return numero1 - numero2;
        }

        // MULTIPLICAÇÃO
        public double Multiplicação(double numero1, double numero2)
        {
            return numero1 * numero2;
        }

        // DIVISÃO
        public double Divisão(double numero1, double numero2)
        
        {
            if (numero2 == 0) // condição se for vdd aciona o comando
            {
                throw new DivideByZeroException("Erro: Divisão por zero."); // funciona como alarme de emergencia
            }

            return numero1 / numero2;
        }
    }
}
