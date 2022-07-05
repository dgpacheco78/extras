int contador = 0;
double periodo = 60000;
unsigned long tiempoAhora = 0;
int valorFijado = 0;

void setup() {
  pinMode(2, INPUT);
  Serial.begin(9600);
}

void loop() {
  if(millis() > (periodo + tiempoAhora)){
    valorFijado = contador;
    Serial.println(contador);
    tiempoAhora = millis();
    contador = 0;
  }


  if(digitalRead(2) == 0){
    delay(300);
    contador++;
  }
  Serial.println(contador);
}
