#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN  9       //Pin 9 para el reset del RC522
#define SS_PIN_ENB  10   //Pin 10 para el SS (SDA) del RC522
MFRC522 MyLectorRF(SS_PIN_ENB, RST_PIN); //Creamos el objeto para el RC522

String BufferID = "";
 
void setup() {
  Serial.begin(9600); //Iniciamos la comunicación  serial
  SPI.begin();        //Iniciamos el Bus SPI
  MyLectorRF.PCD_Init(); // Iniciamos  el MyLectorRF
}

void loop() {
  // Verificamos si se ha detectado alguna tarjeta
  if ( MyLectorRF.PICC_IsNewCardPresent()){  
    // Determinamos el codigo de la tarjeta
    if ( MyLectorRF.PICC_ReadCardSerial()){
      // Recuperamos en ID de la Tarjeta
      BufferID = "";
      for (byte i = 0; i < MyLectorRF.uid.size; i++){
        MyLectorRF.uid.uidByte[i] < 0x10 ? " 0" : " ";
        MyLectorRF.uid.uidByte[i], HEX;
        BufferID = BufferID + String(MyLectorRF.uid.uidByte[i], HEX);
      }
      Serial.println(BufferID);
  
      // Terminamos la lectura de la tarjeta  actual
      MyLectorRF.PICC_HaltA();         
    }      
  } 
}