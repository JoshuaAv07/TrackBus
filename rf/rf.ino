#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN  9       
#define SS_PIN_ENB  10  
MFRC522 MyLectorRF(SS_PIN_ENB, RST_PIN); 

String BufferID = "";
 
void setup() {
  Serial.begin(9600); 
  SPI.begin();        
  MyLectorRF.PCD_Init(); 
}

void loop() {
  if ( MyLectorRF.PICC_IsNewCardPresent()){  
    if ( MyLectorRF.PICC_ReadCardSerial()){
      BufferID = "";
      for (byte i = 0; i < MyLectorRF.uid.size; i++){
        MyLectorRF.uid.uidByte[i] < 0x10 ? " 0" : " ";
        MyLectorRF.uid.uidByte[i], HEX;
        BufferID = BufferID + String(MyLectorRF.uid.uidByte[i], HEX);
      }
      Serial.println(BufferID);
      
      MyLectorRF.PICC_HaltA();         
    }      
  } 
}