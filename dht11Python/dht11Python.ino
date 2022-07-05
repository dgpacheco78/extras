//Bibliotecas
#include <DHT.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);
DHT dht (12, DHT11);
float t;
float h;

// Inicialización del programa
void setup() {
  // Iniciar comunicación serial
  Serial.begin (9600);
  lcd.init();
  lcd.backlight();
  dht.begin();
  delay(100);
}// fin del void setup ()

// Cuerpo del programa, bucle principal
void loop() {
    t = dht.readTemperature();  // Lee la temp en ºC 
    h = dht.readHumidity();     // Lee la humed en % 
    Serial.println(String(t));
    Serial.println(String(h));
    lcd.setCursor(0, 0);
    lcd.print(String(t) + ":" + String(h));
    delay(500);
}// fin del void loop ()
